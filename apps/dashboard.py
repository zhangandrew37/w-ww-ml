import streamlit as st
from hydralit import HydraHeadApp
import global_
import pandas as pd
from datetime import date

class DashboardApp(HydraHeadApp):

    def __init__(self, title = 'Loader', delay=0, **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        self.delay = delay

    def run(self):

        try:
            example_data = open("Data-AI-1.csv")
            df = pd.read_csv(example_data)
            params = df.select_dtypes(['float', 'int']).columns
            st.title('Dashboard')
            algorithm = st.sidebar.selectbox('Select an Algorithm', ['Random Forest', 'Linear Regression', 'Logistic Regression', 'Decision Tree', 'SVM', 'Naïve Bayes', 'KNN', 'K-means'])

            col1, col2, col3 = st.columns(3)
            col1.text("Model Score")
            col1.info("89%")
            col2.text("Algorithm Selected")
            col2.info(algorithm)
            today = date.today()
            col3.text("Last Updated")
            col3.info(today)

            parameter = st.sidebar.selectbox('Select an Input Parameter', params)

            c1, c2 = st.columns(2)

            with c1:
                st.subheader(parameter)
                st.text("Maximum")
                st.info(df[parameter].max())
                st.text("Minimum")
                st.info(df[parameter].min())
                st.text("Mean")
                st.info(df[parameter].mean())
                st.text("Count")
                st.info(df[parameter].count())

            with c2:
                st.bar_chart(df[parameter])
                st.line_chart(df[parameter])
            #frequency


            ##st.subheader('Model Parameters')
            #st.write(rf.get_params())
      
        except Exception as e:
            st.image("./resources/failure.png",width=100,)
            st.error('An error has occurred. If you are not being redirected or if you encounter other issues, please use the navbar at the top to navigate through the app.')
            st.error('Error details: {}'.format(e))