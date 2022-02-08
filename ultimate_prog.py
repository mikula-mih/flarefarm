from bs4 import BeautifulSoup
from func import *


def HTML_dirTree_parser(tree):


    class HTML_timestamp_data():
        def __init__(self, html_timestamp):
            self.html_timestamp = html_timestamp


    def isHTML(file):
        if file[-4:] == 'html': return True


    for file in tree:
        while(isHTML(file)):
            sum = 0
            html_timestamp = html_filename_disambiguation(file)
            with open(file) as f:
                soup = BeautifulSoup(f, 'lxml')
                """
                HELLO THERE
                """
                balance = soup.find('div', class_='flex balanceWrapper').text
                print(balance)
                for flexBox in soup.find_all('div', class_='flex column whiteBox poolWidget flexAuto'):
                    stakeBox_name = flexBox.find('div', class_='flex column flexAuto').find('strong').text
                    print(stakeBox_name)
                    #
                    _list = list() # list = list(APY, Pool Supply, Total Staked, Reward Rate)
                    APY_Box = flexBox.find('div', class_='flex flexAuto column borderedBox')
                    for class_tag in APY_Box.find_all(class_='flex row'):
                        for div_tag in class_tag.find_all('div'):
                            _list.append(div_tag.find('p').text)
                    print(_list)
                    #
                    _list2 = list() # list = list(You Staked, Unclaimed)
                    Staked_Box = flexBox.find('div', class_='flex column widgetPersonal whiteBox')
                    _list2.append(Staked_Box.find('b').text)
                    _list2.append(Staked_Box.find(name='span').text)
                    print(_list2)
                    DelegationReward = flexBox.find('div', class_='flex column flexAuto').find('b')
                    print(DelegationReward)
                #
                for flexBox in soup.find_all('div', class_='flex column borderedBox poolWidget flexAuto'):
                    '''Do smthing'''
                    stakeBox_name = flexBox.find('div', class_='flex column flexAuto').find('strong').text
                    print(stakeBox_name)
                    #
                    _list = list() # list = list(APY, Pool Supply, Total Staked, Reward Rate)
                    APY_Box = flexBox.find('div', class_='flex flexAuto column borderedBox')
                    try:
                        for class_tag in APY_Box.find_all(class_='flex row'):
                            _list.append(class_tag)
                    except AttributeError:
                            _list.append('NoneType')
                    print(_list)

            break


        # return print(soup)



dir_path = os.path.dirname(os.path.realpath(__file__))
HTML_dirTree_parser(list_directory_tree(dir_path))
