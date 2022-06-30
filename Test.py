from time import process_time
import streamlit as st
from streamlit_option_menu import option_menu
from load_image import load_image
import numpy as np
from PIL import Image
import cv2
from tensorflow.keras.models import load_model

def streamlit_menu():
    selected = option_menu(
        menu_title=None, 
        options=["Home", "Project","Team","Future","Demo"],  
        icons=["house", "book","people", "pen","search"], 
        menu_icon="cast",  
        default_index=0,  
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "20px"},
            "nav-link": {
                   "font-size": "20px",
                   "color": "black",
                   "text-align": "left",
                   "margin": "0px",
                   "--hover-color": "#eee",
                   },
                   "nav-link-selected": {"background-color": "green"},
                   },
                   )
    return selected


selected = streamlit_menu()

if selected == "Home":
    st.title(f"Banana leaves diseases detection using CNN")
    st.image("https://p1.pxfuel.com/preview/176/296/904/dji-uav-plant-protection-drone-farmland-agriculture-plant-protection.jpg",use_column_width='always')


    
if selected == "Project":
    st.title(f"About this project")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Introduction")
        st.write('Agriculture playing a big role', ' in sustainable development goals', 'especially in no poverty, zero hunger and  good health and well-being')
        
        
    with col2:
        st.subheader("Problem")
        
    with col3:
        st.subheader("Solution")
        #st.image("")




if selected == "Team":
    st.title(f"Person behind this project")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Marie-Ritha")
        st.image("https://avatars.githubusercontent.com/u/71000965?v=4",use_column_width='always')
    with col2:
        st.header("Savanna")
        st.image("https://mail.google.com/mail/u/0?ui=2&ik=ed41038630&attid=0.1&permmsgid=msg-f:1731973978323104800&th=180935282a2b3420&view=att&disp=safe&realattid=f_l2p2eoxn0",use_column_width='always')
  
     
if selected == "Future":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Spray medicine")
        st.image("https://previews.123rf.com/images/akinina/akinina2004/akinina200400034/144110759-drone-spraying-agent-on-crops-linear-icon-of-fertilizer-disinfection-watering-irrigation-from-air-bl.jpg",use_column_width='always')
    with col2:
        st.header("Alert the farmer")
        st.image("https://media.istockphoto.com/vectors/hand-holding-mobile-phone-with-new-email-icon-vector-illustration-vector-id1256767138?k=20&m=1256767138&s=612x612&w=0&h=CCNflxf6O4nT2g2vYyAljOaNGTJBXpvPj6t4bQhfh44=",use_column_width='always')
    with col3:
        st.header("Other factors on banana")
        st.image("https://thumbs.dreamstime.com/b/planting-solid-icon-sprout-care-vector-illustration-isolated-white-soil-humidity-glyph-style-design-designed-web-app-138064460.jpg", use_column_width='always')



if selected == "Demo":
    st.header("Test our model here")
    img_file=st.file_uploader('upload your image here', accept_multiple_files=False, type=['.jpg','.png'])
   
    if img_file is not None:
        show_img = st.image(load_image(img_file),use_column_width='always')
        
        submit=st.button('Classify')
        if submit:
            img = Image.open(img_file)
            x = np.array(img)/255
            #y = cv2.resize(x, dsize=(128,128))
            
            #x=np.expand_dims(x, axis=0)
            #y=x/255
            #y = cv2.resize(x,dsize=(128,128))     
            #y = x.reshape(1,224,224,3)
            
            model = load_model('model.h5')
            prediction=model.predict(x)  
                     

