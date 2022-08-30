#defines n as the function for fb
def fb(n):
  #uses remainders to say that if a number is divisible by 3 then put buzz, if 5 then put Fizz, if both, put FizzBuzz
  if n%5 == 0 and n%3 == 0:
   print("FizzBuzz")
  elif n%3 == 0:
   print("Buzz")
  elif n%5 == 0:
    print ("Fizz")
   #defines what n is equal to
fb(15)
