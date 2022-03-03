

while 1 :#5 

  print("\ninput number:")
  N = int( input() )

  O = (N % 2) != 0

  if O != 0:#2

    print("\nOdd Weird")

  elif N < 2: #2.2
    
    print("\nWlang below 2 ang input\n eexit tayo")
    exit()

  elif O ==0 and (N <= 5 or N >20): #2.3 
    print("\nEven Not Weird")

  elif O ==0 and ( N <20):#2.4
    print("\nEven Weird")

  #2.4

#5

# Od W, 2-5 even N W, 6-20 even W, > 20 even N W
#1< N < 100