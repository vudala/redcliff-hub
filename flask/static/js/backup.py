#CODIGO PORCO ARRUMARH

from classes.character import Character
from classes.character import Attributes


import json

FILEPATH = 'resources/scaling.json'
scaling = None
with open(FILEPATH, 'r') as f:
    scaling = json.loads(f.read())


def add_bonus(attributes, bonus):
    split = bonus.split('_')
    try:
        split[1]
    except:
        return
    if split[1] == 'ALL':
        for k in vars(attributes):
            vars(attributes)[k] += int(split[0])
        return
    vars(attributes)[split[1].lower()] += int(split[0])

def level_up(character, add_experience):
    upgrades = {
        'att_points': 0,
        'common_points': 0,
        'superior_points': 0,
        'divine_points': 0,
        'bonus_points': Attributes(),
        'return_points': 0,
    }

    xp_needed = character.level * 100 - character.experience
    while xp_needed < add_experience:
        add_experience -= xp_needed
        character.level += 1
        xp_needed = character.level * 100

        scale = scaling[str(character.level)]

        upgrades['att_points'] += scale['att_points']
        upgrades['common_points'] += scale['common_points']
        upgrades['superior_points'] += scale['superior_points']
        upgrades['divine_points'] += scale['divine_points']
        add_bonus(upgrades['bonus_points'], scale['bonus_points'])
        upgrades['return_points'] += scale['return_points']
        
    character.experience = add_experience
    if character.experience == xp_needed:
        character.level += 1
        character.experience = 0


    print('Você ganhou:')
    print('{} pontos de atributo'.format(upgrades['att_points']))
    print('{} pontos comuns'.format(upgrades['common_points']))
    print('{} pontos superiores'.format(upgrades['superior_points']))
    print('{} pontos divinos'.format(upgrades['divine_points']))
    for k in vars(upgrades['bonus_points']):
        print('+{} {}'.format(vars(upgrades['bonus_points'])[k],k))
    print('{} pontos de retorno'.format(upgrades['return_points']))


hero = Character('Eduardo', 20)
level_up(hero, 70000)