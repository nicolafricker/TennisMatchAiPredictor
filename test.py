import pandas as pd
import streamlit as st
import io

csv_url = "https://raw.githubusercontent.com/JeffSackmann/tennis_atp/refs/heads/master/atp_matches_qual_chall_2023.csv"
df = pd.read_csv(csv_url)

st.title("ATP Matches 2023")

# Text input for search
search_term = st.text_input("Search in table")

# Filter rows based on search term
if search_term:
    filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
else:
    filtered_df = df

st.subheader("Filtered Results")
st.dataframe(filtered_df)
