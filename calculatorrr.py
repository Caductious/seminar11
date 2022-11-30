import sys
def summ():
  x=[int(number) for number in sys.argv[1:]]
  return(sum(x))
def both():
    lst=[int(number) for number in sys.argv[2:]]
    if (sys.argv[1])=='+':
        print(sum(lst))
    elif (sys.argv[1])=='*':
        result=1
        for number in lst:
            result*=number
        return(result)