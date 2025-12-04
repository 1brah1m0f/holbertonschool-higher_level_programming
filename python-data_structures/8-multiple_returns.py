#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        first = None
        enght = len(sentence)
    else:
        enght = len(sentence)
        first = sentence[0]
    return enght
    return first