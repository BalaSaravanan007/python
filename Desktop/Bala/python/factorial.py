##factorials

##def factorial(num):
##    if num == 0:
##        return 1
##    else:
##        return num * factorial(num -1)
##
##print(factorial(5))
##

##squares

##def sqr(a):
##    return a**2
##
##print(sqr(10))

##square roots

##def sqrt(a):
##    return a **0.5
##
##print(sqrt(100))

##exponents

##def expo(a, b):
##    return a **b
##
##print(expo(2, 10))

##fabonacci

##def fabonacci(a):
##    seq = [0,1]
##    while len(seq) < a:
##        seq.append(seq[-1] + seq[-2])
##    return seq
##
##print(fabonacci(10))

#check for prime

##def check_prime(a):
##    if a <= 1:
##        return False
##    
##    else:
##        for i in range(2, int(a**0.5)+1):
##            if a % i == 0:
##                return False
##        return True
##
##result = check_prime(12)
##print(result)
##

##reverse a list

##def reverse_list(a):
##    return a[::-1]
##
##result = reverse_list([1,2,3,4,5])
##print(result)

##Palindrome

##def is_palindrome(a):
##    if a == a[::-1]:
##        return True
##    else:
##        return False
##
##result = is_palindrome("MALAYALAM")
##print(result)
##


##lambda func

##print((lambda x, y: x + y)(36, 44))
##
##print((lambda x,y,z:(x+y+z)**3)(1,2,3))

##class

##class Person:
##    def  __init__(self, name, age):
##        self.name = name
##        self.age = age
##
##    def my_func(self):
##        print("My name is " + self.name)
##        print(f"My age is {self.age}")
##
##person1 = Person("Bala", 17)
##person1.my_func()

##class Persons:
##    def __init__(self, fname, lname):
##        self.fname = fname
##        self.lname = lname
##
##    def printname(self):
##        print(self.fname, self.lname)
##
##p1 = Persons("Bala", "Saravanan")
##p1.printname()
##
##class Students(Persons):
##    def __init__(self, fname, lname):
##        super().__init__(fname, lname)
##
##s1 = Students("Dinesh", "Kumar")
##s1.printname()

##classes

####class temp_convertor:
####    def to_celcius(farenheit):
####        return (farenheit - 32)*5/9
####
####    def to_farenheit(celcius):
####        return (celcius *9/5) + 32
####
####print(temp_convertor.to_celcius(100), "C")
####print(temp_convertor.to_farenheit(37.77777777777778), "F")


##class ATM:
##    def __init__(self):
##        self.balance = 1000
##
##    def check_balance(self):
##        return self.balance
##
##    def deposit(self, amount):
##        self.balance += amount
##        return f"deposited amount :{amount} , current balance :{self.balance}"
##
##    def withdraw(self, amount):
##        if amount <= self.balance:
##            self.balance -= amount
##            return f"withdrew amount: {amount}, current balance: {self.balance}"
##        else:
##            return "Invalid"
##
##atm = ATM()
##
##print(atm.deposit( 500))
    
        


##for i in range(4):
##    for j in range(4):
##        print("*",end=" ")
##        
##    print()
  
##for i in range(1):
##    print("    *    ")
##    for j in range(1):
##        print("  *  *  ")
##        for k in range(1):
##            print(" * * * ")
##            for l in range(1):
##                print("* * * *")
##print(i,"i  ", j, "j  ")
    
##for i in range(4):
##    print("*", end = " ")
##for j in range(2):
##    print("\n*      *")
##for k in range(4):
##    print("*", end = " ")
##print(i,"i   ",j,"j   ")


##for i in range(5):
##    for j in range(5-i-1):
##        print("",end = " ")
##    for j in range(i+1):
##        print("*",end =  " ")
##    print()
##
##for i in range(4):
##    for j in range(4):
##        if i == 0 or i == 3 or j == 0 or j == 3:
##            print("*", end = " ")
##        
##        else:
##            print(" ", end = " ")
##    print()
####

##for i in range(5):
##    for j in range(5):
##        if i == j or j == 4-i:
##            print("*", end = " ")
##        else:
##            print(" ", end = " ")
##    print()


##for i in range(5):
##    for j in range(i+1):
##        print("*",end =  " ")
##    print()

##for i in range(5):
##    for j in range(9):
##        if j == 5-i-1 or (i == 2 and j == 4) or j == 5+i-1:
##            print("*", end = " ")
##        else:
##            print(" ", end = " ")
##    print()


##n = range(104)
##for x in n:
##    if x % 2 != 0:
##        print(x, end = " ")
##        if (x +1) % 8 == 0:
##            print("")
##    else:
##        print(" ", end = " ")
##print()




##class Student_Management:
##    def __init__(self):
##        self.name = []
##
##    def add_name(self, name):
##        self.name.append(name)
##        return f"added name: {name}"
##
##    def remove_name(self,name):
##        if name in self.name:
##            self.name.remove(name)
##            return f"removed name: {name}"
##        else:
##            return f" {name} is not found in the list"
##
##    def show_name(self):
##        return self.name
##
##s_m = Student_Management()
##
##print(s_m.add_name(name = "Bala Saravanan"))
##print(s_m.add_name(name = "Dinesh Kumar"))
##print(s_m.show_name())
        
        
##n = range(1,21)
##
##x = int(input("Table: "))
##for i in n:
##    print(i, "*", x, "=", i*x)
##print()

