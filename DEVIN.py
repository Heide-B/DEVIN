import streamlit as st
import pandas as pd
import numpy as np
import base64
import matplotlib.pyplot as plt
import geopandas as gpd
import os

st.set_page_config(layout="wide")


virus = pd.read_csv("https://raw.githubusercontent.com/Heide-B/RNA-Virus-Clustering/main/Streamlit/Virus_Data.csv")
regions = pd.read_csv("https://raw.githubusercontent.com/Heide-B/RNA-Virus-Clustering/main/Streamlit/Region_Data.csv")
regions = gpd.GeoDataFrame(regions)

main_bg = "Streamlit/bg1.png"
main_bg_ext = "png"
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True)

def write_recoms(region, ttype):
    path = 'Streamlit/recomms/'
    region_s = regions[regions['AREA']==region]['Recom_Clusters'].iloc[0]
    
    for i in os.listdir(path):
        x = i.split('.')[0]
        if i.startswith(str(region_s)) and x.endswith(ttype):
            text = os.path.join(path,i)
            file = open(text,'r').read()  
            st.write(file)

def images(reg_clu):
    path = 'Streamlit/'    
    for i in os.listdir(path):
        if i.startswith(str(reg_clu)) and i.endswith('png'):
            files = os.path.join(path,i)
            col1.image(files)
            
def icons(ic):
    path = 'Streamlit/Risk/'
    icc = regions[regions['AREA']==ic]['vulneb_labels'].iloc[0]
    for i in os.listdir(path):
        if i.startswith(str(icc)) and i.endswith('png'):
            files = os.path.join(path,i)
            col2.image(files)


st.image('Streamlit/DEVIN.png')
st.header("Focused Preparation Leads to Effective Preventions")
st.write('The next pandemic is not a question of if, but when. It is our responsibility to equip ourselves with the right information to better our prevention and mitigation efforts. DEVIN is a simple dashboard that aims to provide a guide on how each Philippine region can prepare for this pandemic.')

my_expander = st.beta_expander('A simple guide to DEVIN')
my_expander.write('Hello there!')
prez = '[Check the presentation here!](https://docs.google.com/presentation/d/e/2PACX-1vS5YdweotyAsrIFa2YeWF-gQsLLgKe4vLk1tysDVDP56qoMTH2qmmmJ_HekSMtrO9nd7SeLw0YcU3ww/pub?start=false&loop=false&delayms=5000)'
x = my_expander.markdown(prez, unsafe_allow_html=True)


col1, col2 = st.beta_columns((2, 1))

col1.header("Map of Regions")

col2.header("User Input")
reg_choices = ['']

for index, value in enumerate(regions['AREA']):
    reg_choices.append(value)
selected_region = col2.selectbox('Select a Region',reg_choices)
if selected_region != '':
    icons(selected_region)
    col2.write('Region Vulnerability: ' + str(regions[regions['AREA']==selected_region]['vulneb_labels'].iloc[0]))
    col2.write('Doctors (per 10k pop): ' + str(regions[regions['AREA']==selected_region]['Doctors'].iloc[0]))
    col2.write('Nurses (per 10k pop): ' + str(regions[regions['AREA']==selected_region]['Nurses'].iloc[0]))
    col2.write('Beds (per 10k pop): ' + str(regions[regions['AREA']==selected_region]['Beds'].iloc[0]))
    col2.write('Population Density: ' + str(regions[regions['AREA']==selected_region]['Pop Density'].iloc[0]))
else:
    col2.write('Select a region to view its data and recommendations!')

if selected_region != '':
    regim = regions[regions['AREA']==selected_region]['Recom_Clusters'].iloc[0]
    images(regim)
else:
    col1.image('Streamlit/Original.png')

if selected_region != '':
    st.header('DEVIN Recommended Interventions for ' + selected_region)
    st.subheader('For the Individual')
    write_recoms(selected_region, 'indiv')
    st.subheader('For Communities')
    write_recoms(selected_region, 'work')
    st.subheader('For Healthcare Systems')
    write_recoms(selected_region, 'health')
else:
    st.write('')

st.subheader('')
st.subheader('Thank you for visiting DEVIN!')
expander = st.beta_expander('This project would not be possible without these wonderful people')
expander.write('Gino Asuncion - Mentor')
expander.write('[Justin Benedict Balcera - Brother / Domain Expert](https://www.linkedin.com/in/jblbalcera/)',unsafe_allow_html=True)
expander.write('Eskwelabs Data Science Team')
expander.markdown('[Heide Mae Balcera - Project Owner and Developer](https://www.linkedin.com/in/heidemae-balcera-sci/)',unsafe_allow_html=True)
