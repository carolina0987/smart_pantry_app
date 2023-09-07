import streamlit as st
import pandas as pd

# Set page title and layout
st.set_page_config(
    page_title="Smart Pantry",
    page_icon=":apple:",
    layout="wide"
)

#Logo
# logo_path = "logo.png"  # Replace with the actual path to your logo file
# st.image(logo_path, width = 150)

# Define a custom CSS style for consistent styling
st.markdown(
    """
    <style>
    .title {
        font-size: 36px;
        color: #333;
        margin-bottom: 20px;
    }
    .section-header {
        font-size: 24px;
        color: #555;
        margin-top: 20px;
    }
    .step-header {
        font-size: 18px;
        color: #333;
        margin-top: 10px;
    }
    .contact-info {
        font-size: 16px;
        color: #555;
        margin-top: 10px;
    }
    .button-container {
        display: flex;
        justify-content: space-between;
        margin-top: 20px;
    }
    .step-container {
        margin-top: 20px;
    }
    .contact-container {
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title (home page)
st.title("Welcome to Smart Pantry!")

# Description (home page)
st.markdown(
    "Smart Pantry is your solution to managing your kitchen inventory efficiently while combating food waste."
)
st.markdown("With Smart Pantry, you can:")
st.markdown("- Keep track of your pantry products and their expiration dates.")
st.markdown("- Receive timely reminders to use products before they expire.")
st.markdown("- Discover delicious recipes based on the ingredients you have.")

# Add some spacing
st.write("Join us in the fight against food waste!")

# Section Header
st.markdown("<hr class='section-header' />", unsafe_allow_html=True)

# Header
st.title("How it works?")

# Step 1: Inventory Tracking
with st.expander("Step 1: Inventory Tracking", expanded=True):
    st.write("Start by adding your pantry products to the app. You can upload the image of your product, and the app will identify the product's name. Then, you can input its expiration date.")

# Step 2: Expiration Reminders
with st.expander("Step 2: Expiration Reminders", expanded=True):
    st.write("Smart Pantry will keep track of your products' expiration dates and send you timely reminders. Never let food go to waste again!")

# Step 3: Recipe Suggestions
with st.expander("Step 3: Recipe Suggestions", expanded=True):
    st.write("Wondering what to cook with the ingredients you have? Smart Pantry provides you with delicious recipe suggestions based on your inventory.")

# Step 4: Reduce Food Waste
with st.expander("Step 4: Reduce Food Waste", expanded=True):
    st.write("By efficiently using what you have and minimizing food waste, you're not only saving money but also contributing to a more sustainable environment.")

