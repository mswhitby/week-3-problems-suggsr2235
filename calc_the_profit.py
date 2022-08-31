#lists the functions for cost, sell price, and inventory
def pro(c,s,i):
  #equation to calculate profit
  a=(s-c)*i
  #rounds equation to nearest Hundreth
  a=round(a,2)
  #prints the profit
  print (str(a) + " is your profit")
pro(700.553,1000.7322,455)
