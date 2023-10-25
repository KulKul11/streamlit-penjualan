import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
from streamlit_option_menu import option_menu

# Import data from Excel file
excel_file = 'data_penjualan.xlsx'
data = pd.read_excel(excel_file)

# Generate dynamic colors based on selected dates
data['Date'] = data['Date'].dt.date  # Menghapus komponen waktu, hanya menyisakan tanggal
selected_dates = data['Date'].unique()
colors = plt.cm.viridis(np.linspace(0, 1, len(selected_dates)))

# Set the figure size
fig_size = (800, 600)

# Set the Streamlit page theme
st.set_page_config(
    page_title="Visualisasi Data Penjualan",
    page_icon=":bar_chart:",
    layout="wide",  # Wide layout for larger content
    initial_sidebar_state="expanded",  # Expanded sidebar by default
)

# Streamlit app
st.markdown(
    """
    <style>
    .title, .subheader {
        text-align: center;
    }
    .title {
        margin-top: -90px;
    }
    .subheader {
        margin-top: -60px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar :
    selected = option_menu("Visualization",
                ["File Excel","Bar Chart", "Line Chart", "Pie Chart", "Doughnut Chart", "Area Chart"],
                icons=['file-earmark-excel-fill','bar-chart', 'rulers','pie-chart','stop-circle-fill','graph-up'],
                menu_icon="file-earmark-bar-graph",
                default_index = 0
            )

if (selected == "File Excel") :
    # Main title
    st.markdown('<h1 class="title">Visualisasi Data Penjualan</h1>', unsafe_allow_html=True)

    # Display the raw data
    st.write('Data Penjualan dari file Excel:')
    st.write(data)

elif (selected == "Bar Chart") :
    # Header for daily sales charts
    st.markdown('<h3 class="subheader">Grafik Penjualan Harian</h3>', unsafe_allow_html=True)

    # Bar Chart
    st.markdown('**Bar Chart**')
    fig_bar = plt.figure(figsize=(fig_size[0] / 80, fig_size[1] / 80))
    for i, date in enumerate(selected_dates):
        date_data = data[data['Date'] == date]
        date_total_quantity = date_data['Quantity'].sum()
        plt.barh(date, date_total_quantity, color=colors[i], label=date.strftime("%Y-%m-%d"))

    plt.xlabel('Total Quantity')
    plt.ylabel('Tanggal')
    plt.legend()
    st.pyplot(fig_bar)
    st.markdown('<div class="chart"></div>', unsafe_allow_html=True)

elif (selected == "Line Chart") :
    # Header for daily sales charts
    st.markdown('<h3 class="subheader">Grafik Penjualan Harian</h3>', unsafe_allow_html=True)

    # Line Chart
    st.markdown('**Line Chart**')
    line_data = data.groupby('Date')['Quantity'].sum()
    line_data.index = line_data.index.astype(str)  # Mengonversi indeks ke tipe data string
    st.line_chart(line_data, use_container_width=True)
    st.markdown('<div class="chart"></div>', unsafe_allow_html=True)

elif (selected == "Pie Chart") :
    # Header for daily sales charts
    st.markdown('<h3 class="subheader">Grafik Penjualan Harian</h3>', unsafe_allow_html=True)

    # Pie Chart
    st.markdown('**Pie Chart**')
    fig_pie = px.pie(names=selected_dates, values=data.groupby('Date')['Quantity'].sum())
    fig_pie.update_layout(height=fig_size[1], width=fig_size[0])
    st.plotly_chart(fig_pie, use_container_width=True)
    st.markdown('<div class "chart"></div>', unsafe_allow_html=True)


elif (selected == "Doughnut Chart") :
    # Header for daily sales charts
    st.markdown('<h3 class="subheader">Grafik Penjualan Harian</h3>', unsafe_allow_html=True)

    # Doughnut Chart
    st.markdown('**Doughnut Chart**')
    fig_doughnut = px.pie(names=selected_dates, values=data.groupby('Date')['Quantity'].sum())
    fig_doughnut.update_traces(hole=0.4)
    fig_doughnut.update_layout(height=fig_size[1], width=fig_size[0])
    st.plotly_chart(fig_doughnut, use_container_width=True)
    st.markdown('<div class="chart"></div>', unsafe_allow_html=True)


elif (selected == "Area Chart") :
    # Header for daily sales charts
    st.markdown('<h3 class="subheader">Grafik Penjualan Harian</h3>', unsafe_allow_html=True)

    # Area Chart
    st.markdown('**Area Chart**')
    area_data = data.groupby('Date')['Quantity'].sum()
    area_data.index = area_data.index.astype(str)  # Mengonversi indeks ke tipe data string
    st.area_chart(area_data, use_container_width=True)
    st.markdown('<div class="chart"></div>', unsafe_allow_html=True)