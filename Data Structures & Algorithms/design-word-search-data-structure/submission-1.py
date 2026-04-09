class WordDictionary:

    def __init__(self):
        self.words = []

    def addWord(self, word: str) -> None:
        self.words.append(word)
        return None
        

    def search(self, word: str) -> bool:
        
        if word in self.words:
            return True

        for wrd in self.words:
            if len(wrd) == len(word):
                for idx in range(len(wrd)):
                    if word[idx] == ".":
                        continue
                    elif word[idx] == wrd[idx]:
                        continue
                    elif word[idx] != wrd[idx]:
                        break
                else:
                    return True

        return False
                





