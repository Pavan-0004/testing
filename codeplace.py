import streamlit as st
from streamlit_option_menu import option_menu
def codeplace():
    st.header('codeplace')
    html_string = '<iframe src=\"https://trinket.io/embed/python\" width=\"150%\" height=\"800\"frameborder=\"10\" marginwidth=\"10\" marginheight=\"10\"></iframe>'
    st.markdown(html_string, unsafe_allow_html=True)
    with st.sidebar :
        uploaded_files = st.file_uploader("Upload multiple files", type=["txt", "py"], accept_multiple_files=True)

# Check if files have been uploaded
        if uploaded_files is not None:
            # Display uploaded files and create download buttons
            for uploaded_file in uploaded_files:
                
                file_contents = uploaded_file.read()
                # Create a download button for each uploaded file
                download_button = st.download_button(f"Download {uploaded_file.name}", file_contents)
        
                # Optionally, save the uploaded file to disk with its original filename
                if download_button:
                    with open(uploaded_file.name, "wb") as f:
                        f.write(file_contents)
                    st.success(f"{uploaded_file.name} downloaded successfully!")

codeplace()