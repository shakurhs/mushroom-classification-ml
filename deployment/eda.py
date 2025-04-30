import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image

def run():

    # membuat title
    st.title('Survival Guide: "Is This *Shroom* Edible?" ')

    # membuat subtitle 
    st.subheader('Aplikasi Petunjuk dalam memilih Spesies Jamur yang dapat Dikonsumsi')

    # input gambar
    image = Image.open('mushroom_bg.jpg')
    st.image(image, caption='Ilustrasi Jamur Liar')

    st.write('## Exploratory Data Analysis')

    # data laoding
    df = pd.read_csv("https://huggingface.co/spaces/shakurhs/Predict_Edible_Mushroom/raw/main/secondary_data.csv", delimiter=';')
    
    # menngubah nama kolom
    df.columns = [col.replace('-','_') for col in df.columns]
    

    # mengganti inisial menjadi value yang lebih jelas
    class_mapping = {'e': 'edible', 'p': 'poisonous'}
    cap_shape_mapping = {'b': 'bell', 'c': 'conical', 'x': 'convex', 'f': 'flat', 's': 'sunken', 'p': 'spherical', 'o': 'others'}
    cap_surface_mapping = {'i': 'fibrous', 'g': 'grooves', 'y': 'scaly', 's': 'smooth', 'h': 'shiny', 'l': 'leathery', 'k': 'silky', 't': 'sticky', 'w': 'wrinkled', 'e': 'fleshy', 'd': 'dry'}
    cap_color_mapping = {'n': 'brown', 'b': 'buff', 'g': 'gray', 'r': 'green', 'p': 'pink', 'u': 'purple', 'e': 'red', 'w': 'white', 'y': 'yellow', 'l': 'blue', 'o': 'orange', 'k': 'black'}
    does_bruise_or_bleed_mapping = {'t': 'yes', 'f': 'no'}
    gill_attachment_mapping = {'a': 'adnate', 'x': 'adnexed', 'd': 'decurrent', 'e': 'free', 's': 'sinuate', 'p': 'pores', 'f': 'none'}
    gill_spacing_mapping = {'c': 'close', 'd': 'distant', 'f': 'none'}
    gill_color_mapping = {'n': 'brown', 'b': 'buff', 'g': 'gray', 'r': 'green', 'p': 'pink', 'u': 'purple', 'e': 'red', 'w': 'white', 'y': 'yellow', 'l': 'blue', 'o': 'orange', 'k': 'black', 'f': 'none'}
    stem_root_mapping = {'b': 'bulbous', 's': 'swollen', 'c': 'club', 'e': 'equal', 'z': 'rhizomorphs', 'r': 'rooted'}
    stem_surface_mapping = {'i': 'fibrous', 'g': 'grooves', 'y': 'scaly', 's': 'smooth', 'h': 'shiny', 'l': 'leathery', 'k': 'silky', 't': 'sticky', 'w': 'wrinkled', 'e': 'fleshy', 'f': 'none'}
    stem_color_mapping = {'n': 'brown', 'b': 'buff', 'g': 'gray', 'r': 'green', 'p': 'pink', 'u': 'purple', 'e': 'red', 'w': 'white', 'y': 'yellow', 'l': 'blue', 'o': 'orange', 'k': 'black', 'f': 'none'}
    veil_type_mapping = {'p': 'partial', 'u': 'universal'}
    veil_color_mapping = {'n': 'brown', 'b': 'buff', 'g': 'gray', 'r': 'green', 'p': 'pink', 'u': 'purple', 'e': 'red', 'w': 'white', 'y': 'yellow', 'l': 'blue', 'o': 'orange', 'k': 'black', 'f': 'none'}
    has_ring_mapping = {'t': 'yes', 'f': 'no'}
    ring_type_mapping = {'c': 'cobwebby', 'e': 'evanescent', 'r': 'flaring', 'g': 'grooved', 'l': 'large', 'p': 'pendant', 's': 'sheathing', 'z': 'zone', 'm': 'movable', 'f': 'none'}
    spore_print_color_mapping = {'n': 'brown', 'b': 'buff', 'g': 'gray', 'r': 'green', 'p': 'pink', 'u': 'purple', 'e': 'red', 'w': 'white', 'y': 'yellow', 'l': 'blue', 'o': 'orange', 'k': 'black', 'f': 'none'}
    habitat_mapping = {'g': 'grasses', 'l': 'leaves', 'm': 'meadows', 'p': 'paths', 'h': 'heaths', 'u': 'urban', 'w': 'waste', 'd': 'woods'}
    season_mapping = {'s': 'spring', 'u': 'summer', 'a': 'autumn', 'w': 'winter'}

    # Apply the mappings to the respective columns
    # df['class'] = df['class'].replace(class_mapping)
    # df['cap_shape'] = df['cap_shape'].replace(cap_shape_mapping)
    # df['cap_surface'] = df['cap_surface'].replace(cap_surface_mapping)
    # df['cap_color'] = df['cap_color'].replace(cap_color_mapping)
    # df['does_bruise_or_bleed'] = df['does_bruise_or_bleed'].replace(does_bruise_or_bleed_mapping)
    # df['gill_attachment'] = df['gill_attachment'].replace(gill_attachment_mapping)
    # df['gill_spacing'] = df['gill_spacing'].replace(gill_spacing_mapping)
    # df['gill_color'] = df['gill_color'].replace(gill_color_mapping)
    # df['stem_root'] = df['stem_root'].replace(stem_root_mapping)
    # df['stem_surface'] = df['stem_surface'].replace(stem_surface_mapping)
    # df['stem_color'] = df['stem_color'].replace(stem_color_mapping)
    # df['veil_type'] = df['veil_type'].replace(veil_type_mapping)
    # df['veil_color'] = df['veil_color'].replace(veil_color_mapping)
    # df['has_ring'] = df['has_ring'].replace(has_ring_mapping)
    # df['ring_type'] = df['ring_type'].replace(ring_type_mapping)
    # df['spore_print_color'] = df['spore_print_color'].replace(spore_print_color_mapping)
    # df['habitat'] = df['habitat'].replace(habitat_mapping)
    # df['season'] = df['season'].replace(season_mapping)

    df['class'].replace(class_mapping, inplace=True)
    df['cap_shape'].replace(cap_shape_mapping, inplace=True)
    df['cap_surface'].replace(cap_surface_mapping, inplace=True)
    df['cap_color'].replace(cap_color_mapping, inplace=True)
    df['does_bruise_or_bleed'].replace(does_bruise_or_bleed_mapping, inplace=True)
    df['gill_attachment'].replace(gill_attachment_mapping, inplace=True)
    df['gill_spacing'].replace(gill_spacing_mapping, inplace=True)
    df['gill_color'].replace(gill_color_mapping, inplace=True)
    df['stem_root'].replace(stem_root_mapping, inplace=True)
    df['stem_surface'].replace(stem_surface_mapping, inplace=True)
    df['stem_color'].replace(stem_color_mapping, inplace=True)
    df['veil_type'].replace(veil_type_mapping, inplace=True)
    df['veil_color'].replace(veil_color_mapping, inplace=True)
    df['has_ring'].replace(has_ring_mapping, inplace=True)
    df['ring_type'].replace(ring_type_mapping, inplace=True)
    df['spore_print_color'].replace(spore_print_color_mapping, inplace=True)
    df['habitat'].replace(habitat_mapping, inplace=True)
    df['season'].replace(season_mapping, inplace=True)

    # menghapus data terduplikat
    df = df.drop_duplicates()

    # menampilkan dataframe
    st.write('#### Raw Mushroom Dataset')
    st.dataframe(df)
    

    # membuat plot
    categorical_column = df.select_dtypes(include=['object']).columns
    categorical_column = st.selectbox('#### Bar Chart of:', ('class', 'cap_shape', 'cap_surface', 'cap_color',
    'does_bruise_or_bleed', 'gill_attachment', 'gill_spacing', 'gill_color',
    'stem_root', 'stem_surface', 'stem_color', 'veil_type', 'veil_color',
    'has_ring', 'ring_type', 'spore_print_color', 'habitat', 'season'))
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x=categorical_column, data=df, color='skyblue')
    plt.grid(True)
    st.pyplot(fig)
    st.write('Menampilkan grafik Bar Chart dari kolom data Categorical')
    

    # membuat histogram
    option = st.selectbox('#### Histogram of:', ('cap_diameter', 'stem_width', 'stem_height'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(df[option], bins=30, kde=True)
    plt.axvline(x = df[option].median(), color='yellow', label = 'Median')
    plt.axvline(x = df[option].mean(), color = 'red', label = 'Mean')
    plt.legend()
    plt.grid(True)
    st.pyplot(fig)
    st.write('Menampilkan grafik Histogram dari kolom data Continuous')

    st.write('#### Statistika Deskriptif Data Continuous')
    # statistika deskriptif
    desc = df.describe()
    st.dataframe(desc)

    # membuat plot menggunakan plotly
    st.write('#### Plot Perbandingan Attribute stem_height dengan stem_width')
    fig = px.scatter(df, x='stem_height', y='stem_width', hover_data=['class'])
    plt.grid(True)
    st.plotly_chart(fig)
    st.write('Kedua variabel memiliki nilai korelasi yang dihitung menggunakan metode Spearman dengan score: 0.498')

if __name__ == '__main__':
    run()