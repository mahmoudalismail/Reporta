import datetime
import random

def name_or_empty(name):
    print "NAME**"
    print name
    print (name and random.random() < 0.3)
    print " " + name if (name and random.random() < 0.3) else ""
    return " " + name if (name and random.random() < 0.3) else ""

class Greeting:
  def __init__(self, username, request_time):
    self.username = username
    self.time = request_time
    self.phrases = []
    if self.time.time().hour < 12:
      tod = "morning"
    elif (self.time.time().hour >= 12 and self.time.time().hour < 17):
      tod = "afternoon"
    else:
      tod = "evening"
    self.phrases = [
      "Hello %s" % self.username,
      "Hi %s" % self.username,
      "Hey %s" % self.username,
      "Good %(tod)s %(user)s" % {'tod': tod, 'user': self.username}
    ]
    self.exclamations = [
      "I hope you've had a good day today!",
      "I missed you since last time we chatted.",
      "I'm very excited that I get to share the news with you today!"
    ]
    return self.phrases, self.exclamations
  def get_phrase(self):
    n = random.randrange(len(self.phrases))
    m = random.randrange(len(self.exclamations))
    return self.phrases[n] + self.exclamations[m] if random.random() < 0.25 else self.phrases[n]

class UpdatesOrNoUpdates:
  def __init__(self, name, updates=False):
    self.updates = updates
    if self.updates:
      self.phrases = [
        "I have some updates on stories you've been following. Would you like to hear them%s?" % name_or_empty(name),
        "I have some stories I think you may be interested in. Would you like to hear them%s?" % name_or_empty(name)
      ]
    else:
      self.phrases = [
        "Would you like to hear about what's going on today%s?" % name_or_empty(name),
        "Do you want me to tell you about today's headlines%s?" % name_or_empty(name),
        "Want me to fill you in on today's news%s?" % name_or_empty(name)
      ]

  def get_phrase(self):
    n = random.randrange(len(self.phrases))
    return self.phrases[n]

class FoundHeadlines:
  def __init__(self, sentence_headlines, topic_headlines, name):
    self.sentence_headlines = sentence_headlines
    self.topic_headlines = topic_headlines
    self.num_stories = len(self.sentence_headlines) + len(self.topic_headlines)
    first_sentence, second_sentence = '',''
    if self.sentence_headlines:
      if len(self.sentence_headlines) > 1:
        first_sentence = ", ".join(self.sentence_headlines[:-1]) + ", and " + self.sentence_headlines[-1] + "."
      else:
        first_sentence = self.sentence_headlines[0] + "."
    if self.topic_headlines:
      if len(self.topic_headlines) > 1:
        second_sentence = "I also have news about " + ", ".join(self.topic_headlines[:-1]) + ", and " + self.topic_headlines[-1] + "."
      else:
        second_sentence = "I also have news about " + topic_headlines[0] + "."
    self.base_phrase = "I have %s stories for you:" % self.num_stories + " " + first_sentence + " " + second_sentence
    self.phrases = [
      "Are any of these interesting to you%s?" % name_or_empty(name),
      "Would you like to hear about any of these%s?" % name_or_empty(name),
      "Do you want me to tell you more about any of these stories%s?" % name_or_empty(name),
      "Do any of these interest you%s?" % name_or_empty(name),
      "Let me know if any of these stories interest you%s?" % name_or_empty(name)
    ]

  def get_phrase(self):
    n = random.randrange(len(self.phrases))
    return self.base_phrase + " " + self.phrases[n]

class LoadingConfirmation:
  def __init__(self, user_input=None):
    self.user_input = user_input
    self.phrases = [
      "Sure! Just give me a second to find that for you."
    ]
    subject = "some stories about %s" % self.user_input if self.user_input else "today's top stories"
    self.phrases.append("Okay! I will find you %s" % subject)

  def get_phrase(self):
    n = random.randrange(len(self.phrases))
    return self.phrases[n]

class SaveConfirmation:
  def __init__(self, name):
    self.phrases = [
      "Okay! I've saved this story for you to read later!",
      "I've saved the article to your Kindle so you can read it later.",
      "All done! When you have time, you can read this story on your Kindle."
    ]

  def get_phrase(self):
    n = random.randrange(len(self.phrases))
    return self.phrases[n]

class Media:
  def __init__(self, name):
    self.phrases = [
      "Here are the photos for this story.",
      "Here are some images from this article",
      "Here are the photos you requested."
    ]
    
  def get_phrase(self):
    n = random.randrange(len(self.phrases))
    return self.phrases[n]
    
class Error:
  def __init__(self, name):
    self.phrases = [
      "I'm sorry, but I didn't understand what you said. Would you mind repeating that?",
      "I didn't quite catch that. Could you say that again?",
      "Can you please repeat your request for me?"
    ]
    
  def get_phrase(self):
    n = random.randrange(len(self.phrases))
    return self.phrases[n]
