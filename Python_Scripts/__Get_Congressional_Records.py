##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################

#Could possibly also look at VP, Press Conferences, etc

def getURL(date):

	#base_url = "http://www.whitehouse.gov/briefing-room/Speeches-and-Remarks/"+year+"/"+month
	#base_url = "https://www.gpo.gov/fdsys/pkg/CREC-"+year+"-"+month+"-"+day+"/pdf/CREC-"+year+"-"+month+"-"+day+".pdf"

	base_url = "https://www.gpo.gov/fdsys/pkg/CREC-"+date+"/pdf/CREC-"+date+".pdf"

	#https://www.gpo.gov/fdsys/pkg/CREC-2011-09-21/pdf/CREC-2011-09-21.pdf
	print base_url


def getfullURL(date):
	base_url = "https://www.gpo.gov/fdsys/pkg/CREC-"+date+"/pdf/CREC-"+date+".pdf"
	return base_url


def getdates(yr1=2009, yr2=2016, month1=1, month2=12, day1=1, day2=31):

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

	#x = (list(itertools.product(req_years, req_months)))
	x = (list(itertools.product(req_years, req_months, req_days)))
	#print x
	return x

#getdates()

def getcongressURLs():

	#x = (list(itertools.product(req_years, req_months)))
	x = getdates()

	f = open('congressional_records_URLs2.csv', 'w')
	try:
		for dt in range(0, len(x)):
			date = str(x[dt]).replace("'", "").replace(",", "-").replace(" ", "").replace("(", "").replace(")", "")
			#print date
			full_url = getfullURL(date)
			print full_url
			f.write(u'%s\n' % (full_url))
	finally:
		f.close()

#getcongressURLs()


def getparentURLs(yr1=2009, yr2=2016, month1=1, month2=12, day1=1, day2=31):

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

	#x = (list(itertools.product(req_years, req_months)))
	x = (list(itertools.product(req_years, req_months, req_days)))

	f = open('congressional_records_URLs.csv', 'w')
	try:
		for dt in range(0, len(x)):
			date = str(x[dt]).replace("'", "").replace(",", "-").replace(" ", "").replace("(", "").replace(")", "")
			full_url = getfullURL(date)
			f.write(u'%s\n' % (full_url))
	finally:
		f.close()


#getparentURLs()

import signal

class TimeoutException(Exception):   # Custom exception class
    pass

def timeout_handler(signum, frame):   # Custom signal handler
    raise TimeoutException

# Change the behavior of SIGALRM
signal.signal(signal.SIGALRM, timeout_handler)


def get_congressional_records():

	import sys, csv, time, os, subprocess, wget
	sys.path.append('../Python_Scripts/')
	sys.path.append('..')

	#import wget
    #url = 'http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3'

    #filename = wget.download(url)

	#os.chdir('bash_Speech')
	#os.chdir('Speech_President')
	try:
		os.mkdir("Congressional_Records")
	except:
		pass

	os.chdir("Congressional_Records")
	#getcongressURLs()

	x = getdates()
	#print x

	#f = open('congressional_records_URLs2.csv', 'w')
	try:
		for dt in range(0, len(x)):
		#for dt in range(300, 350):
			date = str(x[dt]).replace("'", "").replace(",", "-").replace(" ", "").replace("(", "").replace(")", "")
			url = str(getfullURL(date))
			print "Downloading congressional record for date: ", date

			signal.alarm(20)
			try:
				filename = wget.download(url)
				print "\n"
				time.sleep(5.5)
			except TimeoutException:
				print "Timeout exception"
				f = open('congressional_records_exception_URLs.csv', 'a')
				try:
						f.write(u'%s\n' % (url))
				finally:
					f.close()
				continue # continue the for loop if function A takes more than 5 second

			except:
				time.sleep(5.5)
				print "No congression record found, date: ", date
				f = open('congressional_records_exception_URLs.csv', 'a')
				try:
						f.write(u'%s\n' % (url))
				finally:
					f.close()
				pass


	except:
		print "An unexpected error occurred."
		f = open('congressional_records_exception_URLs.csv', 'a')
		try:
			f.write(u'%s\n' % (url))
		finally:
			f.close()
		pass





get_congressional_records()



