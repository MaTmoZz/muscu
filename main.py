import streamlit as st

st.set_page_config(page_title="Plan Nutrition & Musculation", layout="wide")

st.title("💪 Plan Nutrition & Musculation – Recomposition (Végétarien)")

# Onglets principaux
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["📊 Objectifs", "🍽️ Nutrition", "🏋️ Musculation", "💊 Compléments & Courses", "🎵 Musique"]
)


# =====================================================================
# TAB 1 — OBJECTIFS
# =====================================================================
with tab1:
    st.subheader("🧔‍♂️ Ton Profil")
    st.info(
        "**Taille**: 1m83\n\n"
        "**Poids**: 83 kg\n\n"
        "**Objectif**: prise de muscle + réduction du gras abdominal (recomposition)\n\n"
        "**Kcal/jour**: 3300–3500\n"
        "**Protéines**: 175–185 g"
    )


# =====================================================================
# DONNÉES NUTRITION (végétarien, alignées sur l'objectif de recomposition)
# =====================================================================
DAILY_TARGETS = {"kcal": 3400, "prot": 180, "gluc": 460, "lip": 90}

FOODS = {
    # --- Protéines ---
    "Œuf entier (1 pièce ~60g)": {"kcal": 90, "prot": 7.2, "gluc": 0.4, "lip": 6.6},
    "Whey (1 scoop 30 g)": {"kcal": 114.6, "prot": 23.4, "gluc": 2.69, "lip": 1.11},
    "Tofu ferme poêlé (200g)": {"kcal": 290, "prot": 30, "gluc": 8, "lip": 16},
    "Bouché végétal (175g)": {"kcal": 408, "prot": 40, "gluc": 5.6, "lip": 21.7},
    "Emincé végétal (175g)": {"kcal": 237, "prot": 31, "gluc": 2.1, "lip": 9.75},
    "Boulettes végétales (200g)": {"kcal": 301, "prot": 32.4, "gluc": 10.4, "lip": 14.4},
    "Steaks vege (172.5 g)": {"kcal": 330, "prot": 36.2, "gluc": 7, "lip": 15},
    "Lentilles corail cuites (150g)": {"kcal": 174, "prot": 13.5, "gluc": 30, "lip": 0.6},
    "Pois chiches cuits (100 g)": {"kcal": 164, "prot": 8.9, "gluc": 27.4, "lip": 2.6},
    "Fromage blanc 0% (250g)": {"kcal": 112, "prot": 20, "gluc": 10, "lip": 0.5},
    "Skyr Chocolat (100g)": {"kcal": 71, "prot": 9, "gluc": 3.8, "lip": 2.2},
    "Salers (50 g)": {"kcal": 200, "prot": 12, "gluc": 0.5, "lip": 17},

    # --- Glucides ---
    "Riz complet cuit (100g)": {"kcal": 123, "prot": 2.7, "gluc": 25.6, "lip": 1},
    "Pates complètes (100g)": {"kcal": 349, "prot": 13, "gluc": 65, "lip": 2.2},
    "Flocons d'avoine (80g)": {"kcal": 300, "prot": 10.4, "gluc": 52.8, "lip": 5.6},
    "Quinoa cuit (100g)": {"kcal": 120, "prot": 4.4, "gluc": 21, "lip": 1.9},
    "Patate douce cuite (150g)": {"kcal": 135, "prot": 3, "gluc": 31.5, "lip": 0.2},
    "Patate 50g": {"kcal": 38, "prot": 0.9, "gluc": 8.5, "lip": 0.05},
    "Pain blanc (50 g)": {"kcal": 135, "prot": 4, "gluc": 27, "lip": 0.7},
    "Demae Ramen Spicy (100 g préparé)": {"kcal": 452, "prot": 8.3, "gluc": 56.0, "lip": 20.0},

    # --- Légumes & fruits ---
    "Brocolis cuits (150g)": {"kcal": 53, "prot": 3.6, "gluc": 10.5, "lip": 0.6},
    "Tomate (1 moyenne - 120 g)": {"kcal": 22, "prot": 1.1, "gluc": 4.8, "lip": 0.2},
    "Champignon de Paris (1 moyen - 30 g)": {"kcal": 6, "prot": 0.8, "gluc": 0.6, "lip": 0.1},
    "Oignon (100 g)": {"kcal": 40, "prot": 1.1, "gluc": 9, "lip": 0.1},
    "Banane (1 moyenne, 120g)": {"kcal": 107, "prot": 1.3, "gluc": 27.6, "lip": 0.4},

    # --- Matières grasses & extras ---
    "Avocat (1/2)": {"kcal": 120, "prot": 1.5, "gluc": 6, "lip": 11},
    "Huile d'olive (1 c. à soupe, 10g)": {"kcal": 90, "prot": 0, "gluc": 0, "lip": 10},
    "Beurre de cacahuète (20g)": {"kcal": 118, "prot": 5, "gluc": 4, "lip": 10},
    "Amandes (30g)": {"kcal": 174, "prot": 6.3, "gluc": 6.6, "lip": 15},
    "Graines de courge/tournesol (20g)": {"kcal": 112, "prot": 6, "gluc": 2.2, "lip": 9.8},
}


