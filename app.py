import streamlit as st
import requests
from datetime import datetime

st.markdown('''NY Taxi''')

col1, col2 = st.columns(2)
with col1:
    pickup_date= st.date_input('enter day of trip', format='YYYY/MM/DD')
with col2:
    pickup_time= st.time_input('enter time')

pickup_datetime = datetime.combine(pickup_date, pickup_time).strftime('%Y-%m-%d %H:%M:%S')

col1, col2 = st.columns(2)
with col1:
    st.subheader('Pick up')
    pickup_longitude = st.number_input('pickup_lon', value=-73.98)
    pickup_latitude = st.number_input('pickup_lat', value=40.76)
with col2:
    st.subheader('Dropoff')
    dropoff_longitude = st.number_input('dropoff_lon', value=-73.78)
    dropoff_latitude = st.number_input('dropoff_lat', value=40.64)


passenger_count= st.number_input('passenger count')


if st.button('🔮 Predecir tarifa'):
    url= "https://taxifare-1029998951756.europe-west1.run.app/predict"
    params = {'pickup_datetime': pickup_datetime,
        'pickup_longitude':pickup_longitude,
        'pickup_latitude':pickup_latitude,
        'dropoff_longitude':dropoff_longitude,
        'dropoff_latitude':dropoff_latitude,
        'passenger_count':passenger_count}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        prediction = response.json()
        st.success(f"💵 Tarifa estimada: ${prediction['fare']:.2f}")
    else:
        st.error(f"Error {response.status_code}: no se pudo obtener la predicción.")
