# House Price Prediction Project

## 📌 Project Overview
This project aims to predict house prices using machine learning models by leveraging real estate data. The system preprocesses data, performs feature engineering, trains multiple models, and provides price recommendations and analysis.

## 📂 Project Structure

## 📊 Data Description
The project includes multiple CSV files containing real estate information such as:
- **apartments.csv, flats.csv, houses.csv** - Raw property data
- **gurgaon_properties.csv** - Processed dataset for training
- **latlong.csv** - Location-based data for geospatial analysis
- **Feature-engineered datasets** - Cleaned and transformed datasets for modeling

## 🔍 Notebooks Overview
- **EDA Notebooks:** Data visualization, univariate & multivariate analysis.
- **Data Preprocessing:** Handling missing values, outlier treatment, feature selection.
- **Model Building:** Training baseline models, feature engineering, and model selection.
- **Recommender System:** Implementing recommendation algorithms based on cosine similarity.

## 🏗️ Web Application
A web-based interface is built to make the price prediction system interactive. It includes:
- **Price Calculator** (`1_Price_Calculator.py`): Predicts house prices based on input features.
- **Analysis Dashboard** (`2_Analysis_App.py`): Provides data insights and visualizations.
- **Apartment Recommender** (`3_Recommend_Apartments.py`): Suggests similar apartments based on user preferences.

## 🚀 Installation & Setup
### Prerequisites
- Python 3.8+
- Virtual environment (optional but recommended)
- Required libraries (listed in `requirements.txt`)

### Setup Steps
1. **Clone the repository:**
   ```sh
   git clone https://github.com/netra212/House-Price-Predictions.git
   cd House-Price-Predictions```

2. **Create and activate virtual environment (optional):**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the web application:**
    ```sh
    streamlit run Home.py
    ```

### **🔥 Key Features**

    ✅ Data Cleaning & Preprocessing
    ✅ Advanced Feature Engineering
    ✅ House Price Prediction Models
    ✅ Apartment Recommendation System
    ✅ Interactive Web Application

### **🤝 Contributing**

Contributions are welcome! Feel free to fork the repository and submit a pull request.

### **📜 License**

This project is open-source and available under the MIT License.

Developed by Netra Bahadur Khatri.