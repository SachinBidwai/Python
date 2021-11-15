''' PROBLEM 9 . Write a Python program to count the number 4 in a given list.'''

num = input("Enter minimum 10 digit number : ") 
if len(num)>=10:
    print("You enter ", len(num)," digits number : " , num)
else: 
    print("You enter ", len(num)," digits number : " , num, " \n Please follow the instrutions")

numcheck = input("Enter a single digit number : ")
if len(numcheck)==1:
    print("You enter ", len(numcheck)," digits number : " , numcheck)
else: 
    print("You enter ", len(numcheck)," digits number : " , numcheck, " \n Please follow the instrutions") 

num1= list(num)
print(num1)

count =0

for i in range(0,len(num)):
    if numcheck == num1[i]: 
    
    #num(range(0,len(num))):
        count = count + 1
print (numcheck , " digit occures", count, " times in number ", num )    

