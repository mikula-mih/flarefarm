import os, time, datetime
import json
from bs4 import BeautifulSoup


def print_directory_tree(path):
    for root, directories, files in os.walk(path, topdown=True):
        for name in files:
            print(os.path.join(root, name))
        for name in directories:
            print(os.path.join(root, name))


def list_directory_tree(path):
    tree = []
    for root, directories, files in os.walk(path, topdown=True):
        for name in files:
            p = os.path.join(root, name)
            tree.append(p)
        for name in directories:
            p = os.path.join(root, name)
            tree.append(p)
    return tree


def html_filename_disambiguation(f):
    '''
    filename_example = FlareFarm_y2022m01d21_t1309.html
    '''
    epoch = datetime.datetime.utcfromtimestamp(0)
    tm_year, tm_mon, tm_mday, time = int(f[-21:-17]), int(f[-16:-14]), int(f[-13:-11]), f[-9:-5]
    tm_hour, tm_min = int(time[:2]), int(time[2:])
    dt = datetime.datetime(tm_year, tm_mon, tm_mday, tm_hour, tm_min, 0)
    return (dt - epoch).total_seconds()

class Flare_asset():

    def __init__(self, source, value):
        self.source = source
        self.value = value

    def __repr__(self):
        return f'{self.source}: {self.value}'


class FSIN_snapshot():
    '''info'''

    def __init__(self, timestamp, assets):
        self.timestamp = timestamp
        self.assets = assets

    def add_asset(self, asset_name, asset_value):
        self.assets[asset_name] = asset_value



    def __repr__(self):
        str = f'FlareFarm snapshot: {self.timestamp}\n'

        return str
        # print(f'{self.assets})
        # for key, value in self.assets.items:
        #     print(f'{key}: {value}')
