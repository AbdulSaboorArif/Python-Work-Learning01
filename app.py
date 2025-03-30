import streamlit as st


conversion_factors = {
        'Length': {
            'meters': 1,
            'kilometers': 0.001,
            'miles': 0.000621371,
            'feet': 3.28084,
        },
        'Weight': {
            'grams': 1,
            'kilograms': 0.001,
            'pounds': 0.00220462,
            'ounces': 0.035274,
        },
        'Temperature': {
            'Celsius': lambda x: x,
            'Fahrenheit': lambda x: (x * 9/5) + 32,
            'Kelvin': lambda x: x + 273.15,
        }
    }

st.title("Google Unit Converter With Python and Streamlit")

# Select Category
category = st.selectbox("Select Conversion Category", ["Length", "Weight", "Temperature"])

# Select From and To Units
if category in conversion_factors:
  units = list(conversion_factors[category].keys())
  from_unit = st.selectbox("From Unit", units)
  to_unit = st.selectbox("To Unit", units)

# convert value form unit to to unit

def convert_unit (value, from_unit, to_unit, category):
  if category in conversion_factors:
    from_factor = conversion_factors[category][from_unit]
    to_factor = conversion_factors[category][to_unit]
    return value * (to_factor/from_factor)
  return None

# Temperature Conversation work

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value  # If units are the same

# Input Value
value = st.number_input("Enter Value", min_value=0.0, step=0.1)

# Button to Convert
if st.button("Convert"):
  if category == "Temperature":
      result = convert_temperature(value, from_unit, to_unit)
  else:
      result = convert_unit(value, from_unit, to_unit, category)


  st.success(f"{value} {from_unit} = {result} {to_unit}")
