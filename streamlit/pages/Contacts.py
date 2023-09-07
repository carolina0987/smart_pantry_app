import streamlit as st

# Set page title and layout
st.set_page_config(
    page_title="Smart Pantry",
    page_icon=":apple:",
    layout="wide"
)

def main():
    st.title("Contact Information")
    
    st.markdown(
        """
        Feel free to connect with me on LinkedIn or send me an email:
        
        [LinkedIn](https://www.linkedin.com/in/carolinasmsilva)

        [Email](mailto:carolinasilva.vp@hotmail.com)
        """
    )

if __name__ == "__main__":
    main()

