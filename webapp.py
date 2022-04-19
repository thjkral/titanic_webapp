#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:45:41 2022

@author: tom
"""

import streamlit as st
import numpy as np
import pandas as pd
import joblib

from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier


def predict(new_data):
    
    new_data = scaler.transform(new_data)
    
    new_pred = model.predict(new_data)
    
    if new_pred[0] == 0:
        st.subheader("You didn't make it")
        st.image('images/dead.gif')
    elif new_pred[0] == 1:
        st.subheader('You survived!')
        st.image('images/alive.gif')
    else:
        st.subheader('Something went wrong')


# Load model and scaler
model = joblib.load('model_and_scaler/knn_titanic_model.sav')
scaler = joblib.load('model_and_scaler/knn_titanic_scaler.sav')

# Add welcome text
st.title('Would you survive the Titanic?')
st.header('Fill in your information and find out')
st.markdown('**Please enter personal details**')

# Ask for age
age = st.number_input('Enter your age', value=0)

# Ask for sex and convert to dummy value
sex = st.radio('Gender',('Male', 'Female'))
gender = 1
if sex == 'Female':
    gender = 0


st.markdown('**Please enter details about your trip**')

# Ask for passenger class and assign fare price
pclass = st.radio('What kind of ticket would you like to buy?',
                  ('First class | €12.318', 'Second class | €3.079', 'Third class | €2.053'))

pclass_int = 3
if pclass == 'First class | €12.318':
    pclass_int = 1
elif pclass == 'Second class | €3.079':
    pclass_int = 2


fare = 14
if pclass == 'First class | €12.318':
    fare = 84
elif pclass == 'Second class | €3.079':
    fare = 21

# Ask for family
sibsp = st.number_input('How many siblings and spouses are coming with you? *', value=0)
parch = st.number_input('How many parents or children are coming with you? **', value=0)

st.text('* Sibling = brother, sister, stepbrother, stepsister\n Spouse = husband, wife (fiancés were ignored in the original dataset)')
st.text('** Parent = mother, father\n Child = daughter, son, stepdaughter, stepson')

# Ask about embarkation
port = st.radio('Where would you like to embark?',
                ('Cherbourg (France)', 'Queenstown (UK)', 'Southampton (UK)'))

q = 0
s = 0
if port == 'Queenstown (UK)':
    q = 1
elif port == 'Southampton (UK)':
    s = 1


if st.button('CALCULATE'):
    # Make new data entry
    new_data = np.array([pclass_int, age, sibsp, parch, fare, gender, q, s])    
    new_data = new_data.reshape(1, -1)
    predict(new_data)







