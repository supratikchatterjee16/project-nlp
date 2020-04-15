import nltk
import psycopg2

import pgsql_config as config

connection = psycopg2.connect(host=config.host, dbname=config.dbname, user=config.user, password=config.password)
cursor = connection.cursor()
cursor2 = connection.cursor()
cursor.execute('select words from gcide_sourced_data;')
for val in cursor:
	x = val[0]
	try:
		x = x.replace('"','\'')
	except Exception as w:
		pass
	val_t = nltk.word_tokenize(val[0])
	tagged = nltk.pos_tag([val[0]])
	print(tagged)
	cursor2.execute('insert into nltk_map_check_table values(\'{}\', \'{}\')'.format(tagged[0][0], tagged[0][1]))
connection.commit()


#select gsd.words, gsd.tags, nmct.tag from gcide_sourced_data gsd, nltk_map_check_table nmct where gsd.words = nmct.words;
