#include<iostream>
#include<math.h>
using namespace std;

void FindSum(){
    float a, b, answer;
     cout << "enter the numbers a and b: ";
     cin >> a >> b;
     answer = a+b;
     cout << "The sum of " <<  a << " and " << b << " is " << answer << endl;
}

void FindDifference(){
    float a, b, answer;
    cout << "enter the numbers a and b: ";
     cin >> a >> b;
     answer = a-b;
     cout << "The difference of " <<  a << " and " << b << " is " << answer << endl;
}

void FindProduct(){
    float a, b, answer;
    cout << "enter the numbers a and b: ";
     cin >> a >> b;
     answer = a*b;
     cout << "The product of " <<  a << " and " << b << " is " << answer << endl;
}

void FindQuotient(){
    float a, b, answer;
    cout << "enter the numbers a and b: ";
     cin >> a >> b;
     answer = a/b;
     cout << "The answer on division of " <<  a << " with " << b << " is " << answer << endl;
}

void FindRemainder(){
    int a, b, answer;
    cout << "enter the numbers a and b: ";
     cin >> a >> b;
     answer = a%b;
     cout << "The remainder on division of " << a << " with " << b << " is " << answer << endl;

}

void FindAbsValue(){
    float a, answer;
    cout << "enter value for a to find its absolute value: ";
    cin >> a;
    answer = abs(a);
    cout << "The absolute value of " <<  a << " is " << answer << endl;
}

void FindExponent(){
    int a, b, answer;
    cout << "enter value for a and b to calculate a to the power b: ";
    cin >> a >> b;
    answer  =  pow(a,b);
    cout << a << " to the power " << b << " is " << answer << endl;

}

void FindFloor(){
    float a;
    int answer;
    cout << " enter value for a to find the largest integer less than a: ";
    cin >> a;
    answer = floor(a);
    cout << "floor of " << a << " is " << answer << endl;

}

void FindCeil(){
    float a;
    int answer;
    cout << " enter value for a to find the smallest integer greater than a: ";
    cin >> a;
    answer = ceil(a);
    cout << "ceil of " << a << " is " << answer << endl;
}

void FindRound(){
    float a;
    int answer;
    cout << "enter value for a to find its nearest integer: ";
    cin >> a;
    answer = round(a);
    cout << "Rounded value of " << a << " is " << answer << endl;
}

void FindSine(){
    float a, answer;
    cout << "enter the value of a to find its sine value: ";
    cin >>a;
    answer = sin(a);
    cout << "sine value of " << a << " is " << answer << endl;
}

void FindCosine(){
    float a, answer;
    cout << "enter the value of a to find its cosine value: ";
    cin >>a;
    answer = cos(a);
    cout << "cosine value of " << a << " is " << answer << endl;
}

void FindTangent(){
    float a, answer;
    cout << "enter the value of a to find its tangent value: ";
    cin >>a;
    answer = tan(a);
    cout << "tangent value of " << a << " is " << answer << endl;
}


int main(){
    int choice;
    cout << "what operation do you want to perform? Choose by entering the corresponding integer" << endl;
    cout << "1. Addition\n"
    "2. Subtraction\n"
    "3. Multiplication\n"
    "4. division\n"
    "5. remainder\n"
    "6. Absolutevalue\n"
    "7. Exponent\n"
    "8. Floor\n"
    "9. ceil\n"
    "10. round\n"
    "11. sin\n"
    "12. cos\n"
    "13. tan\n" << endl;

    //input user's choice
    cout << "enter your choice: ";
    cin >> choice;

    switch(choice){
        case 1:
           FindSum();
           break;

        case 2:
           FindDifference();
           break;
        case 3:
           FindProduct();
           break;
        case 4:
           FindQuotient();
           break;
        case 5:
           FindRemainder();
           break;
        case 6:
           FindAbsValue();
           break;
        case 7:
           FindExponent();
           break;
        case 8:
           FindFloor();
           break;
        case 9:
           FindCeil();
           break;
        case 10:
           FindRound();
           break;
        case 11:
           FindSine();
           break;
        case 12:
           FindCosine();
           break;
        case 13:
           FindTangent();
           break;
        default: 
           cout << "OOPS! INVALID CHOICE!" << endl;

        

    }


    return 0;
}