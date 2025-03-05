import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(page_title="GetFit Dashboard", layout="wide")

# Apply Dark Theme
st.markdown(
    """
    <style>
        body, .stApp {
            background-color: #1E1E1E;
            color: #FFFFFF;
            font-family: 'Poppins', sans-serif;
        }
        .stTextInput > label, .stNumberInput > label, .stSelectbox > label, .stSlider > label {
            color: #FFFFFF !important;
        }
        .stProgress > div > div {
            background-color: #FF5733 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar for User Input
st.sidebar.image("https://via.placeholder.com/100", width=100)
st.sidebar.title("🏋️ User Profile")
name = st.sidebar.text_input("Name", "John Doe")
age = st.sidebar.number_input("Age", min_value=1, max_value=100, value=25)
gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
weight = st.sidebar.number_input("Weight (kg)", min_value=20, max_value=200, value=70)
height = st.sidebar.number_input("Height (cm)", min_value=50, max_value=250, value=170)
heart_rate = st.sidebar.slider("💓 Heart Rate (bpm)", min_value=40, max_value=200, value=72)
body_temp = st.sidebar.slider("🌡 Body Temperature (°C)", min_value=35.0, max_value=42.0, value=36.5)
disease = st.sidebar.text_input("🩺 Any Medical Condition", "None")

# Main Dashboard
st.title(f"🔥 Hello, {name} 👊")
st.write("**Stay active and track your fitness journey!**")

# Health Metrics
col1, col2, col3 = st.columns(3)
col1.metric("😴 Sleep", "7.5 hrs", "Last Night")
col2.metric("💧 Water Intake", "2.5 Liters", "Today")
col3.metric("🚶 Steps", "8500", "Walked Today")

# Activity Chart
data = pd.DataFrame({
    "Day": ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
    "Exercise": [30, 60, 45, 50, 40, 55, 70],
    "Rest": [90, 100, 85, 95, 80, 100, 110]
})
fig = px.bar(data, x="Day", y=["Exercise", "Rest"], barmode="group",
             labels={"value": "Minutes", "variable": "Activity"},
             color_discrete_map={"Exercise": "#FF5733", "Rest": "#3498DB"})
st.plotly_chart(fig, use_container_width=True)

# Weather Information
col4, col5 = st.columns(2)
col4.subheader("🌦 Weather")
col4.write("📍 Los Angeles")
col4.metric("🌡 Temperature", "22°C")
col4.metric("💦 Humidity", "60%")
col4.metric("💨 Wind Speed", "10 km/h")

# Goals & Tasks
col6, col7 = st.columns(2)
col6.subheader("🎯 Monthly Goals")
col6.progress(0.4, text="🏃 Running: 40%")
col6.progress(0.6, text="😴 Sleep: 60%")
col6.progress(0.3, text="⚖️ Weight Loss: 30%")

col7.subheader("📆 Upcoming Tasks")
col7.write("✅ 🏋️ Gym Session - 6 PM")
col7.write("❌ 🧘 Yoga - 8 AM (Missed)")

# Map Section
st.subheader("🗺 Running Route")
st.image("https://via.placeholder.com/600x300", caption="Your Running Path")

# Recommendations
st.subheader("🍎 Diet & Health Recommendations")
st.write("**Based on your data, here are your personalized health tips:**")
st.success("🥩 Increase protein intake to build muscle.")
st.warning("💦 Hydrate properly before workouts.")
st.info("🛌 Maintain a steady sleep schedule for better recovery.")

# Generate Report Button
if st.button("📄 Generate Fitness Report"):
    st.success("✅ Your fitness report has been generated successfully!")
