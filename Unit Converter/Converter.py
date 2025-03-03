import streamlit as st
import time

# Initialize session state for conversion history
if 'history' not in st.session_state:
    st.session_state.history = []

def length_conversion(value, from_unit, to_unit):
    conversion_factors = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Miles": 0.000621371,
        "Feet": 3.28084,
        "Yards": 1.09361,
        "Inches": 39.37,
    }
    return (value / conversion_factors[from_unit]) * conversion_factors[to_unit]

def weight_conversion(value, from_unit, to_unit):
    conversion_factors = {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274,
    }
    return (value / conversion_factors[from_unit]) * conversion_factors[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value

st.title("✨ Real-Time Unit Converter with History")
st.write("Convert between different units of Length, Weight, and Temperature instantly!")

conversion_option = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter value to convert", value=0.0, step=0.1)

col1, col2 = st.columns(2)

if conversion_option == "Length":
    with col1:
        from_unit = st.selectbox("From Unit", ["Meters", "Kilometers", "Miles", "Feet", "Yards", "Inches"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Meters", "Kilometers", "Miles", "Feet", "Yards", "Inches"])
elif conversion_option == "Weight":
    with col1:
        from_unit = st.selectbox("From Unit", ["Kilograms", "Grams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Kilograms", "Grams", "Pounds", "Ounces"])
elif conversion_option == "Temperature":
    with col1:
        from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])

# Real-time conversion
if value > 0:
    with st.spinner("Converting..."):
        time.sleep(1)  # Animation delay
        if conversion_option == "Length":
            result = length_conversion(value, from_unit, to_unit)
        elif conversion_option == "Weight":
            result = weight_conversion(value, from_unit, to_unit)
        elif conversion_option == "Temperature":
            result = temperature_conversion(value, from_unit, to_unit)
        
        st.success(f"Converted Value: {value} {from_unit} = {result:.4f} {to_unit}")
        
        # Store conversion in history
        st.session_state.history.append(f"{value} {from_unit} → {result:.4f} {to_unit}")
else:
    st.warning("Enter a positive value for conversion.")

# Display conversion history
st.subheader("📜 Conversion History")
if st.session_state.history:
    for record in reversed(st.session_state.history[-5:]):  # Show last 5 conversions
        st.write(record)
else:
    st.write("No conversions yet.")