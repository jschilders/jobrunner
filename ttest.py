from tqdm import tqdm
from time import sleep
from random import randrange


bar = []
numbars=150
for task in range(0,numbars):
    bar.append(tqdm(
            #total=10, 
            unit='',
            desc=f'Task{task}'
        )
    )

i=0  
while True:
    i+=1 
    bar[randrange(0,numbars)].update()
    if i>100:
        bar[randrange(0,numbars)].close()
    else:
        bar[randrange(0,numbars)].set_description(f"Task_{randrange(100,200)}")
    
    sleep(randrange(5,15)/30)
