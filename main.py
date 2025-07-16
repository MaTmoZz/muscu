import streamlit as st
import os
from PIL import Image



st.set_page_config(page_title="Plan Nutrition & Musculation", layout="wide")

st.title("💪 Plan Nutrition & Musculation – Prise de masse (Végé/Végan)")

# Onglets principaux
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Objectifs", "🍽️ Nutrition", "🏋️ Musculation", "💊 Compléments & Courses", "🎵 Musique"])


# OBJECTIFS
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🧔‍♂️ Ton Profil")
        st.info("**Taille**: 1m83\n\n**Poids**: 75 kg\n\n**Objectif**: +3 à 5 kg de muscle\n\n**Kcal/jour**: 2800–3100\n**Protéines**: 140–160 g")
    with col2:
        st.subheader("👩‍🦰 Profil de ta copine")
        st.info("**Taille**: 1m70\n\n**Poids**: 68 kg\n\n**Objectif**: recomposition corporelle\n\n**Kcal/jour**: 2000–2200\n**Protéines**: 110–130 g")


with tab2:
    st.subheader("🍽️ Nutrition")

    # Sous‑onglets
    menu_tab, track_tab = st.tabs(["📖 Journées types", "📅 Suivi journalier"])


    with menu_tab:
        st.success("🧔‍♂️ Journée type (Toi)")

    with track_tab:
        st.subheader("📅 Suivi journalier – Ajoute tes aliments")

        # Objectifs quotidiens (à adapter)
        targets = {"kcal": 2900, "prot": 150, "gluc": 380, "lip": 85}

        # Base d'aliments (1 portion)
        foods = {
            "Œuf (100g)":            {"kcal": 143,  "prot": 13,  "gluc": 1.1, "lip": 10},
            "Whey (1 scoop 30 g)":      {"kcal": 114.6, "prot": 23.4, "gluc": 2.69,   "lip": 1.11},
            "Gainer (1 scoop 50 g)":      {"kcal": 192.5, "prot": 12.5, "gluc": 33.5,   "lip": 0.75},
            "Avocat (1/2)":      {"kcal": 120, "prot": 1.5, "gluc": 6,   "lip": 11},
            "Bouché vegetal (175g)":      {"kcal": 408, "prot": 40, "gluc": 5.6,   "lip": 21.7},
            "Emincé vegetal (175g)":      {"kcal": 237, "prot": 31, "gluc": 2.1,   "lip": 9.75},
            "Riz (50g)":      {"kcal": 55, "prot": 1.16, "gluc": 36,   "lip": 0.5},
            "Galette (burrito) 100g":      {"kcal": 594, "prot": 7.8, "gluc": 50,   "lip": 6.5},
            "Patate 50g":      {"kcal": 38, "prot": 0.9, "gluc": 8.5,   "lip": 0.05},
            "Oignon (100 g)": {"kcal": 40, "prot": 1.1, "gluc": 9, "lip": 0.1},
            "Salers (50 g)": {"kcal": 200, "prot": 12, "gluc": 0.5, "lip": 17},
            "Pain blanc (50 g)": {"kcal": 135, "prot": 4, "gluc": 27, "lip": 0.7},
            "Tomate (1 moyenne - 120 g)": {"kcal": 22, "prot": 1.1, "gluc": 4.8, "lip": 0.2},
            "Champignon de Paris (1 moyen - 30 g)": {"kcal": 6, "prot": 0.8, "gluc": 0.6, "lip": 0.1},
            "Boulettes Végétales (200g)": {"kcal": 454, "prot": 32.4, "gluc": 10.4, "lip": 14.4},
            "Pates complètes (100g)": {"kcal": 349, "prot": 13, "gluc": 65, "lip": 2.2},
            "Skyr Chocolat (100g)": {"kcal": 299, "prot": 9, "gluc": 3.8, "lip": 2.2},



        }

        # Initialisation de l'état
        if "totals" not in st.session_state:
            st.session_state.totals = {"kcal": 0, "prot": 0, "gluc": 0, "lip": 0}
        if "counts" not in st.session_state:
            st.session_state.counts = {f: 0 for f in foods}

        # Callback générateur
        def create_adjust_callback(food_name, delta):
            def callback():
                # Met à jour la quantité de l'aliment
                st.session_state.counts[food_name] = max(
                    0, st.session_state.counts[food_name] + delta
                )
                # Met à jour les totaux
                for key in ["kcal", "prot", "gluc", "lip"]:
                    st.session_state.totals[key] = max(
                        0,
                        st.session_state.totals[key] + foods[food_name][key] * delta,
                    )
            return callback

        # Bouton reset quotidien
        if st.button("🔄 Reset journée"):
            st.session_state.totals = {k: 0 for k in st.session_state.totals}
            st.session_state.counts = {f: 0 for f in foods}

        # ----------------------- Barres de progression ----------------------
        colA, colB, colC, colD = st.columns(4)
        for col, key, label in zip(
            [colA, colB, colC, colD],
            ["kcal", "prot", "gluc", "lip"],
            ["kcal", "protéines (g)", "glucides (g)", "lipides (g)"],
        ):
            progress = min(st.session_state.totals[key] / targets[key], 1.0)
            col.metric(label, f"{st.session_state.totals[key]:.0f}/{targets[key]}")
            col.progress(progress)

        st.divider()

        # ----------------------- Cartes aliments ---------------------------
        cards_per_row = 3
        food_items = list(foods.items())
        for i in range(0, len(food_items), cards_per_row):
            row_cols = st.columns(cards_per_row)
            for col, (name, macros) in zip(row_cols, food_items[i : i + cards_per_row]):
                with col:
                    st.markdown(f"#### {name}")
                    st.caption(
                        f"{macros['kcal']} kcal • {macros['prot']} g P • "
                        f"{macros['gluc']} g G • {macros['lip']} g L"
                    )
                    c1, c2, c3 = st.columns([1, 1, 1])
                    with c1:
                        st.button(
                            "➖",
                            key=f"minus_{name}",
                            on_click=create_adjust_callback(name, -1),
                        )
                    with c2:
                        st.markdown(f"### {st.session_state.counts[name]}")
                    with c3:
                        st.button(
                            "➕",
                            key=f"plus_{name}",
                            on_click=create_adjust_callback(name, +1),
                        )



