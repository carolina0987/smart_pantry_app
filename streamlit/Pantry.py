import streamlit as st
import pandas as pd
from datetime import datetime
from PIL import Image
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\carol\Desktop\final_project\tesseract-ocr\tesseract.exe"
import cv2
import numpy as np


# OCR Logic for each product image
def extract_beans_product(image_path):
    myconfig = r"--psm 11 --oem 3"

    # Extract text from the image
    beans_image = Image.open("beans.png")
    beans_text = pytesseract.image_to_string(beans_image, lang="por", config=myconfig)

    # # Extract the words you want
    beans_data = beans_text.split()
    words_to_extract = beans_data[8:10]
    beans_product = ' '.join(words_to_extract).lower()
    
    return beans_product

def extract_bread_product(image_path):
    myconfig = r"--psm 11 --oem 3"

    # Extract text from the image
    bread_image = Image.open("bread.png")
    bread_text = pytesseract.image_to_string(bread_image, lang="por", config=myconfig)

    # Extract the words you want
    bread_data = bread_text.split()
    words_to_extract = bread_data[9:12]
    bread_product = ' '.join(words_to_extract).lower()
    
    return bread_product

def extract_egg_product(image_path):
    myconfig = r"--psm 11 --oem 3"
    
    # Extract text from the image
    eggs_image = Image.open("eggs.png")
    eggs_text = pytesseract.image_to_string(eggs_image, lang="por", config=myconfig)
    
    # Extract the words you want
    eggs_data = eggs_text.split()
    words_to_extract = eggs_data[19:22]
    egg_product = ' '.join(words_to_extract).replace("-", " ").lower()
    
    return egg_product

def extract_flour_product(image_path):
    myconfig = r"--psm 6 --oem 3"
    
    flour_image = Image.open("flour.png")
    flour_text = pytesseract.image_to_string(flour_image, lang="por", config=myconfig)
    
    flour_data = flour_text.split()
    flour_product = flour_data[3].lower()
    
    return flour_product

def extract_yogurt_product(image_path):
    myconfig = r"--psm 11 --oem 3"
    
    yogurt_image = Image.open("iogurt.png")
    yogurt_text = pytesseract.image_to_string(yogurt_image, lang="por", config=myconfig)
    
    yogurt_data = yogurt_text.split()
    yogurt_words = yogurt_data[2:4]
    yogurt_product = ' '.join(yogurt_words).replace("-", " ").lower()
    
    return yogurt_product

def extract_meat_product(image_path):
    myconfig = r"--psm 6 --oem 3"
    
    meat_image = Image.open("meat.png")
    meat_text = pytesseract.image_to_string(meat_image, lang="por", config=myconfig)
    
    meat_data = meat_text.split()
    meat_product = meat_data[7].lower()
    
    return meat_product

def extract_oliveoil_product(image_path):
    myconfig = r"--psm 11 --oem 3"
    
    oliveoil_image = Image.open("oliveoil.png")
    oliveoil_text = pytesseract.image_to_string(oliveoil_image, lang="por", config=myconfig)
    
    oliveoil_data = oliveoil_text.split()
    oliveoil_product = oliveoil_data[7].lower()
    
    return oliveoil_product

def extract_pasta_product(image_path):
    myconfig = r"--psm 6 --oem 3"
    
    pasta_image = Image.open("pasta.png")
    pasta_text = pytesseract.image_to_string(pasta_image, lang="por", config=myconfig)
    
    pasta_data = pasta_text.split()
    pasta_product = pasta_data[4].lower()
    
    return pasta_product

def extract_rice_product(image_path):
    myconfig = r"--psm 6 --oem 3"
    
    rice_image = Image.open("rice.png")
    rice_text = pytesseract.image_to_string(rice_image, lang="por", config=myconfig)
    
    rice_data = rice_text.split()
    rice_product = rice_data[1].lower()
    
    return rice_product

def extract_salmon_product(image_path):
    myconfig = r"--psm 11 --oem 3"
    
    salmon_image = Image.open("salmon.png")
    salmon_text = pytesseract.image_to_string(salmon_image, lang="por", config=myconfig)
    
    salmon_data = salmon_text.split()
    salmon_product = salmon_data[7].lower()
    
    return salmon_product

