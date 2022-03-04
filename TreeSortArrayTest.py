# tree sort using array
# N * 2 + 1 (number of tree)
def fNw(A, N, V): #1A 
  
  if A[N] == -1: #2

    A[N] = V
    
    print("Ang huling lengt na dinag dag (N*2)+2", (N*2)+2, "N", N)
    #left
    A[(N*2)+1] = -1
   
    #right
    A[(N*2)+2] = -1

    return
  #2

  if   V < A[N] : #2
    #left
    
    fNw( A, (N*2)+1, V) 
  else :#2.2  .. V > N
    #right
     fNw( A, (N*2)+2, V) 
  #2


#1A 

def fPr(A, N): #1B

  if A[N]==-1: #2
    return
  #2
  #left
  
  
  fPr( A, (N*2)+1) 
  
  
  print(A[N])

  #right
  fPr( A, (N*2)+2) 


#1B

def fMn(): #1C 
  A = []  
  B=[0,1,2,3,4 ,5,6,7,8,9]
  N= 10

  print("Bilang ng na aasign na length (N*4)+2+1", (N*300)+2+1)
  #print("L9B", A)
  
  for I in range(0, (N*300)+2+1): #2
    A.append(-2)
  #2

  #initial null
  A[0] =-1
  I =0
  while I < N : #2

    fNw(A, 0, B[I])
        
    I+=1
  #2

  print("\nprint tree A:")  

  fPr(A, 0)
  #print(A)
#1A 


fMn() 


Bilang ng na aasign na length (N*4)+2+1 3003
Ang huling lengt na dinag dag (N*2)+2 2046 N 1022


