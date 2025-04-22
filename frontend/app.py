from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the standard scaler
with open('model/standard-scaler.pkl', 'rb') as scaler_file:
    scaler = joblib.load(scaler_file)

# Load the trained machine learning model
with open('model/RandomForestClassifier.pkl', 'rb') as model_file:
    model = joblib.load(model_file)

# home route
@app.route('/')
def home():
    return render_template('index.html')

# dashboard route
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/predict', methods=['post'])
def predict():
    
    # Fetching form values
    tenure = float(request.form.get('Tenure'))
    Contract = int(request.form.get('Contract'))
    Partner = int(request.form.get('Partner'))
    Dependents = int(request.form.get('Dependents'))
    SeniorCitizen = int(request.form.get('SeniorCitizen'))
    InternetService_Fiber_optic = 1 if request.form.get('InternetService') == 'Fiber optic' else 0
    InternetService_No = 1 if request.form.get('InternetService') == 'No' else 0  
    OnlineSecurity_Yes = 1 if request.form.get('OnlineSecurity') == 'Yes' else 0
    OnlineSecurity_No_internet_service = 1 if request.form.get('OnlineSecurity') == 'No internet service' else 0
    OnlineBackup_No_internet_service = 1 if request.form.get('OnlineBackup') == 'No internet service' else 0
    DeviceProtection_No_internet_service = 1 if request.form.get('DeviceProtection') == 'No internet service' else 0
    StreamingTV_No_internet_service = 1 if request.form.get('StreamingTV') == 'No internet service' else 0
    StreamingMovies_No_internet_service = 1 if request.form.get('StreamingMovies') == 'No internet service' else 0
    TechSupport_No_internet_service = 1 if request.form.get('TechSupport') == 'No internet service' else 0
    TechSupport_Yes = 1 if request.form.get('TechSupport') == 'Yes' else 0
    PaperlessBilling = int(request.form.get('PaperlessBilling'))
    PaymentMethodType_Manual = 1 if request.form.get('PaymentMethod') == 'Electronic check' or request.form.get('PaymentMethod') == 'Mailed check' else 0
    MonthlyCharges = float(request.form.get('MonthlyCharges'))
    total_charges = float(request.form.get('TotalCharges'))
    
    HighRisk = 1 if Contract == 1 and MonthlyCharges > 70.35 else 0 # median of monthly charges is 70.35
   
    services = ['PhoneService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
    # Count only services that are explicitly 'Yes'
    service_count = sum(1 for service in services if request.form.get(service, 'No') == 'Yes')
    
    # apply scaling
    scaled_features = scaler.transform(np.array([[tenure, MonthlyCharges, total_charges, service_count]]))
    
    tenure, MonthlyCharges, total_charges, service_count = scaled_features[0]

    # Create feature array
    features = np.array([[SeniorCitizen, Partner, Dependents, tenure, Contract,
        PaperlessBilling, MonthlyCharges, HighRisk,
        InternetService_Fiber_optic, InternetService_No,
        OnlineSecurity_No_internet_service, OnlineSecurity_Yes,
        OnlineBackup_No_internet_service,
        DeviceProtection_No_internet_service,
        TechSupport_No_internet_service, TechSupport_Yes,
        StreamingTV_No_internet_service,
        StreamingMovies_No_internet_service, PaymentMethodType_Manual]])
    # # Make prediction
    prediction = model.predict(features)

    # Return result
    return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
