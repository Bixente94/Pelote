from datetime import datetime, timedelta
import streamlit as st
debut_poules = datetime(2026,6,20)
fin_poules = debut_poules + timedelta(days = 45)
print(f"Début des poules le {debut_poules.strftime('%A %d %B')}.")

jours_parties = []
jour_actuel = debut_poules
while jour_actuel <= fin_poules :
    if jour_actuel.weekday() >= 2:
        jours_parties.append(jour_actuel)
    jour_actuel += timedelta(days=1)
 
creneaux = [] 
for jours in jours_parties: 
   creneau_19 = jours + timedelta(hours = 19)
   creneau_20 = jours + timedelta(hours = 20)
   creneaux.extend([creneau_19, creneau_20])
   for creneau in creneaux:   
     print(creneau.strftime("%A %d %B à %Hh")) 
     
   
