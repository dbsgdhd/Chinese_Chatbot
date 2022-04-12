from lib.chinese_word_segmentation import segmentation
from lib import stopwords
if __name__ == '__main__':
    s = "阿里不哥python难不难，c++好简单,这儿,鄙人。"
    result = segmentation(s,by_word=False,with_sg=False,use_stop_word=False)
    print(result)
    # print(stopwords)