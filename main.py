# for c in range (1,13):
#     if c/2 == int(c/2):
#         print(c , 'is even')
#     else:
#         print(c , 'is odd')

# import pandas as pd
# import numpy as np
# print('yaho')
# def multi_100(i):
#   for x in range (i, 100, i):
#     print(x)
    
# multi_100(5)
def multi_100(i):
    k= int(100/i)
    for x in range (1,k+1):
      if x*i < 100:
          print(i, '*', x, '=',x*i)
multi_100(11)