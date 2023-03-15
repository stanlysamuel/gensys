import threading
from z3 import *
from time import sleep
import random

def simpleSatCheck():
    ctx=Context()
    solver = Solver(ctx=ctx)
    x=Real('x',ctx=ctx)
    solver.add(x > 10, x < 20)
    print(solver.check())

threads = []
for i in range(0,2):
    thread = threading.Thread(target=simpleSatCheck, args=())
    threads.append(thread)
    thread.start()

for thread in threads:
        thread.join()

# class ContextManager():
#     def __init__(self):
#         print('init method called')
         
#     def __enter__(self):
#         print('enter method called')
#         return self
     
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         print('exit method called')
 
# threads = []

# for i in range(0,2):
#     with ContextManager() as manager:
#         thread = threading.Thread(target=simpleSatCheck, args=())
#         threads.append(thread)
#         thread.start()

# with ContextManager() as manager:
#     for thread in threads:
#         thread.join()
