# The files that can be found in the WikiMIDs are not exactly CSV compliant formats, 
# and would require me to write utilities to extract and store relevant information from them.

import os
import re
import traceback


#def get_segments(line, start_char, end_char):
	#segments = []
	#brackets = []
	#if '[' in line:
		#for index in range(0, len(line)):
			#if line[index] == start_char:
				#brackets.append(index)
			#if line[index] == end_char:
				#try:
					#start = brackets.pop()
				#except:
					#print()
				#segments.append(line[start+1:index])
	#segments.sort(key=len)
	#return segments

def dictionary_level1_filter(line):
	string = ''
	ctr1= 0
	for i in line:
		if i == '[' or i == '(' or i == '{':
			ctr1 = ctr1 + 1
		if ctr1 == 1:#Main segment
			string = string + i
		if i == ']' or i == ')' or i == '}':
			ctr1 = ctr1 - 1
	return string

def read_gcide(func):
	base_dir = '/home/supratik/Documents/programming/python/nlp/dicts_and_thesarus'
	gcide = os.path.join(base_dir,'gcide')
	file_list = os.listdir(gcide)
	file_list = [i for i in file_list if i.startswith('directory') and i.endswith('.csv')]
	file_list.sort()
	file_list.sort(key=len)
	lookout = ['a.', 'acc.', 'act.', 'adp.', 'adv.', 'adj.', 'comp.', 'compar.', 'conj.', 'contr.', 'dat.', 'imp.', 'interj.', 
			'n.', 'neut.', 'nom.', 'p.', 'phr.', 'pl.', 'pr.', 'prefix.', 'prep.', 'prop.', 'pron.', 't.', 'v.', 'vb.', 'inf.', 'E.', 'L.']
	regexpattern = re.compile('[a-z]+[.]')
	types = []
	for filename in file_list:
		with open(os.path.join(gcide, filename), 'r') as file:
			for line in file.readlines():
				word = line[0:line.index('\t')]
				line = line.replace(r'\n', ' ')
				filtered = dictionary_level1_filter(line[line.index('\t') + 1 :])
				if filtered.startswith('[01') and '\\' in filtered:
					regex_satisfy = regexpattern.findall(filtered)
					#print(word)
					if len(regex_satisfy) == 0 or regex_satisfy[0] not in lookout:
							# print(word,regex_satisfy)
							pass
					else:
						tags = ''
						check = ''
						for element in regex_satisfy:
							if element in lookout:
								tags = tags + element + ' '
								check = element
							else:
								break
						tags = tags.strip()
						filtered = filtered[filtered.index(check) + len(check): len(filtered) - 1]
						#filtered = filtered.replace('\n','')
						filtered = re.sub(r'[0-9]+.[ ]+', '\n', filtered)
						#filtered = re.sub(r'[;]+', '\n', filtered)
						filtered = re.sub(r'(See)+[ ]*(under[ ]*)*[.,][ ]*', '', filtered)
						#filtered = re.sub(r'(same)+[ ]*(as[ ]*)*[.][ ]*', '', filtered)
						filtered = filtered.strip()
						if tags not in types:
							types.append(tags)
						#print('Successful\nWord : ',word, '\nTags : ', tags, '\ndefn. : ', filtered)
						func(word, tags, filtered)
						#print(line)
						#print('------------------------------------------------------------------------------------------------------------')
						#print('Completed : {}        '.format(total), end='\r')

if __name__ == '__main__':
	def xyz(a, b, c):
		print(a, '\n', b, '\n', c)
	read_gcide(xyz)
