import time, datetime
from func import *

'''
snap = FSIN_snapshot(time.time(), dict())

# snap.add_asset('FSIN1', '0.1')
# snap.add_asset('FSIN2', '0.2')
# snap.add_asset('FSIN3', '0.3')
# snap.add_asset('FSIN4', '0.4')

print(snap)
'''

def start_timer():
    prog_start = time.time()
    dt = datetime.datetime.fromtimestamp(prog_start)
    epoch_duration = 3_600.0
    delta = epoch_duration - (dt.minute * 60 + dt.second)
    time.sleep(delta)

def main():
    timer('2022/01/24 23:00:00')
    # while True:
    #     print(time.ctime())
    #     print(time.time())
    #     print('#')
    #     time.sleep(60)

def timer(str_time):
    '''    %Y/%m/%d %H:%M:%S    '''
    prog_start = time.time()
    dt = datetime.datetime.fromtimestamp(prog_start)
    new_time = datetime.datetime.strptime(str_time, '%Y/%m/%d %H:%M:%S')
    epoch_duration = 3_600.0
    delta = datetime.timedelta(days=new_time.day-dt.day,
                                hours=new_time.hour-dt.hour,
                                minutes=new_time.minute-dt.minute,
                                seconds=new_time.second-dt.second)
    print(delta)
    print(delta.total_seconds())

if __name__ == '__main__':
    main()
