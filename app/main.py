import streamlit as st
from over_view import over_view
from user_engagment import engagement
from experience_analytics import experiencd
from satisfaction_analytics import satisfaction

# Sidebar for navigation
page_options = ["Over view", "User Engagment", "Experience Analytics", "Satisfaction Analytics"]
selected_page = st.sidebar.selectbox("Select a page", page_options)

# Display the selected page
if selected_page == "Over view":
    over_view()
elif selected_page == "User Engagment":
    engagement()
elif selected_page == "Experience Analytics":
    experiencd()
elif selected_page == "Satisfaction Analytics":
    satisfaction()
