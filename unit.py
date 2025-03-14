import streamlit as st
import base64
import time

def set_bg_image(image_url):
    page_bg_img = f'''
    <style>
    .stApp {{
        no-repeat center center fixed;
        background-size: cover;
    }}
    .loading-animation {{
        display: none;
        text-align: center;
        font-size: 24px;
        color: #ffcc00;
        animation: blink 1s infinite;
    }}
    @keyframes blink {{
        0% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
        100% {{ opacity: 1; }}
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

def convert_units(value, from_unit, to_unit, category):
    conversions = {
        "Length": {
            "Meter": {"Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000},
            "Kilometer": {"Meter": 1000, "Centimeter": 100000, "Millimeter": 1000000},
            "Centimeter": {"Meter": 0.01, "Kilometer": 0.00001, "Millimeter": 10},
        },
        "Weight": {
            "Kilogram": {"Gram": 1000, "Pound": 2.20462},
            "Gram": {"Kilogram": 0.001, "Pound": 0.00220462},
            "Pound": {"Kilogram": 0.453592, "Gram": 453.592},
        },
        "Temperature": {
            "Celsius": {"Fahrenheit": lambda c: (c * 9/5) + 32, "Kelvin": lambda c: c + 273.15},
            "Fahrenheit": {"Celsius": lambda f: (f - 32) * 5/9, "Kelvin": lambda f: (f - 32) * 5/9 + 273.15},
            "Kelvin": {"Celsius": lambda k: k - 273.15, "Fahrenheit": lambda k: (k - 273.15) * 9/5 + 32},
        },
        "Volume": {
            "Liter": {"Milliliter": 1000, "Cubic Meter": 0.001},
            "Milliliter": {"Liter": 0.001, "Cubic Meter": 1e-6},
            "Cubic Meter": {"Liter": 1000, "Milliliter": 1e6},
        },
        "Speed": {
            "Kilometers per Hour": {"Meters per Second": 0.277778, "Miles per Hour": 0.621371},
            "Meters per Second": {"Kilometers per Hour": 3.6, "Miles per Hour": 2.23694},
            "Miles per Hour": {"Kilometers per Hour": 1.60934, "Meters per Second": 0.44704},
        }
    }
    if category in conversions and from_unit in conversions[category] and to_unit in conversions[category][from_unit]:
        conversion = conversions[category][from_unit][to_unit]
        return conversion(value) if callable(conversion) else value * conversion
    return None

st.set_page_config(page_title="🔄 Unit Converter", layout="wide")

st.sidebar.title("⚙️ Choose a Category")
category = st.sidebar.radio("Select Conversion Type:", ["Length", "Weight", "Temperature", "Volume", "Speed"])

unit_options = {
    "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter"],
    "Weight": ["Kilogram", "Gram", "Pound"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Volume": ["Liter", "Milliliter", "Cubic Meter"],
    "Speed": ["Kilometers per Hour", "Meters per Second", "Miles per Hour"]
}

st.title("🔄Unit Converter App")
st.markdown("Convert different units with ease! 🌟")

value = st.number_input("🔢 Enter Value:", min_value=0.0, format="%f")
from_unit = st.selectbox("📏 From Unit:", unit_options[category])
to_unit = st.selectbox("📐 To Unit:", unit_options[category])

placeholder = st.empty()

if st.button("🚀 Convert"):
    with st.spinner("⏳ Calculating..."):
        placeholder.markdown("<div class='loading-animation'>⚙️ Processing...</div>", unsafe_allow_html=True)
        time.sleep(1.5)
    result = convert_units(value, from_unit, to_unit, category)
    placeholder.empty()
    if result is not None:
        st.success(f"✅ {value} {from_unit} = {result:.2f} {to_unit}")
    else:
        st.error("⚠️ Conversion not available!")

st.write("**Created by Saniya Malik**")       
