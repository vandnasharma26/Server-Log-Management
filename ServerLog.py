# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
from datetime import datetime

selected = option_menu(
    menu_title=None,
    options=["Home", "Dashboard", "Contact"],
    icons=["house", "book", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

if selected == "Dashboard":
    st.title(f"Dashboard")

    def load_data():
        data = pd.read_excel("server_log_dataset.xlsx", engine="openpyxl")
        return data

    df = load_data()

    # Display the data as a table
    st.write("## Server Logs Data")
    st.write(df)

    date_condition = datetime.strptime("2017-03-15", "%Y-%m-%d").date()  # Adjust the date as needed
    df['Date first seen'] = pd.to_datetime(df['Date first seen'], format="%Y-%m-%d %H:%M:%S")
    filtered_df = df[df['Date first seen'].dt.date <= date_condition]

    # Display the filtered data as a table
    st.write("## Server Log Table (Filtered by Date)")
    st.write(filtered_df)

    numeric_columns = filtered_df.select_dtypes(include=['number'])

    for column in numeric_columns.columns:
        if column != "Date first seen":  # Exclude the "Bytes" column (or any other column you want to exclude)
            st.write(f"## {column} vs. Class")
            grouped_data = filtered_df.groupby("class")[column].mean()
            plt.figure(figsize=(8, 6))
            grouped_data.plot(kind="bar", alpha=0.7)
            plt.xlabel("Class")
            plt.ylabel(column)
            plt.title(f"{column} vs. Class")
            plt.xticks(rotation=45)
            st.pyplot(plt)



elif selected == "Home":
    st.title(f"Welcome!")

elif selected == "Contact":
    st.title(f"Reach Us")

from google.colab import drive
drive.mount('/content/drive')