import streamlit as st
import joblib
PCI= joblib.load('model1.pkl')
Houseprice=joblib.load('price.pkl')

st.sidebar.title("Pages")
## page=st.sidebar.selectbox("Select Model",["PCI","Houseprice"]) to select multiple values
page=st.sidebar.radio('Select Model',options=["Per Capita Income Prediction","House Price Prediction"]) #to select one value at a time


if page=='Per Capita Income Prediction':

    st.title('Per Capita Income of Canada')
    st.write('This is a simple web app to predict the per capita income of canada')
    year=st.number_input('Enter the year')
    prediction=PCI.predict([[year]])

    if st.button('Predict'):
        st.write("The per capita Income of Canada in the year",year,'is',prediction[0])
else: 
    st.title('House Price Prediction')
    st.write('This is a simple web app to predict the House Price')
    sqft=st.number_input('Enter the area in Square Feet',min_value=100)
    bedroom=st.number_input('Enter the number of Bedrooms')
    Age=st.number_input('Enter the Age of House')
    slider=st.slider("Area",0,1000)
    st.radio
    prediction=Houseprice.predict([[sqft,bedroom,Age]])
    if st.button('Predict'):
        st.write(prediction)
