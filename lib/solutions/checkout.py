
from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counter = Counter(skus)

    if not set(counter.keys()) <= set('ABCDEF'):
        return -1

    discount = 0


    if 'F' in counter:
        div = counter['F'] // 3
        counter['F'] -= div

    if 'E' in counter and 'B' in counter:
        div = counter['E'] // 2
        counter['B'] -= div
        if counter['B'] <= 0:
            del counter['B']

    if 'A' in counter:
        div5, mod5 = divmod(counter['A'], 5)
        div3 = mod5 // 3
        discount += div5 * 50 + div3 * 20

    if 'B' in counter:
        div = counter['B'] // 2
        discount += div * 15

    print discount, counter
    return (counter['A'] * 50 +
            counter['B'] * 30 +
            counter['C'] * 20 +
            counter['D'] * 15 +
            counter['E'] * 40 +
            counter['F'] * 10 -
            discount)


def checkout(skus):
    counter = Counter(skus)

    if not set(counter.keys()) <= set('ABCDEF'):
        return -1

    discount = 0