def extract_spinach_product(image_path):
    myconfig = r"--psm 11 --oem 3"
    
    spinach_image = Image.open("spinach.png")
    spinach_text = pytesseract.image_to_string(spinach_image, lang="por", config=myconfig)
    
    spinach_data = spinach_text.split()
    spinach_product = spinach_data[2].lower()
    
    return spinach_product

def extract_veggies_product(image_path):
    myconfig = r"--psm 11 --oem 3"
    
    veggies_image = Image.open("veggies.png")
    veggies_text = pytesseract.image_to_string(veggies_image, lang="por", config=myconfig)
    
    veggies_data = veggies_text.split()
    veggies_product = veggies_data[4].lower()
    
    return veggies_product

def extract_apple_product(image_path):
    myconfig = r"--psm 11 --oem 3"
    
    apple_image = Image.open("apple.png")
    apple_text = pytesseract.image_to_string(apple_image, lang="por", config=myconfig)
    
    apple_data = apple_text.split()
    apple_product = apple_data[3].lower()
    
    return apple_product

def extract_milk_product(image_path):
    myconfig = r"--psm 11 --oem 3"
    
    milk_image = Image.open("milk.png")
    milk_text = pytesseract.image_to_string(milk_image, lang="por", config=myconfig)
    
    milk_data = milk_text.split()
    milk_product = milk_data[0].lower()
    
    return milk_product

def extract_potatoes_product(image_path):
    myconfig = r"--psm 6 --oem 3"
    
    potatoes_image = Image.open("potatoes.png")
    potatoes_text = pytesseract.image_to_string(potatoes_image, lang="por", config=myconfig)
    
    potatoes_data = potatoes_text.split()
    potatoes_product = potatoes_data[1].lower()
    
    return potatoes_product

def extract_cheese_product(image_path):
    myconfig = r"--psm 11 --oem 3"
    
    cheese_image = Image.open("cheese.png")
    cheese_text = pytesseract.image_to_string(cheese_image, lang="por", config=myconfig)
    
    cheese_data = cheese_text.split()
    cheese_word = cheese_data[1:4]
    cheese_product = '-'.join(cheese_word)
    cheese_product = cheese_product.replace("-", " ").lower()
    
    return cheese_product

def extract_salad_product(image_path):
    myconfig = r"--psm 11 --oem 3"
    
    salad_image = Image.open("salad.png")
    salad_text = pytesseract.image_to_string(salad_image, lang="por", config=myconfig)
    
    salad_data = salad_text.split()
    salad_word = salad_data[1:5]
    salad_product = '-'.join(salad_word)
    salad_product = salad_product.replace("-", " ").lower()
    
    return salad_product

def extract_avocado_product(image_path):
    myconfig = r"--psm 11 --oem 3"
    
    avocado_image = Image.open("avocado.png")
    avocado_text = pytesseract.image_to_string(avocado_image, lang="por", config=myconfig)
    
    avocado_data = avocado_text.split()
    avocado_product = avocado_data[14].lower()
    
    return avocado_product

def extract_mushrooms_product(image_path):
    myconfig = r"--psm 11 --oem 3"
    
    mushrooms_image = Image.open("mushrooms.png")
    mushrooms_text = pytesseract.image_to_string(mushrooms_image, lang="por", config=myconfig)
    
    mushrooms_data = mushrooms_text.split()
    mushrooms_word = mushrooms_data[7:9]
    mushrooms_product = '-'.join(mushrooms_word)
    mushrooms_product = mushrooms_product.replace("-", " ").lower()
    
    return mushrooms_product

def extract_ham_product(image_path):
    myconfig = r"--psm 11 --oem 3"
    
    ham_image = Image.open("ham.png")
    ham_text = pytesseract.image_to_string(ham_image, lang="por", config=myconfig)
    
    ham_data = ham_text.split()
    ham_product = ham_data[2].lower()
    
    return ham_product

# Initialize an empty DataFrame for the user's pantry
pantry_data = {
    'Product': [],
    'Expiration Date': []
}
df = pd.DataFrame(pantry_data)  # Initialize the 'df' DataFrame

