import streamlit as st
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Calculadora de Presupuesto Mensual", layout="centered")

# Título
st.title("🧮 Calculadora de Presupuesto Mensual")

# Entrada de datos
st.header("1. Ingresa tus datos")
ingreso = st.number_input("💰 Ingreso mensual:", min_value=0.0, step=100.0)

st.subheader("Gastos Fijos")
gastos_fijos = {}
n_fijos = st.number_input("¿Cuántos gastos fijos tienes?", min_value=1, max_value=10, step=1)
for i in range(n_fijos):
    concepto = st.text_input(f"Concepto de gasto fijo {i+1}:", key=f"fijo_{i}")
    monto = st.number_input(f"Monto para {concepto}:", min_value=0.0, step=50.0, key=f"monto_fijo_{i}")
    if concepto:
        gastos_fijos[concepto] = monto

st.subheader("Gastos Variables")
gastos_variables = {}
n_variables = st.number_input("¿Cuántos gastos variables tienes?", min_value=1, max_value=10, step=1)
for i in range(n_variables):
    concepto = st.text_input(f"Concepto de gasto variable {i+1}:", key=f"variable_{i}")
    monto = st.number_input(f"Monto para {concepto}:", min_value=0.0, step=50.0, key=f"monto_variable_{i}")
    if concepto:
        gastos_variables[concepto] = monto

# Cálculos
if st.button("Calcular"):
    total_fijos = sum(gastos_fijos.values())
    total_variables = sum(gastos_variables.values())
    total_gastos = total_fijos + total_variables
    saldo = ingreso - total_gastos

    # Resultados
    st.header("2. Resultados")
    st.write(f"**Total Gastos Fijos:** S/{total_fijos:.2f}")
    st.write(f"**Total Gastos Variables:** S/{total_variables:.2f}")
    st.write(f"**Saldo Disponible:** S/{saldo:.2f}")
    
    # Gráficos
    st.header("3. Visualización")
    labels = ['Gastos Fijos', 'Gastos Variables', 'Saldo Disponible']
    values = [total_fijos, total_variables, max(0, saldo)]
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99'])
    ax.axis('equal')  # Hacer el gráfico circular
    st.pyplot(fig)