import sys
import gcide
import psycopg2

import pgsql_config as config

tags_list = []
ctr = 0
connection = psycopg2.connect(host=config.host, dbname=config.dbname, user=config.user, password=config.password)
errors = []
def tagger(word, tags, defn):
	global tags_list, ctr, connection, errors
	if tags not in tags_list:
		tags_list.append(tags)
	ctr = ctr + 1
	cursor = connection.cursor()
	word = word.replace('\'', '"')
	defn = defn.replace('\'', '"')
	#try:
	cursor.execute('insert into gcide_sourced_data values(\'{}\', \'{}\', \'{}\');'.format(word, tags, defn))
	#except:
		##print(word, '\n', defn, '\n', len(defn))
		#errors.append((word, defn, len(defn), len(word)))
	print('Inserted : {}\t\t\t\r'.format(ctr), end='')

gcide.read(tagger)
connection.commit()
print('Completed commit. Check db.')
for tag in tags_list:
	print(tag)

print('Number of error words : ', len(errors))

with open('errors.txt', 'w') as error_file:
	for error in errors:
		error_file.write(error[0], error[1], '\n')

lw = 99999999999
uw = 0
ld = 99999999999
ud = 0
for i in errors:
	if i[3] > uw:
		uw = i[3]
	if i[3] < lw:
		lw = i[3]
	if i[2] > ud:
		ud = i[2]
	if i[2] < ld:
		ld = i[2]

print(ld, ud, lw, uw)
