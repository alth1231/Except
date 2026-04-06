# int('dragon')
# 10.0 / 0.0
# my_list = []
# print(my_list[99])
#
# try:
#         raw = input('RNtrt your hero"s level:')
#         level = int(raw)
#         print(f'level {levl}hero ready')
# except ValueError:
#         print('please enter a number')
# except Exception as e:
#         print(e)
#  def load_save fil (filname)
#  try:
#      f = open (filmname
#                data -= f.read)
#      ecept FileNotFoundError:
#      print('file not found')
#  finally :
#      print('closing file')
#
# def heal_hero(hero_hp, heal_amount):
#
#     try:
#         heal_amount = int(heal_amount)
#         new_hp = hero_hp + heal_amount
#
#     except ValueError:
#         print('iNVALID HEAL AMOUNT')
#     else:
#         print(f'hero hp: {new_hp}')
#     finally:
#         print('healing attempt over')
#
#     heal_hero(5,'25')
#     heal_hero(5, 'max')
#
# Square each level
# squares = [n** 2
#            for n in [1, 2, 3,4]]
# print(squares)
#
# names = ['John', 'Jane', 'Bob']
# upper = [n.upper() for n in names]
# print(upper)
#
# levels = [1, 5, 12, 20]
# xp     = [lvl * 100 for lvl in levels]
# print(xp)
#
# party = [
#     {"name": "Aria",  "level": 15},
#     {"name": "Brom",  "level": 7},
#     {"name": "Caela", "level": 22},
#     {"name": "Dex",   "level": 3},
# ]
#
# veterans = [ h['names']for h in party
#              if h ['level'] >= 10]
#
# print(veterans)

monsters = [
    {"name": "Goblin",   "hp": 30,  "gold": "5"},
    {"name": "Troll",    "hp": 80,  "gold": "twenty"},
    {"name": "Skeleton", "hp": 20,  "gold": "12"},
    {"name": "Dragon",   "hp": 200, "gold": "500"},
    {"name": "Bat",      "hp": 10,  "gold": "1"},
]

def safe_gold(m):
    try:
        gold = int(m['gold'])
        return gold
    except ValueError:
        return 0

tough_monsters_names = [m['names']
                        for m in monsters
                        if m ['hp'] > 25]
print(tough_monsters_names)

gold_amounts = [safe_gold(m) for m in monsters if m ['gold'] != 'twenty']

print(gold_amounts)

