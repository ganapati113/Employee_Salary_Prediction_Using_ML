# 📊 Employee Salary Prediction
This project predicts an employee's salary based on multiple features such as education, occupation, gender, hours per week, etc., using a machine learning model. The frontend is developed using Streamlit, and the backend is powered by Python and scikit-learn.

# 📌 Features
Upload or enter employee details to predict salary category (<=50K or >50K)
Batch prediction from CSV file
Data preprocessing with label encoding and scaling
Clean Streamlit web interface
Deployable on platforms like Streamlit Cloud.

# 🧰 Tools & Technologies Used
Area	         Tools / Libraries
Language	      Python
Data Handling	  Pandas, NumPy
Visualization 	Matplotlib, Seaborn
Model Building	scikit-learn
UI Framework	  Streamlit
Model Saving	  Joblib
Deployment	    Streamlit Cloud

# 📁 Folder Structure
Employee-Salary-Prediction/
│
├── app.py                       # Streamlit App
├── train_model.py              # ML model training script
├── salary_predictor.pkl        # Trained model with encoders and scaler
├── requirements.txt            # All dependencies
├── Salary Data.csv             # Dataset (Adult Census Income)
├── README.md                   # Project documentation
└── images/                     # Optional images for UI or README

# ⚙️ How It Works
Data is loaded and preprocessed (train_model.py)
Model is trained and saved as a .pkl file using Joblib
Streamlit app loads model and encoders
User inputs or uploads batch data
App shows salary prediction (<=50K or >50K)