# NUTRITION
with tab2:
    st.subheader("🍽️ Exemples de journées types")
    col1, col2 = st.columns(2)
    with col1:
        st.success("🧔‍♂️ Journée type (Toi)")
        st.markdown("""
**Petit-déjeuner**  
- Flocons d’avoine + lait végétal  
- Banane + beurre d’amande  
- 1 scoop de whey ou protéine végétale  
- Graines de lin

**Déjeuner**  
- Quinoa + pois chiches + brocolis  
- Tofu ou œuf dur  
- 1 fruit

**Collation**  
- Barre ou shake protéiné  
- Fruits + noix

**Dîner**  
- Pâtes lentilles + légumes + seitan  
- Chocolat noir
""")
    with col2:
        st.success("👩‍🦰 Journée type (Elle)")
        st.markdown("""
**Petit-déjeuner**  
- Smoothie protéiné (lait soja, banane, flocons, graines, protéine)  
- Tartine beurre de cacahuète

**Déjeuner**  
- Riz complet + tofu + légumes  
- Yaourt végétal enrichi

**Collation**  
- Barre ou shake protéiné  
- Fruits secs

**Dîner**  
- Patate douce + pois chiches + légumes rôtis  
- Compote ou chocolat noir
""")

    st.divider()
    st.subheader("🛒 Liste de courses")
    with st.expander("🌱 Protéines végétales"):
        st.write("- Tofu, tempeh, seitan\n- Lentilles, pois chiches\n- Quinoa, edamame\n- Flocons d’avoine\n- Lait végétal enrichi")
    with st.expander("🍚 Glucides complexes"):
        st.write("- Riz complet, patate douce, boulgour\n- Pâtes aux légumineuses\n- Fruits variés\n- Légumes verts")
    with st.expander("🥑 Bonnes graisses"):
        st.write("- Avocats, huile d'olive\n- Noix, amandes\n- Graines de chia/lin/courge")


