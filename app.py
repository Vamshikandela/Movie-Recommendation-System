import streamlit as st
import pandas as pd
import joblib

similarity = joblib.load('movierecommendation.pkl')


df = pd.read_csv('tmdbdf.csv')
#df=df.head(5000)


st.image('netflix.jpeg',use_column_width=True)
st.title(' Netflix Movie Recommendation')

# Movie selection
movie_name = st.selectbox('Select the Movie', df['title'].values)

def recommend(movie):
    movie_index = df[df['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movie = []
    recommend_poster = []

    for tag in movie_list:
        recommend_movie.append(df.iloc[tag[0]].title)
        poster = df.iloc[tag[0]]['poster_path']
        if pd.notnull(poster):
            recommend_poster.append('https://image.tmdb.org/t/p/w500/' + poster)
        else:
            recommend_poster.append('https://via.placeholder.com/500x750?text=No+Poster')

    return recommend_poster, recommend_movie

if st.button('Click here for getting similar movies'):
    posters, names = recommend(movie_name)

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.header(names[idx])
            st.image(posters[idx])