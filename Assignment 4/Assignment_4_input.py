print("Assignment 4 \n\n")


# Question 1
print("Question 1\n\n")
def tower_of_hanoi(n,s,d,h):
    if(n==1):
        print("Move plate 1 from %s to %s"%(s,d))
        return
    tower_of_hanoi(n-1,s,h,d)
    print("Move plate %d from %s to %s"%(n,s,d))
    tower_of_hanoi(n-1,h,d,s)

n_terms=int(input("Enter number of plates"))
Source= "A"
Helper="B"
Destination="C"
tower_of_hanoi(n_terms,Source,Destination,Helper)
print("\n")

# Question 2
print("Question 2\n\n")
print("Using Recursion")
def pascal_triangle(n,original_length):
    if n==0:
        return
    pascal_triangle(n-1,original_length)
    print(" "*(original_length-n),end=" ")    # to print spaces
    first_term=1                              # first term is always 1
    for i in range(1,n+1):
        print(int(first_term),end=" ")
        first_term=first_term*(n-i)/i         # using binomial coefficient
    print()

n_rows=int(input("Enter no. of rows"))
pascal_triangle(n_rows,n_rows)


print("Using Iterations")

n_rows=int(input("Enter no of rows" ))
for i in range(1,n_rows+1):
    print(" "*(n_rows-i),end=" ")
    first_term1=1
    for j in range(1,i+1):
        print(int(first_term1),end=" ")
        first_term1=first_term1*(i-j)/j
    print() 

print("\n")

#QUESTION 3
print("Question 3\n\n")
int1, int2 = map(int,input("Enter 2 numbers: ").split())
Quotient = int1 // int2
Remainder = int1 % int2

#part <a>
print("a. Checking if the quotient and remainder is a callable value or not.")
print(callable(Quotient))
print(callable(Remainder))

#part <b>
if (Quotient == 0):
    print("<b> The quotient is zero")
if (Remainder == 0):
    print("<b> The reminder is zero")
if (Quotient != 0 and Remainder != 0):
    print("<b> All the values are non zero")

#part <c>
part_C_list = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(part_C_list)):
    if part_C_list[i] > 4:
        result.append(part_C_list[i])
print(f"<c> Filtered out numbers that are greater than 4 are : {result}")

#part <d>
set_result = set(result)
print("<d> Set:",set_result)

#part <e>
immutable_Set = frozenset(set_result) #frozen Set is used to make the set immutable
print("<e> Immutable set:",immutable_Set)

#part <f>
print("<f> Hash value of the max value from the above set:", hash(max(immutable_Set)))
print("\n\n")

# Question 4
print("Question 4\n\n")
class Student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
    def __del__(sf):
        print("Object is Deleted")   


student1=Student("Tejvir",21103088)           # creating object
print("Object is created")         
print("Name of Student is %s and Roll Number is %d"%(student1.name,student1.roll_number) )     # printing assigned values
del student1                                                                                    #deleting object

print("\n\n")    

# Question 5
print("Question 5\n\n")
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
# creating objects    
employee1=Employee("Mehak",40000)            
employee2=Employee("Ashok",50000)            
employee3=Employee("Viren",60000)            
print("Objects Created")
# printing assigned values
print(employee1.__dict__)
print(employee2.__dict__)
print(employee3.__dict__)
employee1.salary=70000          # modifying value
del employee3                   # deleting object
print("After Updating....")
print("Record of Viren Deleted")
print(employee1.__dict__)

print("\n\n")


#QUESTION 6
print("Question 6\n\n")
#input a word from the first friend
word =input("Enter the word: ")
word=word.lower()

#input a meaningful word with the exact same letters
word_input = input("Enter a new meaningful word using the exact same letters to test your friendship: ")
word_input=word_input.lower()
#defining dictionary
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count
#shopkeeper's input to verify the word's meaning
def userinput():
    if count_in_dict(word) != count_in_dict(word_input):
        print("The letters aren't exact, friendship is fake")
        return
    ans = input("Does the word makes sense?(y/Y or n/N )")

    if ans == 'y' or ans=='Y':
        print("The friends pass the friendship test")
    elif ans == 'n' or ans=='N':
        print("The word doesn't have a meaning, friendship is fake")
    else:
        print("Invalid input,try again with y/Y or n/N ")
        userinput()
userinput()


    
