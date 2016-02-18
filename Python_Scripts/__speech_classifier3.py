###################################
###                             ###
###      Joshua G. Mausolf      ###
###   Department of Sociology   ###
###    Computation Institute    ###
###    University of Chicago    ###
###                             ###
###################################

import re
import pandas as pd
import numpy as np
import glob
import os


##########################################################
#Preliminary Functions
##########################################################

def group_text(text, group_size):
    """
    groups a text into text groups set by group_size
    returns a list of grouped strings
    """
    word_list = text.split()
    group_list = []
    for k in range(len(word_list)):
        start = k
        end = k + group_size
        group_slice = word_list[start: end]
        # append only groups of proper length/size
        if len(group_slice) == group_size:
            group_list.append(" ".join(group_slice))
    return group_list
        

def remove_non_ascii_2(text):
	import re
	return re.sub(r'[^\x00-\x7F]+', "", text)


def read_speech(speechfile):
	speech = str(speechfile)
	f = open(speech, 'rU')
	raw = f.read().decode('utf8')
	raw1 = raw.replace('.', ' ')
	sent = remove_non_ascii_2(raw1)
	return sent

def get_url(speechfile):
	speech = str(speechfile)
	f = open(speech, 'rU')
	raw = f.read().decode('utf8')
	sent = remove_non_ascii_2(raw)
	url = sent.split('\n')[1]
	return url


def get_group_set(group_size, text):
	group_list = group_text(text, group_size)
	group_set = set(group_list)
	return group_set


def ngram(n, data):
	ngram = get_group_set(n, data)
	return ngram




##########################################################
#Speech Phrase Counter Functions
##########################################################

def speech_phrase_counter(ngram1, ngram2, ngram3, ngram4, terms):
	#print "FUNCTION TEST"
	for term in terms:
		for gram in ngram4:
			if term == gram:
				count = sent.count(gram)
				print "Count: ", count, "| ", gram
		for gram in ngram3:
			if term == gram:
				count = sent.count(gram)
				print "Count: ", count, "| ", gram
		for gram in ngram2:
			if term == gram:
				count = sent.count(gram)
				print "Count: ", count, "| ", gram
		for gram in ngram1:
			if term == gram:
				count = sent.count(gram)
				print "Count: ", count, "| ", gram

#speech_phrase_counter(ngram1, ngram2, ngram3, ngram4, terms)


def find_time(text):
	#Add Time to Data Frame
	try:
		try:
			time = re.findall(r'\d{1,2}:\d{1,2}\s[A-Z].[A-Z].+', sent)
			#time = time0[0].replace('P M ', 'PM').replace('A M ', 'AM')
			#df.ix[n, "TIME"] = time
			return time[0]
		except:
			try:
				time = re.findall(r'\d{1,2}:\d{1,2}\s[A-Z].[A-Z].+', sent)
				#df.ix[n, "TIME"] = time[0]
				return time[0]
			except:
				time = re.findall(r'\d{1,2}(?:(?:AM|PM)|(?::\d{1,2})(?:AM|PM)?)', sent)
				#df.ix[n, "TIME"] = time[0]
				return time[0]
	except:
		pass



def return_time(text):
	#Add Time to Data Frame
	try:
		try:
			time0 = re.findall(r'\d{1,2}:\d{1,2}\s[A-Z].[A-Z].+', sent)
			time = time0[0].replace('P M ', 'PM').replace('A M ', 'AM')
			#df.ix[n, "TIME"] = time
			return time
		except:
			try:
				time = re.findall(r'\d{1,2}:\d{1,2}\s[A-Z].[A-Z].+', sent)
				#df.ix[n, "TIME"] = time[0]
				return time[0]
			except:
				time = re.findall(r'\d{1,2}(?:(?:AM|PM)|(?::\d{1,2})(?:AM|PM)?)', sent)
				#df.ix[n, "TIME"] = time[0]
				return time[0]
	except:
		pass

