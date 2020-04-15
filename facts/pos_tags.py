import nltk
print(nltk.help.upenn_tagset())
# we don't go back, we make sure we have more than originally stated
pos_tags = {
	'ADJ'   : 'adjective',
	'ADP'   : 'adposition',
	'ADV'   : 'adverb',
	'AUX'   : 'auxiliary',
	'CCONJ' : 'coordinating conjunction',
	'DET'   : 'determiner',
	'INTJ'  : 'interjection',
	'NOUN'  : 'noun',
	'NUM'   : 'numeral',
	'PART'  : 'particle',
	'PRON'  : 'pronoun',
	'PROPN' : 'proper noun',
	'PUNCT' : 'punctuation',
	'SCONJ' : 'subordinating conjunction',
	'SYM'   : 'symbol',
	'VERB'  : 'verb',
	'X'     : 'other'
	}

#Conjunctions
cconj_list = ['for', 'and', 'nor', 'but', 'or', 'yet', 'so'] #fanboys, coordinating conjunctions
sconj_list = ['while', 'as soon as', 'although', 'before', 'even if', 'because', 'no matter how', 'whether', 'wherever', 'when', 'until', 'after', 'as if', 'how', 'if', 'provided', 'in that', 'once', 'supposing', 'while', 'unless', 'in case', 'as far as', 'now that', 'as', 'so that', 'though', 'since']

corrconj_list = ['either*or', 'neither*nor', 'not only*but also', 'both*and', 'whether*or', 'so*as']
conjadv_list = ['in addition', 'for example', 'however', 'therefore', 'on the contrary', 'hence', 'in fact', 'otherwise', 'as a result', 'indeed', 'still', 'thus', 'on the other hand', 'furthermore', 'instead', 'incidentally', 'after all', 'finally', 'likewise', 'meanwhile', 'consequently']

#Adverbs
advm_list = []# Manner, How?
advp_list = []# Place, Where?
advt_list = []# Time, When?
advd_list = []# Degree, intensity

wdt_list = ['which']
wp_list = ['who', 'what']
wp$_list = ['whose']
wrb_list = ['where', 'when']
