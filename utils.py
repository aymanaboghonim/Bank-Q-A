import jieba
from gensim.models.word2vec import Word2Vec
import random


# 获取词向量：
def get_word2vec(word2vec_path):
    word2vec = Word2Vec.load(word2vec_path)
    return word2vec


def cut(string): return jieba.lcut(string)


def get_stopwords(stopwords_path):
    stopwords = [word.strip() for word in open(stopwords_path, 'r', encoding='utf-8').readlines()]
    return stopwords


def remove_stopwords(sentence, stopwords):
    '''

    :param sentence: sentence list after cut words
    :param stopwords: list
    :return:
    '''
    sentence_cut_stopwords = [word for word in sentence if word not in stopwords]
    return sentence_cut_stopwords


def findKsmallest(nums, k):
    def partition(left, right, pivot_index):
        pivot = nums[pivot_index][0]
        # 1. move pivot to end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        # 2. move all smaller elements to the left
        store_index = left
        for i in range(left, right):
            if nums[i][0] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        # 3. move pivot to its final place
        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index

    def select(left, right, k_largest):
        #         if (right - left) < k_largest:
        #             return nums

        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)

        if k_largest == pivot_index:
            return nums[:k_largest]
        elif k_largest < pivot_index:
            return select(left, pivot_index - 1, k_largest)
        else:
            return select(pivot_index + 1, right, k_largest)

    if len(nums) <= k:
        return nums
    return select(0, len(nums) - 1, k)


if __name__ == '__main__':
    # import os
    # root_path = os.path.abspath('./')
    # stopwords_path = os.path.join(root_path, 'dataset', 'stop_words.txt')
    # stopwords = get_stopwords(stopwords_path)
    # print(stopwords)
    print(findKsmallest([(3, 'question1', 'answer1'), (2, 'question2', 'answer2'), (3, 'question3', 'answer3'),
                         (1, 'question4', 'answer4'), (2, 'question5', 'answer5'), (4, 'question6', 'answer6'),
                         (5, 'question7', 'answer7'), (5, 'question8', 'answer8'), (6, 'question9', 'answer9')], 4))