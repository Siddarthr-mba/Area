import streamlit as st
import math

# Title of the app
st.title("Shape Area Calculator")

# Dropdown to select the shape
shape = st.selectbox("Select the shape:", ["Circle", "Rectangle"])

# Input fields based on the selected shape
if shape == "Circle":
    radius = st.number_input("Enter the radius of the circle:", min_value=0.0, step=0.1)
elif shape == "Rectangle":
    length = st.number_input("Enter the length of the rectangle:", min_value=0.0, step=0.1)
    breadth = st.number_input("Enter the breadth of the rectangle:", min_value=0.0, step=0.1)

# Calculate button
if st.button("Calculate"):
    if shape == "Circle":
        area = math.pi * (radius ** 2)
        st.write(f"The area of the circle with radius {radius} is {area:.2f}")
    elif shape == "Rectangle":
        area = length * breadth
        st.write(f"The area of the rectangle with length {length} and breadth {breadth} is {area:.2f}")

