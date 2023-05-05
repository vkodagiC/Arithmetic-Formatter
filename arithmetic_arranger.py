def arithmetic_arranger(problems,flag = False):
  if(len(problems)>5):
    raise ValueError("Error: Too many problems.")

  numerators = []
  denominators = []
  signs = []

  for arg in problems:
    temp = ""                    #Cleaning the input and putting                                   data in respective lists 
    arg = arg.strip()
    arg = arg.replace(" ","")
    # print(arg)
    for c in arg:
      if(c.isnumeric() == False):
        if c == '+':
          signs.append(1)
        elif c == '-':
          signs.append(0)
        else:
          raise ValueError("Error: Operator must be '+' or '-'.")
        try:
         temp = int(temp)
        except:
          raise ValueError("Error: Numbers must only contain digits.")
        if len(str(temp))>4:
          raise ValueError("Error: Numbers cannot be more than four digits.")
        numerators.append(int(temp))
        temp = ""
        continue
      temp += c
    try:
         temp = int(temp)
    except:
          raise ValueError("Error: Numbers must only contain digits.")
    if len(str(temp))>4:
      raise ValueError("Error: Numbers cannot be more than four digits.")
    denominators.append(int(temp))

  # for i in numerators:
  #   print(i)
  # print("\n")
  # for i in denominators:
  #   print(i)
  # print("\n")
  # for i in signs:
  #   print(i)
  # print(len(signs))
  # print(len(numerators))
  # print(len(denominators))
  secondline = ""                #Making the secondline
  for i in range(len(signs)):
    if(signs[i] == 1):
      secondline = secondline + '+'
    else:
      secondline = secondline + '-'
    k = max(len(str(numerators[i])),len(str(denominators[i])))
    if len(str(numerators[i]))<len(str(denominators[i])):
      secondline += " "
      secondline += str(denominators[i])
    else:
      k = k - len(str(denominators[i])) + 1
      while k > 0:
        secondline += " "
        k -= 1
      secondline += str(denominators[i])
    
    secondline += "    "
  # print(secondline)
  # print(len(secondline))
  secondline.strip(" ")
  firstline = ""
  index = []
  i = 0
  t = ''
  for c in secondline:
    if c == ' ' and t!='':     #Creating index on each last                                      digit in second line 
      index.append(i)
      t = ''
      
    if c.isnumeric() == True:
      t+=c
    i+=1


  # print(len(secondline))
  # print(len(index))
  # for i in index:
  #   print(i ,"\n")
  for i in range(len(numerators)):    
    num = str(numerators[i])
    k = len(num)
    if i == 0:
     k = index[i] - k                #Creating first line
    else:
      k = index[i] - index[i-1] - k
    while k>0:
      num = ' '+ num
      k -= 1
    firstline += num
    
  # print(firstline)
  firstline.rstrip()

  thirdline = ""

  # for i in index:
  #   print(i)
  k = 0
  for i in range(len(index)):
    temp = index[i]
    while temp - k > 0:
      thirdline += "-"               #Creating third line
      temp -= 1
    k = index[i] + 4
    thirdline += "    "
  thirdline.rstrip()
  
  # print(firstline)
  # print("\n")
  # print(secondline)
  # print("\n")
  # print(thirdline)

  fourthline = ""
  if flag == True:
    sum = []
    for i in range(len(signs)):
      sum.append(numerators[i] + denominators[i])
    
    for i in range(len(sum)):
     num = str(sum[i])
     k = len(num)
     if i == 0:
      k = index[i] - k
     else:                              #Creating last line
      k = index[i] - index[i-1] - k
     while k>0:
      num = ' '+ num
      k -= 1
     fourthline += num
    
  # print(firstline)
  firstline.rstrip()
  arranged_problems = firstline + "\n" + secondline + "\n" + thirdline + "\n" + fourthline
  return arranged_problems