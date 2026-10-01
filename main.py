import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
from database.database import create , fill , display
import pandas as pd
from datetime import date

st.set_page_config(page_title="Broken Fracture Classification")
st.title("Bone Fracture Classification System")
st.info("v1.0")

create()

@st.cache_resource
def load_model():
    return tf.keras.models.load_model('model/bone_break_classifier.keras')

model = load_model()

co1, co2, co3 = st.columns(3)
with co1:
    first_name = st.text_input("First name")
with co2:
    second_name = st.text_input("Second name")
with co3:
    age = st.number_input("Age",min_value=0,max_value=120,step=1)

date = st.date_input("Date",max_value=date.today())

upload = st.file_uploader("choose an image",type=['jpg', 'jpeg', 'png'])

if upload:
    image = Image.open(upload).convert("RGB")
    st.image(image,caption="uploaded image")
    if st.button("Predict"):
        image_resized = image.resize((240,240))
        image_array = np.array(image_resized)
        image_array = np.expand_dims(image_array,axis=0)
        prediction = model.predict(image_array,verbose=False)[0]
        prediction_class = np.argmax(prediction)
        confidence = prediction[prediction_class]
        classes = ['fractured', 'not fractured']
        st.success(f"predicted class : {classes[prediction_class]}")
        st.info(f"confidence : {confidence * 100:.2f}%")

        prediction_label = classes[prediction_class]
        conf = f"{confidence * 100:.2f}%"

        fill(first_name,second_name,age,date,conf,prediction_label)

with st.sidebar:
    st.title("System History")
    data = display()
    if data:
        df = pd.DataFrame(data,columns=["ID","First Name","Second Name","Age","Date","Confidence","Prediction"])
        df = df[["ID", "First Name", "Age", "Date", "Confidence", "Prediction"]]
        st.dataframe(df,hide_index=True,use_container_width=True)

st.markdown("---")
st.markdown(
    "<small>Note: This system is designed to assist with preliminary screening only, "
    "It is not intended to provide a definitive diagnosis or replace professional medical advice</small>",
    unsafe_allow_html=True
)