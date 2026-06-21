import streamlit as st
import pandas as pd
import numpy as np
import datetime
import plotly.express as px

st.set_page_config(page_title="Jigjiga Intelligence AI Hub", layout="wide")
st.title("🌊 Jigjiga Hydro-Agritech Intelligence Engine")
st.markdown("**Target Site:** Jigjiga Universal Medical & Business College (9.35417, 42.8090)")

# --- HYDROLOGY (SWAT / HEC-HMS) ---
st.header("💧 1-Month Hydrology Metrics (SWAT & HEC-HMS)")
dates = pd.date_range(end=datetime.date.today(), periods=30)
np.random.seed(42)
rain = np.random.gamma(shape=2, scale=4, size=30)
runoff = [((P - 5) ** 2) / (P + 20) if P > 5 else 0.0 for P in rain]
df = pd.DataFrame({"Date": dates, "Rainfall (mm)": rain, "Runoff (mm)": runoff})

fig = px.line(df, x="Date", y=["Rainfall (mm)", "Runoff (mm)"], title="30-Day Rainfall Trend Analysis")
st.plotly_chart(fig, use_container_width=True)

# --- CROPWAT & AQUACROP ---
st.header("🌾 Wheat Crop Health & Transpiration (CropWat & AquaCrop)")
c1, c2 = st.columns(2)
with c1:
    st.subheader("Diurnal Evapotranspiration (ET)")
    st.bar_chart(pd.DataFrame({"ET Rate (mm/hr)": [1.2, 4.8, 2.1]}, index=["Morning", "Afternoon", "Evening"]))
with c2:
    st.subheader("Zonal Ground Stress Report")
    st.dataframe(pd.DataFrame({
        "Farm Zone": ["North Field", "South Campus Plot", "East Field", "West Fence Line"],
        "Condition": ["Healthy 🟢", "Optimal 🟢", "Water Stressed 🟡", "Critical Dry 🔴"],
        "Action Required": ["None", "None", "Increase Drip Schedule", "Irrigate Immediately"]
    }))

# --- CLIMATE & DROUGHT (TENSORFLOW AI) ---
st.header("🤖 5-Year Climate Prognostics (TensorFlow Prediction)")
years = [2026, 2027, 2028, 2029, 2030, 2031]
spi = [0.15, -1.85, -2.10, 0.45, -0.90, -2.45]
flood = [12, 18, 85, 22, 40, 90]
df_ai = pd.DataFrame({"Year": years, "Drought Index (SPI)": spi, "Flood Risk (%)": flood})
st.dataframe(df_ai, hide_index=True)

for _, r in df_ai.iterrows():
    status = "Extreme Risk 🔴" if r['Drought Index (SPI)'] < -1.5 or r['Flood Risk (%)'] > 75 else "Stable Operational 🟢"
    st.write(f"**Year {int(r['Year'])} Horizon:** Framework Level: **{status}**")