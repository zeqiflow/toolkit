def dedupe(items, key=None):
    '''
    this function designed for remove duplicate contents but do not mass original sequence.

    :param items: original data sequence.
    :param key: rules for dict, which key need to check.
    '''
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(item)

# path = './test.txt'
# with open(path, 'r') as f:
#    for line in dedupe(f):
#        print(line)


