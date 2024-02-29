import requests
import time
import random
import numpy as np
import datetime
import sys

def make_fake_data():

    names = ['창고1','냉장고','사무실','휴계실']

    temperature_range={'창고1':{'mean':10,'std':2},
                       '냉장고':{'mean':5,'std':1},
                       '휴계실':{'mean':20,'std':2},
                       '사무실':{'mean':24,'std':3}}
    
    

    name =random.choice(names)

    temperature=round(np.random.normal(temperature_range[name]['mean'],temperature_range[name]['std'],1)[0],2)

    present_datetime=  datetime.datetime.now().replace(microsecond=0).strftime("%Y-%m-%d %H:%M:%S")
    return f"기록 시간: {present_datetime}, 위치: {name}, 온도 :{temperature}"
    

    
    




def write_file(data:str):
                
    with open("./record.txt",'a') as f:
        f.write(data)
        f.write("\n")



def collecting():

    while True:
        

        try:
            fake_data= make_fake_data()
            
            write_file(data=fake_data)

            time.sleep(10)
        except InterruptedError as e:
            print("user interrupt this process")
            sys.exit(0)
        except KeyboardInterrupt as e:
            print("key board interrupt rise")
            sys.exit(0)

        

if __name__=="__main__":
    # fake_data=make_fake_data()

    # print(fake_data)
    collecting()