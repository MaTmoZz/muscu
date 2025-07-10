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
    circuit_tab1, circuit_tab2, circuit_tab3 = st.tabs(["🟧 Haut du corps", "🟦 Centre & Dos", "🟩 Jambes & Fessiers"])

    with circuit_tab1:
        st.markdown("### 🟧 Circuit 1 – Haut du corps : Trapèze / Épaules / Bras / Pecs")
    st.write("**Objectif** : prise de masse, posture, force du haut du corps")

    # Développé militaire avec image
    st.markdown("#### 🔸 Développé militaire — 4 × 10 — Épaules, triceps")
    st.image(
        "https://www.docteur-fitness.com/wp-content/uploads/2000/08/developpe-militaire-exercice-musculation.gif",
        caption="Exécution du développé militaire",
        width=300  # ✅ Ajuste ici (en pixels)
    )

    st.markdown("#### 🔸 Élévations latérales — 3 × 15 — Épaules externes")
    st.image(
        "https://www.docteur-fitness.com/wp-content/uploads/2000/08/elevations-laterales-exercice-musculation.gif",
        caption="Élévations latérales",
        width=300  # ✅ Ajuste ici (en pixels)
    )

    st.markdown("#### 🔸 Shrugs — 4 × 12 — Trapèzes")
    st.image(
        "https://cdn.shopify.com/s/files/1/0547/0486/5477/files/dumbbell-shrug_480x480.gif?v=1701426774",
        caption="Shrugs",
        width=300  # ✅ Ajuste ici (en pixels)
    )


    # Autres exos en tableau
    st.markdown("""
    | Exercice | Séries × Rép. | Zones |
    |----------|---------------|-------|
    | Élévations latérales | 3 × 15 | Épaules externes |
    | Shrugs | 4 × 12 | Trapèzes |
    | Curl biceps | 3 × 12 | Biceps |
    | Dips | 3 × 10–15 | Triceps, pecs |
    | Pompes déclinées | 3 × 12–15 | Pecs, épaules |
    """)

    with circuit_tab2:
        st.markdown("### 🟦 Circuit 2 – Centre / Dos / Abdos")
        st.write("""
**Objectif** : gainage, renforcement postural, solidité dorsale

| Exercice | Séries × Rép. | Zones |
|----------|---------------|-------|
| Rowing barre/haltères | 4 × 10 | Dos, trapèzes |
| Superman | 3 × 20s | Lombaires |
| Bird-dog | 3 × 12 / côté | Gainage, dos profond |
| Gainage frontal | 3 × 45s | Core |
| Crunch + relevés jambes | 3 × 15 | Abdos |
| Face pull | 3 × 12 | Arrière épaules |
        """)

    with circuit_tab3:
        st.markdown("### 🟩 Circuit 3 – Jambes / Mollets / Fessiers")
        st.write("""
**Objectif** : force, volume, explosivité

| Exercice | Séries × Rép. | Zones |
|----------|---------------|-------|
| Squats | 4 × 12–15 | Quadriceps, fessiers |
| Hip Thrust | 4 × 10 | Fessiers |
| Fentes marchées | 3 × 12 / jambe | Jambes complètes |
| Soulevé de terre jambes tendues | 3 × 12 | Ischios |
| Pont fessier 1 jambe | 3 × 10 / jambe | Fessiers, gainage |
| Mollets debout | 3 × 20 | Mollets |
        """)


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
