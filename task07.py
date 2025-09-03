class StringTools:
    def __init__(self, words):
        self.words = words

    @classmethod
    def is_palindrome(cls,text):
        return text == text[::-1]

    @classmethod
    def from_sentence(cls,text):
        return cls(text.split())

print(StringTools.is_palindrome("level"))
st = StringTools.from_sentence("I love Python")
print(st.words)