# Set Streamlit page title and description
st.set_page_config(
    page_title="Smart Pantry",
    page_icon="🍏",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Smart Pantry")
st.write("Welcome to Smart Pantry! You can view and manage your pantry products here.")

st.header("Add a new Product")

uploaded_images = st.file_uploader("Upload Image(s)", accept_multiple_files=True)

if uploaded_images:
    # Input expiration dates for all products together
    st.subheader("Add Expiration Dates for All Products")
    expiration_dates = []
    product_names = []  # To store product names

    for i, uploaded_image in enumerate(uploaded_images):
        product_name = None
        if uploaded_image is not None:
            image_filename = str(uploaded_image.name.lower()) 

            if 'beans' in image_filename:
                product_name = extract_beans_product(uploaded_image)
            elif 'bread' in image_filename:
                product_name = extract_bread_product(uploaded_image)
            elif 'apple' in image_filename:
                product_name = extract_apple_product(uploaded_image)
            elif 'avocado' in image_filename:
                product_name = extract_avocado_product(uploaded_image)
            elif 'cheese' in image_filename:
                product_name = extract_cheese_product(uploaded_image)
            elif 'eggs' in image_filename:
                product_name = extract_egg_product(uploaded_image)
            elif 'flour' in image_filename:
                product_name = extract_flour_product(uploaded_image)
            elif 'ham' in image_filename:
                product_name = extract_ham_product(uploaded_image)
            elif 'iogurt' in image_filename:
                product_name = extract_yogurt_product(uploaded_image)
            elif 'meat' in image_filename:
                product_name = extract_meat_product(uploaded_image)
            elif 'milk' in image_filename:
                product_name = extract_milk_product(uploaded_image)
            elif 'mushrooms' in image_filename:
                product_name = extract_mushrooms_product(uploaded_image)
            elif 'oliveoil' in image_filename:
                product_name = extract_oliveoil_product(uploaded_image)
            elif 'pasta' in image_filename:
                product_name = extract_pasta_product(uploaded_image)
            elif 'potatoes' in image_filename:
                product_name = extract_potatoes_product(uploaded_image)
            elif 'rice' in image_filename:
                product_name = extract_rice_product(uploaded_image)
            elif 'salad' in image_filename:
                product_name = extract_salad_product(uploaded_image)
            elif 'salmon' in image_filename:
                product_name = extract_salmon_product(uploaded_image)
            elif 'spinach' in image_filename:
                product_name = extract_spinach_product(uploaded_image)
            elif 'veggies' in image_filename:
                product_name = extract_veggies_product(uploaded_image)
            


            expiration_date = st.date_input(f"Expiration Date for {product_name}", key=f"exp_date_{i}")
            expiration_dates.append(expiration_date)
            product_names.append(product_name)  # Store product name


            if product_name is not None:
                new_item = {
                    'Product': product_name,
                    'Expiration Date': expiration_date.strftime('%Y-%m-%d') if expiration_date else 'N/A'
                }

                df = df.append(new_item, ignore_index=True)

    # Display success message after processing all uploaded items
    if st.button("Add Products"):
        st.success("Product added successfully!")

    df.to_csv('pantry_data.csv', index=False)  # This line saves the DataFrame to a CSV file

col1, col2 = st.columns(2)
with col1:
    # Display the user's pantry items
    st.header("Your Pantry Products")
    if not df.empty:
        # Convert 'Expiration Date' column to Timestamp format
        df['Expiration Date'] = pd.to_datetime(df['Expiration Date'])
        st.dataframe(df, height=400)
    else:
        st.write("Your pantry is empty. Add products using the section above!")

with col2:
    # Expiring Soon Section
    st.header("Expiring Soon")
    today = pd.Timestamp.now()
    threshold = today + pd.DateOffset(days=7)  # Items expiring within a week

    expiring_soon = df[pd.to_datetime(df['Expiration Date']) <= threshold]
    if not expiring_soon.empty:
        st.dataframe(expiring_soon, height=200)
    else:
        st.write("You have no products expiring within the next week.")