import numpy as np
import pickle
import streamlit as st

# Load the trained model
pickle_in = open("classifier3.pkl", "rb")
classifier = pickle.load(pickle_in)

def predict_stress(skin_resistance, respiratory_rate, temp, blood_oxygen, heart_rate):
    prediction = classifier.predict([[skin_resistance, respiratory_rate, temp, blood_oxygen, heart_rate]])
    return prediction[0]

def main():
    st.title("Stress Detection ML App")
    
    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .big-font {
            font-size: 24px !important;
        }
        .btn {
            background-color: tomato;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 18px;
        }
        .btn:hover {
            background-color: #FF5733;
        }
        .result {
            padding: 10px;
            border-radius: 5px;
            margin-top: 20px;
            font-size: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('<p class="big-font">Stress Detection ML App</p>', unsafe_allow_html=True)
    
    skin_resistance = st.text_input("Skin Resistance", "")
    respiratory_rate = st.text_input("Respiratory Rate", "")
    temp = st.text_input("Temperature", "")
    blood_oxygen = st.text_input("Blood Oxygen", "")
    heart_rate = st.text_input("Heart Rate", "")
    
    # Removed Sleep Activity input as it was not in the original model

    if st.button("Predict", class_='btn'):
        if skin_resistance and respiratory_rate and temp and blood_oxygen and heart_rate:
            result = predict_stress(float(skin_resistance), float(respiratory_rate), float(temp), float(blood_oxygen), float(heart_rate))
            if result == 0 or result == 1:
                st.success('<p class="result">Low Stress</p>', unsafe_allow_html=True)
            elif result == 2:
                st.warning('<p class="result">Medium Stress</p>', unsafe_allow_html=True)
            elif result == 3 or result == 4:
                st.error('<p class="result">High Stress</p>', unsafe_allow_html=True)
        else:
            st.warning("Please fill in all fields before predicting.")
    
    if st.button("About", class_='btn'):
        st.text("Stress Prediction")

if __name__ == '__main__':
    main()
