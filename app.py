import streamlit as st
import pandas as pd
import numpy as np 
import joblib


model = joblib.load('model.pkl')

teams = [
    'Australia',
    'India',
    'Bangladesh',
    'New Zealand',
    'South Africa',
    'England',
    'West Indies',
    'Afghanistan',
    'Pakistan',
    'Sri Lanka'    
]


cities = ['Colombo',
 'Dubai',
 'Johannesburg',
 'Auckland',
 'Mirpur',
 'Sydney',
 'Lahore',
 'Cape Town',
 'Dhaka',
 'London',
 'Durban',
 'Wellington',
 'Melbourne',
 'Pallekele',
 'Christchurch',
 'Barbados',
 'Centurion',
 'Abu Dhabi',
 'Lauderhill',
 'Mount Maunganui',
 'Southampton',
 'Hamilton',
 'Gros Islet',
 'Manchester',
 'Nottingham',
 'St Lucia',
 'Karachi',
 'Kolkata',
 'Bridgetown',
 'Cardiff',
 'Mumbai',
 'Adelaide',
 'Tarouba',
 'Birmingham',
 'Brisbane',
 "St George's",
 'Kandy',
 'Perth',
 'Sharjah',
 'Chittagong',
 'Delhi',
 'Ahmedabad',
 'Providence',
 'Chandigarh',
 'Kingston',
 'Rajkot',
 'Napier',
 'Nagpur',
 'Pune',
 'Bangalore',
 'Sylhet',
 'Dambulla',
 'Hobart',
 'Trinidad']

st.title('Cricket Score Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select Bowling Team', sorted(teams))

city = st.selectbox('Select city', sorted(cities))

col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')
with col4: 
    overs = st.number_input('Over done(works for over > 5)')
with col5:
    wickets = st.number_input('Wicket out')

last_five = st.number_input('Runs scored in last 5 overs')

if st.button('Predict Score'):
    balls_left = 120 - (overs*6)
    wickets_left = 10 - wickets
    crr = current_score/overs

    input_df = pd.DataFrame(
        {'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [city], 'current_score': [current_score],
            'balls_left': [balls_left], 'wickets_left': [wickets], 'crr': [crr], 'last_five': [last_five]}
    )
    result = model.predict(input_df)

    st.header("Predicted Score : " + str(int(result[0])))