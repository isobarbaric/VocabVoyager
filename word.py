
from definer import Dictionary
from variant import Variant
import json

class Word:

    common_dictionary = Dictionary()

    def __init__(self, word: str):
        self.word = word
        definition = Word.common_dictionary.define(word)
        if definition == '404':
            self.meanings = 404
            return
        query_response = json.loads(definition)
        self.meanings = []
        for etymology in query_response:
            self.meanings.append(dict())
            for part_of_speech in etymology['meanings']:
                self.meanings[-1][part_of_speech['partOfSpeech']] = [] 
                for variant in part_of_speech['definitions']:
                    self.meanings[-1][part_of_speech['partOfSpeech']].append(Variant(word, part_of_speech['partOfSpeech'], variant['definition']))

    def __repr__(self):
        info = ''
        cnt = 1
        for etymology in self.meanings:
            info += "Etymology #" + str(cnt) + '\n'
            for part_of_speech in etymology:
                info += ' ' * 2 + part_of_speech + '\n'
                for word in etymology[part_of_speech]:
                    info += ' ' * 4 + str(word) + '\n'
            info += '\n'
            cnt += 1
        return info

