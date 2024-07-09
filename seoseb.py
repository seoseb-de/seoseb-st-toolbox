#####
#
# base app for collecting my seo tools
#
####

import streamlit as st

###########################################
# page config - must be first st command! #
###########################################

st.set_page_config(
    page_title='Seoseb - Toolbox',
    page_icon='https://www.seoseb.de/artikel/media/files/favicon-16.png',
    layout='centered',
    initial_sidebar_state='expanded'
)

with st.sidebar:
    
    st.title('Sidebar Stuff')
    st.caption('Work in progress…')
    st.markdown('_fiddled by [seoseb](https://www.seoseb.de) | [@seoseb](https://seocommunity.social/@seoseb)_')

#############
# variables #
#############



##################
# layout the app #
##################

st.title('![@seoseb](https://www.seoseb.de/img/seoseb_icon_x48.png) Seoseb SEO Tools')
st.markdown('Here I will collect my Streamlit apps for SEO use in one place')

with st.container():

    col_1, col_2 = st.columns(2, gap='large')

    with col_1:
        st.subheader('CLS Element Extractor')
        st.image('cls-extractor-screen.png', use_column_width=True, caption='Check which elements are shifted during page load.')
        st.markdown('This app lets you upload CLS error reports from your Google Search Console property and checks the Pagespeed API for the elements that get shiftet on the URLs.')
        st.page_link('pages/01_⚡_get-CLS-Elements.py', label = 'CLS Elements Extractor ', icon = '⚡' )
        
    with col_2:
        st.subheader('Campixx 2024 Demo')
        st.image('seoseb-campixx2024-streamlit-demo-app.png', use_column_width=True, caption='Show some usecases for Streamlit in SEOs daily work.')
        st.markdown('This app was build for demonstration purposes during my Campixx 2024 talk on Streamlit and SEO usecases.')
        st.page_link('https://campixx2024.streamlit.app', label = 'Campixx 2024 - Demo App ', icon = '🎈' )

    st.info('further tools will be added')
    st.divider()

with st.container():
    
    st.markdown('I also do other things. Maybe you want to head over to my website 🇩🇪')
    st.markdown('''
    - [Xpath für SEO](https://www.seoseb.de/artikel/texte/xpath-fur-seo-ein-einstieg)
    - [Sitemap Monitor mit GSheets & DataStudio](https://www.seoseb.de/artikel/texte/sitemap-monitor-mit-google-apps-script-data-studio)
    - [Page Speed Monitoring mit GSheets](https://www.seoseb.de/artikel/texte/pagespeed-monitoring-mit-der-psi-api)
    ''')

##########
# footer #
##########

st.markdown('---')
