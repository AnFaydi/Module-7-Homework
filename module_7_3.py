class WordsFinder:
    def __init__(self, *args):
        self.file_names = list(args)
    def get_all_words(self):
        all_words = dict()
        for files in self.file_names:
            list_for_dict = list()
            with open(files, encoding= 'utf-8') as file:
                for lines in file:
                    lines = lines.lower()
                    for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        if lines.find(i) != -1:
                            lines = lines.replace(i,'')
                    lines = lines.split()
                    for i in lines:
                        list_for_dict.append(i)
            all_words[files] = list_for_dict
        return all_words
    def find(self, word):
        first_word = dict()
        for key, value in self.get_all_words().items():
            for i in range(len(value)):
                if word.lower() == value[i].lower():
                    finded_word = i
                    break
            first_word[key] = i+1
        return first_word

    def count(self, word):
        count_words = dict()
        for key, value in self.get_all_words().items():
            count = 0
            for i in range(len(value)):
                if word.lower() == value[i].lower():
                    count += 1
            count_words[key] = count
        return count_words

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))