import streamlit as st
import streamlit.components.v1 as components

# Set up page configuration
st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="🏠",
)

# Frontend Part (HTML + JavaScript for header and interactivity)
header_html = """
    <style>
        /* Header styling */
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #3b3b3b;
            color: white;
            padding: 20px;
            border-radius: 8px;
        }
        .logo {
            font-size: 1.5em;
            font-weight: bold;
        }
        .header .nav-links {
            display: flex;
            gap: 20px;
        }
        .header .nav-links a {
            color: white;
            text-decoration: none;
            font-size: 1.1em;
            font-weight: 500;
        }
        .header .nav-links a:hover {
            text-decoration: underline;
        }
    </style>

    <div class="header">
        <div class="logo">Gurgaon Real Estate</div>
        <div class="nav-links">
            <a href="#">Home</a>
            <a href="#">Properties</a>
            <a href="#">Contact</a>
        </div>
    </div>
    
    <script>
        // JavaScript for header interaction, if any.
        console.log("Header section loaded!");
    </script>
"""

# Inject frontend code into Streamlit using components
components.html(header_html, height=200)

# Python Part (Home Section with dynamic house details)
st.write("# Welcome to Streamlit! 👋")

# House details (sample data)
house_details = {
    "Address": "1234 Gurgaon St, Sector 50",
    "Price": "$1,000,000",
    "Size": "3000 sqft",
    "Bedrooms": 4,
    "Bathrooms": 3,
    "Year Built": 2015,
    "Garage": "2-car garage",
    "Description": "A beautiful, spacious home located in a prime neighborhood of Gurgaon.",
}

# Add some CSS for Flexbox layout
st.markdown("""
    <style>
        .house-details {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: space-between;
        }
        .house-detail {
            flex: 1 1 30%;
            min-width: 250px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .house-detail h3 {
            margin-top: 0;
        }
    </style>
""", unsafe_allow_html=True)

# Display house details using Flexbox
st.markdown('<div class="house-details">', unsafe_allow_html=True)

for key, value in house_details.items():
    st.markdown(f"""
        <div class="house-detail">
            <h3>{key}</h3>
            <p>{value}</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Sidebar
st.sidebar.success("Select a demo above.")
