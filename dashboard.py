import streamlit as st
import matplotlib.pyplot as plt
import io

st.title('Barraca de Churros')

st.subheader('Sabores Vendidos Hoje')

sabores = {
    'Chocolate Preto': 0,
    'Chocolate Branco': 0,
    'Chocolate Misto': 0,
    'Doce de Leite': 0,
    'Nutella': 0,
    'Banana com Leite Condensado': 0
}

sabores['Chocolate Preto'] = st.number_input(label='Chocolate Preto', step=1, format='%i')
sabores['Chocolate Branco'] = st.number_input(label='Chocolate Branco', step=1, format='%i')
sabores['Chocolate Misto'] = st.number_input(label='Chocolate Misto', step=1, format='%i')
sabores['Doce de Leite'] = st.number_input(label='Doce de Leite', step=1, format='%i')
sabores['Nutella'] = st.number_input(label='Nutella', step=1, format='%i')
sabores['Banana com Leite Condensado'] = st.number_input(label='Banana com Leite Condensado', step=1, format='%i')

total_consumido = sum(sabores.values())

if total_consumido > 0:
    porcentagens = [valor / total_consumido * 100 for valor in sabores.values()]
    sabores_filtrados = []
    porcentagens_filtradas = []

    for sabor, porcentagem in zip(sabores.keys(), porcentagens):
        if porcentagem > 0:
            sabores_filtrados.append(sabor)
            porcentagens_filtradas.append(porcentagem)

    fig, ax = plt.subplots()
    ax.pie(porcentagens_filtradas, labels=sabores_filtrados, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')

    ax.set_title('Porcentagem de Consumo de Churros por Sabor')

    img_buffer = io.BytesIO()
    fig.savefig(img_buffer, format='png')
    img_buffer.seek(0)

    st.pyplot(fig)

    st.download_button(
        label='Download Gráfico',
        data=img_buffer,
        file_name='grafico.png',
        mime='image/png'
    )
else:
    st.write("Nenhum churro foi consumido. Por favor, insira valores para gerar o gráfico.")
