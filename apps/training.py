import streamlit as st
from hydralit import HydraHeadApp
import global_

class TrainingApp(HydraHeadApp):

    def __init__(self, title = 'Loader', delay=0, **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        self.delay = delay

    def run(self):

        try:
            algo_choice = st.selectbox("Algorithm", ['Random Forest', 'Linear Regression', 'Logistic Regression', 'Decision Tree', 'SVM', 'Naïve Bayes', 'KNN', 'K-means'])
            st.title('Training')
            st.markdown("**Training set**")
            col1, col2 = st.columns(2)
            col1.text("Coefficient of determination (R^2)")
            col1.info("0.7565002320512857")
            col2.text("Error (MSE)")
            col2.info("14.720181896908045")
            st.markdown("**Test set**")
            col1, col2 = st.columns(2)
            col1.text("Coefficient of determination (R^2)")
            col1.info("0.3707331235426088")
            col2.text("Error (MSE)")
            col2.info("41.100604421093976")
            st.write("")
            st.write("")
            st.markdown("**Compare with other algorithms:**")
            st.write("")
            col1, col2 = st.columns(2)
            with col1:
                img = Image.open("assets/images/lazypredict.png")
                st.image(img, width=500)
            with col2:
                img = Image.open("assets/images/lazyplot.png")
                st.image(img, width=800)
            

      
        except Exception as e:
            st.image("./resources/failure.png",width=100,)
            st.error('An error has occurred. If you are not being redirected or if you encounter other issues, please use the navbar at the top to navigate through the app.')
            st.error('Error details: {}'.format(e))