import streamlit as st
import langchain_helper

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Italian", "Chinese", "Mexican", "Indian", "Arabic", "Pakistani"))

if cuisine:
   response = langchain_helper.generate_restaurant_name_and_items(cuisine)

   st.header(response['restaurant_name'].strip())
   menu_items = response['menu_items'].strip().split(',')
   st.subheader("Menu Items")

   for item in menu_items:
         st.write(f"- {item.strip()}")