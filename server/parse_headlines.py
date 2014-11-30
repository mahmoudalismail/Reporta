import random
import re

import nltk
from nltk.corpus import brown

grammar = r"""
  NP:   {<DT>?<JJ>?<(N.*)|(PERSON)|(ORGANIZATION)|(LOCATION)>+}
  PP:   {<(IN)|(AT)|(OD)|(WBS)><NP>}
  NP:   {<DT>?<NP><PP>}
  VP:   {<V.*><(NP)|(PP)>}
  SBAR: {<NP><VP>}
  """
  
cp = nltk.RegexpParser(grammar)

train_sents = brown.tagged_sents()

t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
t3 = nltk.TrigramTagger(train_sents, backoff=t2)

def simple_headline(headline):
  match_obj = re.match(r'(.*)\: (.*)', headline)
  if match_obj:
    return match_obj.group(2)
  else:
    match_obj = re.match(r'(.*), (.*), (.*)', headline)
    if match_obj:
      return match_obj.group(1) + ' ' + match_obj.group(3)
    else:
      match_obj = re.match(r'(.*), (.*)', headline)
      if match_obj:
        return match_obj.group(2) + ' ' + match_obj.group(1)
      else:
        return headline
      
def check_headline(headline):
  headline = headline.lower()
  tokens = nltk.word_tokenize(headline)
  tagged = t3.tag(tokens)
  entities = nltk.ne_chunk(tagged, binary=True)
  parsed = cp.parse(entities)
  for node in parsed:
    if type(node) is nltk.Tree and node.label() == 'SBAR':
      sentence = node.leaves()
      sentence = ' '.join([t[0] for t in sentence])
      return sentence, 'sentence'
  tag_sequence = [t[1] for t in tagged]
  for node in parsed:
    if type(node) is nltk.Tree and node.label() == 'NE':
      subject = node.leaves()
      if subject[0][1] == 'DET' or subject[0][1] == 'NNS' or subject[0][1] == 'VBG':
        subject = ' '.join([t[0] for t in subject])
      else:
        subject = 'the ' + ' '.join([t[0] for t in subject])
      return subject, 'topic'
  np_len = 0
  np_topic = []
  for node in parsed:
    if type(node) is nltk.Tree and node.label() == 'NP':
      np = node.leaves()
      if len(np) >= np_len and 'PP' not in np:
        np_len = len(np)
        np_topic = np
  if np_topic:
    if np_topic[0][1] == 'DET' or np_topic[0][1] == 'NNS' or np_topic[0][1] == 'VBG':
      np_topic = ' '.join([t[0] for t in np_topic])
    else:
      np_topic = 'the ' + ' '.join([t[0] for t in np_topic])
    return np_topic, 'topic'
  else:
    for t in tag_sequence:
      if re.match(r'VB.*', t):
        return simple_headline(headline), 'sentence'
    return simple_headline(headline), 'topic'
        
def parse_headlines(payload):
  sentence_headlines = []
  topic_headlines = []
  for item in payload:
    headline, headline_type = check_headline(item)
    if headline_type == 'sentence':
      sentence_headlines.append(headline)
    else:
      topic_headlines.append(headline)
  return sentence_headlines, topic_headlines
    