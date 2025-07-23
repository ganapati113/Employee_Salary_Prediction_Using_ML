# 📊 Employee Salary Prediction
This project predicts an employee's salary based on multiple features such as education, occupation, gender, hours per week, etc., using a machine learning model. The frontend is developed using Streamlit, and the backend is powered by Python and scikit-learn.

# 📌 Features
Upload or enter employee details to predict salary category (<=50K or >50K) <br>
Batch prediction from CSV file <br>
Data preprocessing with label encoding and scaling <br>
Clean Streamlit web interface <br>
Deployable on platforms like Streamlit Cloud.<br>

# 🧰 Tools & Technologies Used
Area	         Tools / Libraries <br>
Language	      Python <br>
Data Handling	  Pandas, NumPy <br>
Visualization 	Matplotlib, Seaborn <br>
Model Building	scikit-learn <br>
UI Framework	  Streamlit <br>
Model Saving	  Joblib <br>
Deployment	    Streamlit Cloud <br>

# 📁 Folder Structure 
Employee-Salary-Prediction/ <br>
│
├── app.py                       # Streamlit App <br>
├── train_model.py              # ML model training script <br>
├── salary_predictor.pkl        # Trained model with encoders and scaler <br>
├── requirements.txt            # All dependencies <br>
├── Salary Data.csv             # Dataset (Adult Census Income) <br>
├── README.md                   # Project documentation <br>
└── images/                     # Optional images for UI or README <br>

# ⚙️ How It Works 
Data is loaded and preprocessed (train_model.py) <br>
Model is trained and saved as a .pkl file using Joblib <br>
Streamlit app loads model and encoders <br>
User inputs or uploads batch data <br>
App shows salary prediction (<=50K or >50K)





