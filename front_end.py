import streamlit as st
# Import your converted script or functions here
from test import UF_get_cell_value, UFcomms, UFtypes,UFR_get_cell_value, UFRcomms, UFRtypes

st.title("3SB Edge solver")

# Use your notebook functions as needed
# input_str = 'mx ow ea ju rf np'.replace(" ", "")
input_str = st.text_input("Enter the memorization...")
input_str = input_str.replace(" ", "")

result = UF_get_cell_value(input_str, UFtypes, UFcomms)
print(result)
st.write(result)

st.title("3SB Corner solver")

# Use your notebook functions as needed
# input_str = 'mx ow ea ju rf np'.replace(" ", "")
input_str = st.text_input("Enter the memorization for the corner...")
input_str = input_str.replace(" ", "")

result = UFR_get_cell_value(input_str, UFRtypes, UFRcomms)
print(result)
st.write(result)
