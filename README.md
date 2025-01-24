# House-Price-Predictions
 Machine Learning project for predicting house prices using advanced regression techniques.
# House Price Predictions

This project is focused on predicting house prices using machine learning techniques and is structured for scalability and user accessibility. The repository is well-organized and features distinct modules for preprocessing, analysis, and deployment. The project can be used for real estate insights and pricing models, making it valuable for professionals and data enthusiasts alike.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [File Structure](#file-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Notebooks](#notebooks)
- [Website Deployment](#website-deployment)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

House Price Predictions leverages advanced machine learning workflows to estimate property prices based on various attributes. With robust preprocessing and an intuitive user interface, this project is designed for scalability and efficient deployment.

### Key Highlights:
- Data cleaning and preprocessing.
- Exploratory Data Analysis (EDA).
- Feature selection and engineering.
- Model building, selection, and evaluation.
- Web-based interface for real-time predictions.

---

## Features
- **Preprocessing:** Handles missing values, outlier treatments, and feature selection.
- **EDA:** Generates univariate and multivariate visual insights.
- **Machine Learning Models:** Implements baseline and advanced models.
- **Web Application:** Interactive interface for property price predictions.

---

## File Structure

```plaintext
.
├── data
│   ├── apartments.csv
│   ├── flats.csv
│   ├── gurgaon_properties_cleaned_v1.csv
│   ├── gurgaon_properties_cleaned_v2.csv
│   ├── gurgaon_properties_missing_value_imputation.csv
│   ├── gurgaon_properties_outlier_treated.csv
│   ├── gurgaon_properties_post_feature_selection.csv
│   ├── houses.csv
│
├── models
│   ├── df.pkl
│   ├── pipeline.pkl
│
├── notebooks
│   ├── flat_preprocessing.ipynb
│   ├── house_preprocessing.ipynb
│   ├── Housing_Project_Building_Baseline_Model.ipynb
│   ├── Housing_Project_EDA_Multivariate_Analysis.ipynb
│   ├── Housing_Project_EDA_Univariate.ipynb
│   ├── Housing_Project_Feature_Selection_And_Feature_Engineering.ipynb
│   ├── Housing_Project_Feature_Selection.ipynb
│   ├── Housing_Project_Missing_Values_Imputation.ipynb
│   ├── Housing_Project_Model_Selection.ipynb
│   ├── Housing_Project_Outlier_Treatment.ipynb
│   ├── Project_Feature_Engineering.ipynb
│
├── website
│   ├── Pages
│   │   ├── Analysis_App.py
│   │   ├── Price_Calculator.py
│   │
│   ├── Home.py
│
├── .gitignore
├── README.md
├── requirements.txt
```

### Description:
- **Data:** Contains raw and processed datasets used in the project.
- **Models:** Stores serialized machine learning models.
- **Notebooks:** Jupyter notebooks for step-by-step analysis and processing.
- **Website:** Code for the web interface.
- **requirements.txt:** Dependencies required to run the project.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/house-price-predictions.git
   cd house-price-predictions
   ```

2. Set up a virtual environment and install dependencies:
   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

3. Run Jupyter notebooks or deploy the web app locally.

---

## Usage

### For Jupyter Notebooks:
1. Open any `.ipynb` file in the `notebooks` directory to explore and execute workflows step by step.

### For the Web Application:
1. Navigate to the `website` folder.
2. Run the web application:
   ```bash
   python Home.py
   ```
3. Access the app on `http://127.0.0.1:8000/`.

---

## Notebooks

### Key Notebooks:
- **EDA:** Perform visual analysis of the datasets.
- **Preprocessing:** Clean and transform data for model training.
- **Feature Engineering:** Enhance predictive power through feature selection.
- **Model Training:** Build and evaluate various machine learning models.

---

## Website Deployment

The web interface allows users to input property attributes and receive price predictions. The application can be extended for deployment on platforms like AWS, Heroku, or any cloud service provider.

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request.

For major changes, please open an issue first to discuss.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

