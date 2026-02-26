from datetime import datetime, timedelta
import streamlit as st

# Dates tournoi
debut_poules = datetime(2026,6,20)
fin_poules = debut_poules + timedelta(days = 45)

# Jours et créneaux
jours_parties = []
jour_actuel = debut_poules
creneaux = [] 
while jour_actuel <= fin_poules:
  if jours.weektime() >= 2:
   creneau_19 = jours.replace(hours = 19)
   creneau_20 = jours.replace(hours = 20)
   creneaux.extend([creneau_19, creneau_20])
  jour_actuel += timedelta(days = 1)

st.title("Inscription tournoi Halsou 2026")
st.write("page d’inscription")
st.metric("total de creneaux :", len(creneaux))
st.info("cochez au moins 15 reponses")
#Formulaire
with st.form("Formulaire d’inscription"):
  nom = st.text_input("Nom")
  prenom = st.text_input("Prénom")
  tel = st.text_input("Numéro de téléphone")
  poule = st.selectbox("Série", [1ère série A, 1ère série B, 2ème série, 3ème série)

  dispos = {}
  with st.expander("Disponibilités"):
    for creneau in creneaux:   
      label = creneau.strftime("%A %d %B à %Hh"))
      dispos[creneau] = st.checkbox(label, key = creneau)
        
  submit = st.form_submit_button("Valider")

if submit :
    disponibilites = [date for date, coche in dispos if coche)
    st.write(disponibilites)
