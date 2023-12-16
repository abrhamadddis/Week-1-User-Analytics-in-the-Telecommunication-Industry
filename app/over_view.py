import streamlit as st
from other_module import fetch_data, create_conn
from visualization import create_top_10_handsets_chart, create_top_3_manufacturers_chart, create_top_5_handsets_per_manufacturer_chart

def over_view():
    st.title("Over view")
    st.write("This is Over view analysis TellCo's company")

    engine = create_conn()
    data = fetch_data(engine, "xdr_data")
    
    
    st.write("#Top 10 Handsets")
    create_top_10_handsets_chart(data)
    st.write("#Top 3 Manufacturers")
    create_top_3_manufacturers_chart(data)

    st.write("#top_5_handsets_per_manufacturer")
    create_top_5_handsets_per_manufacturer_chart(data)