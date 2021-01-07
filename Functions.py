#Functions

z = 100

while z == 100:
    print(z)
    break
    
def example3():
    global z
    z += 1
    print(z)

example3()

def example():
    global a
    x = 5
    y = 9
    print(x+y)
    print(z)

    a = z + 1
    print(a)

    a += 1
    print(a)
    
example()
    
def addition(num1,num2):
    answer = num1+num2
    return answer

x = addition(5,6)
print(x)

def example2():
    x = 3
    y = 7
    print(x+y)

example2()

