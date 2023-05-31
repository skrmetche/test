import streamlit as st

st.set_page_config(layout="wide")

def main():
    st.title("File Upload Example")
    file = st.file_uploader("Upload a file")

    if file is not None:
        file_contents = file.read()
        st.write("File contents:")
        st.write(file_contents)
        

if __name__ == "__main__":    
    st.title("Test Program")
    st.write("<p style='text-align: center;'>Hello, *World!*:sunglasses:</p>", unsafe_allow_html=True)
    main()
