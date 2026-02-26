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
  if jour_actuel.weekday() >= 2:
   creneau_19 = jour_actuel.replace(hour = 19)
   creneau_20 = jour_actuel.replace(hour = 20)
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
  serie = st.selectbox("Série", ["1ère série A", "1ère série B", "2ème série", "3ème série"])

  dispos = {}
  with st.expander("Disponibilités"):
    for creneau in creneaux:   
      label = creneau.strftime("%A %d %B à %Hh")
      dispos[creneau] = st.checkbox(label, key = creneau)

  disponibilites = [date for date, coche in dispos.items() if coche]
  champs_ok = nom.strip() != "" and prenom.strip() != "" and tel.strip() != ""
  serie_ok = serie != "Série"
  dispo_ok = len(disponibilites) >= 15
  tout_ok = serie_ok dispo_ok champs_ok
  submit = st.form_submit_button("Valider", disabled=not tout_ok)

