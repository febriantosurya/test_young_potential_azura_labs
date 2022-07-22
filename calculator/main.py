import os

def calculator(operation):
  total = 0
  if operation.count('+') == 1 and operation.count(' ') == 2:
    total = int(operation.partition('+')[0]) + int(operation.partition('+')[2])
    print(total)
    input('Press enter to continue')
  elif operation.count('-') == 1 and operation.count(' ') == 2:
    total = int(operation.partition('-')[0]) - int(operation.partition('-')[2])
    print(total)
    input('Press enter to continue')
  elif operation.count('*') == 1 and operation.count(' ') == 2:
    total = int(operation.partition('*')[0]) * int(operation.partition('*')[2])
    print(total)
    input('Press enter to continue') 
  elif operation.count('/') == 1 and operation.count(' ') == 2:
    total = float(operation.partition('/')[0]) / float(operation.partition('/')[2])
    print(total)
    input('Press enter to continue')
  else:
    print('Input format is wrong!\n')
    input('Press enter to try again')
  

def main():
  while True:
    os.system('clear')
    print('\t\t\t===CALCULATOR===\n')
    print('*Input the number and the operator in one line [e.g. A + B = X]')
    print('*You can only use these operators ["x","/","+","-"]')
    print('*Use space between operand and operator\n')
    operation = input("=> ")
    if operation.find('+') == -1 and operation.find('-') == -1 and operation.find('*') == -1 and operation.find('/') == -1:
      if operation == '0':
        break
    calculator(operation)
    

if __name__ == '__main__':
  main()