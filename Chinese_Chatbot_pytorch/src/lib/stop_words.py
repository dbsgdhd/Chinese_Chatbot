from config import config

stopwords = [ i.strip() for i in open(config.stop_word_dict,encoding="utf-8").readlines()]
