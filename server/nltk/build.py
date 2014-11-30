import os, sys, inspect
import pickle
import re

import nltk
from nltk.corpus import brown


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
nltkpath = currentdir
 
def main(): 
  grammar = r"""
    NP:   {<DT>?<JJ>?<(N.*)|(PERSON)|(ORGANIZATION)|(LOCATION)>+}
    PP:   {<(IN)|(AT)|(OD)|(WBS)><NP>}
    NP:   {<DT>?<NP><PP>}
    VP:   {<V.*><(NP)|(PP)>}
    SBAR: {<NP><VP>}
    """
  train_sents = brown.tagged_sents()
  
  cp = nltk.RegexpParser(grammar)

  t0 = nltk.DefaultTagger('NN')
  t1 = nltk.UnigramTagger(train_sents, backoff=t0)
  t2 = nltk.BigramTagger(train_sents, backoff=t1)
  t3 = nltk.TrigramTagger(train_sents, backoff=t2)
  
  pickle.dump(cp, open(os.path.join(nltkpath, 'cp.pickle'), 'wb'), -1)
  pickle.dump(t1, open(os.path.join(nltkpath, 't1.pickle'), 'wb'), -1)
  pickle.dump(t2, open(os.path.join(nltkpath, 't2.pickle'), 'wb'), -1)
  pickle.dump(t3, open(os.path.join(nltkpath, 't3.pickle'), 'wb'), -1)
  

if __name__ == '__main__':
  main()