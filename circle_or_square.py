import math
#defines the circle and square function
def cos(c,s):
  #calculations to get the perimeter of a square and circle (represented by sp and cp repsectively) 
 sp=s/math.sqrt(s)*4
 cp= c*2*3.14
  #states that if the perimeter of the circle is bigger than the square's, print true, if the opposite print false
 if cp > sp:
   print ('true')
 if sp > cp:
   print ("False")
cos(1500,1200)
