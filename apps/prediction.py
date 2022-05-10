import streamlit as st
from hydralit import HydraHeadApp
import global_
import pandas as pd

class PredictionApp(HydraHeadApp):

    def __init__(self, title = 'Loader', delay=0, **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        self.delay = delay

    def run(self):

        try:
            example_data = open("Data-AI-1.csv")
            df = pd.read_csv(example_data)
            dict = {}
            st.title('Prediction')
            inputs = df.select_dtypes(['float', 'int']).columns
            with st.form(key = "create", clear_on_submit=False):
                output = st.selectbox("Select Prediction (output) Parameter", inputs, index=len(inputs)-1)
                st.markdown("**Please enter your input values**")
                for p in inputs:
                    if p == output:
                        continue
                    input = st.text_input(p)
                    dict[p] = input
                submit = st.form_submit_button(label= "Predict")
            if (submit):
                st.markdown("**Predicted Value: **")
                st.write("TN")
                st.info("1.9500")
                st.json(dict)
                st.markdown("**New Dataset:**")
                df.append(dict, ignore_index=True)
                st.bar_chart(df)
                st.line_chart(df)
                st.area_chart(df)
                dict.clear()
                #display in chart format

      
        except Exception as e:
            st.image("./resources/failure.png",width=100,)
            st.error('An error has occurred. If you are not being redirected or if you encounter similar issues, please use the navbar at the top to navigate through the app.')
            st.error('Error details: {}'.format(e))