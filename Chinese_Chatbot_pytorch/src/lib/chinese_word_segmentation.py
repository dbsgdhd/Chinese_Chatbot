"""
中文分词

"""
import jieba
import jieba.posseg as psg #返回词性
from config import config
import string
import re
from lib import stopwords
# 加载词典
jieba.load_userdict(config.history_word)
# 准备英文字符
letters = string.ascii_lowercase+"+"
#标点符号
filters= [",","-","."," ","。","，"]


"""
:param sentence: 句子
:param by_word: 是否按照单个词分词
:param use_stop_word是否运用停词
:param with_sg：分词结果是否带有词性
:return
"""
def segmentation(sentence,by_word=False,use_stop_word=False,with_sg=True):
    if by_word:
        result = seg_sentense_by_word(sentence)
    else:
        result = psg.lcut(sentence)
        if use_stop_word:
            result = [(i.word,i.flag) for i in result if i.word not in stopwords]
        if not with_sg:
            # result = [i.word for i in result]
            try:
                result = [i.word for i in result]
            except AttributeError:
                raise Exception("当use_stop_word为True时 与 with_sg 不能为False!")

    return  result


def seg_sentense_by_word(sentence):
    sentence = re.sub("\s+", "", sentence)
    sentence = sentence.strip()
    result = []
    temp = ""
    for word in sentence:
        if word.lower() in letters:
            temp += word.lower()
        else:
            if temp != "":  # 不是字母
                result.append(temp)
                temp = ""
            if word.strip() in filters:  # 标点符号
                continue
            else:  # 是单个字
                result.append(word)
    if temp != "" :  # 最后的temp中包含字母
        print(temp)
        result.append(temp)
    print(result)
    return result


if __name__ == '__main__':
    seg_sentense_by_word("python   ,和,c  ++那   个更难c++")
