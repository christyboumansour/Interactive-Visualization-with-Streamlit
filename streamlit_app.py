# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
df=pd.read_csv("COVID-19_in_bd.csv")

#theming
primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"

#put a title to the webpage
st.title('COVID-19 in Bangladesh between March-April 2020')

#About section
txt = st.text_area('About:', '''
    As the COVID-19 virus made its way worldwide, an opportunity to stop the spread of the virus during its early stages was missed.
    Let's take a look at how the virus progressed in its early stages during the months of March and April 2020 in Bangladesh and draw some conclusions!'
    ''')


#interaction 1 (button)
if st.button('Start exploring'):
    st.write('Lets go!')

#original code with some modifications
st.header("Line Graph")
fig = px.line(df, x="Date", y="Deaths",title='COVID-19 deaths cases in Bangladesh, between March-April 2020')

st.plotly_chart(fig, use_container_width=True)

st.header("3D Scatter Plot")
fig2 = px.scatter_3d(df, x='Date', y='Recovered', z='Confirmed',
              color='Deaths', title='Variation of Covid 19 confirmed, recovered and deaths cases in Bangladesh (March-April 2020)')

st.plotly_chart(fig2, use_container_width=True)

st.header("Scatter Plot")
fig3 = px.scatter(df, x="Date", y="Confirmed",
	         size="Deaths", color="Deaths", size_max=45, title='Increase of COVID-19 confirmed and deaths cases in Bangladesh, between March and April 2020')
st.plotly_chart(fig3)

st.header("Histogram")
fig4 = px.histogram(df, x="Date", y="Confirmed", title='Increase of COVID-19 confirmed cases in Bangladesh, between March-April 2020')
fig.update_layout(bargap=0.2)
st.plotly_chart(fig4)

st.header("Scatter With Slider")
fig5 = px.scatter(df, x="Confirmed", y="Recovered", animation_frame="Date",
           size="Deaths", size_max=55, range_x=[3,805], range_y=[3,45],title='Variation of COVID-19 recovered cases in Bangladesh as related to confirmed and deaths cases (March-April 2020)')

fig["layout"].pop("updatemenus")
st.plotly_chart(fig5)

#interaction 2: creating sidebar with streamlit allowing us to choose the desired visualization section
st.sidebar.title('Outline:')
st.sidebar.markdown("[Line Graph](#line-graph)")
st.sidebar.markdown('[3D Scatter Plot](#3d-scatter-plot)')
st.sidebar.markdown('[Scatter Plot](#scatter-plot)')
st.sidebar.markdown('[Histogram](#histogram)')
st.sidebar.markdown('[Scatter with slider](#scatter-with-slider)')

#interaction 3: radio button
change = st.radio(
    "Do you think COVID-19 cases increased in Bangladesh during the indicated timeframe?",
    ('Yes', 'No'))

if change == 'Yes':
    st.write('Correct!')
else:
    st.write("Try again.")
    


  

