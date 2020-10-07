def multi_100(i):
    k= int(100/i)
    for x in range (1,k+1):
      if x*i < 100:
          print(i, '*', x, '=',x*i)

multi_100(0.5)



def multiplication_less_100(x):
    i = 1
    while x*i < 100:
        print(x, '*', i, '=',x*i)
        i = i + 1