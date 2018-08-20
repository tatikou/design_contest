#------------#
# Libraries. #
#------------#
import sys
# Word2Vec.
from gensim.models import word2vec as w2v
import MeCab

#------------#
# Parameters.#
#------------#
MODEL_FILE = '/home/mlab/FA/models/jwp.model'

#------------#
#   Setup.   #
#------------#
# Loads the model.
print('Loading %s...' % MODEL_FILE)
model = w2v.Word2Vec.load(MODEL_FILE)
mecab = MeCab.Tagger('-d %s' % ('/usr/lib64/mecab/dic/mecab-ipadic-neologd'))

#------------#
#  Methods.  #
#------------#


def calc_similarity():

    # 幸せ,容認,不安,放心,哀愁,うんざり,怒る,興味がfeelの配列の添え字と対応
    feel = [0,0,0,0,0,0,0,0]
    l = ['幸せ', '容認', '不安','放心','哀愁','うんざり','怒る','興味']

    while True:

        input_word = input(">")
        mecab.parse('')#空でパースする必要がある
        node=mecab.parseToNode(input_word)
        while node :

            while node != None and node.feature.split(",")[0] != "形容詞":#形容詞じゃなければ飛ばす
                node = node.next

            if node == None:
                continue
            input_word1 = node.feature.split(",")[6]

            print(node.feature.split(",")[6])
            for name in l:
                sim = model.similarity(input_word1, name)
                if sim > 0.5:#類似度が0.5を超えていればメータに1をプラスする
                    if name == '幸せ':
                        feel[0] += 1
                    elif name == '容認':
                        feel[1] += 1
                    elif name == '不安':
                        feel[2] += 1
                    elif name == '放心':
                        feel[3] += 1
                    elif name == '哀愁':
                        feel[4] += 1
                    elif name == 'うんざり':
                        feel[5] += 1
                    elif name == '怒る':
                        feel[6] += 1
                    elif name == '興味':
                        feel[7] += 1

                print('name:%s  value:%.3f' % (name, sim))

            print(feel)
            print('')
            node = node.next

def __main__():
    calc_similarity()


#------------#
#   Main.    #
#------------#
while True:
    __main__()
