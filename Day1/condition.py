# from numpy import char
# age = int(input("Whats your age? "))
# if age>=18:
#     print("Your age is greater than or equal to 18")
# else:
#     print("Your age is less 18")

# str = " Hello Sharpsailor"
# for i in range (1,len(str)+1):
#     print(i)



# rows= int(input("How many rows?"))
# cols= int(input("How many Columns?"))
# Symbols =input("Enter a Symbol :")

# for i in range(rows):
#     for j in range(cols):
#         print(Symbols)
#     print()


# def add(*args):
#     sum = 0
#     tuple= list(args)
#     tuple[0] =0
#     for i in tuple:
#         sum+=i
#     return sum

# x= add(1,2,3,4,5,6)
# print(x) 
# KWARGS
def hello (**kwargs):
    print("Hello")
    for key,value in kwargs.items():
        print(value)


hello(fist = "This" ,middle ="SHARPSAILOR ", last ="HOPE  YOU DOING WELL") 