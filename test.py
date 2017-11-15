# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:32:29 2017

@author: Daniel
"""

import praw
import csv
import re
reddit = praw.Reddit(client_id='YcfxGiBKgBL_TA',
                     client_secret='R0CMG-edo8RVXnPdMcLuxDFRT80',
                     password='',
                     user_agent='testscript by /u/',
                     username='')
with open('Conservative.csv','w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_NONE, escapechar = ' ')
    for comment in reddit.subreddit('Conservative').stream.comments():
        csvdata = [re.sub('[,\n]', '', comment.body),'1']
        spamwriter.writerow(csvdata)