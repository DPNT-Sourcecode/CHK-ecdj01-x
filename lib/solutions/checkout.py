
from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counter = Counter(skus)

    if not set(counter.keys()) <= set('ABCD'):
        return -1

    discount = 0
    if 'A' in counter:
        div = counter['A'] // 3
        discount += div * 20

    if 'B' in counter:
        div = counter['B'] // 2
        discount += div * 15

    print discount, counter
    return (counter['A'] * 50 + counter['B'] * 30 < counterI'C'] ‘ 20 .
    counterl'D'] - 15 discount)

