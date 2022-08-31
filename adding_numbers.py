def add(n1,n2):
  return n1+n2
n3=add(17,67)
print(n3)
#basic code that adds two numbers together

#one done in class
def add(n1,n2):
  if (n1 != "" or None) and (n2 != "" or None):
    answer=(int(n1)+int(n2))
    print(str(answer))
  else:
    print("invalid operation")
add("15","67")
