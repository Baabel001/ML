import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import time
import pandas as pd

from dataloader import data
from preprocessing import final_data



st.set_page_config(page_title='Machine leanring',  layout='wide', page_icon=':ambulance:')

with st.spinner('Information about variable'):
    
    variable = st.selectbox('Choose variable', data.columns, help = 'Filter report to show information about one variable') 
    m1, m2, m3, m4, m5 = st.columns((1,1,1,1,1))
    
    m1.write('')
    # m1.metric(label="Type", value=type(data[variable].iloc[0]))
    m2.metric(label="Mean", value=round(data[variable].mean(), 2))
    m3.metric(label="std", value=round(data[variable].std(), 2))
    m4.metric(label="min", value=round(data[variable].min(), 2))
    m5.metric(label="max", value=round(data[variable].max(), 2))
    # m5.write('')
    
with st.expander('Working data before data preprocessing'):
    #cw1, cw2 = st.columns((2.5, 1.7))
    
    fig = go.Figure(
            data = [go.Table (
                header = dict(
                 values = list(data.columns),
                 font=dict(size=10, color = 'white'),
                 fill_color = '#264653',
                 align = 'center',
                 height=20
                 )
              , cells = dict(
                  values = [data[K].tolist() for K in data.columns], 
                  font=dict(size=10),
                  align = 'right',
                  fill_color='#F0F2F6',
                  height=20))]) 
        
    fig.update_layout(title_text="Working data before preprocessing",title_font_color = '#264653',title_x=0,margin= dict(l=0,r=10,b=10,t=30), height=480)
        
    # cw2.plotly_chart(fig, use_container_width=True)
    st.plotly_chart(fig, use_container_width=True)
    
with st.spinner('Report updated!'):  

    if variable != "Y":
        fig = px.histogram(data, x=variable)

        fig.update_layout(title_text="Histogram of "+variable, title_font_color = '#264653', title_x=0, margin = dict(l=0,r=10,b=10,t=30), height=480)
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        c1, c2 = st.columns((1, 1))
         
        fig = px.box(data, y=variable, points="all")
        fig.update_layout(title_text="Box Plot of "+variable, title_font_color = '#264653', title_x=0, margin = dict(l=0,r=10,b=10,t=30), height=480)
        c1.plotly_chart(fig, use_container_width=True)
        
        fig = px.histogram(data, x=variable)
        fig.update_layout(title_text="Histogram of "+variable, title_font_color = '#264653', title_x=0, margin = dict(l=0,r=10,b=10,t=30), height=480)
        c2.plotly_chart(fig, use_container_width=True)

with st.expander("Contact us"):
    with st.form(key='contact', clear_on_submit=True):
        
        email = st.text_input('charles.thiam14@gmail.com')
        st.text_area("Query","Please fill in all the information about your request")  
        
        submit_button = st.form_submit_button(label='Send Information')