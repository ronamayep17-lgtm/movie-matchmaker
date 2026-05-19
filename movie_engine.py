import streamlit as st
import random
import urllib.parse

# 1. Page Configuration
st.set_page_config(page_title="Movie Matchmaker", page_icon="🎬", layout="centered")

# 2. Ang Mas Pinahabang Database (Malinis at walang sumasablay na link!)
movies_database = {
    "Animated / Cartoon 🦄": {
        "Movie (Mabilisan)": {
            "Local (Pinoy)": ["Saving Sally", "Hayop Ka! The Nimfa Dimaano Story", "Urduja", "Dayo: Sa Mundo ng Elementalia"],
            "Foreign (International)": [
                "Spiderman: Into the Spider-Verse", "Shrek", "Howl's Moving Castle", "Inside Out 2", 
                "Demon Slayer: Mugen Train", "Toy Story", "The Lion King", "Kung Fu Panda", 
                "Coco", "Frozen", "Despicable Me", "Ratatouille", "Moana", "Zootopia", 
                "Puss in Boots: The Last Wish", "The Super Mario Bros. Movie", "Nimona", "Soul"
            ]
        },
        "Series (Commitment)": {
            "Local (Pinoy)": ["Barangay 143"],
            "Foreign (International)": [
                "Arcane", "Attack on Titan", "Cyberpunk: Edgerunners", "Rick and Morty", 
                "Avatar: The Last Airbender", "Ben 10", "Jujutsu Kaisen", "Demon Slayer", 
                "Invincible", "Castlevania", "The Legend of Vox Machina", "Blue Eye Samurai"
            ]
        }
    },
    "Bakbakan / Action 💥": {
        "Movie (Mabilisan)": {
            "Local (Pinoy)": ["BuyBust", "OTJ (On The Job)", "Maria", "AWOL"],
            "Foreign (International)": [
                "John Wick", "Mad Max: Fury Road", "Extraction", "The Raid", "Top Gun: Maverick", 
                "Gladiator", "The Batman", "Nobody", "Bullet Train", "The Gray Man", "Deadpool"
            ]
        },
        "Series (Commitment)": {
            "Local (Pinoy)": ["FPJ's Ang Probinsyano", "The Iron Heart", "Black Rider"],
            "Foreign (International)": [
                "Daredevil", "The Punisher", "Reacher", "Gangs of London", "The Boys", 
                "Loki", "The Terminal List", "Warrior", "Peaky Blinders"
            ]
        }
    },
    "Patayan / Brutal 🩸": {
        "Movie (Mabilisan)": {
            "Local (Pinoy)": ["Bliss", "Eerie", "Kampon", "In My Mother's Skin"],
            "Foreign (International)": [
                "Saw", "The Texas Chainsaw Massacre", "Kill Bill", "Terrifier", "Hostel", 
                "The Sadness", "Project Wolf Hunting", "Evil Dead Rise", "Midsommar"
            ]
        },
        "Series (Commitment)": {
            "Local (Pinoy)": ["Cattleya Killer"],
            "Foreign (International)": [
                "Dahmer", "Hannibal", "Squid Game", "Alice in Borderland", "Dexter", 
                "The Walking Dead", "Gannibal", "Chucky"
            ]
        }
    },
    "Thriller / Kaba 🤫": {
        "Movie (Mabilisan)": {
            "Local (Pinoy)": ["Arisaka", "Dead Kids", "Untrue", "Nuuk"],
            "Foreign (International)": [
                "Get Out", "Prisoners", "Gone Girl", "A Quiet Place", "Parasite", 
                "The Invisible Man", "Leave the World Behind", "Nightcrawler", "Shutter Island"
            ]
        },
        "Series (Commitment)": {
            "Local (Pinoy)": ["Linlang", "Lavender Fields"],
            "Foreign (International)": [
                "You", "Mindhunter", "Stranger Things", "The Glory", "The Last of Us", 
                "Presumed Innocent", "Black Mirror", "Severance"
            ]
        }
    },
    "Sci-Fi / Science Fiction 🚀": {
        "Movie (Mabilisan)": {
            "Local (Pinoy)": ["Instalado", "Respeto"],
            "Foreign (International)": [
                "Inception", "Interstellar", "The Matrix", "Dune: Part Two", "Avatar: The Way of Water", 
                "Blade Runner 2049", "Tenet", "Everything Everywhere All at Once", "The Creator", "Prey"
            ]
        },
        "Series (Commitment)": {
            "Local (Pinoy)": ["Mystified"],
            "Foreign (International)": [
                "Dark", "Black Mirror", "The 100", "Love, Death & Robots", "Fallout", 
                "3 Body Problem", "The Mandalorian", "Foundation", "Silo"
            ]
        }
    },
    "Sexy / Hubaran 🔥": {
        "Movie (Mabilisan)": {
            "Local (Pinoy)": ["Silip sa Apoy", "Scorpio Nights", "Taya", "Selina's Gold"],
            "Foreign (International)": [
                "365 Days", "Fifty Shades of Grey", "The Voyeurs", "Wild Things", "Basic Instinct", 
                "The Wolf of Wall Street", "Chloe", "Deep Water", "No Hard Feelings"
            ]
        },
        "Series (Commitment)": {
            "Local (Pinoy)": ["Iskandalo", "High on Sex"],
            "Foreign (International)": [
                "Sex/Life", "Bridgerton", "Elite", "Obsession", "The Idol", 
                "Euphoria", "Game of Thrones", "Spartacus"
            ]
        }
    },
    "Mind-Blow / Patalasan ng Isip 🧠": {
        "Movie (Mabilisan)": {
            "Local (Pinoy)": ["Honor Thy Father", "Fan Girl", "Goyo"],
            "Foreign (International)": [
                "Shutter Island", "The Invisible Guest", "Memento", "The Prestige", 
                "The Usual Suspects", "Fight Club", "Knives Out", "Glass Onion"
            ]
        },
        "Series (Commitment)": {
            "Local (Pinoy)": ["Dirty Linen", "Senior High"],
            "Foreign (International)": [
                "Breaking Bad", "Sherlock", "Severance", "Mr. Robot", "Better Call Saul", 
                "True Detective", "Succession"
            ]
        }
    },
    "Sawi / Hugot 💔": {
        "Movie (Mabilisan)": {
            "Local (Pinoy)": ["Starting Over Again", "That Thing Called Tadhana", "The Hows of Us"],
            "Foreign (International)": [
                "500 Days of Summer", "La La Land", "Eternal Sunshine of the Spotless Mind", 
                "Past Lives", "The Fault in Our Stars", "A Star Is Born", "About Time"
            ]
        },
        "Series (Commitment)": {
            "Local (Pinoy)": ["Replacing Chef Chico"],
            "Foreign (International)": [
                "Twenty-Five Twenty-One", "Crash Landing on You", "Normal People", 
                "One Day", "Fleabag", "Queen of Tears"
            ]
        }
    },
    "Masaya / Good Vibes 😂": {
        "Movie (Mabilisan)": {
            "Local (Pinoy)": ["Ang Tanging Ina", "Kimmy Dora", "Seven Sundays"],
            "Foreign (International)": [
                "The Hangover", "White Chicks", "Superbad", "Free Guy", "Barbie", 
                "Red Notice", "We're the Millers", "Central Intelligence"
            ]
        },
        "Series (Commitment)": {
            "Local (Pinoy)": ["Pepito Manaloto"],
            "Foreign (International)": [
                "Friends", "The Office", "Modern Family", "Brooklyn Nine-Nine", 
                "Ted Lasso", "The Bear", "Abbott Elementary", "Young Sheldon"
            ]
        }
    },
    "Takot / Kilabot 👻": {
        "Movie (Mabilisan)": {
            "Local (Pinoy)": ["Feng Shui", "Sukob", "Seklusyon"],
            "Foreign (International)": [
                "The Conjuring", "Hereditary", "Insidious", "Talk to Me", "Smile", 
                "The Nun", "A Nightmare on Elm Street", "Barbarian", "Late Night with the Devil"
            ]
        },
        "Series (Commitment)": {
            "Local (Pinoy)": ["Simula sa Gitna"],
            "Foreign (International)": [
                "The Haunting of Hill House", "Stranger Things", "All of Us Are Dead", 
                "Midnight Mass", "From", "The Fall of the House of Usher"
            ]
        }
    }
}

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

