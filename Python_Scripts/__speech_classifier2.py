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
	return re.sub(r'[^\x00-\x7F]+', "'", text)


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
#Establish Keyword Categories with Keywords/Phrases
##########################################################

wall_street = ["lobby", "lobbying", "lobbies", "special interest", "special interests", "revolving door", "campaign donor", "campaign donation", "campaign donations", "bidder", "highest bidder", "campaign contributions", "loophole", "loopholes", "tax shelter", "tax evasion", "write their own rules", "own rules", "Wall Street", "bailout", "bailouts"]

corporate_greed = ["cheat", "cheating", "stacked against", "stacked up against", " stacked against", "good benefits", "decent salary", "stack the deck", "deck got stacked against", "exploit", "exploiting",  "protect workers", "protecting workers", "protect laborers", "protecting laborers", "protect Americans", "protecting Americans", "protect employee", "protect employees", "protecting employees", "work safe", "working safely", "safe at work", "work conditions", "innocent", "minimum wage", "pollute", "polluting", "regulate", "regulating", "federal oversight", "financial reform", "gambling", "derivative", "derivatives", "sub-prime", "risky investment", "risky investments", "bust unions", "union", "unions", "labor unions", "dirtiest air", "cheapest labor", "wages", "workplace safety", "Consumer Finance Protection Bureau", "consumer protection", "unions", "union label", "union workers", "CEO", "CEO's", "corporation", "corporations"]


inequality = ["wealth", "wealthy", "income equality", "income inequality", "inequality", "privileged", "rich", "1%", "1 percent", "one percent", "99%", "99 percent", "ninety-nine percent", "ninety nine percent", "fair", "unfair", "fairness", "unfairness", "middle-class", "middle class", "working class", "working-class", "lower class", "poor", "poverty", "rich", "upper class", "equity", "inequity", "egalitarian", "disparity", "unequal", "average American", "average Americans", "Wall Street", "Main Street", "main street", "50 million", " Warren Buffet", "Warren Buffett's secretary", "secretary", "class warfare", "class warefare", "warrior for the middle class", "Giving everybody a shot", "giving everybody a shot", "everybody a fair shot", "work your way up", "working your way up", "starting at the bottom", "blood, sweat and tears", "blood sweat and tears", "blood, sweat, and tears", "willing to work hard", "fair and just", "everybody is included", " folks at the top", "folks at the bottom"]

fair_share = ["fair shot", "fair shake", "gets a fair shake", "pay their fair share", "our fair share", "fair share"]

occupy = ["occupy", "occupying", "OWS", "Occupy Wall Street"]


#Top Keywords Listed by OWS Protestors 
#Keywords kepts if >=5 responses for first, second, and third, choices
#These were pooled, and duplicates removed.
#http://occupyresearch.net/orgs/
OWS_survey = ["income inequality", "inequality", "economic conditions", "corruption", "justice", "corporate influence in politics", "corporations", "corporate personhood", "injustice", "social justice", "corporate greed", "anti-capitalism", "greed", "unemployment", "citizens united", "equality", "money in politics", "government corruption", "poverty", "environmental concerns", "democracy", "fairness", "freedom", "change", "inequity", "jobs", "money out of politics", "health care", "financial reform", "solidarity", "war", "movement building", "foreclosures", "frustration", "banks", "politics", "curiosity", "money", "campaign finance reform", "climate change", "education", "disparity", "bailouts", "future", "anger", "hope", "revolution", "humanity", "equity", "children", "police brutality", "rights", "community", "Oligarchy", "0.99", "fascism", "freedom of speech", "food", "civil liberties", "taxes", "peace", "plutocracy", "love", "corporate corruption", "joblessness", "campaign finance", "fraud", "Wall Street", "human rights", "compassion", "accountability", "NDAA", "debt", "tax the rich", "lobbyists", "broken political system", "agreement", "inequality", "corruption", "economy", "justice", "environment", "income inequality", "economic inequality", "healthcare", "capitalism", "corporatism", "economics", "social injustice", "income disparity", "political corruption", "government", "economic justice", "economic disparity", "economic injustice", "civil rights", "wealth disparity", "oppression", "racism", "patriarchy", "sustainability", "homelessness", "corporate power", "workers rights", "student loans", "wall street", "corrupt government", "exploitation", "accountability", "housing", "patriotism", "apathy", "responsibility", "corporations"]

other_terms = ["jobs", "economy", "unemployment"]

terms = wall_street+corporate_greed+inequality+fair_share+occupy+OWS_survey+other_terms


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



def speech_classifier(folder_name, output_file, addtime=0, addloc=0, addcite=0):

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
		print "Analyzing speech file ", speech, "..."
		date = speech.split('-', 1)[1].replace(".txt", "")
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


speech_classifier("Congressional_Records", "Congressional_Records_data.csv")

