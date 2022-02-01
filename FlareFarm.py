import os, sys
import requests
import subprocess
import time, datetime
import threading
from bs4 import BeautifulSoup
from func import *


def parse_dirTree(tree):
    for file in tree:
        if file[-4:] == 'html':
            sum = 0
            tm = html_filename_disambiguation(file)
            print('FlareFarm ', time.strftime("%Y/%m/%d %H:%M", time.gmtime(tm)))
            with open(file) as f:
                soup = BeautifulSoup(f, 'lxml')
                for flexBox in soup.find_all('div', class_='flex column whiteBox poolWidget flexAuto'):
                    StakeBox_Name = flexBox.find('div', class_='flex column flexAuto')
                    print(StakeBox_Name.find('strong').text, end='\t')
                    APY_Box_Name = flexBox.find('div', class_='flex flexAuto column borderedBox')
                    Staked_Box = flexBox.find('div', class_='flex column widgetPersonal whiteBox')
                    for item_n_text in Staked_Box.find_all(name='span'):
                        print(item_n_text.text)
                        last_entries.append(float(item_n_text.text))
                        sum += float(item_n_text.text)
            print('TOTAL = ', sum, '\n')

def main():
    staked_SFIN = 0.0000_5717_6279_19914
    print("Hello World", '\t', staked_SFIN)

    *_, SGB, EXFI, SFIN = last_entries
    SGB_SFIN = SGB / SFIN
    EXFI_SFIN = EXFI / SFIN
    SGB_EXFI = SGB / EXFI
    print(f'\nSGB_SFIN = {SGB_SFIN: 0.3f}\nEXFI_SFIN = {EXFI_SFIN: 0.3f}\nSGB_EXFI = {SGB_EXFI: 0.3f}')

    N = int(len(last_entries) / 3)
    print(N)
    SGB, EXFI, SFIN = [], [], []
    for i in range(N):
        SGB.append(last_entries[i*3])
        EXFI.append(last_entries[i*3+1])
        SFIN.append(last_entries[i*3+2])

    print(f'\nSGB_SFIN = ', end='\b')
    for i in range(N):
        num = SGB[i] / SFIN[i]
        print(f'{num: 0.3f}\b', end='')

    print(f'\nEXFI_SFIN = ', end='\b')
    for i in range(N):
        num = EXFI[i] / SFIN[i]
        print(f'{num: 0.3f}\b', end='')

    print(f'\nSGB_EXFI = ', end='\b')
    for i in range(N):
        num = SGB[i] / EXFI[i]
        print(f'{num: 0.3f}\b', end='')


dir_path = os.path.dirname(os.path.realpath(__file__))

A = list_directory_tree(dir_path)

last_entries = []
parse_dirTree(A)






'''
https://stackoverflow.com/questions/62165635/how-to-scrape-data-from-flexbox-element-container-with-python-and-beautiful-soup
'''

if __name__ == '__main__':
    main()

'''
print(dir(os))
p = os.listdir(os.getcwd())
print(p)
print(os.getcwd())

print(__file__)
path = os.getcwd()
print(path)
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
'''
