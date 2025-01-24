import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os

st.set_page_config(page_title="Viz Demo", page_icon="🏠", layout="wide")

# --- Header Section ---
st.markdown(
    """
    <style>
    .header {
        text-align: center;
        font-size: 50px;
        color: #4CAF50;
        font-weight: bold;
    }
    .subheader {
        text-align: center;
        font-size: 20px;
        color: #777;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="header">🏠 House Price Prediction 🏡</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Enter property details to predict the price of your house.</div>', unsafe_allow_html=True)


# Function to load a pickled file (returns the loaded object)
def load_pickle_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    
    try:
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    except pickle.UnpicklingError:
        raise ValueError(f"Error unpickling the file: {file_path}")
    except Exception as e:
        raise RuntimeError(f"An error occurred while opening the file {file_path}: {str(e)}")


# File paths
df_path = '/Users/netrakc/Desktop/House-Price-Predictions/models/df.pkl'
pipeline_path = '/Users/netrakc/Desktop/House-Price-Predictions/models/pipeline.pkl'

# Load files
try:
    df = load_pickle_file(df_path)       # Load dataframe
    pipeline = load_pickle_file(pipeline_path)  # Load pipeline

    print("Files loaded successfully.")

except FileNotFoundError as fnf_error:
    print(fnf_error)
except ValueError as unpickle_error:
    print(unpickle_error)
except RuntimeError as runtime_error:
    print(runtime_error)
except Exception as general_error:
    print(f"An unexpected error occurred: {general_error}")

# --- Input Section ---
property_type = st.selectbox("Property Type", ['flat', 'house'])
sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))
bedrooms = float(st.selectbox('Number of Bedroom', sorted(df['bedRoom'].unique().tolist())))
bathroom = float(st.selectbox('Number of Bathrooms', sorted(df['bathroom'].unique().tolist())))
balcony = st.selectbox('Balconies', sorted(df['balcony'].unique().tolist()))
property_age = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()))
built_up_area = float(st.number_input('Built Up Area (sq. ft.)'))
servant_room = float(st.selectbox('Servant Room', [0.0, 1.0]))
store_room = float(st.selectbox('Store Room', [0.0, 1.0]))
furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))
luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))
floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))

# --- Prediction Section ---
if st.button("Predict Property Price"):
    # First build a dataframe.
    data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']
    
    # Convert to pandas dataframe.
    one_df = pd.DataFrame(data, columns=columns)

    # Predicting the property price.
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    # Displaying the result.
    st.markdown(f"### The predicted price of the property is between **₹{round(low, 2)} Cr** and **₹{round(high, 2)} Cr**.")

# --- Footer Section ---
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        background-color: #f1f1f1;
        padding: 10px;
        color: #555;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="footer">Created with ❤️ by Your Team | <a href="https://www.predictyourhouseprice.com">www.yourwebsite.com</a></div>', unsafe_allow_html=True)
