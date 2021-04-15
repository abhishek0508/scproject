# import spacy

# tagger = spacy.load('en_core_web_sm')

# sentence = "My son's name is Dolton"

# doc = tagger(sentence)

# for ent in doc.ents:
#     print(ent.text)

import spacy
import nltk

def _generate_family_tree(sentence):
    # tagger = spacy.load('en_core_web_sm')
    tagger = spacy.load('en_core_web_sm')

    sentence = "My son's name is Dolton"

    doc = tagger(sentence)

    for ent in doc.ents:
        print(ent.text)

    wvar = ""
    family = ['son', 'daughter', 'wife', 'father', 'mother', 'husband', 'brother', 'sister']
    # words = body.split(' ')
    words = nltk.word_tokenize(sentence)
    # print(words)
    for word in words:
        if word in family:
            for ent in doc.ents:
                print(ent.text)
                wvar = ent.text

            famfile = open(word + ".txt", 'a')
            famfile.write(wvar)
            famfile.close()
    return

def main():
    sentence = "My son's name is dolton"
    _generate_family_tree(sentence)

main()
