
from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counter = Counter(skus)

    if not set(counter.keys()) <= set('ABCDE'):
        return -1

    discount = 0

    if 'E' in counter and 'B' in counter:
        div = counter['A'] // 3
        discount += div * 20

    if 'A' in counter:
        div = counter['A'] // 3
        discount += div * 20

    if 'B' in counter:
        div = counter['B'] // 2
        discount += div * 15

    print discount, counter
    return (counter['A'] * 50 + counter['B'] * 30 + counter['C'] * 20 +
        counter['D'] * 15 - discount)

