import streamlit as st
import pandas as pd

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    option = st.radio(
        "Choose one action:",
        ("Show preview", "Show summary", "Filter data", "Plot data"),
    )

    if option == "Show preview":
        st.subheader("Data Preview")
        show_index = st.checkbox("Show index?")
        if show_index:
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_csv(uploaded_file, index_col=0)
        st.write(df.head())

    elif option == "Show summary":
        st.subheader("Data Summary")
        df = pd.read_csv(uploaded_file)
        st.write(df.describe())

    elif option == "Filter data":
        st.subheader("Filter Data")
        df = pd.read_csv(uploaded_file)
        columns = df.columns.tolist()
        selected_column = st.selectbox("Select column to filter by", columns)
        unique_values = df[selected_column].unique()
        selected_value = st.selectbox("Select value", unique_values)
        filtered_df = df[df[selected_column] == selected_value]
        st.write(filtered_df)

    elif option == "Plot data":
        st.subheader("Plot Data")
        df = pd.read_csv(uploaded_file)
        columns = df.columns.tolist()
        x_column = st.selectbox("Select the x-axis column", columns)
        y_column = st.selectbox("Select the y-axis column", columns)

        if st.button("Generate Plot"):
            st.line_chart(df.set_index(x_column)[y_column],x_label=x_column, y_label=y_column)
else:
    st.write("Waiting on file upload...")