# MUSCULATION
with tab3:
    st.subheader("📆 Planning Muscu Hebdomadaire")

    days = {
        "Lundi": "Haut du corps (Push): Développé couché, dips, élévations, triceps",
        "Mardi": "Bas du corps: Squats, fentes, hip thrusts, mollets",
        "Mercredi": "Repos actif ou cardio léger, yoga, mobilité",
        "Jeudi": "Haut du corps (Pull): Rowing, tractions, curl, gainage",
        "Vendredi": "Bas du corps (Force/Plyo): Deadlift, jump squats, goblet squat",
        "Samedi": "Repos actif: marche, vélo cool, étirements",
        "Dimanche": "Circuit Full-body (optionnel): burpees, fentes, pompes, gainage"
    }

    for day, routine in days.items():
        st.write(f"**📅 {day}** — {routine}")

    st.divider()
    st.subheader("🔥 Circuits ciblés")

    # Onglets pour circuits
    circuit_tab1, circuit_tab2, circuit_tab3, circuit_tab4, circuit_tab5 = st.tabs(["🟧 Jour 1", "🟦 jour 2", "🟩 Jour 3","🟪 Jour 4","🟩 jour 5"])

    with circuit_tab1:
        st.markdown("### 🟧 Jour 1")
        st.write("**Objectif** : prise de masse, posture, force du haut du corps")

        # Développé militaire avec image
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔸 Pec-deck ou butterfly — 4 × 8-10 — Pecs")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2000/06/pec-deck-butterfly-exercice-musculation.gif",
                caption="Pec-deck ou butterfly",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="butterfly_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur


        # Développé militaire avec image
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔸 Développé incliné à la machine convergente — 3 × 12 — Pecs, triceps")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2000/06/developpe-incline-machine-convergente-exercice-musculation.gif",
                caption="Développé incliné à la machine convergente",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="dev_inclin_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur


        # Développé militaire avec image
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔸 Développé épaule haltères — 3 × 12 — Pecs, triceps")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2022/02/developpe-epaule-halteres.gif",
                caption="Développé épaule haltères",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="dev_epaule_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur


        # Développé militaire avec image
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔸 Elevation latérales — 3 × 12 — Pecs, triceps")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2000/08/elevations-laterales-exercice-musculation.gif",
                caption="Elevation latérales",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="elev_lat_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur


        # Développé militaire avec image
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔸 Oiseau assis sur un banc — 3 × 12 — Pecs, triceps")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2021/12/oiseau-assis-sur-banc.gif",
                caption="Oiseau assis sur un banc",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="oiseau_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur


        # Développé militaire avec image
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔸 Extension à la poulie haute — 4 × 10 — Triceps")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2022/04/extension-triceps-poulie-haute.gif",
                caption="Extension à la poulie haute",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="ext_p_haute_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur


        # Développé militaire avec image
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔸 Dips — 4 × 10 — Triceps")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2000/01/dips-triceps.gif",
                caption="Dips",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="Dips_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur






    with circuit_tab2:
        st.markdown("### 🟦 Jour 2")
        st.write("**Objectif** : prise de masse, posture, force du haut du corps")


        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔹 Tirage horizontal à la poulie — 4 × 10 — Triceps")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2022/02/tirage-horizontal-poulie.gif",
                caption="Tirage horizontal à la poulie",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="tirage_p_bas_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur



        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔹 Tirage vertical poitrine — 4 × 10 — Triceps")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2021/11/tirage-vertical-poitrine.gif",
                caption="Tirage vertical poitrine",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="tirage_p_haute_dos_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur


        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔹 Shrugs — 4 × 10 — Triceps")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2022/11/shrugs-avec-halteres.gif",
                caption="Shrugs",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="Shrugs_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur


        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔹 Curl biceps assis — 4 × 10 — Triceps")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2022/01/curl-pupitre-machine-prechargee.gif",
                caption="Curl biceps assis",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="curl_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur



        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔹 Curl biceps à la poulie basse — 4 × 10 — Triceps")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2021/10/curl-biceps-poulie-basse.gif",
                caption="Curl biceps à la poulie basse",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="curl_p_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur






    with circuit_tab3:
        st.markdown("### 🟩 Jour 3")
        st.write("**Objectif** : prise de masse, posture, force du haut du corps")

        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔹 Presse à cuisses inclinée — 4 × 10 — Triceps")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2022/08/presse-a-cuisses-inclinee.gif",
                caption="Presse à cuisses inclinée",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="presse_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur



        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔹 Soulevé de terre — 4 × 10 — Triceps")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2021/12/souleve-de-terre.gif",
                caption="Soulevé de terre",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="souleve_de_terre_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur


        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔹 Leg curl — 4 × 10 — Triceps")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2022/02/leg-curl-assis-machine.gif",
                caption="Leg curl",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="leg_curl_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur

    
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔹 Leg extension — 4 × 10 — Triceps")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2000/06/leg-extension-exercice-musculation.gif",
                caption="Leg extension",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="leg_ext_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur

        

        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔹 Extension des mollets à la presse — 4 × 10 — Triceps")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2021/10/extension-mollets-presse-45.gif",
                caption="Extension des mollets à la presse",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="mollet_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur







    with circuit_tab4:
        st.markdown("### 🟪​ Jour 4")
        st.write("**Objectif** : prise de masse, posture, force du haut du corps")

        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔸 Pec-deck ou butterfly — 4 × 8-10 — Pecs")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2000/06/pec-deck-butterfly-exercice-musculation.gif",
                caption="Pec-deck ou butterfly",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="butterfly_2_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur


        # Développé militaire avec image
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔸 Développé incliné à la machine convergente — 3 × 12 — Pecs, triceps")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2000/06/developpe-incline-machine-convergente-exercice-musculation.gif",
                caption="Développé incliné à la machine convergente",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="dev_inclin_2_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur



        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔹 Tirage horizontal à la poulie — 4 × 10 — Triceps")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2022/02/tirage-horizontal-poulie.gif",
                caption="Tirage horizontal à la poulie",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="tirage_p_bas_2_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur



        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔹 Tirage vertical poitrine — 4 × 10 — Triceps")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2021/11/tirage-vertical-poitrine.gif",
                caption="Tirage vertical poitrine",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="tirage_p_haute_dos2_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur


        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔸 Elevation latérales — 3 × 12 — Pecs, triceps")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2000/08/elevations-laterales-exercice-musculation.gif",
                caption="Elevation latérales",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="elev_lat_2_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur


        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔹 Curl biceps assis — 4 × 10 — Triceps")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2022/01/curl-pupitre-machine-prechargee.gif",
                caption="Curl biceps assis",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="curl_2_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur



        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔹 Curl biceps à la poulie basse — 4 × 10 — Triceps")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2021/10/curl-biceps-poulie-basse.gif",
                caption="Curl biceps à la poulie basse",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="curl_p_2_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur


        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("#### 🔸 Dips — 4 × 10 — Triceps")
            st.image(
                "https://www.docteur-fitness.com/wp-content/uploads/2000/01/dips-triceps.gif",
                caption="Dips",
                width=300  # ✅ Ajuste ici (en pixels)
            )
        with col2:
            st.number_input("kg", key="Dips2_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur







with circuit_tab5:
    st.markdown("### 🟩 jour 5")
    st.write("**Objectif** : renforcer les abdominaux profonds, améliorer la posture et la stabilité")

    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("#### 🔹 Extension des mollets à la presse — 4 × 10 — Triceps")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2021/10/extension-mollets-presse-45.gif",
            caption="Extension des mollets à la presse",
            width=300  # ✅ Ajuste ici (en pixels)
         )
    with col2:
        st.number_input("kg", key="mollet2_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur


    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("#### 🔹 Squat bulgare — 4 × 10 — Triceps")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2000/06/squat-bulgare-halteres-exercice-musculation.gif",
            caption="Squat bulgare",
            width=300  # ✅ Ajuste ici (en pixels)
         )
    with col2:
        st.number_input("kg", key="bulgare_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur


    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("#### 🔹 Hip thrust — 4 × 10 — Triceps")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2022/08/hip-thrust-a-la-smith-machine.gif",
            caption="Hip thrust",
            width=300  # ✅ Ajuste ici (en pixels)
         )
    with col2:
        st.number_input("kg", key="hip_thrust_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur


    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("#### 🔹 Presse à cuisses inclinée — 4 × 10 — Triceps")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2022/08/presse-a-cuisses-inclinee.gif",
            caption="Presse à cuisses inclinée",
            width=300  # ✅ Ajuste ici (en pixels)
        )
    with col2:
        st.number_input("kg", key="presse2_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur

    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("#### 🔹 Leg curl — 4 × 10 — Triceps")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2022/02/leg-curl-assis-machine.gif",
            caption="Leg curl",
            width=300  # ✅ Ajuste ici (en pixels)
        )
    with col2:
        st.number_input("kg", key="leg_curl2_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur

    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("#### 🔹 Leg extension — 4 × 10 — Triceps")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2000/06/leg-extension-exercice-musculation.gif",
            caption="Leg extension",
            width=300  # ✅ Ajuste ici (en pixels)
        )
    with col2:
        st.number_input("kg", key="leg_ext2_kg", min_value=0, step=1)  # ✅ Streamlit gère la valeur




























