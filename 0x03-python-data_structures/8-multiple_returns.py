#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_len = len(sentence)
    if sentence == '':
        sent_tuple = (sentence_len, None)
    else:
        sent_tuple = (sentence_len, sentence[0])
    return sent_tuple