# Kung may napili nang movie, ipapakita ang resulta kasama ang mga link buttons
if st.session_state.final_recommendation:
    movie_name = st.session_state.final_recommendation
    
    st.success(f"### 🎉 Ang swak sa mood mo ngayon ay:")
    st.info(f"## 🏆 **{movie_name}**")
    
    st.write("👉 **Pumili ng platform sa ibaba para hanapin at mapanood ang palabas:**")
    
    # Gagamit ng pinaka-stable na URL encoding para sa tatlong pangunahing platform
    encoded_movie_query = urllib.parse.quote_plus(movie_name)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        google_url = f"https://www.google.com/search?q=where+to+watch+{encoded_movie_query}"
        st.link_button("🔍 Saan lilitaw? (Google)", google_url, use_container_width=True)
    with col2:
        netflix_url = f"https://www.netflix.com/search?q={encoded_movie_query}"
        st.link_button("❤️ Netflix Search", netflix_url, use_container_width=True)
    with col3:
        youtube_url = f"https://www.youtube.com/results?search_query={encoded_movie_query}+full+movie"
        st.link_button("📺 YouTube Search", youtube_url, use_container_width=True)

    st.write("\n_Ihanda mo na ang popcorn at pwesto sa kama! Enjoy watching! 🍿🥤_")