# COMPLEMENTS
with tab4:
    st.subheader("💊 Suppléments recommandés")

    st.markdown("""
| Supplément        | Toi (Végétarien) | Elle (Végan) | Pourquoi |
|------------------|------------------|--------------|----------|
| Gainer | ​❌​ (whey ou végétale) | ​❌​ (végétale) | Apports protéiques |
| Créatine | ​❌​ | ​❌​ | Performance & prise de muscle |
| Multivitamine | ​❌​ | ​❌​  | Complement au régime alimentaire |
| Oméga-3 (algues) | ​❌​ | ​❌​ | Anti-inflammatoire |
| BCAA | ​❌​ | ​❌​ | Synthétisation des protéines |
| Protéine poudre | ✅ (whey ou végétale) | ✅ (végétale) | Apports protéiques |
| Créatine | ✅ | ✅ | Performance & prise de muscle |
| Vitamine B12 | ✅ | ✅ obligatoire | Système nerveux |
| Vitamine D3 végan | ✅ | ✅ | Immunité, récupération |
| Oméga-3 (algues) | Optionnel | Recommandé | Anti-inflammatoire |
| Zinc / Fer | Optionnel | Si besoin | Immunité, énergie |
    """)

    st.success("✅ Pense à te supplémenter quotidiennement en B12, D3, et éventuellement Oméga-3 (algues).")

    st.divider()
    st.subheader("📈 Suivi et conseils")
    st.markdown("""
- **Hydratation** : 2-3L/jour  
- **Sommeil** : 7-9h  
- **Pesée** : chaque semaine  
- **Photos mensuelles** : suivi visuel  
- **Progression muscu** : + poids ou + reps chaque semaine
""")
















with tab5:  # 🎵 Musique
    st.markdown("## 🎧 Playlist d'entraînement visuelle")

    st.write("Une sélection musicale motivante, chaque son avec sa cover.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("musique/helldiver-cover.jpg", caption="Helldivers 2 Main Theme - A Cup Of Liber-Tea", use_container_width=True)
        st.audio("musique/Helldivers 2 Main Theme - A Cup Of Liber-Tea.mp3")

    with col2:
        st.image("musique/ssbb.jpg", caption="Main Theme - Super Smash Bros Brawl", use_container_width=True)
        st.audio("musique/Main Theme - Super Smash Bros Brawl.mp3")

    with col3:
        st.image("musique/last.jpg", caption="The Last Stand", use_container_width=True)
        st.audio("musique/The Last Stand.mp3")


    st.markdown("#### ➕ Ajouter une musique")
    st.markdown("- Utilise [ytmp3.nu](https://ytmp3.nu/fr12/) ou tout convertisseur fiable pour télécharger le MP3.")
    st.markdown("- Place le fichier dans le dossier `/musique` de ton projet Streamlit.")

