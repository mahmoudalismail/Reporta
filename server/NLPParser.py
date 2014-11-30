import os, sys, inspect
import pickle
import random
import re

import nltk
from nltk.corpus import brown

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
nltkpath = os.path.join(currentdir, "nltk")
nltk.data.path.append(nltkpath)

class NLPParser:
  loaded = False
  def __init__(self):
    if not NLPParser.loaded:
      self.load()
    
  def load(self):
    NLPParser.cp = pickle.load(open(os.path.join(nltkpath, 'cp.pickle'), 'rb'))

    NLPParser.t0 = nltk.DefaultTagger('NN')
    NLPParser.t1 = pickle.load(open(os.path.join(nltkpath, 't1.pickle'), 'rb'))
    NLPParser.t2 = pickle.load(open(os.path.join(nltkpath, 't2.pickle'), 'rb'))
    NLPParser.t3 = pickle.load(open(os.path.join(nltkpath, 't3.pickle'), 'rb'))

  @staticmethod
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

  @staticmethod
  def check_headline(headline):
    headline = headline.lower()
    tokens = nltk.word_tokenize(headline)
    tagged = NLPParser.t3.tag(tokens)
    entities = nltk.ne_chunk(tagged, binary=True)
    parsed = NLPParser.cp.parse(entities)
    for node in parsed:
      if type(node) is nltk.Tree and node.label() == 'SBAR':
        sentence = node.leaves()
        sentence = ' '.join([t[0] for t in sentence])
        return sentence, 'sentence'
    tag_sequence = [t[1] for t in tagged]
    for node in parsed:
      if type(node) is nltk.Tree and node.label() == 'NE':
        subject = node.leaves()
        subject = ' '.join([t[0] for t in subject])
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
      np_topic = ' '.join([t[0] for t in np_topic])
      return np_topic, 'topic'
    else:
      for t in tag_sequence:
        if re.match(r'VB.*', t):
          return NLPParser.simple_headline(headline), 'sentence'
      return NLPParser.simple_headline(headline), 'topic'

  @staticmethod
  def parse_headlines(payload):
    sentence_headlines = []
    topic_headlines = []
    for item in payload:
      headline, headline_type = NLPParser.check_headline(item)
      if headline_type == 'sentence':
        sentence_headlines.append(headline)
      else:
        topic_headlines.append(headline)
    return sentence_headlines, topic_headlines
