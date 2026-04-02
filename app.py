import streamlit as st
import pandas as pd
st.sidebar.title("🏏 IPL Dashboard")
st.sidebar.markdown("Created by Devashree Patil")

st.title("🏏 IPL Analytics Dashboard")
st.markdown("Interactive dashboard for analyzing IPL match data")

matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

st.subheader("Dataset Preview")
st.write(matches.head())

st.subheader("Top Teams by Wins")

team_wins = matches['winner'].value_counts()

st.bar_chart(team_wins)

st.subheader("Team Analysis")

teams = matches['team1'].unique()
selected_team = st.selectbox("Select a Team", teams)

team_matches = matches[
    (matches['team1'] == selected_team) | 
    (matches['team2'] == selected_team)
]

st.write("Total Matches Played:", team_matches.shape[0])

wins = team_matches[team_matches['winner'] == selected_team].shape[0]
st.write("Matches Won:", wins)

st.subheader("Toss Impact Analysis")

toss_win_match_win = matches[matches['toss_winner'] == matches['winner']]
percentage = (len(toss_win_match_win) / len(matches)) * 100

st.write(f"Toss winner also won match: {percentage:.2f}%")

st.subheader("Top 10 Players by Runs")

top_batsmen = deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10)

st.bar_chart(top_batsmen)

st.write(deliveries.columns)