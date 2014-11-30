import tornado.httpclient
import tornado.gen
import test_nyt_api
import random



class NYTimes():

    def __init__(self):
        self.recent_article_tuples = []
        #self.saved_articles = []

    @staticmethod
    @tornado.gen.coroutine
    def redis_get_headlines(self,callback, topic=None, keywords=None):
        pass

    def get_personal_keywords(self):
        spare_keywords = ['Al Jazeera', 'Russia', 'Water','Obama','Healthcare','Ferguson','Fire']
        keywords = []
        if self.recent_article_tuples:
            for art in random.shuffle(self.recent_article_tuples):
                keywords.append(art[0])
        for i in range (5-len(self.recent_article_tuples)):
            keywords.append(spare_keywords[i])
        return keywords

    def make_friendly_payload(payload):
        # use NFL
        return new_payload




    def test(self):
        payload = []
        topic = 'Ferguson'
        if topic:
            specific_articles = test_nyt_api.get_5_specific(topic)
            if specific_articles:
                for art in specific_articles:
                    clean_art = test_nyt_api.clean_entry(art)
                    self.recent_article_tuples.append((topic,clean_art))
                    payload.append(test_nyt_api.clean_entry(art))

        else:
            keywords = self.get_personal_keywords()
            personal_articles = test_nyt_api.get_5_personal(keywords)
            if personal_articles:
                for art in personal_articles:
                    clean_art = test_nyt_api.clean_entry(art)
                    self.recent_article_tuples.append((topic,clean_art))
                    payload.append(test_nyt_api.clean_entry(art))
        print payload

    @staticmethod
    @tornado.gen.coroutine
    def get_headlines(self,callback, topic=None, keywords=None):
        #if there is a topic, search about that topic
        #none topic is general headline using previous keywords used
        payload = []
        if topic:
            specific_articles = test_nyt_api.get_5_specific(topic)
            if specific_articles:
                for art in specific_articles:
                    clean_art = test_nyt_api.clean_entry(art) 
                    self.recent_article_tuples.append((topic,clean_art))
                    payload.append(test_nyt_api.clean_entry(art))

        else:
            keywords = get_personal_keywords()
            personal_articles = test_nyt_api.get_5_personal(keywords)
            if personal_articles:
                for art in personal_articles:
                    clean_art = test_nyt_api.clean_entry(art) 
                    self.recent_article_tuples.append((topic,clean_art))
                    payload.append(test_nyt_api.clean_entry(art))



        client = tornado.httpclient.AsyncHTTPClient()
        response = yield client.fetch("http://google.com")
        # payload = [
        #     {'type_of_material': u'News', 'headline': u'In Ferguson, Officer Defused Eruptions as Crowds Grew Tense', 'abstract': u'Jerry Lohr, white lieutenant of St Louis County Police, has done much on the ground to relieve tensions and volatility of Ferguson protesters, in wake of grand jury decision not to indict white police officer Darren Wilson for fatal shooting of unarmed black teenager Michael Brown; to many protesters, Lohr is evidence that police have improved community relations at divisive time.', 'multimedia': [{u'subtype': u'wide', u'url': u'images/2014/11/28/us/OFFICER/OFFICER-thumbWide.jpg', u'height': 126, u'width': 190, u'legacy': {u'wide': u'images/2014/11/28/us/OFFICER/OFFICER-thumbWide.jpg', u'wideheight': u'126', u'widewidth': u'190'}, u'type': u'image'}, {u'subtype': u'xlarge', u'url': u'images/2014/11/28/us/OFFICER/OFFICER-articleLarge.jpg', u'height': 400, u'width': 600, u'legacy': {u'xlargewidth': u'600', u'xlarge': u'images/2014/11/28/us/OFFICER/OFFICER-articleLarge.jpg', u'xlargeheight': u'400'}, u'type': u'image'}, {u'subtype': u'thumbnail', u'url': u'images/2014/11/28/us/OFFICER/OFFICER-thumbStandard.jpg', u'height': 75, u'width': 75, u'legacy': {u'thumbnailheight': u'75', u'thumbnail': u'images/2014/11/28/us/OFFICER/OFFICER-thumbStandard.jpg', u'thumbnailwidth': u'75'}, u'type': u'image'}], 'snippet': u'Few law enforcers have done more on the ground to ease tensions than Jerry Lohr, a white lieutenant of the St. Louis County Police who is not above giving hugs.', 'web_url': u'http://www.nytimes.com/2014/11/28/us/officer-defused-eruptions-as-crowds-grew-volatile.html', 'section_name': u'U.S.', 'keywords': [u'Lohr, Jerry (1973- )', u'Demonstrations, Protests and Riots', u'Police Brutality, Misconduct and Shootings', u'Ferguson (Mo)', u'Brown, Michael (1996-2014)'], 'pub_date': u'20141128'},
        #     {'type_of_material': u'News', 'headline': u'AIDS Group Wages Lonely Fight Against Pill to Prevent H.I.V.', 'abstract': u'The Upshot; Michael Weinstein, president of Los Angeles-based nonprofit AIDS Healthcare Foundation, speaks out against use of Truvada to prevent HIV with national ad campaign; warns widespread use of drug erodes condom use and leaves many open to infection; Weinstein also notes that research found many people were not consistently taking Truvada and therefore risking HIV infection.', 'multimedia': [{u'subtype': u'wide', u'url': u'images/2014/11/17/upshot/17UP-HIV-1/17UP-HIV-1-thumbWide.jpg', u'height': 126, u'width': 190, u'legacy': {u'wide': u'images/2014/11/17/upshot/17UP-HIV-1/17UP-HIV-1-thumbWide.jpg', u'wideheight': u'126', u'widewidth': u'190'}, u'type': u'image'}, {u'subtype': u'xlarge', u'url': u'images/2014/11/17/upshot/17UP-HIV-1/17UP-HIV-1-articleLarge.jpg', u'height': 402, u'width': 600, u'legacy': {u'xlargewidth': u'600', u'xlarge': u'images/2014/11/17/upshot/17UP-HIV-1/17UP-HIV-1-articleLarge.jpg', u'xlargeheight': u'402'}, u'type': u'image'}, {u'subtype': u'thumbnail', u'url': u'images/2014/11/17/upshot/17UP-HIV-1/17UP-HIV-1-thumbStandard.jpg', u'height': 75, u'width': 75, u'legacy': {u'thumbnailheight': u'75', u'thumbnail': u'images/2014/11/17/upshot/17UP-HIV-1/17UP-HIV-1-thumbStandard.jpg', u'thumbnailwidth': u'75'}, u'type': u'image'}], 'snippet': u'A growing consensus in favor of Truvada is opposed by one vocal man, Michael Weinstein, and his nonprofit organization.', 'web_url': u'http://www.nytimes.com/2014/11/17/upshot/aids-group-wages-lonely-fight-against-pill-to-prevent-hiv.html', 'section_name': u'The Upshot', 'keywords': [u'Truvada (Drug)', u'Acquired Immune Deficiency Syndrome', u'AIDS Healthcare Foundation', u'Weinstein, Michael Arthur (1952- )', u'Condoms', u'Advertising and Marketing', u'Drugs (Pharmaceuticals)'], 'pub_date': u'20141117'},
        #     {'type_of_material': u'Blog', 'headline': u'Q. and A.: Ann E. Carlson and Alex Wang on the U.S.-China Climate Accord', 'abstract': u'Alex Wang and Ann E. Carlson, law professors at the University of California, Los Angeles, who study environmental policy and regulations in the United States and China, responded to questions about the United States-China agreement on cutting greenhouse gases.', 'multimedia': [{u'subtype': u'wide', u'url': u'images/2014/11/28/world/28sino-WANG1/28sino-WANG1-thumbWide.jpg', u'height': 126, u'width': 190, u'legacy': {u'wide': u'images/2014/11/28/world/28sino-WANG1/28sino-WANG1-thumbWide.jpg', u'wideheight': u'126', u'widewidth': u'190'}, u'type': u'image'}, {u'subtype': u'xlarge', u'url': u'images/2014/11/28/world/28sino-WANG1/28sino-WANG1-articleLarge.jpg', u'height': 422, u'width': 600, u'legacy': {u'xlargewidth': u'600', u'xlarge': u'images/2014/11/28/world/28sino-WANG1/28sino-WANG1-articleLarge.jpg', u'xlargeheight': u'422'}, u'type': u'image'}, {u'subtype': u'thumbnail', u'url': u'images/2014/11/28/world/28sino-WANG1/28sino-WANG1-thumbStandard.jpg', u'height': 75, u'width': 75, u'legacy': {u'thumbnailheight': u'75', u'thumbnail': u'images/2014/11/28/world/28sino-WANG1/28sino-WANG1-thumbStandard.jpg', u'thumbnailwidth': u'75'}, u'type': u'image'}], 'snippet': u'Alex Wang and Ann E. Carlson, law professors at the University of California, Los Angeles, who study environmental policy and regulations in the United States and China, responded to questions about the United States-China agreement on cutting...', 'web_url': u'http://sinosphere.blogs.nytimes.com/2014/11/28/q-and-a-alex-wang-and-ann-e-carlson-on-the-u-s-china-climate-accord/', 'section_name': u'World', 'keywords': [u'Bush, George W', u'Carlson, Ann E', u'McConnell, Mitch', u'Obama, Barack', u'Wang, Alex (Law Professor)', u'Xi Jinping', u'China', u'India', u'United States', u'Environmental Protection Agency', u'Republican Party', u'Senate', u'Air Pollution', u'Carbon Dioxide', u'Global Warming', u'Greenhouse Gas Emissions'], 'pub_date': u'20141128'},
        #     {'type_of_material': u'News', 'headline': u'E.U. Parliament Passes Measure to Break Up Google in Symbolic Vote', 'abstract': u'European Parliament passes nonbinding vote to break up Google; symbolic resolution comes one day after a separate European body sought to expand online privacy rights across Continent, and signifies growing antipathy to American technological dominance in the European Union.', 'multimedia': [{u'subtype': u'wide', u'url': u'images/2014/11/28/business/28EUGOOGLE2/28EUGOOGLE2-thumbWide.jpg', u'height': 126, u'width': 190, u'legacy': {u'wide': u'images/2014/11/28/business/28EUGOOGLE2/28EUGOOGLE2-thumbWide.jpg', u'wideheight': u'126', u'widewidth': u'190'}, u'type': u'image'}, {u'subtype': u'xlarge', u'url': u'images/2014/11/28/business/28EUGOOGLE2/28EUGOOGLE2-articleLarge.jpg', u'height': 375, u'width': 600, u'legacy': {u'xlargewidth': u'600', u'xlarge': u'images/2014/11/28/business/28EUGOOGLE2/28EUGOOGLE2-articleLarge.jpg', u'xlargeheight': u'375'}, u'type': u'image'}, {u'subtype': u'thumbnail', u'url': u'images/2014/11/28/business/28EUGOOGLE2/28EUGOOGLE2-thumbStandard.jpg', u'height': 75, u'width': 75, u'legacy': {u'thumbnailheight': u'75', u'thumbnail': u'images/2014/11/28/business/28EUGOOGLE2/28EUGOOGLE2-thumbStandard.jpg', u'thumbnailwidth': u'75'}, u'type': u'image'}], 'snippet': u'While the vote poses no immediate threat to the company, it symbolizes the growing resentment in Europe toward the American technology titan.', 'web_url': u'http://www.nytimes.com/2014/11/28/business/international/google-european-union.html', 'section_name': u'Business Day', 'keywords': [u'Antitrust Laws and Competition Issues', u'European Parliament', u'Google Inc', u'Europe', u'Computers and the Internet', u'European Commission', u'Vestager, Margrethe', u'European Union', u'Privacy'], 'pub_date': u'20141128'},
        #     {'type_of_material': u'Op-Ed', 'headline': u'Judaism Must Embrace the Convert', 'abstract': u"Op-Ed article by Orthodox Rabbi Shmuly Yanklowitz argues that Judaism must work to reduce the formidable obstacles faced by those who wish to convert; examines his own difficult experience with conversion; contends process needs to become more transparent and pluralistic, in accordance with Judaism's inclusiveness.", 'multimedia': [{u'subtype': u'wide', u'url': u'images/2014/11/22/opinion/1124OPEDbeck/1124OPEDbeck-thumbWide.jpg', u'height': 126, u'width': 190, u'legacy': {u'wide': u'images/2014/11/22/opinion/1124OPEDbeck/1124OPEDbeck-thumbWide.jpg', u'wideheight': u'126', u'widewidth': u'190'}, u'type': u'image'}, {u'subtype': u'xlarge', u'url': u'images/2014/11/22/opinion/1124OPEDbeck/1124OPEDbeck-articleLarge.jpg', u'height': 728, u'width': 600, u'legacy': {u'xlargewidth': u'600', u'xlarge': u'images/2014/11/22/opinion/1124OPEDbeck/1124OPEDbeck-articleLarge.jpg', u'xlargeheight': u'728'}, u'type': u'image'}, {u'subtype': u'thumbnail', u'url': u'images/2014/11/22/opinion/1124OPEDbeck/1124OPEDbeck-thumbStandard.jpg', u'height': 75, u'width': 75, u'legacy': {u'thumbnailheight': u'75', u'thumbnail': u'images/2014/11/22/opinion/1124OPEDbeck/1124OPEDbeck-thumbStandard.jpg', u'thumbnailwidth': u'75'}, u'type': u'image'}], 'snippet': u'Our people believe in inclusiveness as well as chosenness.', 'web_url': u'http://www.nytimes.com/2014/11/24/opinion/judaism-must-embrace-the-convert.html', 'section_name': u'Opinion', 'keywords': [u'Jews and Judaism', u'Rabbis', u'Rabbinical Council of America'], 'pub_date': u'20141124'},
        #     {'type_of_material': u'News', 'headline': u'Israeli Cabinet Approves Nationality Bill ', 'abstract': u"Israeli cabinet approves draft nationality bill that emphasizes nation's Jewish character above its democratic nature; critics point out law could hurt fragile relationship with country's Arab minority at time of heightened tensions.", 'multimedia': [{u'subtype': u'wide', u'url': u'images/2014/11/24/world/24israel/24israel-thumbWide.jpg', u'height': 126, u'width': 190, u'legacy': {u'wide': u'images/2014/11/24/world/24israel/24israel-thumbWide.jpg', u'wideheight': u'126', u'widewidth': u'190'}, u'type': u'image'}, {u'subtype': u'xlarge', u'url': u'images/2014/11/24/world/24israel/24israel-articleLarge.jpg', u'height': 668, u'width': 600, u'legacy': {u'xlargewidth': u'600', u'xlarge': u'images/2014/11/24/world/24israel/24israel-articleLarge.jpg', u'xlargeheight': u'668'}, u'type': u'image'}, {u'subtype': u'thumbnail', u'url': u'images/2014/11/24/world/24israel/24israel-thumbStandard.jpg', u'height': 75, u'width': 75, u'legacy': {u'thumbnailheight': u'75', u'thumbnail': u'images/2014/11/24/world/24israel/24israel-thumbStandard.jpg', u'thumbnailwidth': u'75'}, u'type': u'image'}], 'snippet': u'The draft legislation emphasizes Israel\u2019s Jewish character above its democratic nature, proposing to define Israel as the nation-state of the Jewish people, a move opposed by Arab citizens.', 'web_url': u'http://www.nytimes.com/2014/11/24/world/middleeast/israeli-cabinet-backs-nationality-bill-that-risks-wider-rift-with-arab-minority.html', 'section_name': u'World', 'keywords': [u'Israel', u'Jews and Judaism', u'Law and Legislation', u'Arabs', u'Palestinians', u'Likud Party (Israel)', u'Netanyahu, Benjamin'], 'pub_date': u'20141124'},
        #     {'type_of_material': u'News', 'headline': u'With a New League, a Sport\u2019s Sleeping Giant Begins to Stir', 'abstract': u"Creation of Indian Super League has, at least temporarily, revived nation's interest soccer, sport long overshadowed by cricket\u2019s $3 billion Indian Premier League.", 'multimedia': [{u'subtype': u'wide', u'url': u'images/2014/11/28/sports/28indiasoccer1/28indiasoccer1-thumbWide-v2.jpg', u'height': 126, u'width': 190, u'legacy': {u'wide': u'images/2014/11/28/sports/28indiasoccer1/28indiasoccer1-thumbWide-v2.jpg', u'wideheight': u'126', u'widewidth': u'190'}, u'type': u'image'}, {u'subtype': u'xlarge', u'url': u'images/2014/11/28/sports/28indiasoccer1/28indiasoccer1-articleLarge.jpg', u'height': 431, u'width': 600, u'legacy': {u'xlargewidth': u'600', u'xlarge': u'images/2014/11/28/sports/28indiasoccer1/28indiasoccer1-articleLarge.jpg', u'xlargeheight': u'431'}, u'type': u'image'}, {u'subtype': u'thumbnail', u'url': u'images/2014/11/28/sports/28indiasoccer1/28indiasoccer1-thumbStandard-v2.jpg', u'height': 75, u'width': 75, u'legacy': {u'thumbnailheight': u'75', u'thumbnail': u'images/2014/11/28/sports/28indiasoccer1/28indiasoccer1-thumbStandard-v2.jpg', u'thumbnailwidth': u'75'}, u'type': u'image'}], 'snippet': u'The creation of a professional league in India, backed with huge investments and Bollywood glamour, has prompted a level of excitement more common to cricket.', 'web_url': u'http://www.nytimes.com/2014/11/28/sports/soccer/new-indian-soccer-league-tries-glamour-approach.html', 'section_name': u'Sports', 'keywords': [u'Soccer', u'India', u'Cricket (Game)', u'Indian Super League'], 'pub_date': u'20141128'},
        #     {'type_of_material': u'News', 'headline': u'For Former Embassy Hostages, a Special Interest in Iran Talks', 'abstract': u'Diplomatic Memo; seven-month extension of nuclear negotiations with Iran has been particularly upsetting to the 39 surviving Americans who endured 444 days of captivity in Tehran from 1979 to 1981; former hostages are particularly outraged that Iran will continue to receive $700 million a month in funds that were frozen under Western sanctions.', 'multimedia': [{u'subtype': u'wide', u'url': u'images/2014/11/26/world/POST/POST-thumbWide.jpg', u'height': 126, u'width': 190, u'legacy': {u'wide': u'images/2014/11/26/world/POST/POST-thumbWide.jpg', u'wideheight': u'126', u'widewidth': u'190'}, u'type': u'image'}, {u'subtype': u'xlarge', u'url': u'images/2014/11/26/world/POST/POST-articleLarge.jpg', u'height': 400, u'width': 600, u'legacy': {u'xlargewidth': u'600', u'xlarge': u'images/2014/11/26/world/POST/POST-articleLarge.jpg', u'xlargeheight': u'400'}, u'type': u'image'}, {u'subtype': u'thumbnail', u'url': u'images/2014/11/26/world/POST/POST-thumbStandard.jpg', u'height': 75, u'width': 75, u'legacy': {u'thumbnailheight': u'75', u'thumbnail': u'images/2014/11/26/world/POST/POST-thumbStandard.jpg', u'thumbnailwidth': u'75'}, u'type': u'image'}], 'snippet': u'For the 39 Americans still alive who were held captive in Tehran for 444 days from 1979 to 1981, there has been no financial compensation from Iran and financial deals to extend the nuclear talks add to their anguish.', 'web_url': u'http://www.nytimes.com/2014/11/26/world/middleeast/for-former-embassy-hostages-a-special-interest-in-iran-talks.html', 'section_name': u'World', 'keywords': [u'Iran', u'Nuclear Weapons', u'Kidnapping and Hostages', u'United States International Relations'], 'pub_date': u'20141126'},
        #     {'type_of_material': u'News', 'headline': u'For New Tappan Zee, Questions Persist Over How High the Tolls Will Climb', 'abstract': u'Toll for travelers on the Tappan Zee Bridge, which has long been significantly cheaper than other Hudson River crossings like the George Washington Bridge, is likely to increase; it remains unclear how much New York State will be forced to raise toll due to construction of $3.9 billion replacement for bridge (Series: 21st-Century Span).', 'multimedia': [{u'subtype': u'wide', u'url': u'images/2014/11/28/nyregion/TAPPANZEE/TAPPANZEE-thumbWide.jpg', u'height': 126, u'width': 190, u'legacy': {u'wide': u'images/2014/11/28/nyregion/TAPPANZEE/TAPPANZEE-thumbWide.jpg', u'wideheight': u'126', u'widewidth': u'190'}, u'type': u'image'}, {u'subtype': u'xlarge', u'url': u'images/2014/11/28/nyregion/TAPPANZEE/TAPPANZEE-articleLarge.jpg', u'height': 400, u'width': 600, u'legacy': {u'xlargewidth': u'600', u'xlarge': u'images/2014/11/28/nyregion/TAPPANZEE/TAPPANZEE-articleLarge.jpg', u'xlargeheight': u'400'}, u'type': u'image'}, {u'subtype': u'thumbnail', u'url': u'images/2014/11/28/nyregion/TAPPANZEE/TAPPANZEE-thumbStandard.jpg', u'height': 75, u'width': 75, u'legacy': {u'thumbnailheight': u'75', u'thumbnail': u'images/2014/11/28/nyregion/TAPPANZEE/TAPPANZEE-thumbStandard.jpg', u'thumbnailwidth': u'75'}, u'type': u'image'}], 'snippet': u'The discount afforded by one of the New York City area\u2019s great travel bargains \u2014 crossing the Hudson River on the Tappan Zee Bridge \u2014 is likely to shrink, but no one can say by how much.', 'web_url': u'http://www.nytimes.com/2014/11/28/nyregion/for-new-tappan-zee-questions-persist-over-how-high-the-tolls-will-climb.html', 'section_name': u'N.Y. / Region', 'keywords': [u'Tappan Zee Bridge', u'Dewey, Thomas E, Thruway', u'Bridges and Tunnels', u'Tolls', u'Series', u'New York Metropolitan Area', u'New York State', u'Infrastructure (Public Works)', u'Cuomo, Andrew M', u'Rockland County (NY)', u'Westchester County (NY)'], 'pub_date': u'20141128'},
        #     {'type_of_material': u'News', 'headline': u'OPEC Holds Production Unchanged; Prices Fall ', 'abstract': u"Organization of the Petroleum Exporting Countries decides not to cut petroleum production despite plunge in oil prices that has highlighted group's diminishing clout; price of Brent crude oil falls to four-year low of about $73 on news, as American crude drops below key $70 benchmark; OPEC has been shaken over past months as prices have declined by more than 30 percent.", 'multimedia': [{u'subtype': u'wide', u'url': u'images/2014/11/28/business/28OPEC/28OPEC-thumbWide.jpg', u'height': 126, u'width': 190, u'legacy': {u'wide': u'images/2014/11/28/business/28OPEC/28OPEC-thumbWide.jpg', u'wideheight': u'126', u'widewidth': u'190'}, u'type': u'image'}, {u'subtype': u'xlarge', u'url': u'images/2014/11/28/business/28OPEC/28OPEC-articleLarge.jpg', u'height': 398, u'width': 600, u'legacy': {u'xlargewidth': u'600', u'xlarge': u'images/2014/11/28/business/28OPEC/28OPEC-articleLarge.jpg', u'xlargeheight': u'398'}, u'type': u'image'}, {u'subtype': u'thumbnail', u'url': u'images/2014/11/28/business/28OPEC/28OPEC-thumbStandard.jpg', u'height': 75, u'width': 75, u'legacy': {u'thumbnailheight': u'75', u'thumbnail': u'images/2014/11/28/business/28OPEC/28OPEC-thumbStandard.jpg', u'thumbnailwidth': u'75'}, u'type': u'image'}], 'snippet': u'The 30 percent decline in oil prices in recent months has shaken the solidarity of the 12-member Organization of the Petroleum Exporting Countries.', 'web_url': u'http://www.nytimes.com/2014/11/28/business/international/opec-leaves-oil-production-quotas-unchanged-and-prices-fall-further.html', 'section_name': u'Business Day', 'keywords': [u'Organization of the Petroleum Exporting Countries', u'Oil (Petroleum) and Gasoline', u'International Trade and World Market', u'Naimi, Ali Al-', u'Saudi Arabia'], 'pub_date': u'20141128'},
        #     {'type_of_material': u'News', 'headline': u'Grateful for What\u2019s Left, Not Mourning What\u2019s Lost', 'abstract': u'Catholic Charities Brooklyn and Queens, one of seven agencies supported by The New York Times Neediest Cases Fund, has helped Anna Maria Walsh of Brooklyn to pay for filing Certificate of Citizenship form and for replacement for her washer and dryer.', 'multimedia': [{u'subtype': u'wide', u'url': u'images/2014/11/28/nyregion/NEEDIEST/NEEDIEST-thumbWide.jpg', u'height': 126, u'width': 190, u'legacy': {u'wide': u'images/2014/11/28/nyregion/NEEDIEST/NEEDIEST-thumbWide.jpg', u'wideheight': u'126', u'widewidth': u'190'}, u'type': u'image'}, {u'subtype': u'xlarge', u'url': u'images/2014/11/28/nyregion/NEEDIEST/NEEDIEST-articleLarge.jpg', u'height': 400, u'width': 600, u'legacy': {u'xlargewidth': u'600', u'xlarge': u'images/2014/11/28/nyregion/NEEDIEST/NEEDIEST-articleLarge.jpg', u'xlargeheight': u'400'}, u'type': u'image'}, {u'subtype': u'thumbnail', u'url': u'images/2014/11/28/nyregion/NEEDIEST/NEEDIEST-thumbStandard.jpg', u'height': 75, u'width': 75, u'legacy': {u'thumbnailheight': u'75', u'thumbnail': u'images/2014/11/28/nyregion/NEEDIEST/NEEDIEST-thumbStandard.jpg', u'thumbnailwidth': u'75'}, u'type': u'image'}], 'snippet': u'Anna Maria Walsh has numerous health problems, but her resiliency has led her to win nomination to a Brooklyn community board and to work to help others with disabilities.', 'web_url': u'http://www.nytimes.com/2014/11/28/nyregion/grateful-for-what-remains.html', 'section_name': u'N.Y. / Region', 'keywords': [u'New York Times Neediest Cases Fund', u'Catholic Charities', u'Philanthropy'], 'pub_date': u'20141128'},
        #     {'type_of_material': u'News', 'headline': u'Eagles Come Out Strong Against Cowboys and Take Division Lead', 'abstract': u'Philadelphia Eagles improve to 9-3 and assume control of NFC East with 33-10 win over Dallas Cowboys.', 'multimedia': [{u'subtype': u'wide', u'url': u'images/2014/11/28/sports/Y-COWBOYS/Y-COWBOYS-thumbWide.jpg', u'height': 126, u'width': 190, u'legacy': {u'wide': u'images/2014/11/28/sports/Y-COWBOYS/Y-COWBOYS-thumbWide.jpg', u'wideheight': u'126', u'widewidth': u'190'}, u'type': u'image'}, {u'subtype': u'xlarge', u'url': u'images/2014/11/28/sports/Y-COWBOYS/Y-COWBOYS-articleLarge.jpg', u'height': 425, u'width': 600, u'legacy': {u'xlargewidth': u'600', u'xlarge': u'images/2014/11/28/sports/Y-COWBOYS/Y-COWBOYS-articleLarge.jpg', u'xlargeheight': u'425'}, u'type': u'image'}, {u'subtype': u'thumbnail', u'url': u'images/2014/11/28/sports/Y-COWBOYS/Y-COWBOYS-thumbStandard.jpg', u'height': 75, u'width': 75, u'legacy': {u'thumbnailheight': u'75', u'thumbnail': u'images/2014/11/28/sports/Y-COWBOYS/Y-COWBOYS-thumbStandard.jpg', u'thumbnailwidth': u'75'}, u'type': u'image'}], 'snippet': u'Mark Sanchez, who was 20 of 29 passing for 217 yards, led Philadelphia in a rout of N.F.C. East rival Dallas.', 'web_url': u'http://www.nytimes.com/2014/11/28/sports/football/philadelphia-eagles-come-out-strong-against-dallas-cowboys-and-walk-off-with-division-lead.html', 'section_name': u'Sports', 'keywords': [u'Football', u'National Football League', u'Sanchez, Mark', u'Romo, Tony', u'Philadelphia Eagles', u'Dallas Cowboys'], 'pub_date': u'20141128'}
        # ]
        callback(payload)

    @staticmethod
    @tornado.gen.coroutine
    def get_summary(article, callback):
        client = tornado.httpclient.AsyncHTTPClient()
        response = yield client.fetch("http://google.com")
        payload = "John is a good man"
        callback(payload)


def main():

    times = NYTimes()
    keywords = times.get_personal_keywords()
    times.test()



    
    


if __name__ == "__main__":
    main()



