
import streamlit as st 

l=[]

def button_click(element):
    global final_string
    final_string = final_string + element
    l.append(element)
    print(l)
    st.write(final_string)

def button_clear():
    global final_string 
    final_string = "" 
    st.write("")


def button_equal():
    global final_string
    try:
        result = str(eval(final_string))
    except Exception as e:
        result = "Error: "+str(e)
    st.write(result)
    
final_string = ""



col1, col2, col3, col4 = st.columns(4)

col5, col6, col7, col8 = st.columns(4)

if col1.button('1'):
    button_click('1')

if col2.button('2'):
    button_click('2')

if col3.button("3"):
    button_click("3")
    
if col4.button("4"):
    button_click("4")
    
if col4.button("5"):
    button_click("5")