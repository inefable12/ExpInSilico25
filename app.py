import streamlit as st
import pandas as pd
import pip
pip.main(["install", "openpyxl"])
#from openpyxl import reader,load_workbook,Workbook
import numpy as np
from PIL import Image

##############
st.sidebar.image("img/water1.png",
                 caption="Si lo puedes imaginar, lo puedes programar")

#############################Pagina 1##############################    
def Home():
    st.markdown("# Temario")
    st.sidebar.markdown("# Exploración In Silico")

    total1, total2 = st.columns(2, gap='large')
    with total1:
        st.info('Sesión 1: Construcción del curso')
        st.write('''Formación de grupos. Propuestas de desarrollo. Ejemplos de aplicación de SMILES.
        Github. Streamlit.''')
        
    with total2:
        st.info('Sesión 2: Bases de datos moleculares')
        st.write (pd.DataFrame({'Web': ['PubChem',
                                          'DrugBank', 
                                          'PeruNPDB'], 
                                'Descripción': ["Grupo 1", "Grupo 2", 
                                           "condicionales"]}))
    
    total3, total4 = st.columns(2, gap='large')
    with total3:
        st.info('Sesión 3: Descriptores moleculares')
        st.write('''Análisis exploratorio de datos, Detección de outliers y Procesamiento de datos.''')
        
    with total4:
        st.info('Unidad 4: Docking molecular')
        st.write ('''Ligando, Proteina y configuración.''')

    total5, total6 = st.columns(2, gap='large')

    with total5:
        st.info('Sesión 5: Modelos de IA')
        st.write (pd.DataFrame({'Tema': ['Regresión',
                                          'Clasificación', 
                                          'Clustering'], 
                                'Fecha': ["Grupo 1", "Grupo 2", 
                                           "Grupo 3"]}))

    with total6:
        st.info('Sesión 6: Din{amica molecular')
        st.write ('''Teoría, aplicaciones desde Google Colab y ejercicios propuestos.''')
    
#############################Pagina 2##############################    
def page2():
    st.header("Sesión 1", divider='rainbow')
    st.sidebar.markdown("Proyectos Propuestos")
    
    st.info('Generalidades')
    st.write('''1. Docking molecular Web''')
    st.write('''2. Generación de base de datos moleculares y EDA automatizado''')
    st.write('''3. Creador de INPUT con Pubmed, Scopus, WOS para Bibliometrix''')
    st.info('A. Grupos formados')  

    df = pd.read_csv('csv/grupo_1.csv')
    st.write(df)
    st.write('''Objetivos...''')
#############################Pagina 3##############################    

def page3():
  st.header('''Sesión 2''')

  st.info("A. ")
  st.write('''La ...''')

#############################Pagina 4##############################    

def page4():
  st.header('Sesión 3', divider='rainbow')
   
  st.link_button("Github", "https://github.com/inefable12/")

#############################Pagina 5##############################    

def page5():
  st.header('Sesión 4', divider='rainbow')

#############################Pagina 6##############################    

def page6():
  st.header('Sesión 5', divider='rainbow')
   
  st.link_button("Github", "https://github.com/inefable12/")

#############################Pagina 7##############################    

def page7():
  st.header('Sesión 6', divider='rainbow')
  
  st.write('''Seleccionar... ''')

  st.image("img/water2.png")

#############################Pagina 8##############################    

def page8():
  st.header('Sesión 7 (EXTRA)', divider='rainbow')
   
  st.link_button("Github", "https://github.com/inefable12/")

#############################Pagina 9##############################    

def page9():
  st.header('Sesión 8 (EXTRA)', divider='rainbow')
   
  st.link_button("Github", "https://github.com/inefable12/")

################################################################### 
##########################Configuracion############################    
###################################################################    

page_names_to_funcs = {
  "Contenido del Curso": Home,
  "Sesión 1": page2,
  "Sesión 2": page3,
  "Sesión 3": page4,
  "Sesión 4": page5,
  "Sesión 5": page6,
  "Sesión 6": page7,
  "Sesión 7": page8,
  "Sesión 8": page9,
}

selected_page = st.sidebar.selectbox("Selecciona una página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
