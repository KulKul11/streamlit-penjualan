import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

# Import data from Excel file
excel_file = 'data_penjualan.xlsx'
data = pd.read_excel(excel_file)

# Generate dynamic colors based on selected dates
selected_dates = data['Date'].unique()
colors = plt.cm.viridis(np.linspace(0, 1, len(selected_dates)))

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
    .chart {
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main title
st.markdown('<h1 class="title">Visualisasi Data Penjualan</h1>', unsafe_allow_html=True)

# Display the raw data
st.write('Data Penjualan dari file Excel:')
st.write(data)

# Header for daily sales charts
st.markdown('<h3 class="subheader">Grafik Penjualan Harian</h3>', unsafe_allow_html=True)

# Set the figure size
fig_size = (800, 600)

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

# Line Chart
st.markdown('**Line Chart**')
line_data = data.groupby('Date')['Quantity'].sum()
st.line_chart(line_data, use_container_width=True)
st.markdown('<div class="chart"></div>', unsafe_allow_html=True)

# Pie Chart
st.markdown('**Pie Chart**')
fig_pie = px.pie(names=selected_dates, values=data.groupby('Date')['Quantity'].sum())
fig_pie.update_layout(height=fig_size[1], width=fig_size[0])
st.plotly_chart(fig_pie, use_container_width=True)
st.markdown('<div class "chart"></div>', unsafe_allow_html=True)

# Doughnut Chart
st.markdown('**Doughnut Chart**')
fig_doughnut = px.pie(names=selected_dates, values=data.groupby('Date')['Quantity'].sum())
fig_doughnut.update_traces(hole=0.4)
fig_doughnut.update_layout(height=fig_size[1], width=fig_size[0])
st.plotly_chart(fig_doughnut, use_container_width=True)
st.markdown('<div class="chart"></div>', unsafe_allow_html=True)

# Area Chart
st.markdown('**Area Chart**')
area_data = data.groupby('Date')['Quantity'].sum()
st.area_chart(area_data, use_container_width=True)
st.markdown('<div class="chart"></div>', unsafe_allow_html=True)

# Scatter Plot
st.markdown('**Scatter Plot**')
scatter_data = data[['Date', 'Quantity']]
st.scatter_chart(scatter_data, use_container_width=True)
st.markdown('<div class="chart"></div>', unsafe_allow_html=True)

# 3D Scatter Plot (using Plotly)
st.markdown('**3D Scatter Plot**')
fig_3d = px.scatter_3d(data, x='Date', y='Quantity', z='Items', color='Items')
fig_3d.update_layout(height=fig_size[1], width=fig_size[0])
st.plotly_chart(fig_3d)
st.markdown('<div class="chart"></div>', unsafe_allow_html=True)
