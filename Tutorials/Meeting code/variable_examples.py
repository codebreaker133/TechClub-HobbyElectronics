

print("hello world")

var_1 = "this is a test" # this is a string value

var_2 = 5 # this is a intiger value

var_3 = 3.14 # this is a float value

output = None # this is a type not a value

output = var_2 * var_3

def funciton_1(paramiter_1):
    global var_1 # defined elsewhere
    print(var_1)
    x=1
    for i in range(10):
        print(i)
    print("\n")
    while x <= 10:
        print(x)
        x+=1 # same as x = x - 1


funciton_1(var_1)
print(output)

