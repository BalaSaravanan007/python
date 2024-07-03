# n = int(input("Enter a number: "))
# a, b = 0, 1
# count = 0

# while count < n:
#     print(a, end = ", ")
#     a,b = b, a+b
#     count += 1

# n = int(input("Enter a Number: "))
# sum = 0
# i = 1

# while i <= n:
#     sum += i
#     i += 1
# print(sum)

# x = 1
# y = 1
# z = 2
# n = 3
# perms = [([i, j, k]) for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n] 
# print(perms)
    
# score = [1, 2, 3, 3, 5, 4, 9]
# max_score = max(score)
# runnerUp = [x for x in score if x != max_score]
# print(max(runnerUp))

# if __name__ == '__main__':
#     my_score =[]
#     my_dict = {}
#     for _ in range(int(input("n: "))):
#         name = input("Name: ")
#         score = float(input("Score: "))
#         my_score.append(score)
#         my_dict[name]=score

# Sec_low = [x for x in my_score if x != min(my_score)]
# s = min(Sec_low)

# value_to_find = s

# key_for_value = [key for key, value in my_dict.items() if value == value_to_find]
# key_for_value.sort()

# if key_for_value is not None:
#     for i in key_for_value:
#         print(i)
# else:
#     print("There is no Key")

# if __name__ == '__main__':
#     n = int(input("n: "))
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input("Name: ").split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input("QueryName: ")
# def avg(scores):
#     return sum(scores)/len(scores)
# avg_score = avg(student_marks[query_name])
# TwoDecimal = "{:.2f}".format(avg_score)
# print(TwoDecimal)


# if __name__ == '__main__':
#     N = int(input("Number of Changes: "))
#     my_list = []
#     for _ in range(N):
#         command = input("On your Command: ").split()
#         action = command[0]
        
#         if action == "insert":
#             i= int(command[1])
#             e = int(command[2])
#             my_list.insert(i, e)
#         elif action == "print":
#             print(my_list)
#         elif action == "remove":
#             e = int(command[1])
#             my_list.remove(e)
#         elif action == "append":
#             e = int(command[1])
#             my_list.append(e)
#         elif action == "sort":
#             my_list.sort()
#         elif action == "pop":
#             my_list.pop()
#         elif action == "reverse":
#             my_list.reverse()
# print(my_list)

# n, m = map(int, input().split())

# List_A = []
# for i in range(n):
#     List_A.extend(input().split())

# List_B = []
# for i in range(m):
#     List_B.extend(input().split())

# a = []
# for i in List_B:
#     if i in List_A:
#         a.append(List_A.index(i))
# print(a)


# T = int(input())
# for i in range(T):

#     try:
#         a, b = map(int, input().split())
#         print(a/b)
#     except ZeroDivisionError as e:
#         print("Error Code:", e)
#     except ValueError as a:
#         print("Error Code:", a)

# import re

# T = int(input())
# for i in range(T):
#     try:
#         S = (input())
#         re.compile(S)
#         print(True)
#     except re.error:
#         print(False)
        

from collections import namedtuple

N = int(input())
headers = input().split()
Student = namedtuple('Student', headers)

total_marks = 0

for i in range(N):
    data = input().split()
    student = Student(*data)
    total_marks += int(student.MARKS)

Average = total_marks/N
print(Average)