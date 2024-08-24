# Dictionary Comprehension: Day 26
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

import random as r

new_dict = {name: r.randint(1, 100) for name in names}

passed = {name: score for name, score in new_dict.items() if score > 50}

print(passed)
