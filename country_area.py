#defines c and n as variables
def aoc(c,n):
#the calculations to get the countries % landmass of the earth
  a = (n/148940000)*100
  a = round(a,2)
  #prints the required message back
  print (c+" is " + str(a) +"% of the world's landmass.")
    
aoc('USA',9372610)
