import streamlit as st
import spellchecker

# Set up the Streamlit app
st.title("Spell Checker App")

# Get user input
user_input = st.text_input("Enter a word:")

# Check if the user has entered a word
if user_input:
    # Call the spell checker function
    suggested_corrections = spellchecker.spell_check_edit_2(user_input)
    
    # Display the suggested corrections
    if suggested_corrections:
        st.write("Did you mean:", text_color='green')
        for correction in suggested_corrections:
            st.write(correction)
    else:
        st.write("No suggestions found.")
