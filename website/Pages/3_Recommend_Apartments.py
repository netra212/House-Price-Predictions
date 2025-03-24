import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os

st.set_page_config(page_title="Recommend Apartments")

# Load Data
location_df = pickle.load(open("/Users/netrakc/Desktop/House-Price-Predictions/website/datasets/location_distance.pkl", 'rb'))
cosine_sim1 = pickle.load(open('/Users/netrakc/Desktop/House-Price-Predictions/website/datasets/cosine_sim1.pkl', 'rb'))
cosine_sim2 = pickle.load(open('/Users/netrakc/Desktop/House-Price-Predictions/website/datasets/cosine_sim2.pkl', 'rb'))
cosine_sim3 = pickle.load(open('/Users/netrakc/Desktop/House-Price-Predictions/website/datasets/cosine_sim3.pkl', 'rb'))

# Ensure location_df has the correct index
if not isinstance(location_df.index, pd.Index):
    st.error("Error: location_df does not have a valid index. Check your dataset.")
    st.stop()

def recommend_properties_with_scores(property_name, top_n=5):
    # Create a weighted similarity matrix
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3
    
    # Validate if property_name exists
    if property_name not in location_df.index:
        st.error(f"Error: '{property_name}' not found in the dataset. Please select a valid property.")
        st.stop()

    # Get the index of the property
    property_index = location_df.index.get_loc(property_name)

    # Ensure property_index is within bounds
    if isinstance(property_index, (list, np.ndarray)):  # Handle multiple matches
        property_index = property_index[0]

    if property_index >= cosine_sim_matrix.shape[0]:
        st.error("Error: Property index is out of bounds for the similarity matrix.")
        st.stop()

    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim_matrix[property_index]))

    # Sort properties based on similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get top-n similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

    # Ensure indices are valid
    if max(top_indices) >= len(location_df):
        st.error("Error: Indices out of bounds for location_df.")
        st.stop()

    # Retrieve property names
    top_properties = location_df.index[top_indices].tolist()

    # Return results as a DataFrame
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })

    return recommendations_df

# UI for location search
st.title('Select Location and Radius')

selected_location = st.selectbox('Location', sorted(location_df.columns.to_list()))
radius = st.number_input('Radius in Kms', min_value=0.0, step=0.1)

if st.button('Search'):
    if selected_location in location_df.columns:
        result_ser = location_df[location_df[selected_location] < radius * 1000][selected_location].sort_values()

        if not result_ser.empty:
            for key, value in result_ser.items():
                st.text(f"{key} {round(value / 1000)} kms")
        else:
            st.warning("No properties found within the selected radius.")
    else:
        st.error(f"Error: '{selected_location}' not found in the dataset.")

# UI for recommendations
st.title('Recommend Apartments')
selected_apartment = st.selectbox('Select an apartment', sorted(location_df.index.to_list()))

if st.button('Recommend'):
    recommendation_df = recommend_properties_with_scores(selected_apartment)

    if not recommendation_df.empty:
        st.write("Top Recommended Properties:")
        st.dataframe(recommendation_df)
    else:
        st.warning("No similar properties found.")
