########################################## First Stage Start #############################################

#First Stage: Get two binary inputs from the user for logic gate operations

#Prompt the user for input
print("Insert binary values for logic gates (1 or 0)!")

#Use an infinite loop until valid inputs are provided
while True:
    #Get user inputs as integer
    first_input = int(input("First binary value: "))
    second_input = int(input("Second binary value: "))
    
    #Break the loop if both inputs are either 0 or 1
    if ((first_input == 1 or first_input == 0) and (second_input == 1 or second_input == 0)):
        break
    
    #Display a warning message for invalid inputs
    else:
        print("Invalid input. You must enter 1 or 0!")

#Logic gates information
print("1-AND Gate 2-OR Gate 3-XOR Gate 4-NAND Gate 5-NOT Gate")

#Get user's choice of logic gate
gate_information = int(input("What gate you want to work on (1-5): "))

#We use 4 same print section. So we use simple function
def result(output_result):
    print(f"Result on selected gate: {output_result}")


#We should have third variable for result. That we call 'output_result'

#We create match-case statement using gate_information


match gate_information:
    case 1:
        output_result = first_input and second_input
        result(output_result)
    case 2:
        output_result = first_input or second_input
        result(output_result)
    case 3:
        output_result = int(first_input != second_input) #The boolean result is cast to an integer value.
        result(output_result)
    case 4:
        output_result = int(not (first_input and second_input)) #The boolean result is cast to an integer value.
        result(output_result)
    case 5: 
        output_result = int(not(first_input)) #The boolean result is cast to an integer value.
        print(f"Your first input {first_input} will be {output_result} on NOT gate.") 
        
        output_result2 = int(not(second_input)) #The boolean result is cast to an integer value.
        print(f"Your second input  {second_input} will be {output_result2} on NOT gate")
    case _:
        print("Invalid gate selection!")

########################################## First Stage Finish #############################################

########################################## Second Stage Start #############################################

print(f"{'Value A':^10} | {'Value B':^10} | {'Value C':^10} | {'A and (B or C)':^10}") 
print("-" * 55) 

#Creating nested for loop for A, B and C values
for A in range(0, 2):
    for B in range(0, 2):
        for C in range(0, 2):
            #Logic gate example
            logic_result = int(A and (B or C)) #The boolean result is cast to an integer value.
            
            print(f"{A:^10} | {B:^10} | {C:^10} | {logic_result:^15}") 

########################################## Second Stage Finish #############################################
