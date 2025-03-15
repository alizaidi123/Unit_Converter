import streamlit as stl
import pint

ur = pint.UnitRegistry()
stl.title("Unit Converter")

con_type = stl.selectbox("Select Conversion Type",
                         ["Length", "Weight","Temperature", "Volume", "Time"])

if con_type == "Length":
    units = ["meters","kilometers","centimeters","millimeters","mile","yard",
             "foot","inch"]
elif con_type == "Weight":
    units = ["gram", "kilogram", "milligram", "tonne", "pound", "ounce"]
elif con_type == "Temperature":
    units = ["celsius", "fahrenheit"]
elif con_type == "Volume":
    units = ["liter", "milliliter", "gallon", "quart", "pint", "cup"]
elif con_type == "Time":
    units = ["second", "minute", "hour", "day", "week", "month", "year"]

col1, col2 = stl.columns(2)

with col1:
    stl.subheader("From")
    from_unit = stl.selectbox("Select Unit", units, key="from_unit")
    value = stl.number_input("Enter Value", value=1.0, key="value")

with col2:
    stl.subheader("To")
    to_unit = stl.selectbox("Select Unit", units, key="to_unit")

def con_units(value, from_unit, to_unit):
    try:
        if from_unit == "celsius" and to_unit == "fahrenheit":
            qty = value * ur.degC
            con_qty = qty.to(ur.degF)
            return con_qty.magnitude
        elif from_unit == "fahrenheit" and to_unit == "celsius":
            qty = value * ur.degF
            con_qty = qty.to(ur.degC)
            return con_qty.magnitude
        else:
            qty = value * ur(from_unit)
            con_qty = qty.to(to_unit)
            return  con_qty.magnitude
    except Exception as e:
        return f"Error:{e}"

if stl.button("Convert"):
    result = con_units(value,from_unit,to_unit)
    stl.success(f"{value} {from_unit} = {result} {to_unit}")




