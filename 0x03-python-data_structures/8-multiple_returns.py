#!/usr/bin/python3
def multiple_returns(sentence):
    _len = len(sentence)
    return (_len, sentence[0]) if _len > 0 else (_len, None)
