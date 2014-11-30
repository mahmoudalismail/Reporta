from nytimesarticle import articleAPI
import datetime
import time

api = articleAPI('ae14e1d2f3c40ad244abceddb249d691:17:65860898')

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

def get_articles(cb, so_far=[], topic=None,startdate=None, enddate=None, page=0, limit=5):
        def respond_get_articles(payload):
                good_articles = []
                for art in payload['response']['docs']:
                        if art['keywords'] and (art['snippet'] or art['abstract']) and art['multimedia'] and art['type_of_material']=='News':
                                good_articles.append(clean_entry(art))
                good_articles += so_far
                if len(good_articles) >= limit:
                        cb(good_articles)
                else:
                        get_articles(cb, so_far=good_articles, topic=topic, startdate=startdate,
                                    enddate=enddate, page=(page+1), limit=limit)


        if not startdate and not enddate:
                api.search(respond_get_articles, q = topic , page = page, sort='newest')
        elif not topic:
                api.search(respond_get_articles, sort='newest')
        else:
                api.search(respond_get_articles, q = topic, page = page, sort='newest', begin_date=startdate, end_date=enddate)#, fl={document_type:'article'})
