class sentence:

    def __init__(self, word: str):
            self.word = word
        
    def my_words_backwards(self) -> str:
        return self.word[::-1]

    def my_words_upper(self) -> str:
        return self.word.upper()

    def my_words_lower(self) -> str:
        return self.word.lower()

    def my_words(self, number: int) -> str:
        words = self._split_sentence_in_to_words()
        return words[number]
    

    