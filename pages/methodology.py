import streamlit as st
import streamlit.components.v1 as components

# Load the HTML content
flow_chart_1_path = "pages/FlowChart1.html"
flow_chart_2_path = "pages/FlowChart2.html"
with open(flow_chart_1_path, "r") as html_file1, open(flow_chart_2_path, "r") as html_file2:
    html_content_flow_chart_1 = html_file1.read()
    html_content_flow_chart_2 = html_file2.read()

# Create two columns
col1, col2 = st.columns(2)

# Display each workflow in a separate column
with col1:
    st.header("Workflow 1")
    components.html(html_content_flow_chart_1, height=600, scrolling=True)

with col2:
    st.header("Workflow 2")
    components.html(html_content_flow_chart_2, height=600, scrolling=True)
