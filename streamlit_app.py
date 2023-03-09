import streamlit 

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Outmeal')
streamlit.text('🥗 Kale, Spinach, & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg') 
streamlit.text('🥑🍞 Avocado Toast') 

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

# Let us put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

# Display the table on the page
streamlit.dataframe(my_fruit_list)
