# Question 1
print("Question 1 \n")
str=input("Enter the string : ")
words=str.split()                      # to split the string into a list of words
word_count=words.__len__()             # stores number of words in the string
dict={}
if(word_count==1):                     # executed when there is only one word
    for i in words[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict) 
else:                                  # executed when there are more than one words  
    for i in words:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)          

# Question 2
print("Question 2\n")
valid=False
while(valid==False):                                        # while block to ask the date again if entered dat is invalid

    while(True):                                            # To ensure entered month is valid 
        month=int(input("Enter the month : "))
        if(month <= 12 and month >= 1):
            break
        else:
            print("Please enter valid month")

    while(True):                                            # To ensure entered day is valid
        day=int(input("Enter the day : "))
        if(day>=1 and day<=31):
            break
        else:
            print("Please enter a valid day")

    while (True):                                            # To ensure entered year is within the range given in question
        year=int(input("Enter the year : "))
        if(year <= 2025 and year >= 1800):
            break
        else:
            print("Please enter a valid year")

    print("Date entered is %d/%d/%d"%(day,month,year))        # To print the date entered by user

    if(day>=1 and day <= 27):                                 # Executes when day lies between 1 and 27
        day=day+1
        print("Next Date is : %d/%d/%d"%(day,month,year))    
        valid=True                                            # This ensures that code doesnt execute again if date entered is valid

    elif(day==28 ):                                                # Executes when day entered is 28 
        if(month ==2):                                                       # Executes when month is Feb
            if(((year % 4==0) and (year%100!=0)) or year%400==0 ):           # Executes if the year entered is leap
               day=day+1
               print("Next Date is : %d/%d/%d"%(day,month,year))
               valid=True        
            else:                                                            # Executes for Non Leap year
                day=1
                month=3   
                print("Next Date is : %d/%d/%d"%(day,month,year)) 
                valid=True        
        else:                                                      #Executes when month is not Feb
            day=day+1
            print("Next Date is : %d/%d/%d"%(day,month,year))  
            valid=True      

    elif(day==29):                                           #Executes when day entered is 29
        if(month == 2):                                                   
            if(((year % 4==0) and (year%100!=0)) or year%400==0 ):  # Executes when Year is Leap
                day=1
                month = 3
                print("Next Date is : %d/%d/%d"%(day,month,year))  
                valid=True      
            else:                                                   # 29th Feb does not exist for Non Leap year, hence invalid date
                print("Invalid Date")
        else:
            day=day+1
            print("Next Date is : %d/%d/%d"%(day,month,year))  
            valid=True      

    elif(day==30):                                           # Executes when day entered is 30
        if(month ==1 or 3 or 5 or 7 or 8 or 10 or 12):
            day=day+1
            print("Next Date is : %d/%d/%d"%(day,month,year)) 
            valid=True       
        elif(month ==(4 or 6 or 9 or 11)):
            day =1
            month =month +1
            print("Next Date is : %d/%d/%d"%(day,month,year))   
            valid=True     
        else:                                                 # Executes when date is like 30 Feb
            print("Invalid date")

    elif(day==31):
        if(month ==1 or 3 or 5 or 7 or 8 or 10):
            day=1
            month=month+1
            print("Next Date is : %d/%d/%d"%(day,month,year))  
            valid=True      
        elif(month == 12):
            day=1
            month=1
            year=year+1
            print("Next Date is : %d/%d/%d"%(day,month,year)) 
            valid=True
            Invalid_date=True       
        else:                                                  #Executes when Date entered is like 31 April, which doesnt exist
            print("Invalid Date")
            
             
# Question 3
print("Question 3\n")
list=[]                                                       # Creates an empty list
n=int(input("Enter the number of elements : "))               # asks the user for no. of elements  
print("Enter elements ")
for i in range(n):
    inp=int(input())                              
    list.append(inp)                                          # Adds the entered value to the list
print("Entered list is : ",list)  
print("List of tuples : ")
list_tuples=[]                                                # Creates an empty list in which we will store tuples
for i in list:
    new_tuple=(i,i**2)                                        # creates a tuple which contains a number and its square
    list_tuples.append(new_tuple)                             # adds the tuple to list of tuples
print(list_tuples)                                            # Prints the list containing tuples
        
