import sys
lst=[int(number) for number in sys.argv[2:]]
print(lst)
print(sys.argv[1])
if (sys.argv[1])=='+':
  print(sum(lst))
elif (sys.argv[1])=='x':
  result=1
  for number in lst:
    result*=number
  print(result)
