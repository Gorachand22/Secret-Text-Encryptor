import streamlit as st

# Display a small logo in the sidebar
st.sidebar.image("images\OIG.png", caption="Secret Text Encryptor Logo", width=200)

# Display a note in the sidebar
st.sidebar.markdown("""
### Welcome to Caesar Cipher Encryptor

This web application allows you to encrypt or decrypt messages using the Caesar Cipher method. 
Enter the text, choose the shift, and click the corresponding button to see the results.

**Note:**
- Only alphabetic characters will be encrypted or decrypted. 
- Enter a positive shift value to encrypt and a negative value to decrypt.
- Shift is applied in a circular manner, so entering a shift of 26 is the same as entering 0.

Feel free to explore and have fun with your secret messages!
""")

# Display a warning
st.sidebar.warning("Ensure that you enter valid inputs for text and shift for accurate results.")


def caesar_cipher(text, shift, direction):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    if direction == 'decode':
        shift = -shift

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            index = (alphabet.index(char) + shift) % 26
            result += alphabet[index].upper() if is_upper else alphabet[index]
        else:
            result += char

    return result


# Streamlit App
st.title('Caesar Cipher Encryption and Decryption')

# User input
text_input = st.text_input('Enter the text:', key='text_input')
shift_input = st.number_input('Enter the shift number:', min_value=1, step=1, key='shift_input')
direction_input = st.radio('Select operation:', ['Encrypt', 'Decrypt'], key='direction_input')

# Button to perform encryption or decryption
if st.button('Apply'):
    if not text_input or not shift_input:
        st.warning('Please fill in all fields.')
    else:
        result_text = caesar_cipher(text_input, shift_input, 'decode' if direction_input == 'Decrypt' else 'encode')
        st.markdown(f'<p style="font-size: 30px; font-weight: bold; color: pink;">Original Text: {text_input}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="font-size: 30px; font-weight: bold; color: yellow;">Result: {result_text}</p>', unsafe_allow_html=True)

