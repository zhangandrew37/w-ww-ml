from apps.cheat_app import CheatApp
import streamlit as st
from hydralit import HydraHeadApp
import global_
import pickle as pkle
import os.path
import pandas as pd
import seaborn as sb
#from dataprep.eda import create_report
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

class DataApp(HydraHeadApp):

    def __init__(self, title = 'Loader', delay=0, **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        self.delay = delay

    def run(self):

        try:
            example_data = open("Data-AI-1.csv")
            df = pd.read_csv(example_data)

            # def generate_report():
            #         left, right = st.columns(2)
            #         with left:
            #             if st.button('View detailed report in new tab'):
            #                 report = create_report(df)
            #                 report.show_browser()
            #         with right:
            #             if st.button('Download detailed report'):
            #                     report = create_report(df)
            #                     report.save('Report')
            #                     report.show_browser()

            # def generate_plot():
            #     numeric_columns = df.select_dtypes(['float', 'int']).columns
            #     st.sidebar.subheader("Scatter Plot Setup")
            #     select_box1 = st.sidebar.selectbox(label='X axis', options=numeric_columns)
            #     select_box2 = st.sidebar.selectbox(label='Y axis', options=numeric_columns)
            #     g = sb.relplot(x=select_box1, y=select_box2, data=df, height=5, aspect=15.7/8.27)
            #     st.pyplot()
            
            from global_ import type
            st.title('Data Pre-processing')

            # create a button in the side bar that will move to the next page/radio button choice
            next = st.sidebar.button('Next on list')

            # will use this list and next button to increment page, MUST BE in the SAME order
            # as the list passed to the radio button
            new_choice = ['Customize Input Fields','Quality Check','Data Manipulation','Data Visualization']

            # This is what makes this work, check directory for a pickled file that contains
            # the index of the page you want displayed, if it exists, then you pick up where the
            #previous run through of your Streamlit Script left off,
            # if it's the first go it's just set to 0
            if os.path.isfile('next.p'):
                next_clicked = pkle.load(open('next.p', 'rb'))
                # check if you are at the end of the list of pages
                if next_clicked == len(new_choice):
                    next_clicked = 0 # go back to the beginning i.e. homepage
            else:
                next_clicked = 0 #the start

            # this is the second tricky bit, check to see if the person has clicked the
            # next button and increment our index tracker (next_clicked)
            if next:
                #increment value to get to the next page
                next_clicked = next_clicked +1

                # check if you are at the end of the list of pages again
                if next_clicked == len(new_choice):
                    next_clicked = 0 # go back to the beginning i.e. homepage

            choice = st.sidebar.radio("go to",('Customize Input Fields','Quality Check', 'Data Manipulation', 'Data Visualization'), index=next_clicked)

            # pickle the index associated with the value, to keep track if the radio button has been used
            pkle.dump(new_choice.index(choice), open('next.p', 'wb'))

            if choice == 'Customize Input Fields':
                with st.form(key = "create", clear_on_submit=False):
                    st.subheader("Customize Input Fields")
                    numeric_columns = df.select_dtypes(['float', 'int']).columns
                    choices = st.multiselect("Options", options=numeric_columns)
                    save = st.form_submit_button("Save Changes")
                    st.progress(2)

            elif choice == 'Quality Check':
                data_choice = st.selectbox("Data Quality Check", ["Data Preview", "Check Null Data", "Statistical Analysis"])
                if data_choice == 'Statistical Analysis':
                    with st.sidebar.header('Set Parameters'):
                        split_size = st.sidebar.slider('Data split ratio (% for Training Set)', 10, 90, 80, 5)

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

                    X = df.iloc[:,:-1] # Using all columns except for the last column as X
                    Y = df.iloc[:,-1] # Selecting the last column as Y

                    # Data splitting
                    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=(100-split_size)/100)

                    rf = RandomForestRegressor(n_estimators=parameter_n_estimators,
                    random_state=parameter_random_state,
                    max_features=parameter_max_features,
                    criterion=parameter_criterion,
                    min_samples_split=parameter_min_samples_split,
                    min_samples_leaf=parameter_min_samples_leaf,
                    bootstrap=parameter_bootstrap,
                    oob_score=parameter_oob_score,
                    n_jobs=parameter_n_jobs)

                    rf.fit(X_train, Y_train)
                    score = rf.score(X_train, Y_train)
                    st.write('Prediction Performance Score:')
                    st.write(score)

                    st.subheader('1. Model Performance')

                    st.markdown('**1.1. Training set**')
                    Y_pred_train = rf.predict(X_train)
                    st.write('Coefficient of determination ($R^2$):')
                    st.info( r2_score(Y_train, Y_pred_train) )

                    st.write('Error (MSE or MAE):')
                    st.info( mean_squared_error(Y_train, Y_pred_train) )

                    st.markdown('**1.2. Test set**')
                    Y_pred_test = rf.predict(X_test)
                    st.write('Coefficient of determination ($R^2$):')
                    st.info( r2_score(Y_test, Y_pred_test) )

                    st.write('Error (MSE or MAE):')
                    st.info( mean_squared_error(Y_test, Y_pred_test) )

                    st.subheader('2. Model Parameters')
                    st.write(rf.get_params())

                elif data_choice == 'Check Null Data':
                    nulls = df.isnull().sum().to_frame()
                    for index, row in nulls.iterrows():
                        st.markdown(index)
                        st.code(row[0])

                elif data_choice == 'Data Preview':
                    #generate_report()
                    st.write(df)

                st.progress(3)

            elif choice == 'Data Manipulation':
                st.subheader('Data Manipulation')
                st.text('(Coming Soon)')
                st.write(df)
                st.progress(4)
            elif choice == 'Data Visualization':
                st.subheader('Data Visualization')
                st.warning('Feature not yet available on the web hosted version of this app. Please run locally using the [source code](https://github.com/zhangandrew37/w-ww) for full features.')
                #generate_report()
                #generate_plot()
                st.progress(5)

      
        except Exception as e:
            st.image("./resources/failure.png",width=100,)
            st.error('An error has occurred. If you are not being redirected or if you encounter other issues, please use the navbar at the top to navigate through the app.')
            st.error('Error details: {}'.format(e))