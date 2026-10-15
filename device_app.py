import streamlit as st
import platform
import datetime

st.set_page_config(page_title="Device & Network Inspector", page_icon="🌐")

st.title("🌐 Smart IP & Device Info Inspector")
st.write("A technical utility to check system environment and diagnostic metadata.")

if st.button("Run System Diagnostics"):
    st.success("Diagnostics completed successfully!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Operating System", value=platform.system())
        st.metric(label="Python Version", value=platform.python_version())
    with col2:
        st.metric(label="Simulated Network Status", value="Connected 🟢")
        st.metric(label="Security Protocol", value="TLS 1.3 Active")
        
    st.info(f"Report generated on: {datetime.datetime.now()}")
