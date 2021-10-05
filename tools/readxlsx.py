import openpyxl as pyxl
import json

filepath = 'skills.xlsx'

wb = pyxl.load_workbook(filename = filepath)


sheet = wb['Lista de Habilidades']



current_skill = {}
skill_list = {}
for row in sheet:

    counter = 0

    if row[0].value != None:
        skill_list[row[0].value] = current_skill
        current_skill = {
            'name': row[6].value.replace("\n", " "),
            'type': row[3].value.replace("\n", " "),
            'dmg_type': row[4].value.replace("\n", " "),
            'heal': row[5].value.replace("\n", " "),
            'requirements': str(row[10].value).replace("\n", " "),
            'level': {}
        }

    current_skill['level'][row[8].value] = {
        'description': str(row[9].value).replace("\n", " "),
        'mana_cost': str(row[11].value).replace("\n", " "),
        'points_cost': row[12].value.replace("\n", " ")
    }



    # row[0] # skill_id
    # row[3] # skill_type
    # row[4] # skill_type1
    # row[5] # skill_heal
    # row[6] # skill_name
    # row[7] #
    # row[8] # skill_level
    # row[9] # skill_description
    # row[10] # skill_requirements
    # row[11] # mana_cost 
    # row[12] # skill_cost
    # row[13] #


    
    # for cell in row:

    #     print(cell.value, end=',')
    #     print('[' + str(counter) + ']', end='')
    #     counter += 1

    # print('\n')

print(json.dumps(skill_list, indent=4))