import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import pickle

df = pd.read_csv('diabetes.csv')
model = pickle.load(open('Diabetesmodel.pkl','rb'))

def app():
    img= Image.open(r"photos/diabetes.jpeg.webp")

    st.title('Diabetes Disease Prediction')

    st.image(img,caption= 'Diabetes Image', width=500)

    st.sidebar.title('input features')
    preg=st.sidebar.slider('Pregnancies',0,17,3)
    glucose=st.sidebar.slider('Glucose',0,199,117)
    bp=st.sidebar.slider('BP',0,122,72)
    skin=st.sidebar.slider('Skin Thickness',0,99,23)
    insulin=st.sidebar.slider('Insulin',0,846,30)
    bmi= st.sidebar.slider('BMI',0.0,47.1,32.0)
    dpf= st.sidebar.slider('Diabetes Pedigree Function',0.078,2.42,0.3725,0.001)
    age= st.sidebar.slider('Age',21,81,23)

    input_data=[preg,glucose,bp,skin,insulin,bmi,dpf,age]
    id_array=np.asarray(input_data)
    reshaped_i_d = id_array.reshape(1,-1)
    pred = model.predict(reshaped_i_d)

    if pred ==1:
        st.warning('This person has Diabetes')
    else:
        st.success('This person has no Diabetes ')


if __name__ == "__main__":
    app()