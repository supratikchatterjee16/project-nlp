import os
import sys
from nltk.tokenize import word_tokenize
import source.gcide.gcide as gcide
import psycopg2

from config import pgsql_config as sqlconfig

connection = psycopg2.connect(host=sqlconfig.host, dbname=sqlconfig.dbname, user=sqlconfig.user, password=sqlconfig.password)

def extract_words_tags():
	base_dir = '/home/supratik/Documents/programming/python/nlp/nlp data/dicts_and_thesarus'
	gcide = os.path.join(base_dir,'gcide')
	file_list = os.listdir(gcide)
	file_list = [i for i in file_list if i.startswith('directory') and i.endswith('.csv')]
	file_list.sort()
	file_list.sort(key=len)
	
	ctr = 0
	for filename in file_list:
		with open(os.path.join(gcide, filename), 'r') as file:
			for line in file.readlines():
				line = line.replace(r'\n', ' ')
				word = line[0 : line.index('\t')]
				tokens = word_tokenize(line) # problem at this front. Sometimes it reads '.' as a different token, sometimes it doesn't
				#possible_required = [token for token in tokens if token.endswith('.') and len(token) > 1]
				#possible_required = list(dict.fromkeys(possible_required))
				print(word, tokens)
				ctr += 1
				#if ctr > 10 :
					#break
		break

def run():
	extract_words_tags()