#Question 4
print("Question 4\n")
grade=int(input("Enter the grade points"))
if(grade<4 or grade>10):
    print("Invalid Grade")
elif(grade==10):
    print("Your Grade is A+ and Outstanding Performance")    
elif(grade==9):
    print("Your Grade is A and Excellant Performance")        
elif(grade==8):
    print("Your Grade is B+ and Very Good Performance")        
elif(grade==7):
    print("Your Grade is B and Good Performance") 
elif(grade==6):
    print("Your Grade is C+ and Average Performance")    
elif(grade==5):
    print("Your Grade is C and Below Average Performance")
elif(grade==4):
    print("Your Grade is D and Poor Performance")    

#Question 5
print("Question 5\n")
str="ABCDEFGHIJK"
space=""
len=str.__len__()                            # Gives the length of entered string
for i in range(str.__len__()//2 + 1):        # loop executes until only one letter remains
    print(space+(str[0:(len)]))              # prints apropriate no. of spaces and then substring            
    space=space+" "                          # to increase the spacing for next line of output 
    len=len-2                                # reduces the index (upto which it truncates) by 2 consecutively  

#Question 6
print("Question 6\n")
add= "Y"
dictionary={}                                # Creates ampty dictionary
while(add=="Y"):                             # To take as many inputs as the user wants
    name=input("Enter the name of the student : ")
    SID=input("Enter the SID of the student : ")
    dictionary[SID]=name                                  # Assigns the name (value) to SID (key)
    add=input("Enter Y to add details of more students otherwise enter N ")
print(dictionary)
print("Dictinoary after sorting by Student Name : ")
print({k:v for k,v in sorted(dictionary.items(),key=lambda v:v[1])})   # Sorting by value
print("Dictionary after sorting by SID") 
print({k:v for k,v in sorted(dictionary.items())})                     # Sorting by key
inp_sid=input("Enter SID to find student name : ")
if inp_sid in dictionary.keys():                                       # Checks whether the entered SID is present in the dictionary or not
    print("Name of the Student : ",dictionary[inp_sid])
else:
    print("No Name found for given SID") 

#Question 7
print("Question 7\n")
i=0
j=1
k=0
sum=i+j                                                      # To store the sum of the fibonacci series
n_term=int(input(("Enter number of terms of fibonacci series to print")))
print(i)                                                     # To print first element of fibonacci series          
print(j)                                                     # To print second element of fibonacci series

for k in range(n_term-2):                                    # Prints the remaining elements of series
    k=i+j                                                    
    sum=sum+k                                                # Adds the values to sum one by one   
    print(k)
    i=j
    j=k
print("Average of series: ",(float(sum/n_term)))             # Prints average of series

# Question 8
print("Question 8\n")
Set_1 = {1, 2, 3, 4, 5}
Set_2 = {2, 4, 6, 8}
Set_3 = {1, 5, 9, 13, 17}
# part a
Set_Union = Set_1.union(Set_2)
Set_Intersection = Set_1.intersection(Set_2)
Part_A_Set = Set_Union - Set_Intersection
print("<a>", Part_A_Set)

# part b(Subtracting intersection of sets taken two at a time from the Union of all three sets)
Part_B_Set = Set_1.union(Set_2.union(Set_3)) - Set_1.intersection(Set_2) - Set_2.intersection(Set_3) - Set_3.intersection(Set_1)
print("<b>", Part_B_Set)

# part c(Subtracting the intersection of all three sets from the Intersection of sets taken two at a time)
Part_C_Set=((Set_1.intersection(Set_2)).union((Set_1.intersection(Set_3)).union(Set_2.intersection(Set_3))))-(Set_1.intersection(Set_2.intersection(Set_3)))
print("<c>",Part_C_Set)
# part d(Excluding the numbers from 1 to 10 that are occuring in Set1)
Part_D_Set = set()
for i in range(1, 11):
    if i not in Set_1:
        Part_D_Set.add(i)
print("<d>", Part_D_Set)
# part e(Excluding the numbers from 1 to 10 that are occuring in Set1, Set2 and Set3)
Part_E_Set = set()
for i in range(1, 11):
    if i not in Set_1 and i not in Set_2 and i not in Set_3:
        Part_E_Set.add(i)
print("<e>", Part_E_Set)
    

