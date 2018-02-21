
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

free_item = {
    'E': partial(buy_N_get_one_free, item='E', target=2, free_item='B'),
    'F': partial(buy_N_get_one_free, item='F', target=3),
    'E': partial(buy_N_get_one_free, item='E', target=2, free_item='B'),

}

price = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 80,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 30,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 90,
    'Y': 10,
    'Z': 50
}

def checkout(skus):
    counter = Counter(skus)

    if not set(counter.keys()) <= set(price.keys()):
        return -1

    discount = 0

    for key in free_item:
        if key in counter:
            free_item[key][counter]

    for key in multibuy:
        if key in counter:
            quantity = counter[key]
            discount = multibuy[key][quantity]

    print discount, counter
    return sum(price[k] * v for k, v in counter.items()) - discount
