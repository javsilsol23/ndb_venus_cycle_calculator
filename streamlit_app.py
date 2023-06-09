import streamlit as st
import pandas as pd
import plotly.express as px
import datetime as dt


@st.cache_data
def load_data():
    df = pd.read_excel('cycles.xlsx')
    df['date'] = df['date'].dt.strftime('%Y-%m-%d')
    data = {}

    for i, row in df.iterrows():
        data[row['date']] = {
            'interval': {
                'color': row['color'],
                'number': row['number']
            },
            'phase': {
                'letter': row['letter'],
                'color': row['color2']
            }
        }

    return data


#################################################################
#       MAIN        MAIN        MAIN        MAIN        MAIN    #
#################################################################

st.set_page_config(layout="wide")
st.title('Nick Dagan Best Venus Cycle Calculator')

data_load_state = st.text('Loading data...')
data = load_data()

d = st.date_input(
    "Pick the date",
    min_value=dt.date(1900, 1, 1),
    max_value=dt.date(2026, 12, 31)
)

info = data[d.strftime('%Y-%m-%d')]
interval_color = info['interval']['color']
interval_number = int(info['interval']['number'])

phase_letter = info['phase']['letter']
phase_color = info['phase']['color']

if interval_color == 'White':
    interval_bg_color = 'black'
    interval_fg_color = 'white'
else:
    interval_bg_color = 'white'
    interval_fg_color = interval_color.lower()

if phase_color == 'white':
    phase_bg_color = 'black'
    phase_fg_color = 'white'
else:
    phase_bg_color = 'white'
    phase_fg_color = 'black'

st.markdown(
    f'<div style="background-color="#f0f0f0"><p style = "font-size: 18px; font-weight: bold;color:{interval_fg_color}; background-color:{interval_bg_color};"> Interval {interval_color.upper()} {interval_number}</p><p style = "font-size: 18px; font-weight: bold;color:{phase_fg_color}; background-color:{phase_bg_color};"> Phase {phase_color} {phase_letter.upper()}</p></div>', unsafe_allow_html=True
)
