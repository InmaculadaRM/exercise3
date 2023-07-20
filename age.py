#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def main():
    st.title('Age Calculator')

    # User input for date of birth
    birth_date = st.date_input('Enter your date of birth', date(2000, 1, 1))

    if st.button('Calculate Age'):
        if birth_date >= date.today():
            st.error("Invalid birth date. Please select a date before today.")
        else:
            age = calculate_age(birth_date)
            st.success(f"Your age is: {age} years")

if __name__ == "__main__":
    main()

