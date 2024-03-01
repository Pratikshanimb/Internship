import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def process_legal_text(legal_text):
    # Tokenize the legal text
    tokens = word_tokenize(legal_text)

    # Part-of-speech tagging
    pos_tags = pos_tag(tokens)

    return pos_tags

# Example legal text
legal_document = "This agreement is entered into on this 1st day of January, 2024..."

# Process legal text
result = process_legal_text(legal_document)

# Print the result
print(result)