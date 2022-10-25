
import streamlit as st 
import numpy as np

"""if st.button('Click'): 
    rand = np.random.standard_normal()
    st.write(str(rand))"""

col1, col2, col3, col4 = st.columns(4)

col5, col6, col7, col8 = st.columns(4)

if col1.button('1'):
    st.write('1')

if col2.button('2'):
    st.write('2')

if col3.button("3"):
    st.write("3")
    
if col4.button("4"):
    st.write("4")
    
if col1.button("5"):
    st.write("5")