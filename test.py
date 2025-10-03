import pandas as pd
import streamlit as st

csv_url = "https://raw.githubusercontent.com/JeffSackmann/tennis_atp/refs/heads/master/atp_matches_qual_chall_2023.csv"
df = pd.read_csv(csv_url)

display(df.head())
display(df.info())

st.title("ATP Matches 2023")

search_term = st.text_input("Search in table")

if search_term:
    # Filter DataFrame rows case-insensitively across all string columns
    filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
else:
    filtered_df = df

st.dataframe(filtered_df)
