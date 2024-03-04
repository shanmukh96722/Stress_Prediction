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
    
    html_temp = """
    <div style="background-color: tomato; padding: 10px">
    <h2 style="color: white; text-align: center;">Stress Detection ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    skin_resistance = st.text_input("Skin Resistance", "")
    respiratory_rate = st.text_input("Respiratory Rate", "")
    temp = st.text_input("Temperature", "")
    blood_oxygen = st.text_input("Blood Oxygen", "")
    heart_rate = st.text_input("Heart Rate", "")
    Sleep_Activity=st.text_input("Sleep Activity","")
    result = ""
    if st.button("Predict"):
        result = predict_stress(float(skin_resistance), float(respiratory_rate), float(temp), float(blood_oxygen), float(heart_rate))
        st.success('The output is {}'.format(result))
        if result==0 or result==1:
            st.success("Low Stress")
        elif result==2:
            st.success("Medium Stress")
        elif result ==3 or result ==4:
            st.success("High Stress")        

    if st.button("About"):
        st.text("Stress Prediction")

if __name__ == '__main__':
    main()
