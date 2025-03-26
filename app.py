import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

# Page configuration
st.set_page_config(page_title="Netflix Subscription Analysis", layout="wide")

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

# Main Streamlit App
def main():
    st.title("Netflix Subscription Analysis Dashboard")
    
    # Load data
    data = load_data()
    
    if data is not None:
        # Sidebar for navigation
        st.sidebar.title("Navigation")
        analysis_type = st.sidebar.radio("Choose Analysis", [
            "Overview",
            "Subscription Trends", 
            "Growth Rate Analysis", 
            "Detailed Insights"
        ])

        # Overview Section
        if analysis_type == "Overview":
            st.header("Subscription Overview")
            
            # Key Metrics
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Total Quarters", len(data))
            
            with col2:
                st.metric("Initial Subscribers", f"{data['Subscribers'].iloc[0]:,}")
            
            with col3:
                st.metric("Latest Subscribers", f"{data['Subscribers'].iloc[-1]:,}")
            
            # Data Table
            st.dataframe(data)

        # Subscription Trends Section
        elif analysis_type == "Subscription Trends":
            st.header("Netflix Quarterly Subscription Trends")
            
            # Line Chart of Subscribers Over Time
            fig = px.line(data, x='Time Period', y='Subscribers', 
                          title='Netflix Quarterly Subscriptions')
            st.plotly_chart(fig)
            
            # Quarterly Changes
            data['Quarterly Change'] = data['Subscribers'].diff()
            
            # Bar Chart of Quarterly Changes
            fig_change = px.bar(data, x='Time Period', y='Quarterly Change',
                                title='Quarterly Subscription Changes')
            st.plotly_chart(fig_change)

        # Growth Rate Analysis Section
        elif analysis_type == "Growth Rate Analysis":
            st.header("Subscription Growth Rate Analysis")
            
            # Calculate Quarterly Growth Rate
            data['Quarterly Growth Rate'] = data['Subscribers'].pct_change() * 100
            
            # Growth Rate Line Chart
            fig_growth = px.line(data, x='Time Period', y='Quarterly Growth Rate',
                                 title='Quarterly Subscription Growth Rate')
            st.plotly_chart(fig_growth)
            
            # Growth Rate Distribution
            fig_hist = px.histogram(data, x='Quarterly Growth Rate', 
                                    title='Distribution of Quarterly Growth Rates')
            st.plotly_chart(fig_hist)

        # Detailed Insights Section
        elif analysis_type == "Detailed Insights":
            st.header("Comprehensive Subscription Insights")
            
            # Cumulative Growth Calculation
            data['Cumulative Growth'] = (data['Subscribers'] / data['Subscribers'].iloc[0] - 1) * 100
            
            # Cumulative Growth Chart
            fig_cumulative = px.area(data, x='Time Period', y='Cumulative Growth',
                                     title='Cumulative Subscription Growth')
            st.plotly_chart(fig_cumulative)
            
            # Comparative Analysis
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Total Subscribers by Year")
                yearly_subscribers = data.groupby(data['Time Period'].dt.year)['Subscribers'].max()
                fig_yearly = px.bar(x=yearly_subscribers.index, y=yearly_subscribers.values,
                                    labels={'x': 'Year', 'y': 'Subscribers'})
                st.plotly_chart(fig_yearly)
            
            with col2:
                st.subheader("Year-over-Year Growth")
                yoy_growth = yearly_subscribers.pct_change() * 100
                fig_yoy = px.bar(x=yoy_growth.index[1:], y=yoy_growth.values[1:],
                                 labels={'x': 'Year', 'y': 'YoY Growth (%)'})
                st.plotly_chart(fig_yoy)

        # Footer
        st.markdown("---")
        st.markdown("Netflix Subscription Analysis Dashboard | Powered by Streamlit")

    else:
        st.error("Unable to load Netflix subscription data. Please check the CSV file.")

# Run the app
if __name__ == "__main__":
    main()
    