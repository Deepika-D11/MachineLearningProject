import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def main():
    # Load the dataset
    try:
        df = pd.read_csv('C:/Users/HP/OneDrive/Desktop/Death rates ml project 1/worldometer_snapshots_April18_to_May18.csv')
    except FileNotFoundError:
        st.error("The dataset file was not found. Please check the file path.")
        st.stop()

    # Prepare the features and target variable
    X = df[['Total Cases', 'Total Recovered']].fillna(0)
    y = df['Total Deaths'].fillna(0)

    # Train the model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Sidebar options
    st.sidebar.title("Country Data")
    selected_country = st.sidebar.selectbox('Select a Country', df['Country'].unique())

    # Filter data for the selected country
    country_data = df[df['Country'] == selected_country]

    # Display basic data
    st.title(f"COVID-19 Data for {selected_country}")
    st.write(country_data)

    # Display histograms
    st.subheader(f"Visualizations for {selected_country}")

    # Deaths histogram
    st.subheader('Total Deaths Distribution')
    fig1, ax1 = plt.subplots()
    sns.histplot(country_data['Total Deaths'], bins=20, ax=ax1)
    st.pyplot(fig1)

    # Cases histogram
    st.subheader('Total Cases Distribution')
    fig2, ax2 = plt.subplots()
    sns.histplot(country_data['Total Cases'], bins=20, ax=ax2)
    st.pyplot(fig2)

    # Recovered histogram
    st.subheader('Total Recovered Distribution')
    fig3, ax3 = plt.subplots()
    sns.histplot(country_data['Total Recovered'], bins=20, ax=ax3)
    st.pyplot(fig3)

    # Prediction (Optional, based on your model)
    st.sidebar.title('Model Prediction')
    test_total_cases = st.sidebar.number_input('Enter Total Cases', value=738792)
    test_total_recovered = st.sidebar.number_input('Enter Total Recovered', value=631509)

    # Create a data array to be passed to the model
    input_data = np.array([[test_total_cases, test_total_recovered]])

    # Predict with the trained model
    if st.sidebar.button('Predict'):
        prediction = model.predict(input_data)
        st.sidebar.write(f"Predicted Deaths: {prediction[0]}")

# This ensures that the function runs only when called directly
if __name__ == "__main__":
    main()
