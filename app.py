import streamlit as st
from utils.naics_lookup import get_naics_info
from utils.company_info import get_company_profile
from utils.location_risk import get_location_risk_proxy

st.set_page_config(page_title="Risk Snapshot Generator", page_icon="🕵️‍♂️")

st.title("🕵️‍♂️ Risk Snapshot Generator")

with st.form("input_form"):
    name = st.text_input("Customer Name")
    website = st.text_input("Website")
    address = st.text_input("Address")

    submitted = st.form_submit_button("Generate Snapshot")

if submitted:
    st.write("🔍 Fetching data...")

    naics_data = get_naics_info(name)
    profile_data = get_company_profile(website)
    location_risk = get_location_risk_proxy(address)

    summary = {
        "business_description": profile_data.get("business_description", "N/A"),
        "key_people": profile_data.get("key_people", []),
    }

    st.subheader("📄 Summary")
    st.json(summary)

    st.header("📌 SIC / NAICS Info")
    st.json(naics_data)

    st.header("🏢 Company Profile")
    st.json(profile_data)

    st.header("🌎 Location Risk (Approximate)")
    st.json(location_risk)
