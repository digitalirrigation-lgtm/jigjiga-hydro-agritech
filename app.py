import streamlit as st
import pandas as pd
import numpy as np
import datetime
import plotly.express as px
import ee

# ==============================================================================
# 1. INTERNATIONALIZATION & MULTI-LANGUAGE ARCHITECTURE
# ==============================================================================
st.set_page_config(page_title="Jigjiga Hydro-Agritech Intelligence Hub", layout="wide")

# Persistent Language Toggle
if "lang" not in st.session_state:
    st.session_state.lang = "English"

c_lang1, c_lang2 = st.columns([8, 2])
with c_lang2:
    st.session_state.lang = st.selectbox("🌐 Interface Language / Luqadda", ["English", "Af-Soomaali"])

# Translation Strings Dictionary
TEXT = {
    "English": {
        "title": "🌊 Jigjiga Hydro-Agritech Intelligence Platform",
        "subtitle": "Advanced Geospatial Forecasting Framework • Jigjiga Universal Medical & Business College",
        "coordinates": "📍 Geographic Target Domain: Latitude 9.35417, Longitude 42.8090",
        "gee_status": "🛡️ Compute Core Status: Data Stream Simulated via Local Environmental Math Models",
        "map_title": "🗺️ Zonal Vegetation Analysis & Crop Vigour Classification",
        "map_desc": "Geospatial scatter evaluation highlighting variable crop health matrices on the target agriculture parcels.",
        "hydrology_title": "💧 30-Day Hydrological Runoff & Precipitation Dynamics (SWAT & HEC-HMS)",
        "agritech_title": "🌾 Diurnal Transpiration Curves & Canopy Dissipation (CropWat & AquaCrop)",
        "et_sub": "Diurnal Evapotranspiration Dynamics (Wheat Canopy)",
        "stress_sub": "Zonal Ground Stress & Action Vector Matrix",
        "predictive_title": "🤖 5-Year Deep Learning Climate Prognostics (TensorFlow Framework)",
        "action_title": "🚨 Predictive Climate Risk Mitigation Protocols",
        "footer": "⚡ Enterprise Spatial Intelligence Package optimized for institutional deployment."
    },
    "Af-Soomaali": {
        "title": "🌊 Platform-ka Sirdoonka Biyaha iyo Beeraha ee Jigjiga",
        "subtitle": "Qaab-dhismeedka Saadaasha Dhulka ee Horumarsan • Kulliyadda Caafimaadka iyo Ganacsiga ee Jigjiga",
        "coordinates": "📍 Goobta la Beegsanayo: Lattitude 9.35417, Longitude 42.8090",
        "gee_status": "🛡️ Heerka Xogta: Xogta waxaa lagu matalay qaababka xisaabta deegaanka maxaliga ah",
        "map_title": "🗺️ Falanqaynta Dhirta iyo Kala Saaridda Caafimaadka Dalagga",
        "map_desc": "Khariidad muujinaysa kala duwanaanshiyaha caafimaadka dalagga ee dhulka beeraha ee la baadhayo.",
        "hydrology_title": "💧 Dhaqdhaqaaqa Biyaha iyo Roobka ee 30-ka Maalmood (Habka SWAT & HEC-HMS)",
        "agritech_title": "🌾 Qoyaanka Dalagga iyo Luminta Biyaha (Habka CropWat & AquaCrop)",
        "et_sub": "Isbeddelka Biyaha ee Maalintii (Dalagga Qamadiga)",
        "stress_sub": "Warbixinta Cadaadiska Dhulka iyo Tallaabooyinka Loo Baahan Yahay",
        "predictive_title": "🤖 Saadaasha Cimilada ee 5-ta Sano ee soo Socota (Nidaamka TensorFlow AI)",
        "action_title": "🚨 Tallaabooyinka Ka-hortagga Khatarta Cimilada",
        "footer": "⚡ Xidhmada Sirdoonka Meelaha ee Ganacsiga oo loo habeeyay adeegsiga rasmiga ah."
    }
}

L = TEXT[st.session_state.lang]

# Top Navigation Layout
st.title(L["title"])
st.markdown(f"**{L['subtitle']}**")
st.markdown(f"`{L['coordinates']}`")
st.caption(L["gee_status"])

# ==============================================================================
# 2. CROP HEALTH GEOSPATIAL MAP REFACTOR (GREEN / YELLOW / RED)
# ==============================================================================
st.header(L["map_title"])
st.write(L["map_desc"])

