
import streamlit as st
import joblib

# Load the saved model
loaded_model = joblib.load('best_model.joblib') 

# Load the scaler (if you used one during training)
#scaler = joblib.load('scaler.joblib') 

# Define the input fields
st.title("Music Style Predictor")
danceability = st.slider("Danceability (%)", 0.0, 100.0, 50.0) / 100
valence = st.slider("Valence (%)", 0.0, 100.0, 50.0) / 100
energy = st.slider("Energy (%)", 0.0, 100.0, 50.0) / 100
acousticness = st.slider("Acousticness (%)", 0.0, 100.0, 50.0) / 100
instrumentalness = st.slider("Instrumentalness (%)", 0.0, 100.0, 50.0) / 100
liveness = st.slider("Liveness (%)", 0.0, 100.0, 50.0) / 100
speechiness = st.slider("Speechiness (%)", 0.0, 100.0, 50.0) / 100

# Create a button for prediction
if st.button("Predict"):
    # Preprocess the input data
    features = [danceability, valence, energy, acousticness, instrumentalness, liveness, speechiness]
    scaled_features = scaler.transform([features]) 
    
    # Make prediction
    prediction = loaded_model.predict(scaled_features)[0] 
    st.success(f"Predicted Style: {prediction}")
