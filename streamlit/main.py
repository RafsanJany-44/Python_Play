#importing streamlit package
import streamlit as st
import math


#Normal Calculation
def Add(n1, n2):
    return  n1+n2

def Sub(n1, n2):
    return  n1-n2

def Mul(n1, n2):
    return  n1*n2

def Div(n1, n2):
    try:
        return  n1/n2
    except Exception as e:
        return "Error: " +str(e)

def Power(n1, n2):
    return  n1**n2


def Root(n1, n2):
    try:
        return  n1**(1/n2)
    except Exception as e:
        return "Error: " +str(e)

#trigonomytry
def Sin(n):
    try:
        return math.sin((n*math.pi)/180)
    except Exception as e:
        return "Error: " +str(e)

def Cos(n):
    try:
        return math.cos((n*math.pi)/180)
    except Exception as e:
        return "Error: " +str(e)

def Tan(n):
    try:
        return math.tan((n*math.pi)/180)
    except Exception as e:
        return "Error: " +str(e)

def Sinh(n):
    try:
        return math.sinh(n)
    except Exception as e:
        return "Error: " +str(e)
    

def Cosh(n):
    try:
        return math.cosh(n)
    except Exception as e:
        return "Error: " +str(e)

def Tanh(n):
    try:
        return math.tanh((n*math.pi)/180)
    except Exception as e:
        return "Error: " +str(e)


#prime number
def isPrime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return str(num)+" is not a prime number"
                break
        else:
            return str(num)+" is a prime number"
    else:
        return str(num)+" is not a prime number"



def fib_iter(n):
    a=1
    b=1
    if n==1:
        print('0')
    elif n==2:
        print('0','1')
    else:
        print("Iterative Approach: ", end=' ')
        print('0',a,b,end=' ')
        for i in range(n-3):
            total = a + b
            b=a
            a= total
            print(total,end=' ')
        print()
        return b



# main function
def main():
    st.title("General Calculator")

    #taking input from user
    number_1 = st.number_input("Enter First Number")
    number_2 = st.number_input("Enter Second Number")

    #adding drop down box for selecting operation
    operation = st.selectbox("Select Operation", ["Add", "Substract", "Multiplication",
                                                  "Divided", "Power", "Root",
                                                  "Sin", "Cos", "Tan", "Sinh",
                                                  "Cosh", "Tanh", "isPrime"])


    if operation == "Add":
        st.write(Add(number_1, number_2))
    elif operation == "Substract":
        st.write(Sub(number_1, number_2))
    elif operation == "Multiplication":
        st.write(Mul(number_1, number_2))
    elif operation == "Divided":
        st.write(Div(number_1, number_2))
    elif operation == "Power":
        st.write(Power(number_1, number_2))
    elif operation == "Root":
        st.write(Root(number_1, number_2))
    elif operation == "Sin":
        st.write(Sin(number_1))
    elif operation == "Cos":
        st.write(Cos(number_1))
    elif operation == "Tan":
        st.write(Tan(number_1))
    elif operation == "Sinh":
        st.write(Sinh(number_1))
    elif operation == "Cosh":
        st.write(Cosh(number_1))
    elif operation == "Tanh":
        st.write(Tanh(number_1))
    elif operation == "isPrime":
        st.write(isPrime(number_1))




if __name__ == "__main__":
    main()