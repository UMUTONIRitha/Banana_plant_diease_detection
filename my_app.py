import streamlit as st
import requests
#SIDEBAR_OPTIONS =[]

img_file=st.file_uploader('upload your image here', accept_multiple_files=True, type=['.jpg','.png'])
#if img_file:
 #   response=requests.get('https://smartphone.edgeimpulse.com/classifier.html',img_file)
