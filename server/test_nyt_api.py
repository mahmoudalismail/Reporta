from nytimesarticle import articleAPI
import datetime 
import time


# filter out op-eds
# figure out what is popular and not through the nytimes article API and not the most popular API

# prompt should be: Do you want to hear about 1,2,3,4,5?
# Response is trained to be : I want to hear more about x[subject matter] with basic string match 

# Response is trained to be : I want to hear more about the third




api = articleAPI('ae14e1d2f3c40ad244abceddb249d691:17:65860898')

pop_api = articleAPI('e2baeb5cd07d2b2d2c535d23de3300d9:4:65860898')

recent_articles = []



#list of keyword elements
'''
NYTimes
keywords": [{
                "rank": "1",
                "is_major": "N",
                "name": "organizations",
                "value": "Death by Audio (Brooklyn, NY, Music Venue)"
            },

'''

def get_date_today():
	start = str(datetime.date.today()-datetime.timedelta(70)).replace("-",'')
	return str(datetime.date.today()).replace("-",'')

def get_week_range():
	return str(datetime.date.today()-datetime.timedelta(70)).replace("-",''), str(datetime.date.today()).replace("-",'')


def get_recent_keywords():
	keywords = []
	recent_articles = sorted(recent_articles, key=lambda k: k['last_visit']) 

	for art in recent_articles:
		if art['keyword'] not in keywords:
			keywords.append(art['keyword'])
	return keywords

def isAlreadyFound(article):
	for art in recent_articles:
		if art['article']['_id'] == article['_id']:
			return True
	return False
	

def add_recent_article(keyword, article):
	entry = {}
	entry['keyword'] = keyword
	entry['article'] = article
	entry['last_visit'] = datetime.date.today()
	recent_articles.append(entry)

def get_articles(topic="",startdate=None, enddate=None, page=0, limit=1):
	good_articles = []
	
	# sort newest
	# returns the first clean article
	for i in range(20):
		if not startdate and not enddate:
			query = api.search( q = topic , page = page+i, sort='newest')

		else:
			query = api.search( q = topic, page = page+i, sort='newest', begin_date=startdate, end_date=enddate)#, fl={document_type:'article'})
		for art in query['response']['docs']:
			# if art['keywords'] and art['multimedia'] and art['abstract'] and art['snippet'] and art['abstract'] != art['snippet'] and not isAlreadyFound(art) and art['type_of_material']=='News':
			if (art['snippet'] or art['abstract']) and art['multimedia'] and art['type_of_material']=='News':
				good_articles.append(art)
			if len(good_articles)>=limit:
				return good_articles
	return good_articles


# def new_print(art):
# 	clean = {}
# 	clean['snippet'] = art['snippet']
# 	clean['web_url'] = art['web_url']
# 	clean['abstract'] = art['abstract']
# 	clean['multimedia'] = art['multimedia']
# 	clean['keywords'] = []
# 	for word in art['keywords']:
# 		clean['keywords'].append(word['value'])
# 	#change to just key words to list of just terms
# 	clean['pub_date'] = art['pub_date'][:10].replace("-",'')
# 	clean['type_of_material'] = art['type_of_material']
# 	clean['section_name'] = art['section_name']
# 	clean['headline'] = art ['headline']['main']
# 	clean['_id'] = art['_id']

# 	print clean

def clean_entry(art):
	clean = {}
	if art['snippet']:

		clean['snippet'] = art['snippet']
	else:
		clean['snippet'] = art['abstract']
	# clean['web_url'] = art['web_url']
	# clean['abstract'] = art['abstract']
	#clean['multimedia'] = art['multimedia']
	# clean['keywords'] = []
	# for word in art['keywords']:
	# 	clean['keywords'].append(word['value'])
	#change to just key words to list of just terms
	#clean['pub_date'] = art['pub_date'][:10].replace("-",'')
	#clean['type_of_material'] = art['type_of_material']
	#clean['section_name'] = art['section_name']
	clean['headline'] = art ['headline']['main']
	#clean['_id'] = art['_id']

	return clean

# def get_5_personal(keywords):
# 	# #replace with personal list of keywords
	
# 	# week_articles = []

# 	# articles = get_articles(topic = keyword, limit = 5)
# 	# for keyword in keywords:
# 	# 	articles = get_articles(topic=keyword)
# 	# 	if articles:
# 	# 		week_articles=week_articles+articles
# 	# 		# for a in articles:
# 	# 		# 	add_recent_article(keyword, a)

# 	week_articles = get_articles(topic = keyword, limit = 10)
# 	return week_articles


def get_5_specific(keyword):

	articles = get_articles(topic = keyword, limit = 5)
	# if articles:
	# 	for a in articles:
	# 		add_recent_article(keyword, a)

	return articles



# def main():
# 	recent_articles = []

# 	saved_articles = []

# 	keywords = ['Ferguson','Healthcare']

# 	# personal = get_5_personal()
# 	# for k in personal:
# 	# 	new_print(k)
# 	# print("\n"*(10))


# 	specific = get_5_specific("Russia")
# 	for s in specific:
# 		new_print(s)


	
	


# if __name__ == "__main__":
#     main()

	



