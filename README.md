# 🔥 Algerian Forest Fire: FWI Prediction System

A machine learning solution designed to predict the **Fire Weather Index (FWI)**, a critical component of the Canadian Forest Fire Weather Index System. By analyzing atmospheric conditions, this system enables proactive wildfire risk assessment and environmental monitoring.

## 🚀 Live Demo
[**Click here to view the live app on Render**](https://fwi-prediction-system.onrender.com)
<table sorted>
  <tr>
    <td align="center">
      <img src="app_page1.png" alt="App Page 1" width="450px">
    </td>
    <td align="center">
      <img src="app_page2.png" alt="App Page 2" width="450px">
    </td>
  </tr>
</table>

## 📌 Project Overview
The project utilizes environmental data from the Bejaia and Sidi Bel-Abbes regions of Algeria. The goal is to shift from reactive fire monitoring to predictive risk management using atmospheric parameters.

### 💡 Key Features:
1. **Lasso Regularization:** Leverages L1 regularization for automated feature selection and robust generalization, effectively mitigating multi-collinearity among atmospheric features.
2. **Real-time Inference:** A lightweight Flask-based interface providing instant FWI scoring based on 9 atmospheric and fire-behavior parameters (Temperature, RH, Ws, etc.).
3. **Production-Ready Architecture:** Implements a clean separation between the experimental research phase (Jupyter) and a modular, scalable production environment.

## ⚙️ Tech & Results:
- **Stack:** Stack: Python, Flask, Scikit-Learn, Pandas, Render, CSS3 with HTML.
- **Model Selection:** Lasso Regression was selected as the final production engine due to its superior error-handling and ability to shrink coefficients of less important features to zero.
- **Key Result:** Achieved a high predictive accuracy with an R² score of 89.68% and a Mean Absolute Error (MAE) of 1.02.

## 📊 Results & Insights
- **Core Technique:** Supervised Machine Learning with an End-to-End Deployment pipeline.
- **Feature Importance:** Atmospheric features were analyzed for high correlation with FWI; parameters like FFMC and ISI were identified as critical drivers of fire intensity.
- **Validation:** Performance was verified through residual analysis and R² scoring to ensure reliable predictions across varying weather patterns and geographical regions.


## 📂 Project Structure
```text
├── application.py                                # Flask Server Entry Point
├── models/
│   ├── lasso.pkl                                 # Best performing Lasso model
│   ├── ridge.pkl                                 # Ridge regression model
│   └── scaler.pkl                                # StandardScaler for feature normalization
├── templates/
│   ├── index.html                                # Landing Page
│   └── home.html                                 # Prediction Form & Result UI
├── notebooks/
│   ├── ridgelasso.ipynb                          # Model Training & EDA Notebook
│   └── Algerian_forest_fires_dataset_UPDATE.csv  # Cleaned Dataset
└── requirements.txt        # Python Dependencies

```

## ⚙️ Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/anantj09/Algerian-Forest-Fire-Prediction.git](https://github.com/anantj09/Algerian-Forest-Fire-Prediction.git)
   cd Algerian-Forest-Fire-Prediction
   ```
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application:**
   ```bash
   python application.py
   ```

## 📝 Author - **Anant Jain**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/anant-jain09/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/anantj09)

---

> **Note:** This project focuses on the practical application of Regularization techniques in environmental data science, providing a robust tool for wildfire risk assessment.
