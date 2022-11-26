from pathlib import Path
import streamlit as st
import os
import requests
import streamlit as st
from streamlit_option_menu import option_menu

# --- Global settings ---
PAGE_TITLE = 'FIFA World Cup - Qatar 2022'
PAGE_ICON = '⚽️'
BASE_URL = "https://qatar-2022-api.clement.cloud"

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

        #group_elim = [
            #'Qatar','Ecuador','Iran','USA','Saudi Arabia','Poland',
            #'Australia','Tunisia','Costa Rica','Japan','Canada','Morocco',
            #'Switzerland','Cameroon','Ghana','Korea Republic'
            #]
        #group elimination
        if pick_team == 'Qatar':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Group Stage 😞',unsafe_allow_html=True)

        if pick_team == 'Ecuador':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Group Stage 😞',unsafe_allow_html=True)

        if pick_team == 'Iran':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Group Stage 😞',unsafe_allow_html=True)

        if pick_team == 'USA':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Group Stage 😞',unsafe_allow_html=True)

        if pick_team == 'Saudi Arabia':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Group Stage 😞',unsafe_allow_html=True)

        if pick_team == 'Poland':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Group Stage 😞',unsafe_allow_html=True)

        if pick_team == 'Australia':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Group Stage 😞',unsafe_allow_html=True)

        if pick_team == 'Costa Rica':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Group Stage 😞',unsafe_allow_html=True)

        if pick_team == 'Japan':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Group Stage 😞',unsafe_allow_html=True)

        if pick_team == 'Canada':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Group Stage 😞',unsafe_allow_html=True)

        if pick_team == 'Morocco':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Group Stage 😞',unsafe_allow_html=True)

        if pick_team == 'Switzerland':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Group Stage 😞',unsafe_allow_html=True)

        if pick_team == 'Cameroon':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Group Stage 😞',unsafe_allow_html=True)

        if pick_team == 'Ghana':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Group Stage 😞',unsafe_allow_html=True)

        if pick_team == 'Korea Republic':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Group Stage 😞',unsafe_allow_html=True)


        if pick_team == 'Netherlands':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Round of 16\n: Netherlands wins against Wales 😍🎊🥳',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Quarter Final\n: Netherlands wins against Argentina 😍🎊🥳',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Semi Final\n: Netherlands loss against England 😞',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the semi final 😞',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Third Place\n: Netherlands loss against Portugal for third place in this competition 😞',unsafe_allow_html=True)


        if pick_team == 'Argentina':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Round of 16\n: Argentina wins against Denmark 😍🎊🥳',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Quarter Final\n: Argentina loss against Netherlands 😞',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Quarter Final 😞',unsafe_allow_html=True)


        if pick_team == 'Spain':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Round of 16\n: Spain wins against Croatia 😍🎊🥳',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Quarter Final\n: Argentina loss against Brazil 😞',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Quarter Final 😞',unsafe_allow_html=True)


        if pick_team == 'Croatia':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Round of 16 \n: Croatia loss against Spain 😞',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Round of 16 😞',unsafe_allow_html=True)

        if pick_team == 'Brazil':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Round of 16\n: Brazil wins against Uruguay 😍🎊🥳',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Quarter Final\n: Brazil wins against Spain 😍🎊🥳',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Semi Final\n: Brazil wins against Portugal 😍🎊🥳',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Final\n: Brazil wins against England 😍🎊🥳',unsafe_allow_html=True)


        if pick_team == 'Uruguay':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Round of 16 \n: Croatia loss against Spain 😞',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Round of 16 😞',unsafe_allow_html=True)

        if pick_team == 'Wales':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Round of 16 \n: Wales loss against Netherlands 😞',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Round of 16 😞',unsafe_allow_html=True)

        if pick_team == 'England':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Round of 16\n: England wins against Senegal 😍🎊🥳',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Quarter Final\n: England wins against France 😍🎊🥳',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Semi Final\n: England wins against Netherland 😍🎊🥳',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Final\n: England loss against Brazil 😞',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">🥈 England Runner up in the world cup 2022, 2nd Place in the competitions 🥈',unsafe_allow_html=True)

        if pick_team == 'France':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Round of 16\n: France wins against Mexico 😍🎊🥳',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Quarter Final\n: France loss against England 😞',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Quarter Final 😞',unsafe_allow_html=True)


        if pick_team == 'Belgium':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Round of 16\n: Belgium wins against Germany 😍🎊🥳',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Quarter Final\n: Belgium loss against Portugal 😞',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Quarter Final 😞',unsafe_allow_html=True)

        if pick_team == 'Portugal':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Round of 16\n: Portugal wins against Serbia 😍🎊🥳',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Quarter Final\n: Portugal wins against Belgium 😍🎊🥳',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Semi Final\n: Portugal loss against Brazil 😞',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the semi final 😞',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Third Place\n: Portugal wins against Netherlands 😍🎊🥳',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">🥉 Portugal gets  3rd place in the competition 🥉 ',unsafe_allow_html=True)

        if pick_team == 'Senegal':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Round of 16 \n: Senegal loss against England 😞',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Round of 16 😞',unsafe_allow_html=True)

        if pick_team == 'Mexico':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Round of 16 \n: Mexico loss against France 😞',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Round of 16 😞',unsafe_allow_html=True)

        if pick_team == 'Germany':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Round of 16 \n: Germany loss against Belgium 😞',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Round of 16 😞',unsafe_allow_html=True)


        if pick_team == 'Serbia':
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Round of 16 \n: Serbia loss against Portugal 😞',unsafe_allow_html=True)
            st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Round of 16 😞',unsafe_allow_html=True)


        #Round of 16
        #round_16 = []
        #if pick_team == round_16:
            #st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Round of 16\n: {round_16} ',unsafe_allow_html=True)
        #elif pick_team != round_16:
            #st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Group Stage 😞',unsafe_allow_html=True)
        #else:
            #None




        #for i in range (2,len(results)):
            #try:
                #st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Round Of 16 \n: {results[3]} ',unsafe_allow_html=True)

            #except ValueError:
                #st.write(f'Eliminated in the Group Stage')
            #except IndexError:
               #st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Group Stage 😞',unsafe_allow_html=True)
            #except :
                #st.write(f'Eliminated in the Group Stage')

        #Quarter Final
        #quarter_final= []
        #if pick_team == quarter_final:
            #st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Quarter Final\n: {quarter_final} ',unsafe_allow_html=True)
        #elif pick_team != quarter_final:
            #st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Quarter Final😞',unsafe_allow_html=True)
        #else:
            #None

        #for i in range (2,len(results)):
            #try:
                #st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Quarter Final\n: {results[4]} 🎊🏆⚽🎖️\n',unsafe_allow_html=True)

            #except ValueError:
                #st.write(f'Eliminated in Semi Final')
            #except IndexError:
                #st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in Quarter Final 😞',unsafe_allow_html=True)
            #except :
                #st.write(f'Eliminated in Semi Final')


        #for i in range (2,len(results)):
            #try:
                #st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Quarter Final\n: {results[5]} 🎊🏆⚽🎖️\n',unsafe_allow_html=True)

            #except ValueError:
                #st.write(f'Eliminated in Round of 16')
            #except IndexError:
                #st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in Round of 16 😞',unsafe_allow_html=True)
            #except :
                #st.write(f'Eliminated in Round of 16')

        #Semi Final
        #semi_final =[]
        #if pick_team == semi_final:
            #st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Semi Final\n: {semi_final} ',unsafe_allow_html=True)
        #elif pick_team != semi_final:
            #st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in the Semi Final😞',unsafe_allow_html=True)
        #else:
            #None

        #for i in range (2,len(results)):
            #try:
                #st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Semi Final\n: {results[6]} 🎊🏆⚽🎖️\n',unsafe_allow_html=True)

            #except ValueError:
                #st.write(f'Eliminated in Semi Final')
            #except IndexError:
                #st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Eliminated in Semi Final 😞',unsafe_allow_html=True)
            #except :
               # st.write(f'Eliminated in Semi Final')

        #Final
        #first_place =[]
        #if pick_team == first_place:
            #st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Final\n: {first_place} ',unsafe_allow_html=True)
        #elif pick_team != first_place:
            #st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Runner Up  😭',unsafe_allow_html=True)
        #else:
            #None

        #for i in range (2,len(results)):
            #try:
               # st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Final\n: {results[6]} ',unsafe_allow_html=True)

            #except ValueError:
                #st.write(f'Loss in the Final')
            #except IndexError:
                #st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Lost the Final 😞',unsafe_allow_html=True)
            #except :
                #st.write(f'Loss in the  Final')

        #Third place
        #Third_place =[]
        #if pick_team == Third_place:
            #st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Third Place\n: {Third_place} ',unsafe_allow_html=True)
        #else:
            #st.write(f'<h1 style="color:black;font-size:20px;font-family: Comic Sans MS;">Fourth Place 😑',unsafe_allow_html=True)


        #Fun game
        #expander to guess if team won the world cup
        with st.expander(f'Wanna guess if this team Will Win the World Cup ? 🤔'):
            if pick_team != 'Brazil':
                st.write(f'<h1 style="color:red;font-size:15px;font-family: Comic Sans MS;">No ❌, Try Again with Brazil ❓❓❓',unsafe_allow_html=True)
            else:
                st.write(f'<h1 style="color:orange;font-size:15px;font-family: Comic Sans MS;">Yes, You Win 🤩, Lucky Guess ✅',unsafe_allow_html=True)
                st.image("https://i.ytimg.com/vi/509d5MIR7FY/maxresdefault.jpg")

            st.write(f'<h1 style="color:yellow;font-size:px;font-family: Comic Sans MS;">🏆 🎊 The Winner of FIFA World Cup 2022 is Brazil 🇧🇷 🎊 🏆',unsafe_allow_html=True)


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
    st.title(f"Welcome To the One vs One Showdown 🤜✊🤛👊")

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
    win = st.button("Result")

    if win:
        response = requests.post(API_URL,json=params)
        prediction = response.json()
        winner = prediction['result']
        st.write(f'<h1 style="color:smokie-white;font-size:25px;font-family: Comic Sans MS;">⚽ {winner} ⚽',unsafe_allow_html=True)