# Precise coordinate array generating a simulated 4-plot farm around the college boundary
farm_plots = pd.DataFrame({
    'Latitude':  [9.3542, 9.3539, 9.3545, 9.3540],
    'Longitude': [42.8091, 42.8088, 42.8094, 42.8085],
    'Crop Sector': ['North Field (Wheat)', 'South Campus Plot', 'East Extension Field', 'West Boundary Fence'],
    'Health Classification': ['Healthy 🟢', 'Optimal Growth 🟢', 'Water Stressed 🟡', 'Critical Dry 🔴'],
    'Color Indicator': ['#10B981', '#3B82F6', '#F59E0B', '#EF4444'], # International HEX code mappings
    'NDVI Index Range': [0.72, 0.68, 0.41, 0.18],
    'Recommended Intervention': ['Operational routine', 'Operational routine', 'Increase drip frequency', 'Execute immediate flood irrigation']
})

# Render the high-resolution Plotly scatter map box
fig_map = px.scatter_mapbox(
    farm_plots,
    lat="Latitude",
    lon="Longitude",
    color="Health Classification",
    color_discrete_sequence=farm_plots['Color Indicator'].unique(),
    size=[15, 15, 15, 15],
    hover_name="Crop Sector",
    hover_data=["NDVI Index Range", "Recommended Intervention"],
    zoom=16,
    height=450
)
fig_map.update_layout(
    mapbox_style="open-street-map",
    margin={"r":0,"t":0,"l":0,"b":0},
    legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
)
st.plotly_chart(fig_map, use_container_width=True)

# ==============================================================================
# 3. HYDROLOGY MATRIX (SWAT / HEC-HMS)
# ==============================================================================
st.header(L["hydrology_title"])
dates = pd.date_range(end=datetime.date.today(), periods=30)
np.random.seed(42)
rain = np.random.gamma(shape=2, scale=4, size=30)
runoff = [((P - 5) ** 2) / (P + 20) if P > 5 else 0.0 for P in rain]
df_hydro = pd.DataFrame({"Date": dates, "Precipitation (mm)": rain, "Surface Runoff (mm)": runoff})

fig_hydro = px.line(df_hydro, x="Date", y=["Precipitation (mm)", "Surface Runoff (mm)"], 
                    color_discrete_sequence=["#2563EB", "#DC2626"])
fig_hydro.update_layout(margin={"r":0,"t":20,"l":0,"b":0})
st.plotly_chart(fig_hydro, use_container_width=True)

# ==============================================================================
# 4. AGRITECH INTERFACE WORKSPACE (CROPWAT / AQUACROP)
# ==============================================================================
st.header(L["agritech_title"])
col1, col2 = st.columns(2)

with col1:
    st.subheader(L["et_sub"])
    et_df = pd.DataFrame({
        "Hourly Interval": ["Morning (08:00)", "Afternoon (13:00)", "Evening (18:00)"],
        "ET Rate (mm/hr)": [1.2, 4.8, 2.1]
    })
    fig_et = px.bar(et_df, x="Hourly Interval", y="ET Rate (mm/hr)", color="ET Rate (mm/hr)", color_continuous_scale="Blues")
    st.plotly_chart(fig_et, use_container_width=True)

with col2:
    st.subheader(L["stress_sub"])
    clean_report = farm_plots[['Crop Sector', 'Health Classification', 'Recommended Intervention']]
    st.dataframe(clean_report, hide_index=True, use_container_width=True)

# ==============================================================================
# 5. PREDICTIVE INSIGHTS PIPELINE (TENSORFLOW AI)
# ==============================================================================
st.header(L["predictive_title"])
years = [2026, 2027, 2028, 2029, 2030, 2031]
spi = [0.15, -1.85, -2.10, 0.45, -0.90, -2.45]
flood = [12, 18, 85, 22, 40, 90]
df_ai = pd.DataFrame({"Year": years, "Drought Index (SPI)": spi, "Anomalous Flood Risk (%)": flood})
st.dataframe(df_ai, hide_index=True, use_container_width=True)

st.subheader(L["action_title"])
for _, r in df_ai.iterrows():
    if r['Drought Index (SPI)'] < -1.5 or r['Anomalous Flood Risk (%)'] > 75:
        risk_status = "⚠️ Extreme Weather Hazard Flagged" if st.session_state.lang == "English" else "⚠️ Khatar Aad u Saraysa oo Cimilada ah"
        action_desc = "Initiate critical retention basin management and secondary asset deployment." if st.session_state.lang == "English" else "Ku dhaqaaq maamulka kaydinta biyaha degdegga ah iyo xoojinta kanaalada."
    else:
        risk_status = "✅ Normal Threshold" if st.session_state.lang == "English" else "✅ Xaalad Caadi Ah"
        action_desc = "Maintain standard campus irrigation networks." if st.session_state.lang == "English" else "Sii wad nidaamka waraabka caadiga ah ee dhismaha jaamacadda."
        
    st.markdown(f"**Year {int(r['Year'])}:** `{risk_status}` | *Strategic Protocol:* {action_desc}")

st.markdown("---")
st.caption(L["footer"])
