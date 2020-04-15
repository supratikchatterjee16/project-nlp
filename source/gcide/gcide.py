import os
import re

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

def read(func):
	base_dir = '/home/supratik/Documents/programming/python/nlp/dicts_and_thesarus'
	gcide = os.path.join(base_dir,'gcide')
	file_list = os.listdir(gcide)
	file_list = [i for i in file_list if i.startswith('directory') and i.endswith('.csv')]
	file_list.sort()
	file_list.sort(key=len)
	lookup_list = ['a.', 'acc.', 'act.', 'adp.', 'adv.', 'adj.', 'comp.', 'compar.', 'conj.', 'contr.', 'dat.', 'imp.', 'interj.', 
			'n.', 'neut.', 'nom.', 'p.', 'phr.', 'pl.', 'pr.', 'prefix.', 'prep.', 'prop.', 'pron.', 't.', 'v.', 'i.', 'vb.', 'inf.', 'E.', 'L.', 'G.']
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
					if len(regex_satisfy) == 0 or regex_satisfy[0] not in lookup_list:
							# print(word,regex_satisfy)
							pass
					else:
						tags = ''
						check = ''
						for element in regex_satisfy:
							if element in lookup_list:
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
 
