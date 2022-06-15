#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Last modified on Wednesday June 15 18:11 2022

@author: oscarpiette
"""

import sys, json, pysolr, re, os

# INPUT
paragraph_json = json.load(sys.stdin)

####### 1º Get the Paper JSON: #######
try:
    solr = pysolr.Solr('https://librairy.linkeddata.es/solr/cord19-papers', always_commit=True, timeout=50)
except Exception:
    sys.stderr.write("Error trying to access the solr repository, " + str(Exception))
    exit()
    
if type(paragraph_json["article_id_s"]) is list:
    article_id = paragraph_json["article_id_s"][0]
else:
    article_id = paragraph_json["article_id_s"]
    
article_search = solr.search('id:{}'.format(article_id))
for doc in article_search:
    article_json = doc

####### 2º Create the JSON file to send to the API: ########
output_json = {"paper": article_json, "paragraph": paragraph_json}

# OUTPUT
sys.stdout.write(json.dumps(output_json))
