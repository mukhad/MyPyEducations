"""
Мы хотим отсортировать этот список по последней букве второго элемента каждого tuple, т.е. получить такой список:
"""

items = [('one', 'two'), ('three', 'four'), ('five', 'six'), ('string', 'a')]

sorted_items = [ ('string', 'a'), ('one', 'two'), ('three', 'four'), ('five', 'six')]

sitems = sorted(items, key=lambda x: x[1][-1])

print(sitems)