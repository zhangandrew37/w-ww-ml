from hydralit import HydraApp
import hydralit_components as hc
import apps
import streamlit as st

#Only need to set these here as we are add controls outside of Hydralit, to customise a run Hydralit!
st.set_page_config(page_title='Secure Hydralit Data Explorer',page_icon="⚙️",layout='wide',initial_sidebar_state='auto',)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)

if __name__ == '__main__':

    over_theme = {'txc_inactive': '#FFFFFF'}
    app = HydraApp(
        title='ML Web App',
        favicon="⚙️",
        hide_streamlit_markers=True,
        use_navbar=True, 
        navbar_sticky=False,
        navbar_animation=True,
        navbar_theme=over_theme
    )

    app.add_app("Home", icon="🏠", app=apps.HomeApp(title='Home'),is_home=True)

    app.add_app("Project Setup", icon="", app=apps.ProjectSetupApp(title="Project Setup"))
    app.add_app("Data", icon="", app=apps.DataApp(title="Data"))
    app.add_app("Model Setup", icon="", app=apps.ModelSetupApp(title="Model Setup"))
    app.add_app("Training", icon="", app=apps.TrainingApp(title="Training"))
    app.add_app("Prediction", icon="", app=apps.PredictionApp(title="Prediction"))
    app.add_app("Dashboard", icon="", app=apps.DashboardApp(title="Dashboard"))

    #we have added a sign-up app to demonstrate the ability to run an unsecure app
    #only 1 unsecure app is allowed
    app.add_app("Signup", icon="🛰️", app=apps.SignUpApp(title='Signup'), is_unsecure=True)

    #we want to have secure access for this HydraApp, so we provide a login application
    #optional logout label, can be blank for something nicer!
    app.add_app("Login", apps.LoginApp(title='Login'),is_login=True) 

    #we can inject a method to be called everytime a user logs out
    #---------------------------------------------------------------------
    # @app.logout_callback
    # def mylogout_cb():
    #     print('I was called from Hydralit at logout!')
    #---------------------------------------------------------------------

    #we can inject a method to be called everytime a user logs in
    #---------------------------------------------------------------------
    # @app.login_callback
    # def mylogin_cb():
    #     print('I was called from Hydralit at login!')
    #---------------------------------------------------------------------

    #if we want to auto login a guest but still have a secure app, we can assign a guest account and go straight in
    app.enable_guest_access()

    #check user access level to determine what should be shown on the menu
    user_access_level, username = app.check_access()

    # If the menu is cluttered, just rearrange it into sections!
    # completely optional, but if you have too many entries, you can make it nicer by using accordian menus
    if user_access_level > 1:
        complex_nav = {
            'Home': ['Home'],
            'Project Setup': ['Project Setup'],
            'Data': ['Data'],
            'Model Setup': ['Model Setup'],
            'Training': ['Training'],
            'Prediction': ['Prediction'],
            'Dashboard': ['Dashboard'],
        }
    elif user_access_level == 1:
        complex_nav = {
            'Home': ['Home'],
            'Project Setup': ['Project Setup'],
            'Data': ['Data'],
            'Model Setup': ['Model Setup'],
            'Training': ['Training'],
            'Prediction': ['Prediction'],
            'Dashboard': ['Dashboard'],
        }
    else:
        complex_nav = {
            'Home': ['Home'],
        }

  
    #and finally just the entire app and all the children.
    app.run(complex_nav)


    #print user movements and current login details used by Hydralit
    #---------------------------------------------------------------------
    # user_access_level, username = app.check_access()
    # prev_app, curr_app = app.get_nav_transition()
    # print(prev_app,'- >', curr_app)
    # print(int(user_access_level),'- >', username)
    # print('Other Nav after: ',app.session_state.other_nav_app)
    #---------------------------------------------------------------------

