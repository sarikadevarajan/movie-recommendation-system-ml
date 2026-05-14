import streamlit as st
import pickle

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* Background */

.stApp {
    background: linear-gradient(to right, #0F2027, #203A43, #2C5364);
}

/* Hide Streamlit Branding */

#MainMenu, footer, header {
    visibility: hidden;
}

/* Title */

.title {
    text-align: center;
    font-size: 85px;
    font-weight: bold;
    color: #FFD700;
    margin-top: 20px;
}

/* Subtitle */

.subtitle {
    text-align: center;
    font-size: 34px;
    color: white;
    margin-bottom: 50px;
}

/* Selectbox Label */

.stSelectbox label {
    font-size: 32px !important;
    font-weight: bold !important;
    color: white !important;
}

/* Selectbox */

div[data-baseweb="select"] {
    background-color: #1E1E2F !important;
    border-radius: 18px !important;
    min-height: 70px !important;
    border: 2px solid #555 !important;
    overflow: hidden !important;
    box-shadow: none !important;
}

/* Inner Selectbox */

div[data-baseweb="select"] > div {
    background-color: #1E1E2F !important;
    color: white !important;
    font-size: 24px !important;
    border: none !important;
    box-shadow: none !important;
}

/* Focus Effect */

div[data-baseweb="select"]:focus-within {
    border: 2px solid #00FFD1 !important;
    box-shadow: 0 0 10px rgba(0,255,209,0.4) !important;
    outline: none !important;
}

/* Dropdown Text */

.stSelectbox span {
    color: white !important;
    font-size: 22px !important;
}

/* Buttons */

.stButton {
    display: flex;
    justify-content: flex-start;
}

.stButton button {
    background: linear-gradient(to right, #ff416c, #ff4b2b);
    color: white;
    font-size: 28px;
    font-weight: bold;
    height: 75px;
    width: 350px;
    border-radius: 18px;
    border: none;
    transition: 0.3s;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.4);
}

.stButton button:hover {
    transform: scale(1.03);
    color: white;
}

/* Recommendation Title */

.recommend-title {
    text-align: center;
    font-size: 58px;
    font-weight: bold;
    color: #00FFD1;
    margin-top: 60px;
    margin-bottom: 40px;
}

/* Footer */

.footer {
    text-align: center;
    color: lightgray;
    font-size: 22px;
    margin-top: 60px;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LOAD DATA
# =========================================================

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values

# =========================================================
# TITLE
# =========================================================

st.markdown(
    """
    <div class="title">
        🎬 Movie Recommendation System
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
        Discover movies similar to your favorites instantly 🍿
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SELECT MOVIE
# =========================================================

selected_movie = st.selectbox(
    "🎥 Select Your Favorite Movie",
    movie_list,
    key="movie_selectbox"
)

# =========================================================
# RECOMMENDATION FUNCTION
# =========================================================

def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:

        recommended_movies.append({

            "title": movies.iloc[i[0]].title,

            "rating": round(
                movies.iloc[i[0]].vote_average,
                1
            )
        })

    return recommended_movies

# =========================================================
# BUTTON
# =========================================================

if st.button("✨ Recommend Movies", key="recommend_button"):

    recommendations = recommend(selected_movie)

    st.markdown(
        """
        <div class="recommend-title">
            🔥 Recommended Movies
        </div>
        """,
        unsafe_allow_html=True
    )

    for movie in recommendations:

        with st.container(border=True):

            st.markdown(
                f"""
# 🍿 {movie['title']}

### ⭐ Rating: {movie['rating']}/10
                """
            )

            st.write("")

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        
    </div>
    """,
    unsafe_allow_html=True
)