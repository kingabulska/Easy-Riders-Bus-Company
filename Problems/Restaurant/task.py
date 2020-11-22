import itertools


mc = list(zip(main_courses, price_main_courses))
d = list(zip(desserts, price_desserts))
dr = list(zip(drinks, price_drinks))

dishes = itertools.product(main_courses, desserts, drinks)
prices = itertools.product(price_main_courses, price_desserts, price_drinks)

for nam, price in zip(dishes, prices):
    if sum(price) <= 30:

        print(nam[0], nam[1], nam[2], sum(price))
