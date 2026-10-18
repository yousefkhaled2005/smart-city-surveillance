import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Smart City AI Surveillance", layout="wide")
st.title("📹 Smart City Perimeter Surveillance & Edge AI Ops")
st.markdown("**Architect**: Yousef Khaled | **Serving Engine**: TensorRT INT8 @ 28.4 FPS")

col1, col2, col3 = st.columns(3)
col1.metric("Active RTSP Streams", "32 Feeds", "+4 Today")
col2.metric("Processing Throughput", "28.4 FPS / GPU", "P95 < 35ms")
col3.metric("Security Alerts (24h)", "14 Breaches", "-18% Friction")

st.subheader("🚨 Real-Time Security Incident Stream")
df = pd.read_csv("data/camera_perimeter_alerts_2000.csv")
st.dataframe(df.tail(25), use_container_width=True)
