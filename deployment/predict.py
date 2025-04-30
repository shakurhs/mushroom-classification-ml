import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title='Predict Edible Mushroom',
    initial_sidebar_state='expanded'
)


# loading best model dari file pickle
with open('best_rf_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def run():
    st.title('"Is this *Shroom* Edible?"')
    st.subheader('Input Data untuk Mendapatkan Hasil Prediksi!')
    with st.form(key='Mushroom_Prediction'):
        cap_diameter = st.slider('Diameter of Cap (cm)', min_value= 0.35, max_value = 24.0, value=6.7)
        cap_shape = st.selectbox('Shape of Cap',('bell', 'conical','convex','flat','sunken','spherical','others'))
        cap_surface = st.selectbox('Surface of Cap', ('fibrous','grooves','scaly','smooth','shiny','leathery','silky','sticky','wrinkled','fleshy'))
        cap_color = st.selectbox('Color of Cap', ('brown','buff','gray','green','pink','purple','red','white','yellow','blue','orange','black'))
        does_bruise_or_bleed = st.radio('Bruise or Bleed', ('yes', 'no'))
        gill_attachment = st.selectbox('Gill Attachment', ('adnate','adnexed','decurrent','free','sinuate','pores','none'))
        gill_spacing = st.radio('Gill Spacing', ('close','distant','none'))
        gill_color = st.selectbox('Color of Gill', ('brown','buff','gray','green','pink','purple','red','white','yellow','blue','orange','black'))
        stem_height = st.slider('Height of Stem (cm)', min_value= 0.0, max_value = 17.5, value=6.5)
        stem_width = st.slider('Width of Stem (cm)', min_value= 0.0, max_value = 50.0, value=12.0)
        stem_color = st.selectbox('Color of Stem', ('brown','buff','gray','green','pink','purple','red','white','yellow','blue','orange','black'))
        has_ring = st.radio('Ring', ('yes', 'no'))
        ring_type = st.selectbox('Type of Ring', ('cobwebby','evanescent','flaring','grooved','large','pendant','sheating','zone','movable','none'))
        habitat = st.selectbox('Habitat', ('grasses','leaves','meadows','paths','heaths','urban','waste','woods'))
        season = st.radio('Season', ('spring','summer','autumn','winter'))

        submitted = st.form_submit_button('Predict !')

        # membuat data inference yang akan diprediksi
    df_inf = {
        'cap_diameter' : cap_diameter,
        'cap_shape' : cap_shape,
        'cap_surface' : cap_surface,
        'cap_color' : cap_color,
        'does_bruise_or_bleed' : does_bruise_or_bleed,
        'gill_attachment' : gill_attachment,
        'gill_spacing' : gill_spacing,
        'gill_color' : gill_color,
        'stem_height' : stem_height,
        'stem_width' : stem_width,
        'stem_color' : stem_color,
        'has_ring' : has_ring,
        'ring_type' :ring_type,
        'habitat' : habitat,
        'season' : season
    }

    # menyimpan data inference ke dalam bentuk tabel
    df_inf = pd.DataFrame([df_inf])
    st.dataframe(df_inf)

    if submitted:
        predicton = model.predict(df_inf)


        if predicton == 0:
            st.write('## *Result:* **Edible Mushroom!**')
        else:
            st.write('## *Result:* **Inedible/Poisonous Mushroom!!**')

if __name__ == '__main__':
    run()