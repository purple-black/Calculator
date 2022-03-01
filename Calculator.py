import math
'''
Simple Calculator
'''
def Add():
    
     a = int(input('Enter the first number: '))
     b = int(input('Enter the second number: '))
     ans = a + b
     print(a, " + ", b," = ",ans)
    
def Sub():
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: ' ))
    ans =  a - b
    print(a, " - ", b," = ",ans)
    
def  Prod():
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: ' ))
    ans =  a * b
    print(a, " * ", b," = ",ans)
    
def Div():
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: ' ))
    ans =  a / b
    print(a, " / ", b," = ",ans)
    
def Rem():
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: ' ))
    ans =  math.remainder(a,b)
    print('Remainder on ',a," / ",b," is ",ans)
    
def Absolute():
    a = float(input('Enter a number: '))
    ans = abs(a)
    print('Absolute value of ',a,' is ',ans)
    
def RoundVal():
    a = float(input('Enter a number: '))
    ans = round(a)
    print('Rounded value of ',a,' is ',ans)
    
def CeilVal():
    a = float(input('Enter a number: '))
    ans = math.ceil(a)
    print('Ceil value of ',a,' is ',ans)
    
def FloorVal():
    a = float(input('Enter a number: '))
    ans = math.floor(a)
    print('Floor value of ',a,' is ',ans)
    
def Expo():
    a = int(input('Enter the base number: '))
    b = int(input('Enter the exponent number: ' ))
    ans =  pow(a,b)
    print(a," raised to the power ",b," = ",ans)
    
def Sqroot():
    a = int(input('Enter a number: '))
    ans = math.sqrt(a)
    print('Square root of ',a,' is ',ans)
    
def Fact():
    a = int(input('Enter a number: '))
    ans = math.factorial(a)
    print('Factorial of ',a,' is ',ans)
    
def Cube():
    a = int(input('Enter a number: '))
    ans = num ** 1/3
    print('Cube root of ',a,' is ',ans)
    
def Sine():
    a = float(input('Enter a number: '))
    ans = math.sin(a)
    print('Sine value of ',a,' is ',ans)
    
def Cosine():
    a = float(input('Enter a number: '))
    ans = math.cos(a)
    print('Cosine value of ',a,' is ',ans)
    
def Tangent():
    a = float(input('Enter a number: '))
    ans = math.tan(a)
    print('Tangent value of ',a,' is ',ans)
    
def deg():
    a = float(input('Enter a number: '))
    ans = math.degrees(a)
    print('Degree value of ',a,' is ',ans)
    
def Rad():
    a = float(input('Enter a number: '))
    ans = math.radians(a)
    print('Radian value of ',a,' is ',ans)
    
print('Welcome to the simple calculator!!')
flag = -1
while(flag == -1):
 try:
    num = int(input('Enter the S.No of the operation you want to perform\n'
          '1. Addition\n'
          '2. Subtraction\n'
          '3. Multiplication\n'
          '4. Division\n'
          '5. Remainder\n'
          '6. Absolute Value\n'
          '7. Round\n'
          '8. Ceil\n'
          '9. Floor\n'
          '10. Exponentation\n'
          '11. Square root\n'
          '12. Factorial\n'
          '13. Cube root\n'
          '14. Sin\n'
          '15. Cos\n'
          '16. Tan\n'
          '17. To Degrees\n'
          '18. To Radians\n'
    ))
    if(num == 1):
        Add()
        print('do you want to make another calculation? enter Y for yes')
        choice = input()
        if(choice=="Y"):
            flag = -1
        else:
            flag = 0
    elif(num == 2): 
        Sub()
        print('do you want to make another calculation? enter Y for yes')
        choice = input()
        if(choice=="Y"):
            flag = -1
        else:
            flag = 0
    elif(num == 3):
        Prod()
        print('do you want to make another calculation? enter Y for yes')
        choice = input()
        if(choice=="Y"):
            flag = -1
        else:
            flag = 0
    elif(num == 4):
        Div()
        print('do you want to make another calculation? enter Y for yes')
        choice = input()
        if(choice=="Y"):
            flag = -1
        else:
            flag = 0
    elif(num == 5):
        Rem()
        print('do you want to make another calculation? enter Y for yes')
        choice = input()
        if(choice=="Y"):
            flag = -1
        else:
            flag = 0
    elif(num == 6):
        Absolute()
        print('do you want to make another calculation? enter Y for yes')
        choice = input()
        if(choice=="Y"):
            flag = -1
        else:
            flag = 0
    elif(num == 7):
        RoundVal()
        print('do you want to make another calculation? enter Y for yes')
        choice = input()
        if(choice=="Y"):
            flag = -1
        else:
            flag = 0
    elif(num == 8):
        CeilVal()
        print('do you want to make another calculation? enter Y for yes')
        choice = input()
        if(choice=="Y"):
            flag = -1
        else:
            flag = 0
    elif(num == 9):
        FloorVal()
        print('do you want to make another calculation? enter Y for yes')
        choice = input()
        if(choice=="Y"):
            flag = -1
        else:
            flag = 0
    elif(num == 10):
        Expo()
        print('do you want to make another calculation? enter Y for yes')
        choice = input()
        if(choice=="Y"):
            flag = -1
        else:
            flag = 0
    elif(num == 11):
        Sqroot()
        print('do you want to make another calculation? enter Y for yes')
        choice = input()
        if(choice=="Y"):
            flag = -1
        else:
            flag = 0
    elif(num == 12):
        Fact()
        print('do you want to make another calculation? enter Y for yes')
        choice = input()
        if(choice=="Y"):
            flag = -1
        else:
            flag = 0
    elif(num == 13):
        Cube()
        print('do you want to make another calculation? enter Y for yes')
        choice = input()
        if(choice=="Y"):
            flag = -1
        else:
            flag = 0
    elif(num == 14):
        Sine()
        print('do you want to make another calculation? enter Y for yes')
        choice = input()
        if(choice=="Y"):
            flag = -1
        else:
            flag = 0
    elif(num == 15):
        Cosine()
        print('do you want to make another calculation? enter Y for yes')
        choice = input()
        if(choice=="Y"):
            flag = -1
        else:
            flag = 0
    elif(num == 16):
        Tangent()
        print('do you want to make another calculation? enter Y for yes')
        choice = input()
        if(choice=="Y"):
            flag = -1
        else:
            flag = 0
    elif(num == 17):
        deg()
        print('do you want to make another calculation? enter Y for yes')
        choice = input()
        if(choice=="Y"):
            flag = -1
        else:
            flag = 0
    elif(num == 18):
        Rad()
        print('do you want to make another calculation? enter Y for yes')
        choice = input()
        if(choice=="Y"):
            flag = -1
        else:
            flag = 0
    else:
      print('Invalid input!')
      continue
    
 except:
    flag = -1
    print('Invalid input! please enter a number.')
    continue

print('Thank you!!')