def make_adjust_callback(food_name, delta):
    """Callback pour les boutons ➕/➖ d'une carte aliment."""
    def callback():
        st.session_state.counts[food_name] = max(0, st.session_state.counts[food_name] + delta)
        for key in ["kcal", "prot", "gluc", "lip"]:
            st.session_state.totals[key] = max(
                0, st.session_state.totals[key] + FOODS[food_name][key] * delta
            )
    return callback


# =====================================================================
# TAB 2 — NUTRITION
# =====================================================================
with tab2:
    st.subheader("🍽️ Nutrition")

    menu_tab, track_tab = st.tabs(["📖 Journées types", "📅 Suivi journalier"])

    with menu_tab:
        st.success("🧔‍♂️ Journée type (Toi)")

    with track_tab:
        st.subheader("📅 Suivi journalier – Ajoute tes aliments")

        if "totals" not in st.session_state:
            st.session_state.totals = {"kcal": 0, "prot": 0, "gluc": 0, "lip": 0}
        if "counts" not in st.session_state:
            st.session_state.counts = {f: 0 for f in FOODS}

        if st.button("🔄 Reset journée"):
            st.session_state.totals = {k: 0 for k in st.session_state.totals}
            st.session_state.counts = {f: 0 for f in FOODS}

        # ----------------------- Barres de progression ----------------------
        progress_cols = st.columns(4)
        progress_labels = ["kcal", "protéines (g)", "glucides (g)", "lipides (g)"]
        for col, key, label in zip(progress_cols, ["kcal", "prot", "gluc", "lip"], progress_labels):
            progress = min(st.session_state.totals[key] / DAILY_TARGETS[key], 1.0)
            col.metric(label, f"{st.session_state.totals[key]:.0f}/{DAILY_TARGETS[key]}")
            col.progress(progress)

        st.divider()

        # ----------------------- Cartes aliments ---------------------------
        cards_per_row = 3
        food_items = list(FOODS.items())
        for i in range(0, len(food_items), cards_per_row):
            row_cols = st.columns(cards_per_row)
            for col, (name, macros) in zip(row_cols, food_items[i : i + cards_per_row]):
                with col:
                    st.markdown(f"#### {name}")
                    st.caption(
                        f"{macros['kcal']} kcal • {macros['prot']} g P • "
                        f"{macros['gluc']} g G • {macros['lip']} g L"
                    )
                    c1, c2, c3 = st.columns([1, 1, 1])
                    with c1:
                        st.button("➖", key=f"minus_{name}", on_click=make_adjust_callback(name, -1))
                    with c2:
                        st.markdown(f"### {st.session_state.counts[name]}")
                    with c3:
                        st.button("➕", key=f"plus_{name}", on_click=make_adjust_callback(name, +1))

    st.divider()
    st.subheader("🍽️ Exemple de journée type")
    st.markdown("""
**Petit-déjeuner**  
- Flocons d'avoine + lait végétal  
- Banane + beurre de cacahuète  
- 1 scoop de whey ou protéine végétale  
- Graines de lin

**Déjeuner**  
- Riz complet ou quinoa + pois chiches ou lentilles + brocolis  
- Tofu ou œuf dur  
- 1 fruit

**Collation**  
- Fromage blanc 0% ou skyr + amandes  
- Fruits + noix

**Dîner**  
- Tofu poêlé ou steak vege + patate douce + légumes  
- Chocolat noir
""")

    st.divider()
    st.subheader("🛒 Liste de courses")
    with st.expander("🌱 Protéines végétales"):
        st.write(
            "- Tofu, seitan, steaks vege\n"
            "- Lentilles, pois chiches\n"
            "- Quinoa\n"
            "- Flocons d'avoine\n"
            "- Œufs, fromage blanc 0%, skyr"
        )
    with st.expander("🍚 Glucides complexes"):
        st.write(
            "- Riz complet, patate douce\n"
            "- Pâtes complètes\n"
            "- Fruits variés (banane, pomme)\n"
            "- Légumes verts (brocolis, épinards)"
        )
    with st.expander("🥑 Bonnes graisses"):
        st.write("- Avocats, huile d'olive\n- Amandes, beurre de cacahuète\n- Graines de courge/tournesol")


