from func import *


def HTML_dirTree_parser(tree):


    def flarefarm_snapshot_parser(cls, _dict=dict()):
        '''insert class'''

        for flexBox in soup.find_all('div', class_=cls):
            stakeBox_name = flexBox.find('div', class_='flex column flexAuto').find('strong').text
            rewardBox_name = flexBox.find('div', class_='flex column align-end').find('strong').text
            if rewardBox_name == 'DFLR': stakeBox_name += '|2'

            _dict.update({stakeBox_name: {'reward': rewardBox_name}})

            _list = list() # list = list(APY, Pool Supply, Total Staked, Reward Rate)
            APY_Box = flexBox.find('div', class_='flex flexAuto column borderedBox')
            try:
                for class_tag in APY_Box.find_all(class_='flex row'):
                    for div_tag in class_tag.find_all('div'):
                        _list.append(div_tag.find('p').text)

                _dict[stakeBox_name].update(zip(_list[::2], _list[1::2]))
            except AttributeError:
                _list.append('NoneType')

            _list2 = list() # list = list(You Staked, Unclaimed)
            Staked_Box = flexBox.find('div', class_='flex column widgetPersonal whiteBox')
            try:
                _list2.append(Staked_Box.find('b').text)
                _list2.append(Staked_Box.find(name='span').text)
            except AttributeError:
                _list2.append('NoneType')

            _dict[stakeBox_name].update(zip(["You Staked", "Unclaimed"], _list2))

            try:
                DelegationReward = flexBox.find('div', class_='flex row align-center poolDelegationRow').text
            except AttributeError:
                DelegationReward = 'NoneType'

            _dict[stakeBox_name].update({'delegation': DelegationReward})

        return _dict


    def isHTML(file):
        if file[-5:] == '.html': return True


    def json_dirEXISTS():
        json_dir = f'{dir_path}/json'
        if not os.path.exists(json_dir):
            os.makedirs(json_dir)


    json_dirEXISTS()
    for file in tree:
        if isHTML(file):
            html_timestamp = html_filename_disambiguation(file)

            snapshot = {
                'timestamp': html_timestamp,
            }

            with open(file) as f:
                soup = BeautifulSoup(f, 'lxml')
                balance = soup.find('div', class_='flex balanceWrapper').text

                snapshot.update({'SGB_balance': float(balance.split(' ')[0])})

                box_type = {'activated':'flex column whiteBox poolWidget flexAuto',
                            'passive':'flex column borderedBox poolWidget flexAuto'}

                snapshot.update({'flexBox': dict()})
                for value in box_type.items():
                    S = flarefarm_snapshot_parser(value)
                    snapshot['flexBox'].update(S)

            with open(f'{dir_path}/json/{html_timestamp}.json', 'w') as f:
                json.dump(snapshot, f, indent=2)




############################################################################################################
'''
The Begining of the Programm
'''
dir_path = os.path.dirname(os.path.realpath(__file__))



if __name__ == '__main__':
    HTML_dirTree_parser(list_directory_tree(dir_path))
