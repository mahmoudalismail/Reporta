from nytimesarticle import articleAPI
import datetime 
import time

api = articleAPI('ae14e1d2f3c40ad244abceddb249d691:17:65860898')

def get_articles(topic=None,startdate=None, enddate=None, page=0, limit=1):
	good_articles = []
	
	for i in range(20):
		if not startdate and not enddate:
			query = api.search( q = topic , page = page+i, sort='newest')
		elif not topic:
			query = api.search(sort='newest')
			print query
		else:
			query = api.search( q = topic, page = page+i, sort='newest', begin_date=startdate, end_date=enddate)#, fl={document_type:'article'})
		for art in query['response']['docs']:
			if art['keywords'] and (art['snippet'] or art['abstract']) and art['multimedia'] and art['type_of_material']=='News':
				good_articles.append(art)
			if len(good_articles)>=limit:
				return good_articles
	return good_articles

def clean_entry(art):
	clean = {}
	if art['abstract']:
		clean['snippet'] = art['abstract'].encode('ascii', 'ignore')
	else:
		clean['snippet'] = art['snippet'].encode('ascii', 'ignore')
	# clean['web_url'] = art['web_url']
	# clean['abstract'] = art['abstract']
	clean['multimedia'] = art['multimedia']
	clean['keywords'] = []
	for word in art['keywords']:
		clean['keywords'].append(word['value'].encode('ascii', 'ignore'))
	#change to just key words to list of just terms
	#clean['pub_date'] = art['pub_date'][:10].replace("-",'')
	#clean['type_of_material'] = art['type_of_material']
	#clean['section_name'] = art['section_name']
	clean['headline'] = art ['headline']['main'].encode('ascii', 'ignore')
	#clean['_id'] = art['_id']

	return clean

def get_5_specific(keyword):

	articles = get_articles(topic = keyword, limit = 5)
	# if articles:
	# 	for a in articles:
	# 		add_recent_article(keyword, a)

	return articles

def get_general():
	articles = get_articles(limit = 15)

	return articles


