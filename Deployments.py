import numpy as np
import pandas as np
from sklearn.preprocessing import RobustScaler
import pickle
import streamlit as st


# Loading the saved model
model = pickle.load(open('RandomForestModel.sav', 'rb'))


def HousePrice_Prediction(input_data):
  
  # Convert the input data to an array 2D
  df_input = pd.DataFrame(input_data, columns=['Dien_tich', 'Dien_tich_su_dung', 'Nha_ve_sinh', 'Hem_rong', 'So_lau',
       'Chieu_dai', 'So_phong', 'Quan_Huyện Nhà Bè', 'Rong', 'Duong_mat_tien',
       'Quan_Quận 10'])
  num = ['Chieu_dai', 'Rong', 'Dien_tich', 'Dien_tich_su_dung']
  rb = RobustScaler()
  rb.fit(df_input[num])
  X_scale[num] = rb.transform(df_input[num])

  # Prediction 
  prediction = model.predict(X_scale)

  print(prediction)
  return np.exp(prediction)

def main():
  # Giving app an title
  st.title("House Price Prediction Web App")

  

  # Getting the input data from the user
  Dientich = st.text_input('The space area of the house')
  Dien_tich_su_dung = st.text_input('The total usage area of the house')
  toilet = st.text_input('Number of toilet you want the house has')
  hem = st.text_input('The width of alley around the house')
  so_lau = st.text_input('The number of floors you want')
  chieudai = st.text_input('the length of the house')
  so_phong = st.text_input('Numbers of rooms')
  nhabe = st.text_input('Your house is needed to located in Nha Be District or not? 0 for No and 1 for Yes')
  rong = st.text_input('The width of the house')
  duongmattien = st.text_input('Do you want your house is located next to the big streets? 0 for No and 1 for Yes?')
  quan10 = st.text_input('Your house is needed to located in Quan 10 or not?0 for No and 1 for Yest?')

  # Code for prediction
  houseprice = 0
  if st.button('House Price Prediction'):
    houseprice = HousePrice_Prediction([Dientich, Dien_tich_su_dung, toilet, hem, so_lau, chieudai, so_phong, nhabe, rong, duongmattien, quan10])

    st.success(houseprice)


if __name__ =='__main__':
  main()





