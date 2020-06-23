#Quem é seu pokemon?
#Data: 23/06/2020 às 04:25
#Autor: Victor Lopes
#Status: WIP

import requests
import json
import os

os.system('cls')

class Pokedex():

    def get_infos(self):

        podekex = json.loads(requests.get('https://www.pokemon.com/br/api/pokedex/kalos').content)
        texto_base = 'Seu Pokemon pelo Aniversario'
        espacamento = round((100-len(texto_base))/2)-2
        print(f'\n{"-" * 100}\n#{" " * espacamento}{texto_base}{" " * espacamento}#\n{"-" * 100}\n')  
        print('Informe seu mês de aniversário:\n1 - Janeiro\n2 - Fevereiro\n3 - Março\n4 - Abril\n5 - Maio\n6 - Junho\n7 - Julho\n8 - Agosto\n9 - Setembro\n10 - Outubro\n11 - Novembro\n12 - Dezembro\n')
        mes_pertimido = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        dia_permitido = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
        dict_mes_tipo = {
            1: 'ground',
            2: 'grass',
            3: 'fire',
            4: 'dragon',
            5: 'poison',
            6: 'flying',
            7: 'rock',
            8: 'ice',
            9: 'fairy',
            10: 'ghost',
            11: 'fight',
            12: 'dark'}
        dict_dia_tipo = {
            1: 'fire',
            2: 'dark',
            3: 'flying',
            4: 'dragon',
            5: 'grass',
            6: 'electric',
            7: 'dragon',
            8: 'bug',
            9: 'poison',
            10: 'ghost',
            11: 'fight',
            12: 'water',
            13: 'steel',
            14: 'fire',
            15: 'normal',
            16: 'ground',
            17: 'ice',
            18: 'fairy',
            19: 'psychic',
            20: 'rock',
            21: 'steel',
            22: 'grass',
            23: 'fairy',
            24: 'dark',
            25: 'flying',
            26: 'water',
            27: 'rock',
            28: 'ground',
            29: 'electiric',
            30: 'ghost',
            31: 'poison'
        }
        mes = int(input('Seu mês de Aniversario: '))
        if mes in mes_pertimido:
            mesV = True
            mes_tipo = dict_mes_tipo[mes]
        else:
            print('Inválido. Finalizando')
            exit(0)
        dia = int(input('Que dia voce nasceu: '))
        if dia in dia_permitido:
            diaV = True
            dia_tipo = dict_dia_tipo[dia]
        else:
            print('Inválido. Finalizando')
            exit(0)
        os.system('cls')
        if diaV and mesV:
            if dia_tipo == mes_tipo:
                my_type = [dia_tipo]
            else:
                my_type = sorted([mes_tipo, dia_tipo])
            my_type_reverse = my_type.reverse()
            print(F'Seus pokemons= são:\n')
            count = 0
            for pokemon in podekex:
                if my_type == pokemon['type'] or my_type_reverse == pokemon['type']:
                    count += 1
                    print(f'{pokemon["id"]} - {pokemon["name"]}')
            if count == 0:
                print('Que pena, você não tem nenhum pokemon')
            else:
                print(f'\nParabéns, sua lista teve {count} pokemon')






start = Pokedex()
start.get_infos()