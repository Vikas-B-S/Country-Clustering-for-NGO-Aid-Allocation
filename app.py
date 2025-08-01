
import numpy as np 
import pandas as pd
import joblib
import streamlit as st

# First Lets load the instances that were created 

with open('scaler.joblib','rb') as file:
    scale=joblib.load(file)

with open('pca.joblib','rb') as file:
    scale=joblib.load(file)

with open('kmeans_final_model.joblib','rb') as file:
    scale=joblib.load(file)

def prediction(input_list):
    scaled_input=scale.transform([input_list])
    pca_input=pca.transform(scaled_input)
    output=model.predict(pca_input)[0]

    if output==0:
        return 'Developing'
    elif output==1:
        return 'Developed'
    else:
        return 'Underdeveloped'

def main():
    st.title('Health NGO Foundation')
    st.subheader('This application will give the status of a country based on Socio-economic and Health Factors')
    gdp=st.text_input('Enter the gdp per population of a country')
    income=st.text_input('Enter the per capita income of the country')
    imp=st.text_input('Enter the imports in terms of percent of GDP')
    exp=st.text_input('Enter the exports in terms of percent of GDP')
    inf=st.text_input('Enter the inflation rate in the country(%)')

    hel=st.text_input('Enter the health expenses in terms of percent of GDP')
    child_mor=st.text_input('Enter the number of deaths per 1000 births for less than 5years')
    fert_rate=st.text_input('Enter the average children born to a women in the country')
    lf=st.text_input('Enter the average life expectancy in the country')

    in_data=[child_mor,exp,hel,imp,income,inf,lf,fert_rate,gdp]

    if st.button('Predict'):
       response = prediction(in_data)
       st.success(response)

if __name__=='__main__':
    main()
