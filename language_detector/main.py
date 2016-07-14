"""This is the entry point of the program."""

from .languages import LANGUAGES


def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""
    # implement your solution here

    words = text.split()
    
    # Pull languages and initiate a language word count dictionary
    language_count = {}
    
    # l is dictionary with name=language, common_words=list of words
    for l in languages:
        language_count[l['name']] = 0
    
    # loop through words and add to count of appropriate language
    for word in words:
        for l in languages:
            if word.lower() in l['common_words']:
                language_count[l['name']] += 1
    
    
    # find language with highest count
    high_count_language = 'no_language_detected'
    high_count = 0

    for key, value in language_count.items():
        if value > high_count:
            high_count_language = key
            high_count = value

    return high_count_language
        
