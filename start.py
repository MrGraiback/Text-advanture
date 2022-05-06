import json, os
import level1
import level2
from anecAPI import anecAPI

def save(chars):
    file = open('save.json', 'w')
    file.write(json.dumps(chars))
    file.close()

try:
    file = open('save.json')
    chars = json.loads(file.read())
    file.close()
except:
    chars = {'hp': 1, 'int': 1, 'charisma': 1, 'power': 1, 'level': 1, 'inventory': []}
    save(chars)


if chars['level'] == 1:
    level1.main(chars)
    chars['level'] += 1
    save(chars)


if chars['level'] == 2:
    level2.main(chars)
    chars['level'] += 1
    save(chars)

if chars['level'] >= 3:
    print ('To be continued')
    chars['level'] += 1
    save(chars)


if chars['level'] >= 5:
    print('Do you like what you see?')
    print(anecAPI.random_joke()) # Displays a random USSR or Russian joke
    chars['level'] += 1
    save(chars)

if chars['level'] >= 10:
    os.remove('save.json')



# chars['inventory'].append('knife')
