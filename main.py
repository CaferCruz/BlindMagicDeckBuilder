#Programa para gerar arquivo JSON e imagens contendo qr codes de cartas de magic dada uma lista de nomes

import sys
import os
from CardManager import CardManager
import qrcode

def create_folder(name):
    if not os.path.exists(name):
        os.makedirs(name)

def generate_qr_codes(lines, manager, folder):
    #Itera sobre a lista de nomes de cartas e salva o qr code de cada uma na pasta do deck
    for card_name in lines:
        img = manager.card_to_qr(card_name)
        img.save(folder+'/'+card_name.rstrip()+'.png')

def create_json(lines, manager, filename):
    with open(filename, 'w') as f:
        for card_name in lines:
            obj = manager.card_to_json(card_name)
            f.write(obj)


def main():
    filename = sys.argv[1]
    manager = CardManager()
    with open(filename, 'r') as f:
        lines = f.readlines()
    folder = filename.replace('.txt', '/')+'qr codes'
    create_folder(folder)
    generate_qr_codes(lines, manager, folder)
    folder = filename.replace('.txt', '/')+filename.replace('.txt', '.json')
    create_json(lines, manager, folder)

if __name__ == '__main__':
    main()