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

# ---------------------------------------------------------------------------
# NUTRITION
# ---------------------------------------------------------------------------
with tab2:
    st.subheader("🍽️ Nutrition")

    # Sous‑onglets
    menu_tab, track_tab = st.tabs(["📖 Journées types", "📅 Suivi journalier"])

    # -----------------------------------------------------------------------
    # 1) Onglet Journées types  (garde ton contenu actuel ici)
    # -----------------------------------------------------------------------
    with menu_tab:
        st.success("🧔‍♂️ Journée type (Toi)")
        # … ton texte / markdown existant …

    # -----------------------------------------------------------------------
    # 2) Onglet Suivi journalier – cartes aliments + barres de progression
    # -----------------------------------------------------------------------
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
    circuit_tab1, circuit_tab2, circuit_tab3, circuit_tab4, circuit_tab5 = st.tabs(["🟧 Trapèze, Épaules & Bras", "🟦 Dos", "🟩 Jambes & Fessiers","🟪 Pectoraux","🟩 Abdos"])

    with circuit_tab1:
        st.markdown("### 🟧 Circuit 1 – Haut du corps : Trapèze / Épaules / Bras")
        st.write("**Objectif** : prise de masse, posture, force du haut du corps")

        # Développé militaire avec image
        st.markdown("#### 🔸 Curl biceps assis à la machine — 4 × 10 — Biceps")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2022/01/curl-pupitre-machine-prechargee.gif",
            caption="Curl biceps assis à la machine",
            width=300  # ✅ Ajuste ici (en pixels)
        )

        st.markdown("#### 🔸 Curl biceps à la poulie basse — 3 × 12 — Biceps")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2021/10/curl-biceps-poulie-basse.gif",
            caption="Curl biceps à la poulie basse",
            width=300  # ✅ Ajuste ici (en pixels)
        )

        st.markdown("#### 🔸 Extension à la poulie haute — 4 × 10 — Triceps")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2022/04/extension-triceps-poulie-haute.gif",
            caption="Extension à la poulie haute",
            width=300  # ✅ Ajuste ici (en pixels)
        )

        st.markdown("#### 🔸 Extensions verticales à deux mains avec haltère — 3 × 12 — Triceps")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2022/09/extensions-verticales-a-deux-mains-avec-haltere.gif",
            caption="Extensions verticales à deux mains avec haltère",
            width=300  # ✅ Ajuste ici (en pixels)
        )

        st.markdown("#### 🔸 Élévations latérales à la machine — 4 × 12 — Epaules")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2022/02/elevation-laterale-machine.gif",
            caption="Élévations latérales à la machine",
            width=300  # ✅ Ajuste ici (en pixels)
        )

        st.markdown("#### 🔸 Développé épaules avec haltères — 4 × 10 — Epaules")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2022/02/developpe-epaule-halteres.gif",
            caption="Développé épaules avec haltères",
            width=300  # ✅ Ajuste ici (en pixels)
        )

        st.markdown("#### 🔸 Shrugs avec haltères — 3 × 40 — Trapèzes")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2022/11/shrugs-avec-halteres.gif",
            caption="Shrugs avec haltères",
            width=300  # ✅ Ajuste ici (en pixels)
        )






    with circuit_tab2:
        st.markdown("### 🟦 Circuit 2 – Dos")
        st.write("**Objectif** : prise de masse, posture, force du haut du corps")

        # Développé militaire avec image
        st.markdown("#### 🔹 Tirage vertical poitrine — 4 × 10 — Grand dorsaux")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2021/11/tirage-vertical-poitrine.gif",
            caption="Tirage vertical poitrine",
            width=300  # ✅ Ajuste ici (en pixels)
        )

        st.markdown("#### 🔹​ Tirage horizontal à la poulie — 4 × 12 — Épaisseur du dos")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2022/02/tirage-horizontal-poulie.gif",
            caption="Tirage horizontal à la poulie",
            width=300  # ✅ Ajuste ici (en pixels)
        )

        st.markdown("#### 🔹​ Rowing en pronation assis — 3 x 12 — Rhomboïdes, trapèzes")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2022/02/rowing-assis-machine-prise-pronation.gif",
            caption="Rowing en pronation assis",
            width=300  # ✅ Ajuste ici (en pixels)
        )

        st.markdown("#### 🔹​ Pullover avec haltère — 3 × 12 — Isolation des dorsaux")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2021/12/pullover-haltere.gif",
            caption="Pullover avec haltère",
            width=300  # ✅ Ajuste ici (en pixels)
        )

        st.markdown("#### 🔹​ Rowing unilatéral — 3 × 12 / bras — Dos")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2022/02/rowing-unilateral-landmine-meadows-row.gif",
            caption="Rowing unilatéral",
            width=300  # ✅ Ajuste ici (en pixels)
        )

        st.markdown("#### 🔹​ Extension lombaire à la machine — 4 × 15-20 — Lombaires")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2021/12/extension-lombaire-a-la-machine.gif",
            caption="Extension lombaire à la machine",
            width=300  # ✅ Ajuste ici (en pixels)
        )








    with circuit_tab3:
        st.markdown("### 🟩 Circuit 3 – Jambes / Mollets / Fessiers")
        st.write("**Objectif** : prise de masse, posture, force du haut du corps")

        # Développé militaire avec image
        st.markdown("#### 🔸 Presse à cuisses inclinée — 4 × 10-12 — Quadriceps")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2022/08/presse-a-cuisses-inclinee.gif",
            caption="Presse à cuisses inclinée",
            width=300  # ✅ Ajuste ici (en pixels)
        )

        st.markdown("#### 🔸 Squat — 4 × 12 — Quadriceps")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2021/11/homme-faisant-un-squat-avec-barre.gif",
            caption="Squat",
            width=300  # ✅ Ajuste ici (en pixels)
        )

        st.markdown("#### 🔸 Leg curl allongé — 4 × 12 — Quadriceps Ischios")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2021/10/leg-curl-allonge.gif",
            caption="Leg curl allongé",
            width=300  # ✅ Ajuste ici (en pixels)
        )

        st.markdown("#### 🔸 Leg extension — 3 × 15 — Quadriceps")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2000/06/leg-extension-exercice-musculation.gif",
            caption="Leg extension",
            width=300  # ✅ Ajuste ici (en pixels)
        )

        st.markdown("#### 🔸 Extension des mollets à la presse — 3 × 20 — Mollets")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2021/10/extension-mollets-presse-45.gif",
            caption="Développé incliné à la machine convergente",
            width=300  # ✅ Ajuste ici (en pixels)
        )








    with circuit_tab4:
        st.markdown("### 🟪​ Circuit 4 – Pectoraux")
        st.write("**Objectif** : prise de masse, posture, force du haut du corps")

        # Développé militaire avec image
        st.markdown("#### 🔸 Développé incliné — 4 × 10 — Pecs supérieurs")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2021/10/developpe-incline-barre.gif",
            caption="Développé incliné",
            width=300  # ✅ Ajuste ici (en pixels)
        )

        st.markdown("#### 🔸 Développé décliné à la machine guidée — 3 × 12 — Pecs inférieurs")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2021/12/developpe-decline-barre.gif",
            caption="Développé décliné à la machine guidée",
            width=300  # ✅ Ajuste ici (en pixels)
        )

        st.markdown("#### 🔸 Développé couché — 4 × 8-10 — Pecs")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2019/08/developpe-couche.gif",
            caption="Développé couché",
            width=300  # ✅ Ajuste ici (en pixels)
        )

        st.markdown("#### 🔸 Écartés décliné avec haltères — 3 × 12 — Pecs")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2021/11/ecartes-decline-avec-halteres.gif",
            caption="Écartés décliné avec haltères",
            width=300  # ✅ Ajuste ici (en pixels)
        )

        st.markdown("#### 🔸 Développé incliné à la machine convergente — 3 × 12 — Pecs, triceps")
        st.image(
            "https://www.docteur-fitness.com/wp-content/uploads/2000/06/developpe-incline-machine-convergente-exercice-musculation.gif",
            caption="Développé incliné à la machine convergente",
            width=300  # ✅ Ajuste ici (en pixels)
        )


