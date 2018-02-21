
from collections import Counter
from functools import partial

# noinspection PyUnusedLocal
# skus = unicode string

def multibuy(item_quantity, amount, discount,
                            amount2=None, discount2=None):

    if amount2 and discount2:
        div2, mod2 = divmod(item_quantity, amount2)
        div2 = mod2 // amount
        return div2 * discount2 + div * discount

multibuy = {
    'A': partial(multibuy, amount=3, discount=20, amount2=5, discount2=50),
    'B': partial(multibuy, amount=2, discount=15),
    'H': partial(multibuy, amount=5, discount=5, amount2=10, discount2=20),
    'K': partial(multibuy, amount=2, discount=10),
    'P': partial(multibuy, amount=5, discount=50),
    'Q': partial(multibuy, amount=3, discount=10),
    'V': partial(multibuy, amount=2, discount=10, amount2=3, discount2=20),
}

free_item = {
    'E': partial(buy_N_get_one_free, item='E', target=2, free_item='B'),
    'F': partial(buy_N_get_one_free, item='F', target=3),
    'N': partial(buy_N_get_one_free, item='N', target=3, free_item='M'),
    'R': partial(buy_N_get_one_free, item='R', target=3, free_item='Q'),
    'U': partial(buy_N_get_one_free, item='U', target=4),

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
