import streamlit as st
import libreria_funciones.py as lf

st.title("Mi primera app")

st.sidebar.title("Datos")
st.image("Logopy.png", width=100)
st.sidebar.image("logo.png")
st.title("Clase 5 Funciones")

p=st.number_input("Ingrese el monto Principal")
t=st.number_input("Ingrese la tasa anual")
a=st.slider("Seleccione el numero de años de prestamo",min_value=1, max_value=5)
pa=st.number_input("Cantindad de pago por año")

cota=lf.cuota_prestamo(p,t,a,pa)

st.write(cota)
