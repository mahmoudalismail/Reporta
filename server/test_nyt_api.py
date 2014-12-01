from nytimesarticle import articleAPI
import datetime
import time

api = articleAPI('ae2b43b298972426c8e43a96afcb9aaa:0:70254909')

def clean_entry(art):
	clean = {}
	if art['abstract']:
		clean['snippet'] = art['abstract'].encode('ascii', 'ignore')
	else:
		clean['snippet'] = art['snippet'].encode('ascii', 'ignore')
	clean['url'] = art['web_url']
	clean['multimedia'] = "http://www.nytimes.com/"+str(art['multimedia'][1]['url'])
	clean['keywords'] = []
	for word in art['keywords']:
		clean['keywords'].append(word['value'].encode('ascii', 'ignore'))
	clean['headline'] = art ['headline']['main'].encode('ascii', 'ignore')
	return clean

def get_articles(cb, so_far=[], topic=None, page=0, limit=5):
        def respond_get_articles(payload):
                if not payload:
                    cb(None)

                good_articles = []
                for art in payload['response']['docs']:
                        if (art['snippet'] or art['abstract']) and art['multimedia'] and art['type_of_material'] in ["News", "Editorial"]:
                                good_articles.append(clean_entry(art))
                good_articles += so_far
                if len(good_articles) >= limit:
                        cb(good_articles)
                else:
                        get_articles(cb, so_far=good_articles, topic=topic, page=(page+1), limit=limit)
        if topic:
                api.search(respond_get_articles, q = topic, page = page, sort="newest")
        else:
                api.search(respond_get_articles, sort='newest', page=page)
