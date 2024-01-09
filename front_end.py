import streamlit as st
# Import your converted script or functions here
from test import get_cell_value, comms, types

st.title("3SB solver")

# Use your notebook functions as needed
# input_str = 'mx ow ea ju rf np'.replace(" ", "")
input_str = st.text_input("Enter the memorization...")
input_str = input_str.replace(" ", "")

result = get_cell_value(input_str, types, comms)
print(result)
st.write(result)
