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
            font-size: 36px !important;
            text-align: center;
            margin-bottom: 30px;
        }
        .input-container {
            display: flex;
            flex-direction: column;
            margin-bottom: 20px;
        }
        .input-label {
            font-size: 18px;
            margin-bottom: 5px;
        }
        .btn {
            background-color: tomato;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 18px;
            margin-top: 20px;
        }
        .btn:hover {
            background-color: #FF5733;
        }
        .result-container {
            margin-top: 30px;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
        .low-stress {
            background-color: #7FFF00;
            color: black;
        }
        .medium-stress {
            background-color: #FFFF00;
            color: black;
        }
        .high-stress {
            background-color: #FF6347;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('<p class="big-font">Stress Detection ML App</p>', unsafe_allow_html=True)
    
    with st.form(key='stress_form'):
        st.markdown('<p class="input-label">Please enter the following information:</p>', unsafe_allow_html=True)
        skin_resistance = st.number_input("Skin Resistance")
        respiratory_rate = st.number_input("Respiratory Rate")
        temp = st.number_input("Temperature")
        blood_oxygen = st.number_input("Blood Oxygen")
        heart_rate = st.number_input("Heart Rate")
        
        submitted = st.form_submit_button("Predict")
        
        if submitted:
            result = predict_stress(skin_resistance, respiratory_rate, temp, blood_oxygen, heart_rate)
            if result == 0 or result == 1:
                st.markdown('<div class="result-container low-stress"><p>Low Stress</p></div>', unsafe_allow_html=True)
            elif result == 2:
                st.markdown('<div class="result-container medium-stress"><p>Medium Stress</p></div>', unsafe_allow_html=True)
            elif result == 3 or result == 4:
                st.markdown('<div class="result-container high-stress"><p>High Stress</p></div>', unsafe_allow_html=True)
    
    st.markdown('<p style="text-align:center;">Made with ❤️ by Your Name</p>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
