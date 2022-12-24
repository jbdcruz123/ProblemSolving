
#triangle 6sides screen display

import math


def finit(scr):#2
      
      global row
      global col
      
      i = 0
      while i < row:#3
      
            scr.append( [ ] )
            j =0
            while j < col:#4

                  scr[i].append(".")
                  j+=1
            #4

            i+=1
      #3

      return scr
#2


def fdisp(scr):#2

      global row
      global col
      i = 0
      while i < row:#3
      
            j =0
            while j < col:#4

                  print( scr[i][j], end = "") 
                  j+=1
            #4
            print()
            i+=1
      #3

#2

scr = [ ]
#standard screen
row = 33

col = 40


scr = finit(scr)

#maximum size is 
#size = 18


print("input maximum size, maximum ay dapat wag lalampas sa 18:  ")
size = int(input())

if size >= 18 +1: #11

      print("sobra sa 18, mag exit tayo ")
      exit()
#11


tri = (size * 2) + 1

m = int(tri /2) + 1

les = 1

inc = 1
fin = m
fin_last = -1

print(f"\nL10 measurement {size= }, {m= }, {les= }, {tri= }")

#we use none standard index start at 1
i_row =1
while 1:#3

      #print(f"\nL11 {tri=}, {row= }")
      i_col = 1
      while i_col <= tri :#3

            #print(f"\nL12 {tri=}, {col= }")
            if i_col >= m - (les -1 ) and i_col <= m + (les -1):#7

                  scr[i_row-1][i_col-1] = "*"
            #7
            i_col+=1
      #3
      
      les += inc

      if i_row == fin_last: #10

            break
      #10


      if i_row == fin: #5
            
            fin = -1
            inc = -1
            les = m
             
            i_row = int( m /3 )
            fin_last = i_row + m
            
            #print(f"\nL14 {fin_last=}, {i_row= }")
            #input()

      #5

      i_row+=1
#3


fdisp(scr)

