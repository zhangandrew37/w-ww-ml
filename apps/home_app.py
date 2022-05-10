import os
import streamlit as st
from hydralit import HydraHeadApp

MENU_LAYOUT = [1,1,1,7,2]

class HomeApp(HydraHeadApp):


    def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

    def run(self):

        try:
            st.markdown("<h1 style='text-align: center; black: red;'>ML Web App</h1>", unsafe_allow_html=True)
            col_header_logo_left_far, col_header_logo_left,col_header_text,col_header_logo_right,col_header_logo_right_far = st.columns([1,2,2,2,1])

            _,_,col_logo, col_text,_ = st.columns(MENU_LAYOUT)
            col_logo.image(os.path.join(".","resources","ml.png"),width=80,)
            col_text.subheader("A simple no-code machine tool designed for professionals.")
            st.markdown('<br><br>',unsafe_allow_html=True)

            _,_,col_logo, col_text,col_btn = st.columns(MENU_LAYOUT)
            col_logo.image(os.path.join(".","resources","classroom.png"),width=50,)
            col_text.info("Simple interface - No prior coding experience required to use this application.")

            _,_,col_logo, col_text,col_btn = st.columns(MENU_LAYOUT)                
            col_logo.image(os.path.join(".","resources","denoise.png"),width=50,)
            col_text.info("Easily verify input data quality, delete or fill data if needed in order to meet the ML model requirements.")

            _,_,col_logo, col_text,col_btn = st.columns(MENU_LAYOUT)
            col_logo.image(os.path.join(".","resources","satellite.png"),width=50,)
            col_text.info("Integrates almost all commonly used open source ML algorithms.")

            _,_,col_logo, col_text,col_btn = st.columns(MENU_LAYOUT)
            col_logo.image(os.path.join(".","resources","belgium.png"),width=50,)
            col_text.info("Easily build ML project template cases for various applications")

        
        except Exception as e:
            st.image(os.path.join(".","resources","failure.png"),width=100,)
            st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
            st.error('Error details: {}'.format(e))