with circuit_tab5:
    st.markdown("### 🟩 Circuit – Ceinture abdominale / Abdos")
    st.write("**Objectif** : renforcer les abdominaux profonds, améliorer la posture et la stabilité")

    st.markdown("#### 🔸 Crunch à la machine — 4 × 15 — Grand droit")
    st.image(
        "https://www.docteur-fitness.com/wp-content/uploads/2022/04/crunch-machine-abdos.gif",
        caption="Crunch à la machine",
        width=300
    )

    st.markdown("#### 🔸 Obliques haltère — 3 × 15 de chaque côté — Obliques externes")
    st.image(
        "https://www.docteur-fitness.com/wp-content/uploads/2022/07/flexions-laterales-haltere.gif",
        caption="Torsion du buste à la poulie",
        width=300
    )

    st.markdown("#### 🔸 Relevés de jambes sur banc incliné — 3 × 12 — Bas du grand droit")
    st.image(
        "https://www.docteur-fitness.com/wp-content/uploads/2022/04/releve-jambes-chaise-romaine-abdominaux.gif",
        caption="Relevés de jambes sur banc incliné",
        width=300
    )

    st.markdown("#### 🔸 AB Coaster — 3 × 10 — Transverse")
    st.image(
        "https://www.docteur-fitness.com/wp-content/uploads/2022/04/ab-coaster-abdominaux.gif",
        caption="AB Coaster",
        width=300
    )

    st.markdown("#### 🔸 Flexions des obliques au banc à lombaire à 45° — 3 × 12 — Transverse / stabilisateurs")
    st.image(
        "https://www.docteur-fitness.com/wp-content/uploads/2000/07/flexions-des-obliques-banc-lombaire-45-exercice-musculation.gif",
        caption="Flexions des obliques au banc à lombaire à 45°",
        width=300
    )






















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
        st.image("musique/helldiver-cover.jpg", caption="Helldivers 2 Main Theme - A Cup Of Liber-Tea", use_container_width=True)
        st.audio("musique/Helldivers 2 Main Theme - A Cup Of Liber-Tea.mp3")

    with col3:
        st.image("musique/helldiver-cover.jpg", caption="Helldivers 2 Main Theme - A Cup Of Liber-Tea", use_container_width=True)
        st.audio("musique/Helldivers 2 Main Theme - A Cup Of Liber-Tea.mp3")


    st.markdown("#### ➕ Ajouter une musique")
    st.markdown("- Utilise [ytmp3.nu](https://ytmp3.nu/fr12/) ou tout convertisseur fiable pour télécharger le MP3.")
    st.markdown("- Place le fichier dans le dossier `/musique` de ton projet Streamlit.")