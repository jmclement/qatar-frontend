from pathlib import Path
import streamlit as st
import os
import requests
import streamlit as st
from streamlit_option_menu import option_menu

# --- Global settings ---
PAGE_TITLE = 'FIFA World Cup - Qatar 2022'
PAGE_ICON = '⚽️'
BASE_URL = "https://qatar-2022-api-refactor-3axvvmvj6a-ue.a.run.app"

# --- Path Settings ---
current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = os.path.join(current_dir,'css','main.css')

# --- Set Page Title and Icon ---
st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)



list_2022 = ['Qatar', 'Germany', 'Denmark', 'Brazil', 'France', 'Belgium',
             'Croatia', 'Spain', 'Serbia', 'England', 'Switzerland',
             'Netherlands', 'Argentina', 'Iran', 'Korea Republic',
             'Japan', 'Saudi Arabia', 'Ecuador', 'Uruguay', 'Canada',
             'Ghana', 'Senegal', 'Portugal', 'Poland', 'Tunisia',
             'Morocco', 'Cameroon', 'USA', 'Mexico', 'Wales',
             'Australia',
             'Costa Rica']

list_2022.sort()

#1. as sidebar menu
with st.sidebar:

    selected =option_menu(
        menu_title=0,
        options=["Home","My Team","Battle"],
        icons=["house","dribbble","trophy"],
        menu_icon="cast",
        default_index=0,

    )

if selected == "Home":

    def add_bg_from_url():
        '''Add background image with a link'''
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("https://media.tenor.com/8Q3Y3scvPDsAAAAC/qatar-world-cup.gif");
                background-position: center;
                background-size:contain ;
                background-repeat: no-repeat;
            }}
             </style>
             """,
            unsafe_allow_html=True
         )
    add_bg_from_url()

# background-image: url("https://image.nhandan.vn/w800/Files/Images/2022/04/02/fpnfy6ixmae0udd_1648772051411212-1648834231578.jpg");

if selected == "My Team":
    def add_bg_from_url():
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("https://wallpapercave.com/wp/wp9346588.jpg");
                background-attachment: fixed;
                background-size: cover

            }}
             </style>
             """,
            unsafe_allow_html=True
         )
    add_bg_from_url()

    st.title(f"⚽🏃🏆🎉🎊Welcome To Prediction World Cup 2022 Results of a choosen team 🎊🎉🏆🏃⚽")

    pick_team = st.selectbox(
    "Choose Any team you want",(list_2022)
    )

    params = {
        "name": pick_team
    }

    #TODO
    #put api link
    football_api_url = f'{BASE_URL}/selected_team'

    #TODO
    #To put appropriate prediction like results and where eliminated

    ok = st.button("Results")
    if ok:
        results = []
        response = requests.post(football_api_url,json=params)
        predictions = response.json()

        for prediction in predictions:
            if (predictions[prediction]['Draw'] > predictions[prediction]['Home_win']) and (predictions[prediction]['Draw'] > predictions[prediction]['Away_win']):
                results.append(f"{predictions[prediction]['Home_team']} draws {predictions[prediction]['Away_team']} ⚽⚽⚽\n")
            if (predictions[prediction]['Home_win'] > predictions[prediction]['Draw']) and (predictions[prediction]['Home_win'] > predictions[prediction]['Away_win']):
                results.append(f"{predictions[prediction]['Home_team']} wins against {predictions[prediction]['Away_team']} 😍🎊🥳\n")
            if (predictions[prediction]['Away_win'] > predictions[prediction]['Draw']) and (predictions[prediction]['Away_win'] > predictions[prediction]['Home_win']):
                results.append(f"{predictions[prediction]['Home_team']} loses against {predictions[prediction]['Away_team']} 🫣😱🫠")


        st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">First Match\n: {results[0]} ',unsafe_allow_html=True)
        st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Second Match\n: {results[1]} ',unsafe_allow_html=True)
        st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Third Match\n: {results[2]} ',unsafe_allow_html=True)
        #knockout stage

        #Round of 16
        for i in range (2,len(results)):
            try:
                st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Round Of 16 \n: {results[3]} ',unsafe_allow_html=True)

            except ValueError:
                st.write(f'Eliminated in the Group Stage')
            except IndexError:
                st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Group Stage 😞',unsafe_allow_html=True)
            except :
                st.write(f'Eliminated in the Group Stage')

        #Quarter Final
        for i in range (2,len(results)):
            try:
                st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Quarter Final\n: {results[4]} 🎊🏆⚽🎖️\n',unsafe_allow_html=True)

            except ValueError:
                st.write(f'Eliminated in Round of 16')
            except IndexError:
                st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in Round of 16 😞',unsafe_allow_html=True)
            except :
                st.write(f'Eliminated in Round of 16')

        #Semi Final
        for i in range (2,len(results)):
            try:
                st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Semi Final\n: {results[5]} 🎊🏆⚽🎖️\n',unsafe_allow_html=True)

            except ValueError:
                st.write(f'Eliminated in Semi Final')
            except IndexError:
                st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in Semi Final 😞',unsafe_allow_html=True)
            except :
                st.write(f'Eliminated in Semi Final')

        #Final
        for i in range (2,len(results)):
            try:
                st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Final\n: {results[6]} ',unsafe_allow_html=True)

            except ValueError:
                st.write(f'Loss in the Final')
            except IndexError:
                st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Lost the Final 😞',unsafe_allow_html=True)
            except :
                st.write(f'Loss in the  Final')


# Nice to have as we talked, battle between two teams only, predict the winner
#background-image: url("https://www.aljazeera.com/wp-content/uploads/2022/09/SOR06738.jpg?resize=770%2C513");
if selected == "Battle":

    if 'team1' not in st.session_state:
        st.session_state.team1 = list_2022[0]


    def add_bg_from_url():
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("https://wallpapercave.com/wp/wp10271393.jpg");
                background-attachment: fixed;
                background-size: cover

            }}
             </style>
             """,
            unsafe_allow_html=True
         )
    add_bg_from_url()
    st.title(f"Welcome To the One vs One Showdown")

    Team_1 = st.selectbox(
    "TEAM 1",(list_2022)
    )

    if Team_1:
        st.session_state.team1 = Team_1

    Team_2 = st.selectbox(
    "TEAM 2",(filter(lambda selTeam: selTeam != st.session_state.team1,list_2022))
    )

    API_URL = f'{BASE_URL}/predict'

    params = {
        "matches": [
        {
            "homeTeam": Team_1,
            "awayTeam": Team_2
        }
    ]
}
    win = st.button("Winner")

    if win:
        response = requests.post(API_URL,json=params)
        prediction = response.json()
        st.write(prediction['result'])
    #TODO
    #To put appropriate prediction like probality of win, change to conviance value
    #prob = prediction['probability']


    #if win:

        #winning_team = prob
        #if prob Team_1 > Team_2 :
            #print(f"(Team_1} is the Winner"")
        #elif prob Team_1 < Team_2 :
            #print(f"{Team_2} is the winner")
    #st.subheader(f'🏆 Winner is {pred} 🏆')
