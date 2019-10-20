import threading
import numpy as np
def power_3(x):
    print(f'\nCube({x}) : {x**3}')

def power_2(x):
    print(f'Square({x}) : {x**2}')

if __name__ == '__main__':
    num = np.array([1,2,3,4,5])
    for i in num:
        t1 = threading.Thread(target=power_3, args=(i,))
        t2 = threading.Thread(target=power_2, args=(i,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

    print('Threading Completed...',end="\n\n")

