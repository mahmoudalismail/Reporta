import nltk
import os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

nltk.download("brown", download_dir=currentdir)
nltk.download("punkt", download_dir=currentdir)
nltk.download("maxent_ne_chunker", download_dir=currentdir)
nltk.download("words", download_dir=currentdir)
