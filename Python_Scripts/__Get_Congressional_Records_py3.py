##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################


# Dependencies 
##################################
"""
------------------------------------------------------------------------
Notes: This Package Requires several dependencies
- Anaconda Distribution of Python 3
- 	wget: 
	- 	Download the wget program zipfile:
			https://pypi.python.org/pypi/wget

	- 	Through your command line terminal, navigate to the folder 
		and in your terminal execute "python setup.py install"
------------------------------------------------------------------------
"""

def getURL(date):
	"""Prints Congressional Record URL (of PDF record) for a given date."""
	base_url = "https://www.gpo.gov/fdsys/pkg/CREC-"+date+"/pdf/CREC-"+date+".pdf"
	print (base_url)


def getfullURL(date):
	"""Returns Congressional Record URL (of PDF record) for a given date."""
	base_url = "https://www.gpo.gov/fdsys/pkg/CREC-"+date+"/pdf/CREC-"+date+".pdf"
	return base_url


def getdates(yr1=2009, yr2=2016, month1=1, month2=12, day1=1, day2=31):
	"""Returns a list of all possible dates as a set of tuples:
		E.G. date1 = (2009, 01, 01) or datex = (2011, 12, 06)
		The form is therefore a [(yyyy, mm, dd), ... (yyyy, mm, dd)]

		This function is set up to return all possible dates between 01/01/2009 and 12/31/2016. 

		It can be modified to provide expanded dates if need be.

		Note that while this creates dates that do not exist, the end result
		is simply an invalid url link, which is handled in subsequent functions."""

	import itertools

	years = ['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']
	months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
	days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']


	index_yr1 = yr1-2009
	index_yr2 = yr2-2009
	index_mo1 = month1-1
	index_mo2 = month2-1
	index_dy1 = day1-1
	index_dy2 = day2-1

	req_years = years[index_yr1:index_yr2+1]
	req_months = months[index_mo1:index_mo2+1]
	req_days = days[index_dy1:index_dy2+1]

	dates = (list(itertools.product(req_years, req_months, req_days)))
	return dates


def getcongressURLs():
	"""This function returns a list of urls for the congressional records between 2009 and 2016."""

	dates = getdates()

	f = open('congressional_records_URLs2.csv', 'w')
	try:
		for dt in range(0, len(dates)):
			date = str(dates[dt]).replace("'", "").replace(",", "-").replace(" ", "").replace("(", "").replace(")", "")
			full_url = getfullURL(date)
			f.write(u'%s\n' % (full_url))
	finally:
		f.close()



def get_congressional_records():
	"""This function retrieves the congressional records for the possible dates between 2009 and 2016.

	It writes urls where exceptions occur to a seperate spreadsheet.
	Note that pages where no congressional record exists yield a 404 page for the Congressional record 
	website. As such, the wget function downloads the html code for that page, saving it based
	on the url as a pdf:

	"https://www.gpo.gov/fdsys/pkg/CREC-"+date+"/pdf/CREC-"+date+".pdf"

	As a result, these pages are all identical and have a size of approximately 5618 bytes. 
	A subsequent bash script filters these false hits out based on these parameters.

	Note that the congressional record site will block your bot from downloading the page
	if the time clock is too fast. 

	For example, time.sleep(0.5) quickly locks up. The current set time time.sleep(5.5) 
	has run in testing without issue. Experiment at your own risk.

	"""

	import sys, csv, time, os, subprocess, wget, signal

	sys.path.append('../Python_Scripts/')
	sys.path.append('..')

	## Add Functions for Timeout and Signal ##
	class TimeoutException(Exception):
		pass

	def timeout_handler(signum, frame):
	    raise TimeoutException

	signal.signal(signal.SIGALRM, timeout_handler)


	## Setup Directory and Dates ##
	try:
		os.mkdir("Congressional_Records")
	except:
		pass

	os.chdir("Congressional_Records")

	dates = getdates()

	## Begin Congressional Record Collection ##
	try:
		for dt in range(0, len(dates)):
			date = str(dates[dt]).replace("'", "").replace(",", "-").replace(" ", "").replace("(", "").replace(")", "")
			url = str(getfullURL(date))
			print ("Downloading congressional record for date: ", date)

			signal.alarm(30)
			try:
				filename = wget.download(url)
				print ("\n")
				time.sleep(5.5)
			except TimeoutException:
				print ("Timeout exception")
				f = open('congressional_records_timeout_exception_URLs.csv', 'a')
				try:
						f.write(u'%s\n' % (url))
				finally:
					f.close()
				continue

			except:
				time.sleep(5.5)
				print ("No congression record found, date: ", date)
				f = open('congressional_records_no_record_exception_URLs.csv', 'a')
				try:
						f.write(u'%s\n' % (url))
				finally:
					f.close()
				pass


	except:
		print ("An unexpected error occurred.")
		f = open('congressional_records_unexpected_exception_URLs.csv', 'a')
		try:
			f.write(u'%s\n' % (url))
		finally:
			f.close()
		pass

##Run Get Congressional Records
get_congressional_records()



