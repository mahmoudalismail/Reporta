from nytimesarticle import articleAPI
import datetime 
import time

# filter out op-eds
# figure out what is popular and not through the nytimes article API and not the most popular API

api = articleAPI('ae14e1d2f3c40ad244abceddb249d691:17:65860898')

pop_api = articleAPI('e2baeb5cd07d2b2d2c535d23de3300d9:4:65860898')



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


def get_recent_keywords(articles):
	

def add_recent_keywords(articles):


def get_articles(topic="",startdate="null", enddate="null"):
	good_articles = []
	
	elif not startdate and not enddate:
		query = api.search( q = topic )
	else:
		query = api.search( q = topic)
	
	for art in query['docs']:
		if art['snippet'] != art['abstract'] and art['abstract'] != null and art['multimedia']!=[]:
			good_articles.append(art)
	return good_articles

def get_popular_articles():
	query = pop_api.search() #CHECK THIS !!!!
	good_articles = []

	for art in query['results']:
		if art['abstract'] != null and art['media'] != []:
			good_articles.append(art)

	return good_articles



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
		clean_articles.append(clean)
	for clean in clean_articles:
		for j in clean:
			print(j)
		print("\n")

def print_pop_articles(articles):
	clean_articles = []
	for art in articles:
		clean = {}
		clean['snippet'] = art['title']
		clean['web_url'] = art['url']
		clean['abstract'] = art['abstract']
		clean['multimedia'] = art['media']
		clean['keywords'] = []
		if not art['des_facet']:
			clean['keywords'].append(art['des_facet'])
		if not art['org_facet']:
			clean['keywords'].append(art['des_facet'])
		if not art['per_facet']:
			clean['keywords'].append(art['des_facet'])
		if not art['geo_facet']:
			clean['keywords'].append(art['des_facet'])
		clean['pub_date'] = art['published_date'].replace("-",'')
		clean['type_of_material'] = art['type_of_material']
		clean['section_name'] = art['section']
		
		clean_articles.append(clean)

	for clean in clean_articles:
		for j in clean:
			print(j)
		print("\n")

def main():

	#get from this week
	topic = 'Ferguson'
	startdate,enddate = get_week_range()
	week_articles = get_articles(topic, startdate, enddate)
	add_recent_keywords(week_articles)
	print_articles(week_articles)

	#get from today
	today_articles = get_articles(topic)
	add_recent_keywords(today_articles)
	print_articles(today_articles)


	#get popular
	popular_articles = get_popular_articles()
	add_recent_keywords(popular_articles)
	print_pop_articles(popular_articles)

	



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


