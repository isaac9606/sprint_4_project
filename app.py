import streamlit as st
import pandas as pd
import plotly.express as px

vehicles_us_df = pd.read_csv('vehicles_us.csv')

def main():
    st.title('Car Advertisement Data Analysis')
    
    if st.checkbox('Show Dataset'):
        st.header('Dataset Overview')
        st.write(vehicles_us_df.head())

    st.header('Histogram of Odometer Readings')
    color_by_condition = st.checkbox('Color by Condition')
    fig_odometer_histogram = px.histogram(
        vehicles_us_df,
        x='odometer',
        color='condition' if color_by_condition else None,
        title='Distribution of Odometer Readings',
        labels={'odometer': 'Odometer Reading'},
        nbins=30,  
        height=600,
        width=900
    )
    st.plotly_chart(fig_odometer_histogram)

    st.header('Scatter Plot of Price vs Odometer Reading')

    color_by_model = st.checkbox('Color by Model')

    fig_price_odometer_scatter = px.scatter(
        vehicles_us_df,
        x='odometer',
        y='price',
        color='model' if color_by_model else None,
        title='Price vs. Odometer Reading',
        labels={'odometer': 'Odometer Reading', 'price': 'Price'}
    )
    st.plotly_chart(fig_price_odometer_scatter)

if __name__ == "__main__":
    main()