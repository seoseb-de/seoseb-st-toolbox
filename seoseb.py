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
    initial_sidebar_state='auto'
)

#############
# variables #
#############


st.header('Seoseb SEO Tools')
st.text('Work in progress - apps for SEO use in one place')

st.markdown('[PageSpeeedInsights API - CLS elements extractor](https://seoseb-de-cls-elements-extractor-psi-api-fhczvb.streamlit.app/)')

st.markdown('---')

##########
# footer #
##########

st.markdown('---')
st.markdown('_fiddled by [seoseb](https://www.seoseb.de) | [@seoseb](https://twitter.com/seoseb)_')
