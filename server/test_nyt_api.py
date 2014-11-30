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
	for art in recent_articles:
		keywords.append(art['keyword'])
	return keywords
	

def add_recent_article(keyword, article):
	entry = {}
	entry['keyword'] = keyword
	entry['article'] = article
	entry['last_visit'] = datetime.date.today()
	recent_articles.append(entry)

#headline, snippet, abstract, keywords

def get_articles(topic="",startdate="null", enddate="null", page=0):
	good_articles = []
	
	# sort newest
	# returns the first clean article
	for i in range(10):
		if not startdate and not enddate:
			query = api.search( q = topic , page = page+i, sort='newest')
		else:
			query = api.search( q = topic, page = page+i, sort='newest', begin_date=startdate, end_date=enddate)#, fl={document_type:'article'})
	
		for art in query['response']['docs']:
			if art['keywords'] and art['multimedia'] and art['abstract'] and art['snippet'] and art['abstract'] != art['snippet'] :
			#if art['snippet'] and art['abstract'] and art['snippet'] != art['abstract'] and art['multimedia'] :
			# if art['snippet'] != art['abstract'] and art['abstract'] and art['multimedia']!=[]:
				# good_articles.append(art)
				# return good_articles
				return art



# def elaine_print_articles(articles):
# 	for art in articles:

def new_print(art):
	clean = {}
	clean['snippet'] = art['snippet']
	clean['web_url'] = art['web_url']
	clean['abstract'] = art['abstract']
	clean['multimedia'] = art['multimedia']
	clean['keywords'] = []
	for word in art['keywords']:
		clean['keywords'].append(word['value'])
	#change to just key words to list of just terms
	clean['pub_date'] = art['pub_date'][:10].replace("-",'')
	clean['type_of_material'] = art['type_of_material']
	clean['section_name'] = art['section_name']
	clean['headline'] = art ['headline']['main']

	print clean

def print_articles(articles):
	clean_articles = []
	for art in articles:
		clean = {}
		clean['snippet'] = art['snippet']
		clean['web_url'] = art['web_url']
		clean['abstract'] = art['abstract']
		clean['mutlimedia'] = art['mutlimedia']
		clean['keywords'] = art['keywords'] #change to just key words to list of just terms
		clean['pub_date'] = art['pub_date'][:10].replace("-",'')
		clean['type_of_material'] = art['type_of_material']
		clean['section_name'] = art['section_name']
		clean['headline'] = art ['headline']['main']
		clean_articles.append(clean)
	for clean in clean_articles:
		for j in clean:
			print(j)
		print("\n")

# def get_popular_articles():
# 	query = pop_api.search() #CHECK THIS !!!!
# 	good_articles = []

# 	for art in query['results']:
# 		if art['abstract'] != null and art['media'] != []:
# 			good_articles.append(art)

# 	return good_articles

# def print_pop_articles(articles):
# 	clean_articles = []
# 	for art in articles:
# 		clean = {}
# 		clean['snippet'] = art['title']
# 		clean['web_url'] = art['url']
# 		clean['abstract'] = art['abstract']
# 		clean['multimedia'] = art['media']
# 		clean['keywords'] = []
# 		if not art['des_facet']:
# 			clean['keywords'].append(art['des_facet'])
# 		if not art['org_facet']:
# 			clean['keywords'].append(art['des_facet'])
# 		if not art['per_facet']:
# 			clean['keywords'].append(art['des_facet'])
# 		if not art['geo_facet']:
# 			clean['keywords'].append(art['des_facet'])
# 		clean['pub_date'] = art['published_date'].replace("-",'')
# 		clean['type_of_material'] = art['type_of_material']
# 		clean['section_name'] = art['section']
		
# 		clean_articles.append(clean)

# 	for clean in clean_articles:
# 		for j in clean:
# 			print(j)
# 		print("\n")

def main():

	keywords = ['Ferguson','Healthcare']
	while True:

		
		#5 get from this week
		startdate,enddate = get_week_range()
		week_articles = []
		for keyword in keywords:
			if keyword not in get_recent_keywords():
				article = get_articles(keyword, startdate, enddate, 1)
				week_articles.append(article)
				new_print(article)
				add_recent_article(keyword, article)

		print("\n"*10)
		p = raw_input("Would you like more?")
		for a in recent_articles:
			new_print(a['article'])
		keywords.append(p)
		print(keywords)

if __name__ == "__main__":
    main()

	#5 get from today, preferences


	#get from today

	# today_articles = get_articles(topic)
	# add_recent_keywords(today_articles)
	# print_articles(today_articles)




	#get popular
	# popular_articles = get_popular_articles()
	# add_recent_keywords(popular_articles)
	# print_pop_articles(popular_articles)

	



#5 headlines about a topic




#5 headlines about a topic with time frame


#5 headlines about a location

#Given headline provide summary

#Given headline provide visuals, media, audio, video

#Give relevant articles based on Keywords mentioned, log keywords





'''

Snippets
Keywords

start date
end date
video/audio clips from type_of_source

queries:
most popular
Top 5

'''



