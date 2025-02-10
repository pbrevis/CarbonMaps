# Import libraries
import streamlit as st
import pandas as pd
from PIL import Image

# PAGE CONFIGURATION =========================================================
ic = Image.open(r'Images/bar-chart-icon.png')
st.set_page_config(layout="wide", page_icon=ic,
                   page_title="Carbono Orgánico del Suelo")

# READING INPUT FILES ========================================================
region_list = pd.read_csv('region_list.csv')
province_list = pd.read_csv('province_list.csv')
county_list = pd.read_csv('county_list.csv')

# STREAMLIT PAGE =============================================================

# Main page heading
st.header('Visualice el Carbono Orgánico del Suelo')
    
# Sidebar menus
st.sidebar.title("Escoja un nivel administrativo")

districts = ['Región', 'Provincia', 'Comuna']

slctd_district = st.sidebar.radio("", districts, index= None, label_visibility= "collapsed")

# Page body
if slctd_district == None:
    st.markdown("#### <- Haga su selección para comenzar")

elif slctd_district == 'Región':
    chosen_region = st.sidebar.selectbox("", region_list["REGION"], index= None,
                                         placeholder="Seleccione una región",
                                         label_visibility= "collapsed")
    if chosen_region == None:
        st.markdown("#### <- Seleccione la región a mapear")
    else:
        st.image(f"Region_CarbonMaps/{chosen_region}.png")

        col1, col2, col3 = st.columns(3)
        with col1: st.markdown("")
        with col2: st.markdown("")
        with col3:
            with open(f"Region_CarbonMaps/{chosen_region}.png", "rb") as file:
                btn = st.download_button(
                    label="Bajar imagen en formato PNG",
                    data=file,
                    file_name=f"{chosen_region}.png",
                    mime="image/png")


elif slctd_district == 'Provincia':
    chosen_province = st.sidebar.selectbox("", province_list["PROVINCIA"], index=None,
                                           placeholder="Seleccione una provincia",
                                           label_visibility= "collapsed")
    
    if chosen_province == None:
        st.markdown("#### <- Seleccione la provincia a mapear")
    
    else:
        st.image(f"Province_CarbonMaps/{chosen_province}.png")

        col1, col2, col3 = st.columns(3)
        with col1: st.markdown("")
        with col2: st.markdown("")
        with col3:
            with open(f"Province_CarbonMaps/{chosen_province}.png", "rb") as file:
                btn = st.download_button(
                    label="Bajar imagen en formato PNG",
                    data=file,
                    file_name=f"{chosen_province}.png",
                    mime="image/png")


else:
    chosen_county = st.sidebar.selectbox("", county_list["COMUNA"], index=None,
                                         placeholder="Seleccione una comuna",
                                         label_visibility= "collapsed")

    if chosen_county == None:
        st.markdown("#### <- Seleccione la comuna a mapear")

    else:
        st.image(f"County_CarbonMaps/{chosen_county}.png")

        col1, col2, col3 = st.columns(3)
        with col1: st.markdown("")
        with col2: st.markdown("")
        with col3:
            with open(f"County_CarbonMaps/{chosen_county}.png", "rb") as file:
                btn = st.download_button(
                    label="Bajar imagen en formato PNG",
                    data=file,
                    file_name=f"{chosen_county}.png",
                    mime="image/png")

          
# Sidebar credits
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.markdown("Web app creada por  \nPatricio Brevis (2024)  \ncon datos"
                    " del Global Soil Organic Carbon Map (GSOCmap v1.5) de la FAO.")
