import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("house_price_model.pkl")

st.title("🏡 House Price Prediction App")
st.header("Adjust the parameters below to predict house price:")

# Existing features with sliders
crime_rate = st.slider("Crime Rate (per capita)", 0.0, 100.0, 5.0)
residential_land = st.slider("% Residential Land Zoned", 0.0, 100.0, 20.0)
non_retail_business = st.slider("% Non-retail Business Acres", 0.0, 30.0, 5.0)
rooms_per_dwelling = st.slider("Average Rooms per Dwelling", 3.0, 10.0, 6.0)
age_of_property = st.slider("Age of Property (%)", 0, 100, 50)
distance_to_employment = st.slider("Distance to Employment Centers (km)", 1.0, 12.0, 5.0)
school_quality = st.slider("Pupil-Teacher Ratio", 10.0, 25.0, 15.0)

# New Features!
proximity_to_transport = st.slider("Proximity to Public Transport (km)", 0.1, 10.0, 5.0)
air_quality_index = st.slider("Air Quality Index (AQI)", 0, 500, 100)  # Lower is better
local_amenities_score = st.slider("Local Amenities Score (0-10)", 0, 10, 5)

# Dropdowns for categorical features
highway_access = st.selectbox("Nearby Highway Access Points", [0, 1, 2, 3, 4, 5])
tax_rate = st.slider("Tax Rate per $1000", 100.0, 800.0, 300.0)
ownership_status = st.selectbox("Ownership Status (0: Rental, 1: Owned)", [0, 1])

# Feature Array
features = np.array([
    crime_rate, residential_land, non_retail_business, highway_access, tax_rate, rooms_per_dwelling,
    age_of_property, distance_to_employment, school_quality, ownership_status,
    proximity_to_transport, air_quality_index, local_amenities_score
]).reshape(1, -1)

# Predict Button
if st.button("Predict House Price"):
    prediction = model.predict(features)
    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")