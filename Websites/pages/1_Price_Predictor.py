import streamlit as st
import pickle

st.set_page_config(page_title="Viz Demo")

st.title("Page 2")


with open("df.pkl", "rb") as file:
    df = pickle.load(file)

st.dataframe(df)

st.header(df)

# property_type
property_type = st.selectbox("Property Type", ['flat', 'house'])

# sector.
st.selectbox('Sector', sorted(df['sector'].unique().tolist()))

# bedRoom.
