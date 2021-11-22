#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return None
    output = (len(sentence), sentence[0])
    return output
