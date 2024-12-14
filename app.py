import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import time

from dataloader import data



st.set_page_config(page_title='Machine leanring',  layout='wide', page_icon=':ambulance:')


with st.spinner('Updating Report...'):
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
    time.sleep(1)   

with st.expander("Description of data"):
    
    describe = data.describe()
    
    fig = go.Figure(
            data = [go.Table (
                header = dict(
                 values = list(describe.columns),
                 font=dict(size=10, color = 'white'),
                 fill_color = '#264653',
                 align = 'center',
                 height=20
                 )
              , cells = dict(
                  values = [describe[K].tolist() for K in describe.columns], 
                  font=dict(size=10),
                  align = 'right',
                  fill_color='#F0F2F6',
                  height=20))]) 
        
    fig.update_layout(title_text="Description of variables",title_font_color = '#264653',title_x=0,margin= dict(l=0,r=10,b=10,t=30), height=480)
        
    # cw2.plotly_chart(fig, use_container_width=True)
    st.plotly_chart(fig, use_container_width=True)   

with st.expander("Contact us"):
    with st.form(key='contact', clear_on_submit=True):
        
        email = st.text_input('charles.thiam14@gmail.com')
        st.text_area("Query","Please fill in all the information about your request")  
        
        submit_button = st.form_submit_button(label='Send Information')