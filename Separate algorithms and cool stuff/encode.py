from itertools import groupby

text = 'AAABCCBBBD'

def getCount(group):
    count = len(list(group));
    return str(count) if count > 1 else ''

def encode(text):
    return ''.join([ch + getCount(group) for ch, group in groupby(text)])

print (encode(text))