# =====================================================================
# TAB 3 — MUSCULATION
# =====================================================================
WEEKLY_SCHEDULE = {
    "Lundi": "Haut du corps (Push): Développé couché, dips, élévations, triceps",
    "Mardi": "Bas du corps: Squats, fentes, hip thrusts, mollets",
    "Mercredi": "Repos actif ou cardio léger, yoga, mobilité",
    "Jeudi": "Haut du corps (Pull): Rowing, tractions, curl, gainage",
    "Vendredi": "Bas du corps (Force/Plyo): Deadlift, jump squats, goblet squat",
    "Samedi": "Repos actif: marche, vélo cool, étirements",
    "Dimanche": "Circuit Full-body (optionnel): burpees, fentes, pompes, gainage",
}

CIRCUITS = [
    {
        "tab_label": '🟧 Jour 1',
        "title": '🟧 Jour 1',
        "objectif": 'prise de masse, posture, force du haut du corps',
        "exercises": [
            {"icon": '🔸', "title": 'Pec-deck ou butterfly', "sets": '4 × 12', "muscle": 'Pecs', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2000/06/pec-deck-butterfly-exercice-musculation.gif', "key": 'butterfly_kg'},
            {"icon": '🔸', "title": 'Développé incliné à la machine convergente', "sets": '4 × 12', "muscle": 'Pecs, triceps', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2000/06/developpe-incline-machine-convergente-exercice-musculation.gif', "key": 'dev_inclin_kg'},
            {"icon": '🔸', "title": 'Développé épaule haltères', "sets": '4 × 12', "muscle": 'Épaules, triceps', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2022/02/developpe-epaule-halteres.gif', "key": 'dev_epaule_kg'},
            {"icon": '🔸', "title": 'Elevation latérales', "sets": '4 × 12', "muscle": 'Épaules', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2000/08/elevations-laterales-exercice-musculation.gif', "key": 'elev_lat_kg'},
            {"icon": '🔸', "title": 'Oiseau assis sur un banc', "sets": '4 × 12', "muscle": 'Épaules (deltoïdes postérieurs), dos', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2021/12/oiseau-assis-sur-banc.gif', "key": 'oiseau_kg'},
            {"icon": '🔸', "title": 'Extension à la poulie haute', "sets": '4 × 12', "muscle": 'Triceps', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2022/04/extension-triceps-poulie-haute.gif', "key": 'ext_p_haute_kg'},
            {"icon": '🔸', "title": 'Dips', "sets": '4 × 10', "muscle": 'Pecs, triceps', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2000/01/dips-triceps.gif', "key": 'Dips_kg'},
        ],
    },
    {
        "tab_label": '🟦 jour 2',
        "title": '🟦 Jour 2',
        "objectif": 'prise de masse, posture, force du haut du corps',
        "exercises": [
            {"icon": '🔹', "title": 'Tirage horizontal à la poulie', "sets": '4 × 12', "muscle": 'Dos', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2022/02/tirage-horizontal-poulie.gif', "key": 'tirage_p_bas_kg'},
            {"icon": '🔹', "title": 'Tirage vertical poitrine', "sets": '4 × 12', "muscle": 'Dos', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2021/11/tirage-vertical-poitrine.gif', "key": 'tirage_p_haute_dos_kg'},
            {"icon": '🔹', "title": 'Shrugs', "sets": '4 × 12', "muscle": 'Trapèzes', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2022/11/shrugs-avec-halteres.gif', "key": 'Shrugs_kg'},
            {"icon": '🔹', "title": 'Curl biceps assis', "sets": '4 × 12', "muscle": 'Biceps', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2022/01/curl-pupitre-machine-prechargee.gif', "key": 'curl_kg'},
            {"icon": '🔹', "title": 'Curl biceps à la poulie basse', "sets": '4 × 12', "muscle": 'Biceps', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2021/10/curl-biceps-poulie-basse.gif', "key": 'curl_p_kg'},
        ],
    },
    {
        "tab_label": '🟩 Jour 3',
        "title": '🟩 Jour 3',
        "objectif": 'prise de masse, posture, force du haut du corps',
        "exercises": [
            {"icon": '🔹', "title": 'Presse à cuisses inclinée', "sets": '4 × 12', "muscle": 'Quadriceps', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2022/08/presse-a-cuisses-inclinee.gif', "key": 'presse_kg'},
            {"icon": '🔹', "title": 'Soulevé de terre', "sets": '4 × 12', "muscle": 'Ischios, fessiers, dos', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2021/12/souleve-de-terre.gif', "key": 'souleve_de_terre_kg'},
            {"icon": '🔹', "title": 'Leg curl', "sets": '4 × 12', "muscle": 'Ischios', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2022/02/leg-curl-assis-machine.gif', "key": 'leg_curl_kg'},
            {"icon": '🔹', "title": 'Leg extension', "sets": '4 × 12', "muscle": 'Quadriceps', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2000/06/leg-extension-exercice-musculation.gif', "key": 'leg_ext_kg'},
            {"icon": '🔹', "title": 'Extension des mollets à la presse', "sets": '4 × 12', "muscle": 'Mollets', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2021/10/extension-mollets-presse-45.gif', "key": 'mollet_kg'},
        ],
    },
    {
        "tab_label": '🟪 Jour 4',
        "title": '🟪\u200b Jour 4',
        "objectif": 'prise de masse, posture, force du haut du corps',
        "exercises": [
            {"icon": '🔸', "title": 'Pec-deck ou butterfly', "sets": '4 × 12', "muscle": 'Pecs', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2000/06/pec-deck-butterfly-exercice-musculation.gif', "key": 'butterfly_2_kg'},
            {"icon": '🔸', "title": 'Développé incliné à la machine convergente', "sets": '4 × 12', "muscle": 'Pecs, triceps', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2000/06/developpe-incline-machine-convergente-exercice-musculation.gif', "key": 'dev_inclin_2_kg'},
            {"icon": '🔹', "title": 'Tirage horizontal à la poulie', "sets": '4 × 12', "muscle": 'Dos', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2022/02/tirage-horizontal-poulie.gif', "key": 'tirage_p_bas_2_kg'},
            {"icon": '🔹', "title": 'Tirage vertical poitrine', "sets": '4 × 12', "muscle": 'Dos', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2021/11/tirage-vertical-poitrine.gif', "key": 'tirage_p_haute_dos2_kg'},
            {"icon": '🔸', "title": 'Elevation latérales', "sets": '4 × 12', "muscle": 'Épaules', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2000/08/elevations-laterales-exercice-musculation.gif', "key": 'elev_lat_2_kg'},
            {"icon": '🔹', "title": 'Curl biceps assis', "sets": '4 × 12', "muscle": 'Biceps', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2022/01/curl-pupitre-machine-prechargee.gif', "key": 'curl_2_kg'},
            {"icon": '🔹', "title": 'Curl biceps à la poulie basse', "sets": '4 × 12', "muscle": 'Biceps', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2021/10/curl-biceps-poulie-basse.gif', "key": 'curl_p_2_kg'},
            {"icon": '🔸', "title": 'Dips', "sets": '4 × 12', "muscle": 'Pecs, triceps', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2000/01/dips-triceps.gif', "key": 'Dips2_kg'},
        ],
    },
    {
        "tab_label": '🟩 jour 5',
        "title": '🟩 jour 5',
        "objectif": 'renforcer les abdominaux profonds, améliorer la posture et la stabilité',
        "exercises": [
            {"icon": '🔹', "title": 'Extension des mollets à la presse', "sets": '4 × 12', "muscle": 'Mollets', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2021/10/extension-mollets-presse-45.gif', "key": 'mollet2_kg'},
            {"icon": '🔹', "title": 'Squat bulgare', "sets": '4 × 12', "muscle": 'Quadriceps, fessiers', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2000/06/squat-bulgare-halteres-exercice-musculation.gif', "key": 'bulgare_kg'},
            {"icon": '🔹', "title": 'Hip thrust', "sets": '4 × 12', "muscle": 'Fessiers', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2022/08/hip-thrust-a-la-smith-machine.gif', "key": 'hip_thrust_kg'},
            {"icon": '🔹', "title": 'Presse à cuisses inclinée', "sets": '4 × 12', "muscle": 'Quadriceps', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2022/08/presse-a-cuisses-inclinee.gif', "key": 'presse2_kg'},
            {"icon": '🔹', "title": 'Leg curl', "sets": '4 × 12', "muscle": 'Ischios', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2022/02/leg-curl-assis-machine.gif', "key": 'leg_curl2_kg'},
            {"icon": '🔹', "title": 'Leg extension', "sets": '4 × 12', "muscle": 'Quadriceps', "image": 'https://www.docteur-fitness.com/wp-content/uploads/2000/06/leg-extension-exercice-musculation.gif', "key": 'leg_ext2_kg'},
        ],
    },
]


def render_exercise(exercise):
    """Affiche un exercice : titre, image, et champ de saisie du poids utilisé."""
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"#### {exercise['icon']} {exercise['title']} — {exercise['sets']} — {exercise['muscle']}")
        st.image(exercise["image"], caption=exercise["title"], width=300)
    with col2:
        st.number_input("kg", key=exercise["key"], min_value=0, step=1)


with tab3:
    st.subheader("📆 Planning Muscu Hebdomadaire")

    for day, routine in WEEKLY_SCHEDULE.items():
        st.write(f"**📅 {day}** — {routine}")

    st.divider()
    st.subheader("🔥 Circuits ciblés")

    circuit_tabs = st.tabs([c["tab_label"] for c in CIRCUITS])
    for st_tab, circuit in zip(circuit_tabs, CIRCUITS):
        with st_tab:
            st.markdown(f"### {circuit['title']}")
            st.write(f"**Objectif** : {circuit['objectif']}")
            for exercise in circuit["exercises"]:
                render_exercise(exercise)


# =====================================================================
# TAB 4 — COMPLÉMENTS & COURSES
# =====================================================================
with tab4:
    st.subheader("💊 Suppléments recommandés")

    st.markdown("""
| Supplément | Toi (Végétarien) | Pourquoi |
|---|---|---|
| Gainer | ❌ (whey ou protéine végétale suffisent) | Apports protéiques |
| Multivitamine | ❌ | Complément au régime alimentaire |
| BCAA | ❌ (déjà couvert par l'apport en protéines) | Synthétisation des protéines |
| Protéine poudre | ✅ (whey ou végétale) | Apports protéiques |
| Créatine | ✅ | Performance & prise de muscle |
| Vitamine B12 | ✅ | Système nerveux |
| Vitamine D3 | ✅ | Immunité, récupération |
| Oméga-3 (algues) | Optionnel | Anti-inflammatoire |
| Zinc / Fer | Optionnel | Immunité, énergie |
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


# =====================================================================
# TAB 5 — MUSIQUE
# =====================================================================
PLAYLIST = [
    ("musique/helldiver-cover.jpg", "musique/Helldivers 2 Main Theme - A Cup Of Liber-Tea.mp3", "Helldivers 2 Main Theme - A Cup Of Liber-Tea"),
    ("musique/ssbb.jpg", "musique/Main Theme - Super Smash Bros Brawl.mp3", "Main Theme - Super Smash Bros Brawl"),
    ("musique/last.jpg", "musique/The Last Stand.mp3", "The Last Stand"),
    ("musique/cheat.jpg", "musique/cheat.mp3", "Cheat on me"),
    ("musique/arcane.jpg", "musique/arcane.mp3", "Arcane"),
    ("musique/enemy.jpg", "musique/enemy.mp3", "Enemy"),
]

with tab5:
    st.markdown("## 🎧 Playlist d'entraînement visuelle")
    st.write("Une sélection musicale motivante, chaque son avec sa cover.")

    music_cols = st.columns(3)
    for i, (image_path, audio_path, caption) in enumerate(PLAYLIST):
        col = music_cols[i % 3]
        with col:
            st.image(image_path, caption=caption, use_container_width=True)
            st.audio(audio_path)

    st.markdown("#### ➕ Ajouter une musique")
    st.markdown("- Utilise [ytmp3.nu](https://ytmp3.nu/fr12/) ou tout convertisseur fiable pour télécharger le MP3.")
    st.markdown("- Place le fichier dans le dossier `/musique` de ton projet Streamlit.")
