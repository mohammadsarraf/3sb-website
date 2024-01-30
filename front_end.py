import streamlit as st
# Import your converted script or functions here
from test import UF_get_cell_value, UFcomms, UFtypes, UFR_get_cell_value, UFRcomms, UFRtypes

# Initialize a session state if not already done
if 'solver_type' not in st.session_state:
    st.session_state['solver_type'] = '3SB Corner solver'

# Title with button to change the state
st.write("# 3 Style Blind Solver", unsafe_allow_html=True)
if st.button('Change Solver'):
    st.session_state['solver_type'] = '3SB Edge solver' if st.session_state['solver_type'] == '3SB Corner solver' else '3SB Corner solver'

app_mode = st.session_state['solver_type']

if app_mode == "3SB Corner solver":
    st.header("Corner Solver")

    # Use your notebook functions as needed
    input_str = st.text_input("Enter the memorization for the corner...")
    input_str = input_str.replace(" ", "")

    result = UFR_get_cell_value(input_str, UFRtypes, UFRcomms)
    st.write(result)

elif app_mode == "3SB Edge solver":
    st.header("Edge Solver")

    # Use your notebook functions as needed
    input_str = st.text_input("Enter the memorization for the edge...")
    input_str = input_str.replace(" ", "")

    result = UF_get_cell_value(input_str, UFtypes, UFcomms)
    st.write(result)
