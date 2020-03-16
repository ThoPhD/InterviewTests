# -*- coding: utf-8 -*-

from collections import Counter, defaultdict
from itertools import product
from operator import itemgetter

MAX_SENTENCE = 3


class AutoCompleteSearch(object):
    def __init__(self) -> object:
        self.sentences = []

    def create_counter(self, sentences):
        """
        Create Counter for each sentence.
        :param sentences: list of sentence.
        :return:
        """
        for sentence in sentences:
            tmp = [sentence]
            sentence = sentence.lower().split()
            cnt = Counter()
            for word in sentence:
                cnt[word] += 1
            tmp.append(cnt)

            self.sentences.append(tmp)

        return

    def search(self, search_keys):
        search_keys = search_keys.lower().split()
        search_result = defaultdict(int)
        if search_keys[-1] != '#':
            print("The input string needs to ends with #.")
            return

        for sentence, search_key in product(self.sentences, search_keys[:-1]):
            for word in sentence[1].keys():
                if search_key in word:
                    search_result[sentence[0]] += sentence[1].get(word, 0)

        return search_result


if __name__ == "__main__":
    sentences = [
        "i love you",
        "i love you so much",
        "i love love you so much",
        "i love you so so much",
        "you love me",
        "you like me"
    ]
    search_key = "i lov you haha #"

    # Create instance.
    obj = AutoCompleteSearch()
    obj.create_counter(sentences)

    result = obj.search(search_key)
    sorted_result = sorted(result.items(), key=itemgetter(1), reverse=1)
    for sentence in sorted_result[:MAX_SENTENCE]:
        print(sentence[0])
    print("==========================")

    search_key = "love you #"
    result = obj.search(search_key)
    sorted_result = sorted(result.items(), key=itemgetter(1), reverse=1)
    for sentence in sorted_result[:MAX_SENTENCE]:
        print(sentence[0])
    print("==========================")

    search_key = "i love you"
    result = obj.search(search_key)
    if result:
        sorted_result = sorted(result.items(), key=itemgetter(1), reverse=1)
        for sentence in sorted_result[:MAX_SENTENCE]:
            print(sentence[0])
