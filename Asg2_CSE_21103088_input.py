
#Question 1

print("Question 1")
str="Python is a case sensitive language"
print("a. Length of the string is : ",len(str))
print("b. Reversed String is : ",str[::-1])
str1=str[7:26]
print("c. New String : ",str1)
str2=str.replace("a case sensitive","an object oriented")
print("d. String after replacing : ",str2)
print("e. Index of substring 'a' in the given string is: ",str.index("a"))
print("f. String after removing white spaces: ", str.replace(" ",""))

#Question 2

print("Question 2")
name="Tejvir"
sid="21103088"
dept="CSE"
cgpa="9.9"
print("Hey, %s here"%(name))
print("My SID is %s"%(sid))
print("I am from %s department and my CGPA is %s"%(dept,cgpa))

#Question 3

print("Question 3")
a=56
b=10
print("a & b is :",a&b)
print("a | b is :", a|b)
print("a ^ b is :", a^b)
print("a << 2 equals %d and b << 2 equals %d"%(a<<2,b<<2))
print("a >> 2 equals %d and b >> 4 equals %d"%(a>>2,b>>4))

#Question 4

print("Question 4")
num1=int(input("Enter frist number : "))
num2=int(input("Enter second number : "))
num3=int(input("Enter third number : "))
l=[num1,num2,num3]                #to create a list of three numbers
l.sort()                          #to sort the three numbers
print("Largest number is",l[2])   #l[2] gives largest number in sorted list

#Question 5

print("Question 5")
strng=input("Enter a String ")
if ("name" in strng ):                         #to check whether name is present in string
    print("YES")
else:
    print("NO")    

#Question 6

print("Question 6")
length1=int(input("Enter first length "))        #input lengths of sides of triangle
length2=int(input("Enter second length "))
length3=int(input("Enter third length "))
if((length1+length2)<length3 or (length2+length3)<length1 or (length1+length3)<length2 ):
    print("Triangle not possible")
else:
    print("Triangle is possible")    