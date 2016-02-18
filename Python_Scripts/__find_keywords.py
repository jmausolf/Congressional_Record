###################################
###                             ###
###      Joshua G. Mausolf      ###
###   Department of Sociology   ###
###    Computation Institute    ###
###    University of Chicago    ###
###                             ###
###################################


from __speech_classifier3 import *

##########################################################
#Example Keyword Categories with Keywords/Phrases
##########################################################

#Example

wall_street = ["lobby", "lobbying", "lobbies", "special interest", "special interests", "revolving door", "campaign donor", "campaign donation", "campaign donations", "bidder", "highest bidder", "campaign contributions", "loophole", "loopholes", "tax shelter", "tax evasion", "write their own rules", "own rules", "Wall Street", "bailout", "bailouts"]

corporate_greed = ["cheat", "cheating", "stacked against", "stacked up against", " stacked against", "good benefits", "decent salary", "stack the deck", "deck got stacked against", "exploit", "exploiting",  "protect workers", "protecting workers", "protect laborers", "protecting laborers", "protect Americans", "protecting Americans", "protect employee", "protect employees", "protecting employees", "work safe", "working safely", "safe at work", "work conditions", "innocent", "minimum wage", "pollute", "polluting", "regulate", "regulating", "federal oversight", "financial reform", "gambling", "derivative", "derivatives", "sub-prime", "risky investment", "risky investments", "bust unions", "union", "unions", "labor unions", "dirtiest air", "cheapest labor", "wages", "workplace safety", "Consumer Finance Protection Bureau", "consumer protection", "unions", "union label", "union workers", "CEO", "CEO's", "corporation", "corporations"]


inequality = ["wealth", "wealthy", "income equality", "income inequality", "inequality", "privileged", "rich", "1%", "1 percent", "one percent", "99%", "99 percent", "ninety-nine percent", "ninety nine percent", "fair", "unfair", "fairness", "unfairness", "middle-class", "middle class", "working class", "working-class", "lower class", "poor", "poverty", "rich", "upper class", "equity", "inequity", "egalitarian", "disparity", "unequal", "average American", "average Americans", "Wall Street", "Main Street", "main street", "50 million", " Warren Buffet", "Warren Buffett's secretary", "secretary", "class warfare", "class warefare", "warrior for the middle class", "Giving everybody a shot", "giving everybody a shot", "everybody a fair shot", "work your way up", "working your way up", "starting at the bottom", "blood, sweat and tears", "blood sweat and tears", "blood, sweat, and tears", "willing to work hard", "fair and just", "everybody is included", " folks at the top", "folks at the bottom"]

fair_share = ["fair shot", "fair shake", "gets a fair shake", "pay their fair share", "our fair share", "fair share"]

occupy = ["occupy", "occupying", "OWS", "Occupy Wall Street"]

combined_terms = wall_street+corporate_greed+inequality+fair_share+occupy


##########################################################
#Define Your Own Keyword Categories with Keywords/Phrases
##########################################################

guns = ["_start", "firearm", "guns", "gun", "automatic weapons", "automatic weapon", "cheap handguns", "handguns", "shotgun", "shotguns", "rifle", "rifles", "Saturday night special", "high capacity magazines", "assualt rifles", "sawed off shotguns", "silencers", "AK-47s", "AR15", "AR-15s", "Glock", "Glocks"]

gun_laws = ["Second Amendment", "right to bear arms", "gunshow loophole", "gunshow", "gun dealer", "gun ownership", "gun sales", "gun manufacturers", "background check", "concealed carry", "ATF", "National Rifle Association", "NRA"]

gun_violence = ["mass shooting", "shootings", "guns don't kill people", "gun violence", "gunned down"]

shootings = ["Newtown", "San Bernardino", "Blacksburg", "Navy Yard", "Aurora", "Tucson", "Virginia Tech", "Fort Hood", "Charleston", "_end"]

gun_terms = guns+gun_laws+gun_violence+shootings


##########################################################
#Run 
##########################################################

#speech_classifier("Congressional_Records", "Congressional_Records_data.csv", wall_street)

#filepath = "/Box Sync/Mausolf_Joshua_Congressional_Speech_HW6/Congressional_Records_Text"
speech_classifier("Congressional_Records_Text", 5, 15, "Crec_Shootings.csv", gun_terms)
#speech_classifier("President", 0, 10, "Pres_Small_Shootings.csv", gun_terms)


import sys, os
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re


#______________ FUNCTIONS __________________________#

def camel_to_snake(column_name):
    """
    Converts a string that is camelCase into snake_case
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', column_name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def bar(variable, dataset):

	#Define Data
	data = pd.read_csv(dataset, index_col=0, low_memory=False)
	data.columns = [camel_to_snake(col) for col in data.columns]

	#Generate Graph
	fig =data.groupby(variable).size().plot(kind='bar')
	fig.set_xlabel(variable) #defines the x axis label
	fig.set_ylabel('Number of Observations') #defines y axis label
	fig.set_title(variable+' Distribution') #defines graph title
	plt.draw()
	plt.savefig(variable+"_bar.jpg")
	plt.close('all')

#bar("guns", "Pres_Small_Shootings.csv")

"""
df = pd.read_csv("Pres_Small_Shootings.csv", index_col=0, low_memory=False)

df3 = pd.DataFrame(np.random.randn(1000, 2), columns=['B', 'C']).cumsum()

df3['A'] = pd.Series(list(range(len(df))))

df3.plot(x='A', y='B')
"""
