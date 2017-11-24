# Program to produce inputs from KeyBoard
#sum fo the no & print to Console.

num1= input("enter any interger1 : ")
num2= input("enter any interger2 : ")
#convert string to integer temp conv
add = int(num1) + int(num2)

#No. of ways of print cmmnd in Python.

print("add 2 nos =",add)

print("add 2 nos ="+str,(add))
print("add 2 nos =",+repr(add)) #string to integer
print("sum of %s and %s is %d" %(num1,num2,add))
print("sum of {0} and {1} is {2}".format(num1,num2,add))

num2= input("enter any interger2 : ")
