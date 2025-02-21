<code>
def basic_tokenizer(text):
    """
    A basic tokenizer that splits text into words based on spaces and removes punctuation.
    """
    text = text.lower()
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    text = ''.join([char for char in text if char not in punctuation])
    words = text.split()
    return words

if __name__ == '__main__':
    text = "This is a sample sentence with some punctuation!"
    tokens = basic_tokenizer(text)
    print(tokens)
</code>
