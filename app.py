from pathlib import Path
import os

import streamlit as st
from PIL import  Image


# --- Path Settings ---
current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = os.path.join(current_dir,'css','main.css')
assets_folder = os.path.join(current_dir,'assets')

# --- Global settings ---
PAGE_TITLE = 'FIFA World Cup - Qatar 2022'
PAGE_ICON = '⚽️'


st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)

st.write('#')

list_2022 = ['Qatar', 'Germany', 'Denmark', 'Brazil', 'France', 'Belgium',
             'Croatia', 'Spain', 'Serbia', 'England', 'Switzerland',
             'Netherlands', 'Argentina', 'IR Iran', 'Korea Republic',
             'Japan', 'Saudi Arabia', 'Ecuador', 'Uruguay', 'Canada',
             'Ghana', 'Senegal', 'Portugal', 'Poland', 'Tunisia',
             'Morocco', 'Cameroon', 'USA', 'Mexico', 'Wales',
             'Australia',
             'Costa Rica']

list_2022.sort()

add_selectbox = st.selectbox(
    'Choose your team?',
    (list_2022)
)
