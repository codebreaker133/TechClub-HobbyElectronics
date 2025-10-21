
#basic math
#range(1,5) is the same as [1,2,3,4,]
#range(50) is the same as 0,1,2
output = 0 #output is the name of the variable and 0 is its value (intiger)
floating = 1.01
string = "this is a string"

#def is how you define a variable name and its peramiters
def calculate(opp,var1,var2):  #deffine function name, and give names for function paramiters
    if opp == "+": #checking if opp is equal to + not assigning + as a value to opp
        output = var1 + var2 
        print(output)  #if you want to just print the value you get you can just print it
        return output #return sets the value of your function equal to its variables        
    if opp == "-":
        var1-var2=output
        return output
    if opp == "*":
        var1*var2=output
        return output
    if opp == "/":
        var1/var2=output
        return output
    else:
        print("opperator not recognised try again")

    


calculate(opp="+",var1=2,var2=3)

opp = "+"
number1 = 2
number2 = 3
output_of_calculator = calculate(opp,number1,number1)
print(output_of_calculator)



















    
