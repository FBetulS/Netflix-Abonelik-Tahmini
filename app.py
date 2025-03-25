import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
import pickle
from transformers import AutoModel, AutoTokenizer

# Page configuration
st.set_page_config(page_title="Netflix Subscription Predictor", layout="wide")

# Load the models
@st.cache_resource
def load_models():
    try:
        with open("model.pkl", "rb") as f:
            model = pickle.load(f)
        with open("tokenizer.pkl", "rb") as f:
            tokenizer = pickle.load(f)
        return model, tokenizer
    except Exception as e:
        st.error(f"Error loading models: {e}")
        return None, None

# Sidebar
st.sidebar.title("Netflix Subscription Analysis")
analysis_type = st.sidebar.selectbox("Choose Analysis Type", [
    "Data Overview", 
    "Subscription Trends", 
    "Growth Rate Analysis", 
    "Prediction Forecast", 
    "Model Comparison"
])

# Load Netflix subscription data
@st.cache_data
def load_data():
    try:
        data = pd.read_csv('Netflix-Subscriptions.csv')
        data['Time Period'] = pd.to_datetime(data['Time Period'], format='%d/%m/%Y')
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

data = load_data()
model, tokenizer = load_models()

# Main content based on selected analysis type
if data is not None:
    if analysis_type == "Data Overview":
        st.title("Netflix Subscription Data Overview")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Quarters", len(data))
            st.metric("Initial Subscribers", f"{data['Subscribers'].iloc[0]:,}")
        
        with col2:
            st.metric("Latest Subscribers", f"{data['Subscribers'].iloc[-1]:,}")
            st.metric("Total Growth", f"{((data['Subscribers'].iloc[-1] / data['Subscribers'].iloc[0] - 1) * 100):.2f}%")
        
        st.dataframe(data)

    elif analysis_type == "Subscription Trends":
        st.title("Netflix Quarterly Subscriptions Trend")
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Time Period'], y=data['Subscribers'], mode='lines'))
        fig.update_layout(title='Netflix Quarterly Subscriptions', 
                          xaxis_title='Date', 
                          yaxis_title='Subscribers')
        st.plotly_chart(fig)

    elif analysis_type == "Growth Rate Analysis":
        st.title("Subscription Growth Rate Analysis")
        
        data['Quarterly Growth Rate'] = data['Subscribers'].pct_change() * 100
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Quarterly Growth Rate")
            fig1 = px.bar(data, x='Time Period', y='Quarterly Growth Rate', 
                          color='Quarterly Growth Rate', 
                          color_continuous_scale='RdYlGn')
            st.plotly_chart(fig1)
        
        with col2:
            st.subheader("Growth Rate Distribution")
            fig2 = px.histogram(data, x='Quarterly Growth Rate', nbins=20)
            st.plotly_chart(fig2)

    elif analysis_type == "Prediction Forecast":
        st.title("Subscription Prediction Forecast")
        
        # Note: This would require your ARIMA/SARIMA model prediction logic
        st.warning("Prediction logic needs to be implemented with your trained models.")
        
    elif analysis_type == "Model Comparison":
        st.title("ARIMA vs SARIMA Model Comparison")
        
        st.warning("Model comparison charts need to be integrated with your specific models.")

else:
    st.error("Could not load Netflix subscription data. Please check your CSV file.")

# Optional: NLP Section if BERT model is loaded
if model and tokenizer:
    st.sidebar.header("Text Analysis")
    text_input = st.sidebar.text_area("Enter text for BERT analysis")
    if st.sidebar.button("Analyze Text"):
        # Basic tokenization example
        inputs = tokenizer(text_input, return_tensors="pt")
        st.sidebar.json(inputs)

# Footer
st.markdown("---")
st.markdown("Netflix Subscription Analysis | Powered by Streamlit")
