from random import randint
from tqdm import tqdm
import time

def randtime():
    randtime_int = randint(120, 180)
    return randtime_int

def variable_timer():
	randtime_value = randtime()
	print(randtime_value)

	randtime_mult = randtime_value*10

	for i in tqdm(range(randtime_mult)):
		time.sleep(0.1)