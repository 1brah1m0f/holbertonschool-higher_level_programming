#!/usr/bin/python3
def multiple_returns(sentence):
    if lenght == 0:
        first = None
        enght = len(sentence)
    else:
        enght = len(sentence)
        first = sentence[0]
    return enght
    return first
sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))