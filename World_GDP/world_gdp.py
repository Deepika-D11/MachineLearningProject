import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

def main():
    # Load the dataset
    df = pd.read_csv('C:/Users/HP/OneDrive/Desktop/World GDP Ml project 5/countries of the world.csv')

    # Clean the dataset (Removing commas and converting to numeric)
    columns_to_keep_as_int= ['Population', 'Area (sq. mi.)']
    columns_to_skip = ['Country','Region'] + columns_to_keep_as_int

    for col in df.columns:
        if col not in columns_to_skip and df[col].dtype == "O":
            df[col] = df[col].str.replace(",", '', regex=True).astype(float)

    # Filling missing values
    for col in df.columns.values:
        if df[col].isnull().sum() == 0:
            continue
        if col == 'Climate':
            guess_values = df.groupby('Region')['Climate'].apply(lambda x: x.mode().max())
        else:
            guess_values = df.groupby('Region')[col].median()
        for region in df['Region'].unique():
            df.loc[(df[col].isnull()) & (df['Region'] == region), col] = guess_values[region]

    # Grouping by Region
    region_data = df.groupby('Region').agg({
        'Country': lambda x: ', '.join(x.astype(str)),
        'Population': 'sum',
        'Area (sq. mi.)': 'sum',
        'GDP ($ per capita)': 'mean',
        'Literacy (%)': 'mean',
        'Agriculture': 'mean',
        'Industry': 'mean',
        'Service': 'mean'
    })

    # Streamlit app layout
    st.title('World GDP Analysis by Region')

    # Displaying the cleaned dataset
    st.header("Dataset Overview")
    st.write(df.head())

    # Dropdown for Region selection
    selected_region = st.selectbox("Select a Region:", region_data.index)

    # Displaying region data
    st.subheader(f'Data for {selected_region}')
    st.write(region_data.loc[selected_region])

    # Visualization: GDP vs Literacy
    st.header('GDP vs Literacy by Region')
    fig, ax = plt.subplots(figsize=(10, 6))  # Set figure size
    sns.scatterplot(data=df, x='GDP ($ per capita)', y='Literacy (%)', hue='Region', ax=ax)
    ax.set_title('GDP vs Literacy by Region')
    ax.set_xlabel('GDP ($ per capita)')
    ax.set_ylabel('Literacy (%)')
    st.pyplot(fig)

    # Displaying more data insights
    st.header("Summary Statistics by Region")
    st.write(region_data.describe())

if __name__ == '__main__':
    main()
