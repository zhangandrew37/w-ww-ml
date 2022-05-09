import streamlit as st
from hydralit import HydraHeadApp
import global_
import pandas as pd
from sklearn.model_selection import train_test_split

class ModelSetupApp(HydraHeadApp):

    def __init__(self, title = 'Loader', delay=0, **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        self.delay = delay

    def run(self):

        try:
            st.title('Model Setup')
            example_data = open("Data-AI-1.csv")
            df = pd.read_csv(example_data)

            with st.sidebar.header('Set Parameters'):
                st.sidebar.write("Model Input")

            with st.sidebar.subheader('Learning Parameters'):
                parameter_n_estimators = st.sidebar.slider('Number of estimators (n_estimators)', 0, 1000, 100, 100)
                parameter_max_features = st.sidebar.select_slider('Max features (max_features)', options=['auto', 'sqrt', 'log2'])
                parameter_min_samples_split = st.sidebar.slider('Minimum number of samples required to split an internal node (min_samples_split)', 1, 10, 2, 1)
                parameter_min_samples_leaf = st.sidebar.slider('Minimum number of samples required to be at a leaf node (min_samples_leaf)', 1, 10, 2, 1)

            with st.sidebar.subheader('General Parameters'):
                parameter_random_state = st.sidebar.slider('Seed number (random_state)', 0, 1000, 42, 1)
                parameter_criterion = st.sidebar.select_slider('Performance measure (criterion)', options=['mse', 'mae'])
                parameter_bootstrap = st.sidebar.select_slider('Bootstrap samples when building trees (bootstrap)', options=[True, False])
                parameter_oob_score = st.sidebar.select_slider('Whether to use out-of-bag samples to estimate the R^2 on unseen data (oob_score)', options=[False, True])
                parameter_n_jobs = st.sidebar.select_slider('Number of jobs to run in parallel (n_jobs)', options=[1, -1])

            choice = st.selectbox("Select setup option", ["Split Data", "Data Scaling", "ML Algorithms"])

            if choice == "Split Data":
                split_size = st.slider('Data Split Ratio (% for Training Set)', 10, 90, 80, 5)
                st.markdown('**Data splits**')
                X = df.iloc[:,:-1] # Using all column except for the last column as X
                Y = df.iloc[:,-1] # Selecting the last column as Y
                # Data splitting
                X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=(100-split_size)/100)
                st.write('Training set')
                st.info(X_train.shape)
                st.write('Test set')
                st.info(X_test.shape)

                st.markdown('**Variable details**:')
                st.write('X variable')
                st.info(list(X.columns))
                st.write('Y variable')
                st.info(Y.name)
            elif choice == "Data Scaling":
                st.text("(Coming Soon)")
            elif choice == "ML Algorithms":
                algorithm = st.radio("Choose an algorithm for the model:", ('Random Forest', 'Linear Regression', 'Logistic Regression', 'Decision Tree', 'SVM', 'Naïve Bayes', 'KNN', 'K-means'))
                st.write("You chose: " + algorithm)

      
        except Exception as e:
            st.image("./resources/failure.png",width=100,)
            st.error('An error has occurred. If you are not being redirected or if you encounter other issues, please use the navbar at the top to navigate through the app.')
            st.error('Error details: {}'.format(e))