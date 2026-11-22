# def greet(naam):
#     return "Hello " + naam

# print(greet("Himanshu"))

# print(greet("Rahul"))


# def is_even(num):
#     if num%2==0:
#         return True
#     else:
#         return False

# print(is_even(20))
# print(is_even(0))
# print(is_even(-4))

# print(is_even(7))
# print(is_even(1))
# print(is_even(-3))



# test_cases=[
#     (0,True),
#     (20,True),
#     (-4,True),
#     (7,False),
#     (1,False),
#     (-3,False),
# ]

# for num, expected in test_cases:
#     actual=is_even(num)
#     if actual==expected:
#         print(num,"PASS")
#     else:
#         print(num,"Fail - expeced",expected, "but got", actual)    


# -------------List -----------------------

# fruits=["apple", "banana", "mango"]

# print(fruits[0])
# print(fruits[2])
# print(len(fruits))

# fruits.append("orange")
# print(fruits)

# for f in fruits:
#     print (f)


# num=[10, 25, 7, 40, 3]

# for n in num:
#     if n>20:
#         print(n)


# def above_limit(numbers, limit):
#     result=[]
#     for n in numbers:
#         if n > limit:
#             result.append(n)

#     return result

# print(above_limit([10, 25, 7, 7, 40, 3],20))       

# test_cases=[
#     ([10, 25, 7, 7, 40, 3], 20, [20,40])
# ]

# for numbers, limit, expected in test_cases:
#     actual = above_limit(numbers, limit)
#     if actual == expected:
#         print("PASS")
#     else:
#         print("FAIL - expected", expected, "but got", actual)


# def above_limit(numbers, limit):
#     result = []
#     for n in numbers:
#         if n > limit:
#             result.append(n)

#     return result

# print(above_limit([10, 25, 40], 20))
# print(above_limit([20, 21], 20))
# print(above_limit([], 20))

# def below_limit(numbers, limit):
#     result = []
#     for n in numbers:
#         if n < limit:
#             result.append(n)

#     return result

# print(below_limit([10, 25, 40], 20))
# print(below_limit([20, 21], 20))
# print(below_limit([], 20))

def count_above(numbers, limit):
    count=0
    for n in numbers:
        if n> limit:
            count+=1
    return count        

print(count_above([10, 25, 40], 20))
print(count_above([20, 21], 20))
print(count_above([], 20))