##class Vehicle:
##    def __init__(self, name, brand):
##        self.name = name
##        self.brand = brand
##
##    def move(self):
##        return "Drive!"
##
##class Car(Vehicle):
##    pass
##
##class Train(Vehicle):
##    def move(self):
##        return "Rail!"
##
##class Ship(Vehicle):
##    def move(self):
##        return "Sail!"
##
##class Plane(Vehicle):
##    def move(self):
##        return "Fly!"
##
##C1 = Car("Inova", "Toyota")
##T1 = Train("Bullet", "Japan")
##S1 = Ship("Endevear", "Ocean")
##P1 = Plane("365", "Air Bus")
##
##for x in (C1, T1, S1, P1):
##    print(x.move())
##    print(x.name)
##    print(x.brand)

##class Rectangle:
##    def __init__(self, width, length):
##        self.width = width
##        self.length = length
##
##    def Area(self):
##        return self.width*self.length
##
##    def Perimeter(self):
##        return 2*(self.width + self.length)
##    
##n = int(input("Width: "))
##m = int(input("Length: "))
##
##rect = Rectangle(n, m)
##
##print("Area: ", rect.Area())
##print("Perimeter: ", rect.Perimeter())

##class Bank_acc:
##    def __init__(self, balance):
##        self.balance = balance
##
##    def display_balance(self):
##        return f"balance: {self.balance}"
##
##    def deposit(self, amount):
##        self.balance += amount
##        return f"deposited: {amount}, current: {self.balance}"
##
##    def withdraw(self, amount):
##        if self.balance >= amount:
##            self.balance -= amount
##            return f"withdrew: {amount}, current: {self.balance}"
##        else:
##            return "Error"
##
##bacc = Bank_acc(100000)
##
##print(bacc.deposit(10000))
##print(bacc.withdraw(500))
##print(bacc.display_balance())
    
##class Student:
##    def __init__(self, name):
##        self.name = name
##        self.grade = []
##
##    def add_grade(self, grade):
##        self.grade.extend(list(grade))
##        return f"Your grades: \n{self.grade}"
##        
##
##    def avg_grade(self):
##        x = float(sum(self.grade)/len(self.grade))
##        if x >= 90:
##            return (f"average grade: {x}\nCongratulations you'r Qualified ")
##        else:
##            return (f"average grade: {x}\nSorry you'r Not Qualified")
##        
##
##student = Student("Bala Saravanan")
##print("Name: ", student.name)
##print(student.add_grade([94,99,100]))
##print(student.avg_grade())
    
##class Product:
##    def __init__(self, name, cost, quantity):
##        self.name = name
##        self.cost = cost
##        self.quantity = quantity
##
##    def total_cost(self):
##        return self.cost * self.quantity
##
##prod1 = Product("Nike Shoes", 2999, 1)
##prod2 = Product("Tylor Shirts", 799, 3)
##prod3 = Product("Fastrack Watch" , 1499, 2)
##prod4 = Product("Snitch formal trousers", 899, 4)
##
##n = [prod1, prod2, prod3, prod4]
##
##total_cost = 0
##
##for x in n:
##    print("Product Name: ", x.name)
##    print("Quantity: ", x.quantity)
##    print("cost: Rs.", x.total_cost(),"\n")
##    total_cost += x.total_cost()
##    
##print("Total Cost: Rs.", total_cost)

##nums = [ 1,2,3,4]
##x = nums[:4]
##if 9 in x :
##    print(True)
##else:
##    print(False)

##x = "Hello"
##y = "Hejhllo"
##count = 0
##while 
##for i in range(10):
##    print(x[i:i+2]==y[i:i+2])
    
##print(x[4:6]==y[4:6])
##
##print(x[4:6])


##num = 999
##print((num+5)//10*10)
    
##def double_char(x):
##    result = ""
##    for i in range(len(x)):
##        result +=  x[i]*2
##    return result
##print(double_char("Bala"))

##my_list =  [1, 2, 2, 1, 3, 7,  7]
##a = max(my_list)
##b = min(my_list)
##my_list.remove(a)
##my_list.remove(b)
##print(my_list)

##def sum13(nums):
##    for i in nums:
##        if i == 13:
##            nums.remove(i)
##    return sum(nums)
##            
##
##print(sum13([13, 1, 2, 13, 2, 1, 13]))

##my_list = [1, 2, 3, 4, 5]
##num_indices = {}
##print (num_indices)
##for index, value in enumerate(my_list):
##    print(f"Index: {index}, Value: {value}")

##class ListNode:
##    def __init__(self, val=0, next=None):
##        self.val = val
##        self.next = next
##
##def traverse_linked_list(head):
##    current = head
##    while current:
##        print(current.val, end=" -> ")
##        current = current.next
##    print("None")  # Indicates the end of the list
##
### Example usage
### Construct a linked list: 1 -> 2 -> 3 -> None
##head = ListNode(1)
##head.next = ListNode(2)
##head.next.next = ListNode(3)
##
### Traverse the linked list and print its elements
##traverse_linked_list(head)


##class Solution:
##    def romanToInt(s: str):
##        roman_num = {
##            "I" : 1, 
##            "V" : 5,
##            "X" : 10,
##            "L" : 50,
##            "C" : 100, 
##            "D" : 500, 
##            "M" : 1000
##        }
##        total = 0 
##        prev_val = 0 
##
##        for i in reversed(s):
##            currentVal = roman_num[i]
##            if currentVal < prev_val:
##                total -= currentVal
##            else:
##                total += currentVal
##            prev_val = currentVal
##
##        return total
##s1 = Solution.romanToInt("MDLVXIII")
##print(s1)

n, m = map(int, input().split())

List_A = []
for i in range(n):
    List_A.append(input().split())

List_B = []
for i in range(m):
    List_B.append(input().split())

for word in List_B:
    indices = [i +1 for i, w in enumerate(List_A) if w == word]
    if indices:
        print(' '.join(map(str, indices)))
    else:
        print(-1)



        
    


    

