def speech_phrase_counter2(ngram1, ngram2, ngram3, ngram4, terms, df, n):
	#print "FUNCTION TEST"
	for term in terms:
		for gram in ngram4:
			if term == gram:
				count = sent.count(gram)
				df.ix[n, term] = count
		for gram in ngram3:
			if term == gram:
				count = sent.count(gram)
				df.ix[n, term] = count
		for gram in ngram2:
			if term == gram:
				count = sent.count(gram)
				df.ix[n, term] = count
		for gram in ngram1:
			if term == gram:
				count = sent.count(gram)
				df.ix[n, term] = count

def speech_phrase_counter3(ngram1, ngram2, ngram3, ngram4, terms, df, n, sent):
	#print "FUNCTION TEST"
	for term in terms:
		for gram in ngram4:
			if term == gram:
				count = sent.count(gram)
				df.ix[n, term] = count
		for gram in ngram3:
			if term == gram:
				count = sent.count(gram)
				df.ix[n, term] = count
		for gram in ngram2:
			if term == gram:
				count = sent.count(gram)
				df.ix[n, term] = count
		for gram in ngram1:
			if term == gram:
				count = sent.count(gram)
				df.ix[n, term] = count



##########################################################
#Setup Data Frame
##########################################################



def speech_classifier(folder_name, ds1, ds2, output_file, terms, addtime=0, addloc=0, addcite=0):
	"""
	---------------------------------------------------------------
	Variables
	-	folder_name = path/name of folder where speeches are found
	---------------------------------------------------------------
	- 	ds1:ds2 	= - date slices of filenames
					E.g. the filename "2011-09-17_ID1.txt"
						would want date slices of
						ds1 = 0 and ds2 = 10
						This takes the string slice 0:10
						and provides a date = 2011-09-17
	---------------------------------------------------------------
	- output_file 	= the name of the desired CSV 
	---------------------------------------------------------------
	- terms			= the list of terms to look for in the speeches
	---------------------------------------------------------------


	"""


	#Setup Initial Data Frame
	header = ["DATE", "TIME", "LOCATION", "URL"]+terms
	index = np.arange(0)
	df = pd.DataFrame(columns=header, index = index)


	#Get Files in Folder
	#os.chdir("Speech_President")
	folder = str(folder_name)
	outfile = str(output_file)
	os.chdir(folder)	
	speech_files = glob.glob("*.txt")


	for speech in speech_files:
		date = speech[ds1:ds2]
		print "Analyzing speech file ", speech, "...", date
		n = len(df.index)

		#Add Row to Data Frame
		df.loc[n] = 0
		df.ix[n, "DATE"] = date


		sent = read_speech(speech)

		#Add Time to Data Frame
		if addtime == 1:
			time = return_time(sent)
			if len(str(time)) > 15:
				time = str(time)[0:12]
				#print "Exception ", time
			else:
				pass
			df.ix[n, "TIME"] = time
		else:
			pass


		#Add Location
		if addloc == 1:
			try:
				time_ = find_time(sent)
				location0 = sent
				location1 = location0.replace(time_, '|').split('|', 1)[0]
				location2 = location1.replace('\n\n', '|').replace('|\n', '|').replace('| ', '').split('|')
				X = len(location2)-2
				location3 = location2[X]
				location = location3.replace('\n', ', ').replace('\t', '')
			except:
				location = ''
				pass

			if len(str(location)) > 25:
				location = str(location)[0:35]
				print "Exception ", location
			else:
				pass
			df.ix[n, "LOCATION"] = location
		else:
			pass

		#Add Citation/URL
		if addcite == 1:
			url = get_url(speech)
			df.ix[n, "URL"] = url
		else:
			pass


		ngram1 = get_group_set(1, sent)
		ngram2 = get_group_set(2, sent)
		ngram3 = get_group_set(3, sent)
		ngram4 = get_group_set(4, sent)

		speech_phrase_counter3(ngram1, ngram2, ngram3, ngram4, terms, df, n, sent)

	os.chdir("..")

	print df
	df.to_csv(outfile, encoding='utf-8')
	return df


#speech_classifier("Congressional_Records", "Congressional_Records_data.csv")


"""
Right now the speech terms are globally defined. Make the parser require a list of speech terms. 
Then you can have a separate file for each one. 
Define the list of terms.
Run the parser.

"""




