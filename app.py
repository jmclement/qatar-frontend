from pathlib import Path
import os
import base64
import streamlit as st
from PIL import  Image


# --- Path Settings ---
current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = os.path.join(current_dir,'css','main.css')
assets_folder = os.path.join(current_dir,'assets')

# --- Global settings ---
PAGE_TITLE = 'FIFA World Cup - Qatar 2022'
PAGE_ICON = '⚽️'

# --- Set Page Title and Icon ---
st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)


# --- Load CSS and image ---
banner = Image.open(os.path.join(assets_folder,'banner.jpg'))

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


header_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
    img_to_bytes(os.path.join(assets_folder,'banner.jpg'))
)
# st.markdown(
#     header_html, unsafe_allow_html=True,
# )


st.markdown("<p style='text-align: center; color: grey;'>"+header_html+"</p>", unsafe_allow_html=True)

# st.write('#')
# st.image(banner)

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
