import pandas as pd
import numpy as np
import pickle
import streamlit as st

pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)
  
def welcome():
    return 'welcome all'
  
def prediction(rr, bt, bo, sh, hr):  
   
    prediction = classifier.predict(
        [[rr, bt, bo, sh, hr]])
    print(prediction)
    return prediction
      
def main():
    st.title('PLAY WITH EMOTIONS:')
    st.markdown(" ")


    rr = st.number_input("Enter Respiration Rate")
    bt = st.number_input("Enter Body Temprature")
    bo = st.number_input("Enter Blood Oxygen")
    sh = st.number_input("Enter sleeping_hours")
    hr = st.number_input("Enter heart_rate")
    st.markdown(" ")
    result =" "
      

    if st.button("Predict"):
        result = prediction(rr, bt, bo, sh, hr)
        result = int(result)
    st.success('Stress Level: {} '.format(result))
     
if __name__=='__main__':
    main()