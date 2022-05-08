from apps.cheat_app import CheatApp
import streamlit as st
from hydralit import HydraHeadApp
import global_
import apps
from apps import cheat_app

class ProjectSetupApp(HydraHeadApp):

    def __init__(self, title = 'Loader', delay=0, **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        self.delay = delay

    def run(self):

        try:
            st.title('Create an ML project')
            with st.form(key = "create", clear_on_submit=False):
                # name_ = state["name"] if "name" in state else ""
                # possibly implement state later
                name = st.text_input(label = "Enter the model name")
                # set value = name_ if using state
                
                type = st.selectbox("Type of ML modeling", ('Regression', 'Classification'))
                global_.type = type

                df = st.file_uploader("Upload your data (CSV)")
                submit = st.form_submit_button(label= "Create Project")
                if (submit):
                    st.write("If you are not being redirected or if you encounter other issues, please use the navbar at the top to navigate through the app.")

      
        except Exception as e:
            st.image("./resources/failure.png",width=100,)
            st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
            st.error('Error details: {}'.format(e))