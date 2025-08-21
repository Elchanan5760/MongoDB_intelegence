import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import operator
from services.utils.read_text import read_text

class DataProcessing:
    def __init__(self,df):
        self.df = df
        self.my_dict = {}

    def all_tweets(self):
        list_of_processing = []
        for tweet in self.df.iterrows():
            my_dict = {}
            my_dict['id'] = str(tweet[1]['_id'])
            my_dict['original_text'] = str(tweet[1]['Text'])
            my_dict['rarest_word'] = self.rarest_word(str(tweet[1]['Text']))
            my_dict['sentiment'] = self.post_emotion(str(tweet[1]['Text']))
            my_dict['detected_weapons'] = self.detected_weapons(str(tweet[1]['Text']))
            list_of_processing.append(my_dict)
        return list_of_processing


    def rarest_word(self,tweet):
        list_of_words = tweet.lower().split()
        count_dict = {}
        for word in list_of_words:
            if word in count_dict:
                count_dict[word] += 1
            else:
                count_dict[word] = 1
        rarest = min(count_dict.items(), key=operator.itemgetter(1))[0]
        return rarest

    def post_emotion(self,tweet):
        score = SentimentIntensityAnalyzer().polarity_scores(tweet)
        if score['compound'] > 0.5:
            return 'positive'
        if score['compound'] < -0.5:
            return 'negative'
        else:
            return "neutral"

    def detected_weapons(self,tweet):
        weapons = read_text().lower().split()
        for weapon in weapons:
            if weapon in tweet.lower().split():
                return weapon
        return ''