import streamlit as st
import  pandas as pd
import numpy as np
import pickle

st.title('IPL Win Predictor')

pipe  = pickle.load(open('IplScore.pkl','rb'))
teams = ['Chennai Super Kings', 'Delhi Capitals',
        'Kings XI Punjab', 'Kolkata Knight Riders',
       'Mumbai Indians', 'Rajasthan Royals',
       'Royal Challengers Bangalore', 'Sunrisers Hyderabad']
places=['Abu Dhabi', 'Ahmedabad', 'Bangalore', 'Bengaluru', 'Bloemfontein',
       'Cape Town', 'Centurion', 'Chandigarh', 'Chennai', 'Cuttack',
       'Delhi', 'Dharamsala', 'Durban', 'East London', 'Hyderabad',
       'Indore', 'Jaipur', 'Johannesburg', 'Kimberley', 'Kolkata',
       'Mohali', 'Mumbai', 'Nagpur', 'Port Elizabeth', 'Pune', 'Raipur',
       'Ranchi', 'Sharjah', 'Visakhapatnam']

col1,col2=st.columns(2)
with col1 :
       batting_team=st.selectbox('Select batting team',teams)
with col2 :
       bowling_team=st.selectbox('Select bowling team',teams)

selected_city=st.selectbox('Select Venue',places)
target =st.number_input('Enter Target')

col3,col4,col5  = st.columns(3)
with col3:
       score=st.number_input('Enter Score')
with col4:
       overs=st.number_input('Overs Completed')
with col5:
       wickets=st.number_input('Wickets')

if st.button('Predict Probability'):
       runs_left=target-score
       balls_left=120-(overs*6)
       wickets = 10- wickets
       crr = score / overs
       rrr = (runs_left*6) / balls_left

       input_df =pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team], 'city':[selected_city],
                               'runs_left': [runs_left], 'balls_left':[balls_left] ,
                               'wickets':[wickets], 'crr':[crr], 'rrr':[rrr]})

       result = pipe.predict_proba(input_df)
       loss= result[0][0]
       win = result[0][1]

       st.header(batting_team+ " - " +str(round(win*100))+ "%")
       st.header(bowling_team+ " - " +str(round(loss*100))+ "%")

