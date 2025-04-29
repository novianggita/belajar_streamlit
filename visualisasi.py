import streamlit as st
import pandas as pd
import plotly.express as px


def visualisasi_start():
    st.title("📊 Customer Churn Dashboard")
    st.markdown("Dashboard ini menyajikan eksplorasi visual interaktif terkait perilaku customer churn.")

    # Load data
    df = pd.read_csv("data_eda.csv")

    # Sidebar filters
    with st.sidebar:
        st.header("🔍 Filter Data")
        gender_filter = st.selectbox("Pilih Gender:", options=["All"] + sorted(df["gender"].dropna().unique().tolist()))
        contract_filter = st.selectbox("Pilih Contract Type:", options=["All"] + sorted(df["Contract"].dropna().unique().tolist()))

    # Apply filters
    df_filtered = df.copy()
    if gender_filter != "All":
        df_filtered = df_filtered[df_filtered["gender"] == gender_filter]
    if contract_filter != "All":
        df_filtered = df_filtered[df_filtered["Contract"] == contract_filter]

    # METRICS
    total_customers = len(df_filtered)
    total_churn = len(df_filtered[df_filtered['Churn'] == 'Yes'])
    churn_rate = (total_churn / total_customers * 100) if total_customers > 0 else 0

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customers", f"{total_customers:,}")
    col2.metric("Total Churn", f"{total_churn:,}")
    col3.metric("Churn Rate", f"{churn_rate:.2f}%")

    st.markdown("---")

    # PIE CHART (Plotly)
    st.subheader("1. Churn Distribution")
    churn_counts = df_filtered['Churn'].value_counts().rename({0: 'No Churn', 1: 'Churn'})
    pie_fig = px.pie(
        names=churn_counts.index,
        values=churn_counts.values,
        color=churn_counts.index,
        color_discrete_map={'Churn': 'red', 'No Churn': 'green'},
        hole=0.4
    )
    pie_fig.update_traces(textinfo='percent+label')
    st.plotly_chart(pie_fig, use_container_width=True)

    # HISTOGRAM - Monthly Charges
    st.subheader("2. Monthly Charges Distribution by Churn")
    hist_fig = px.histogram(
        df_filtered, x="MonthlyCharges", color="Churn",
        color_discrete_map={0: 'green', 1: 'red'},
        nbins=40, barmode='overlay', marginal="box"
    )
    hist_fig.update_layout(xaxis_title="Monthly Charges", yaxis_title="Count")
    st.plotly_chart(hist_fig, use_container_width=True)

    # TENURE DISTRIBUTION
    st.subheader("3. Tenure Distribution by Churn Status")
    tenure_fig = px.histogram(
        df_filtered, x="tenure", color="Churn",
        color_discrete_map={0: 'green', 1: 'red'},
        nbins=30, barmode='overlay', marginal="rug"
    )
    tenure_fig.update_layout(xaxis_title="Tenure (months)", yaxis_title="Count")
    st.plotly_chart(tenure_fig, use_container_width=True)

    st.markdown("> Filter data menggunakan sidebar untuk mengeksplorasi lebih dalam.")

