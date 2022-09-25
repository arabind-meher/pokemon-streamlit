import streamlit as st
from pokemon import Pokemon

st.set_page_config(layout='wide')

if __name__ == '__main__':
    pokemon = Pokemon()

    st.title('Pokemon')

    st.sidebar.title('PokeTypes')

    poke_types = ('Any', 'Normal', 'Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Fighting', 'Poison',
        'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dark', 'Dragon', 'Steel', 'Fairy')

    poke_type_1 = st.sidebar.selectbox(
        'Select a Pokemon primary typing.', poke_types)

    poke_type_2 = st.sidebar.selectbox(
        'Select a Pokemon secondary typing.', poke_types )
    
    if st.sidebar.button('Filter'):
        pokemon_df = pokemon.get_pokemon_from_type(poke_type_1, poke_type_2)
        st.table(pokemon_df)