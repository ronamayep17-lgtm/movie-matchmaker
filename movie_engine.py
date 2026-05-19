import streamlit as st
import random
import urllib.parse # Gagamitin natin ito para i-format ang text para sa URL link

# 1. Page Configuration
st.set_page_config(page_title="Movie Matchmaker", page_icon="🎬", layout="centered")

# 2. Ang ating Database ng mga Palabas
movies_database = {
    "Bakbakan / Action 💥": {
        "Movie (Mabilisan)": {
            "Local (Pinoy)": ["BuyBust", "OTJ (On The Job)", "Maria", "AWOL"],
            "Foreign (International)": ["John Wick", "Mad Max: Fury Road", "Extraction", "The Raid"]
        },
        "Series (Commitment)": {
            "Local (Pinoy)": ["FPJ's Ang Probinsyano", "The Iron Heart", "Black Rider"],
            "Foreign (International)": ["Daredevil", "The Punisher", "Reacher", "Gangs of London"]
        }
    },
    "Patayan / Brutal 🩸": {
        "Movie (Mabilisan)": {
            "Local (Pinoy)": ["Bliss", "Eerie", "Kampon", "In My Mother's Skin"],
            "Foreign (International)": ["Saw", "The Texas Chainsaw Massacre", "Kill Bill", "Terrifier"]
        },
        "Series (Commitment)": {
            "Local (Pinoy)": ["Cattleya Killer"],
            "Foreign (International)": ["Dahmer", "Hannibal", "Squid Game", "Alice in Borderland"]
        }
    },
    "Mind-Blow / Patalasan ng Isip 🧠": {
        "Movie (Mabilisan)": {
            "Local (Pinoy)": ["Honor Thy Father", "Fan Girl", "Goyo", "Kamera Obskura"],
            "Foreign (International)": ["Inception", "Interstellar", "Shutter Island", "The Invisible Guest"]
        },
        "Series (Commitment)": {
            "Local (Pinoy)": ["Dirty Linen", "Senior High"],
            "Foreign (International)": ["Dark", "Breaking Bad", "Sherlock", "Severance"]
        }
    },
    "Sawi / Hugot 💔": {
        "Movie (Mabilisan)": {
            "Local (Pinoy)": ["Starting Over Again", "That Thing Called Tadhana", "The Hows of Us", "Sid & Aya"],
            "Foreign (International)": ["500 Days of Summer", "La La Land", "Eternal Sunshine of the Spotless Mind", "Past Lives"]
        },
        "Series (Commitment)": {
            "Local (Pinoy)": ["On the Wings of Love", "Replacing Chef Chico", "Linlang"],
            "Foreign (International)": ["Twenty-Five Twenty-One", "Crash Landing on You", "Normal People", "One Day"]
        }
    },
    "Masaya / Good Vibes 😂": {
        "Movie (Mabilisan)": {
            "Local (Pinoy)": ["Ang Tanging Ina", "Kimmy Dora", "Seven Sundays", "Sisterakas"],
            "Foreign (International)": ["The Hangover", "White Chicks", "Superbad", "Free Guy"]
        },
        "Series (Commitment)": {
            "Local (Pinoy)": ["Pepito Manaloto", "Can't Buy Me Love", "Team A"],
            "Foreign (International)": ["Friends", "The Office", "Modern Family", "Brooklyn Nine-Nine"]
        }
    },
    "Takot / Kilabot 👻": {
        "Movie (Mabilisan)": {
            "Local (Pinoy)": ["Feng Shui", "Sukob", "Seklusyon"],
            "Foreign (International)": ["The Conjuring", "Hereditary", "Insidious", "A Quiet Place"]
        },
        "Series (Commitment)": {
            "Local (Pinoy)": ["Simula sa Gitna"],
            "Foreign (International)": ["The Haunting of Hill House", "Stranger Things", "All of Us Are Dead"]
        }
    }
}

# Gagamit tayo ng Streamlit session state para matandaan ng system yung huling lumabas na movie kapag may na-click na ibang button.
if "final_recommendation" not in st.session_state:
    st.session_state.final_recommendation = None

# 3. Web App UI Design
st.title("🎬 Movie & Series Recommendation Engine")
st.write("Feeling lost kung anong papanoorin? Sagutin mo lang itong 3 mabilisang tanong, bes!")

st.divider()

# Tanong 1: Mood
mood_list = list(movies_database.keys())
selected_mood = st.selectbox("1. Ano ang mood mo ngayon?", mood_list)

# Tanong 2: Format
format_list = list(movies_database[selected_mood].keys())
selected_format = st.selectbox("2. Anong format ang trip mo?", format_list)

# Tanong 3: Origin
origin_list = list(movies_database[selected_mood][selected_format].keys()) + ["Kahit ano / Surprise Me 🎲"]
selected_origin = st.selectbox("3. Gawang Pinoy o Pang-International?", origin_list)

st.divider()

# Ang Button para sa Rekomendasyon
if st.button("✨ HANAPAN MO AKO NG PAPANOORIN! ✨", use_container_width=True):
    with st.spinner("Naghahanap sa database..."):
        if selected_origin == "Kahit ano / Surprise Me 🎲":
            choices = (movies_database[selected_mood][selected_format]["Local (Pinoy)"] + 
                       movies_database[selected_mood][selected_format]["Foreign (International)"])
        else:
            choices = movies_database[selected_mood][selected_format][selected_origin]
            
        st.session_state.final_recommendation = random.choice(choices)
    st.balloons()

# Kung may napili nang movie, ipapakita natin ang resulta kasama ang mga MAGIC BUTTONS!
if st.session_state.final_recommendation:
    movie_name = st.session_state.final_recommendation
    
    st.success(f"### 🎉 Ang swak sa mood mo ngayon ay:")
    st.info(f"## 🏆 **{movie_name}**")
    
    st.write("👉 **WHERE DO YOU WANNA WATCH? PICK A BUTTON BELOW👇:**")
    
    # Dito natin kino-convert ang pangalan ng palabas para maging clickable link (halimbawa: "John Wick" -> "John+Wick")
    encoded_movie = urllib.parse.quote_plus(movie_name)
    
    # Gumawa ng 3 Columns para magkakatabi ang mga buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Button 1: Automatic Google Search para makita kung saan streaming
        google_url = f"https://www.google.com/search?q=where+to+watch+{encoded_movie}"
        st.link_button("🔍 nasaan ito streaming?", google_url, use_container_width=True)
        
    with col2:
        # Button 2: Diretso search sa loob ng Netflix web
        netflix_url = f"https://www.netflix.com/search?q={encoded_movie}"
        st.link_button("❤️ I-Search sa Netflix", netflix_url, use_container_width=True)
        
    with col3:
        # Button 3: Diretso search sa YouTube (para sa mga Pinoy movies/trailers)
        youtube_url = f"https://www.youtube.com/results?search_query={encoded_movie}+full+movie+or+trailer"
        st.link_button("📺 I-Search sa YouTube", youtube_url, use_container_width=True)

    st.write("\n_Ihanda mo na ang popcorn at pwesto sa kama! Enjoy watching! 🍿🥤_")