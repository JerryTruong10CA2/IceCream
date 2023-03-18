import streamlit as st
import pickle
filename = 'IceCreamData.pickle'
model = pickle.load(open(filename, "rb"))
st.title('Revenue Prediction')
a = st.number_input('Input Temperature')
if st.button('Predict'):
    y_pred = model.predict(np.array([a]).reshape(-1,1))
    st.caption('Revenue Prediction')
    st.write(y_pred)
