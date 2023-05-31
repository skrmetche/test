import streamlit as st


st.set_page_config(layout="wide")

def main():
    st.title("File Upload Example")
    file = st.file_uploader("Upload a file")

    if file is not None:
        file_contents = file.read()
        st.write("File contents:")
        st.write(file_contents)
        
        import streamlit as st

def main1():
    st.title("Align Text Example")
    st.write("<p style='text-align: center;'>Center aligned text</p>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
    main1()
    st.write('Hello, *World!* :sunglasses:')
