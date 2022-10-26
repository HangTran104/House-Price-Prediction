import numpy as np
import pickle
import streamlit as st
from joblib import dump, load


# Loading the saved model
model = load('RandomForestModel.joblib')


def HousePrice_Prediction(input_data):
  
  # Convert the input data to an array 2D
  input_data_array = np.array(input_data)

  # Prediction 
  prediction = model.predict(input_data_array)

  print(prediction)
  return np.exp(prediction)

def main():
  # Giving app an title
  st.title("House Price Prediction Web App")

  ['Dien_tich', 'Dien_tich_su_dung', 'Nha_ve_sinh', 'Hem_rong', 'So_lau',
       'Chieu_dai', 'So_phong', 'Quan_Huyện Nhà Bè', 'Rong', 'Duong_mat_tien',
       'Quan_Quận 10']

  # Getting the input data from the user
  Dientich = st.text_input('The space area of the house')
  Dien_tich_su_dung = st.text_input('The total usage area of the house')
  toilet = st.text_input('Number of toilet you want the house has')
  hem = st.text_input('The width of alley around the house')
  chieudai = st.text_input('the length of the house')
  so_phong = st.text_input('Numbers of rooms')
  nhabe = st.text_input('Your house is needed to located in Nha Be District or not? 0 for No and 1 for Yes')
  rong = st.text_input('The width of the house')
  quan10 = st.text_input('Your house is needed to located in Quan 10 or not?')

  # Code for prediction
  houseprice = ''
  if st.button('House Price Prediction'):
    houseprice = HousePrice_Prediction([Dientich, Dien_tich_su_dung, toilet, hem, chieudai, so_phong, nhabe, rong, quan10])

    st.success(houseprice)


if __name__ =='__main__':
  main()





