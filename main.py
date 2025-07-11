import streamlit as st


st.set_page_config(page_title="Plan Nutrition & Musculation", layout="wide")

st.title("💪 Plan Nutrition & Musculation – Prise de masse (Végé/Végan)")

# Onglets principaux
tab1, tab2, tab3, tab4 = st.tabs(["📊 Objectifs", "🍽️ Nutrition", "🏋️ Musculation", "💊 Compléments & Courses"])

# OBJECTIFS
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🧔‍♂️ Ton Profil")
        st.info("**Taille**: 1m83\n\n**Poids**: 75 kg\n\n**Objectif**: +3 à 5 kg de muscle\n\n**Kcal/jour**: 2800–3100\n**Protéines**: 140–160 g")
    with col2:
        st.subheader("👩‍🦰 Profil de ta copine")
        st.info("**Taille**: 1m70\n\n**Poids**: 68 kg\n\n**Objectif**: recomposition corporelle\n\n**Kcal/jour**: 2000–2200\n**Protéines**: 110–130 g")

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
    circuit_tab1, circuit_tab2, circuit_tab3, circuit_tab4 = st.tabs(["🟧 Trapèze, Épaules & Bras", "🟦 Dos", "🟩 Jambes & Fessiers","🟪 Pectoraux"])

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
        st.markdown("### 🟪​ Circuit 3 – Pectoraux")
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





























# COMPLEMENTS
with tab4:
    st.subheader("💊 Suppléments recommandés")

    st.markdown("""
| Supplément        | Toi (Végétarien) | Elle (Végan) | Pourquoi |
|------------------|------------------|--------------|----------|
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
