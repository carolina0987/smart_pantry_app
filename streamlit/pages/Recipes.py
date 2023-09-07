import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
from datetime import datetime, timedelta
import re

# Set page title and layout
st.set_page_config(
    page_title="Smart Pantry",
    page_icon=":apple:",
    layout="wide"
)

# Read the CSV file into a DataFrame
merged_df = pd.read_csv("merged_df.csv")

# Group recipes by product
grouped = merged_df.groupby('name_id')

#For the e-mail:
# Read the CSV file into a DataFrame
pantry_df = pd.read_csv("pantry_data.csv")

# Define your SMTP server settings
smtp_server = "smtp.office365.com"
smtp_port = 587  
smtp_username = "your_email"
smtp_password = "your_password"

# Streamlit app
st.title("Check Expiring Products")

# Create a selectbox to choose a product
selected_product = st.selectbox("Select a product:", pantry_df['Product'].unique())

# Create an input field for the user's email
user_email = st.text_input("Enter your email:")

# Display the selected product name in the tab
st.write(f"Selected Product: {selected_product}")

# Function to send email notification
def send_email(to_email, subject, message):
    from_email = "your_email" 

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(from_email, [to_email], msg.as_string())
        st.success("Email sent successfully!")
    except Exception as e:
        st.error(f"Please enter your email")

# Check for expiring products
if selected_product:
    product_info = pantry_df[pantry_df['Product'] == selected_product]
    expiration_dates = pd.to_datetime(product_info['Expiration Date'])
    today = datetime.now()
    expiration_threshold = today + timedelta(days=7)  # Change this to the desired threshold

    expiring_products = product_info[expiration_dates <= expiration_threshold]

    if not expiring_products.empty:
        st.write(expiring_products)
        
# Here, you can add the logic to compose and send an email notification
# For each product in 'expiring_products', send an email with relevant details
for index, row in expiring_products.iterrows():
    product_name = row['Product']
    expiration_date = row['Expiration Date']

    # Compose your email message here
    subject = f"Expiring Product Alert: {product_name}"

    # Create the email message body
    message = f"Dear user, your product {product_name} is expiring on {expiration_date}.\n\n"

    # Add recipe recommendations from your recipe dataframe
    message += f"Here are some recipe recommendations for you to use {product_name}:\n\n"
    
    # Filter recipes based on ingredients (you may need to adapt this part to your specific logic)
    matching_recipes = merged_df[merged_df['products'].str.contains(product_name, case=False)]
    
    if not matching_recipes.empty:
        for index, recipe_row in matching_recipes.iterrows():
            recipe_title = recipe_row['recipe_title']
            recipe_url = recipe_row['recipe_url']
            instructions = recipe_row['instructions']
            ingredients_list = re.sub("[\[\]\']","", recipe_row['ingredients_list'])

            message += f"Recipe Title: {recipe_title}\n"
            message += f"Recipe URL: {recipe_url}\n"
            message += f"Instructions: {instructions}\n"
            message += f"Ingredients List: {ingredients_list}\n\n"
    else:
        message += "Sorry, we couldn't find any recipes using this ingredient."

    # Add "Best regards"
    message += "Best regards,\n\nYour Smart Pantry."

    # Send the email to the user's input email address
    send_email(user_email, subject, message)
else:
    st.warning("Please select a product to check for expiring products.")

st.write("---")

# Streamlit app 
st.title("Recipes")

# Create a selectbox to choose a product
selected_product = st.selectbox("Select a product:", [None] + list(grouped.groups.keys()))

# Display the selected product name in the tab
st.write(f"Selected Product: {selected_product}")

# Display recipes for the selected product when the product name is selected
for product_name, group in grouped:
    if product_name == selected_product:
        for index, row in group.iterrows():
            recipe_title = row['recipe_title']
            ingredients_list = re.sub("[\[\]\'\"]","", row['ingredients_list'])
            ingredients = ingredients_list.split(', ')
            ingredients_list = "\n".join([f"\n - {ingredient.strip()}" for ingredient in ingredients])
            instructions = row['instructions']
            
            # Display recipe details
            st.subheader(f"{recipe_title}")
            
            # Display ingredients without a bulleted list
            st.write(f"**Ingredients:** {ingredients_list}")
            
            st.write(f"**Instructions:**\n{instructions}")