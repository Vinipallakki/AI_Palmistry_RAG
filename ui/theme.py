import streamlit as st


# ======================================================
# Main Cosmic Theme
# ======================================================

def apply_theme():

    st.markdown(
        """
        <style>

        /* ==================================================
           MAIN APPLICATION
           ================================================== */

        .stApp {

            background:
                linear-gradient(
                    135deg,
                    #08051A 0%,
                    #10082B 50%,
                    #070519 100%
                ) !important;

            color: #F5EDFF !important;

        }


        /* ==================================================
           STREAMLIT MAIN CONTAINER
           ================================================== */

        [data-testid="stAppViewContainer"] {

            background:
                linear-gradient(
                    135deg,
                    #08051A 0%,
                    #10082B 50%,
                    #070519 100%
                ) !important;

        }


        .main {

            background:
                transparent !important;

        }


        /* ==================================================
           CONTENT WIDTH
           ================================================== */

        .main .block-container {

            max-width: 1400px !important;

            padding-top: 2rem !important;

            padding-left: 3rem !important;

            padding-right: 3rem !important;

            padding-bottom: 3rem !important;

        }


        /* ==================================================
           HEADINGS
           ================================================== */

        .stApp h1 {

            color: #F6D77A !important;

            text-shadow:
                0 0 12px
                rgba(246, 215, 122, 0.35);

        }


        .stApp h2,
        .stApp h3 {

            color: #E8CFFF !important;

            text-shadow:
                0 0 10px
                rgba(183, 112, 255, 0.30);

        }


        /* ==================================================
           NORMAL TEXT
           ================================================== */

        .stApp p,
        .stApp label {

            color: #EDE2F7 !important;

        }


        /* ==================================================
           HEADER
           ================================================== */

        [data-testid="stHeader"] {

            background:
                rgba(8, 5, 26, 0.95) !important;

        }


        /* ==================================================
           DIVIDERS
           ================================================== */

        .stApp hr {

            border-color:
                rgba(183, 112, 255, 0.25) !important;

        }


        /* ==================================================
           BUTTONS
           ================================================== */

        .stButton > button {

            background:
                linear-gradient(
                    135deg,
                    #6A1B9A,
                    #32105B
                ) !important;

            color:
                #FFFFFF !important;

            border:
                1px solid
                rgba(246, 215, 122, 0.55) !important;

            border-radius:
                14px !important;

            font-weight:
                700 !important;

            box-shadow:
                0 0 20px
                rgba(183, 112, 255, 0.25) !important;

        }


        .stButton > button:hover {

            background:
                linear-gradient(
                    135deg,
                    #8E24AA,
                    #4A148C
                ) !important;

            border-color:
                #F6D77A !important;

            box-shadow:
                0 0 30px
                rgba(246, 215, 122, 0.35) !important;

        }


        /* ==================================================
           TEXT INPUT
           ================================================== */

        .stTextInput input {

            background:
                #130C2B !important;

            color:
                #FFFFFF !important;

            border:
                1px solid
                rgba(183, 112, 255, 0.55) !important;

            border-radius:
                12px !important;

        }


        .stTextInput input::placeholder {

            color:
                #A99BB8 !important;

        }


        /* ==================================================
           ALERTS
           ================================================== */

        [data-testid="stAlert"] {

            background:
                rgba(31, 17, 55, 0.92) !important;

            border:
                1px solid
                rgba(183, 112, 255, 0.35) !important;

            border-radius:
                14px !important;

        }


        /* ==================================================
           FOOTER
           ================================================== */

        footer {

            visibility:
                hidden;

        }

        </style>
        """,
        unsafe_allow_html=True,
    )

# ======================================================
# Cosmic Background + Stars
# ======================================================

def apply_cosmic_background():

    st.markdown(
        """
        <style>

        /* ==================================================
           COSMIC BACKGROUND GLOW
           ================================================== */

        [data-testid="stAppViewContainer"] {

            background:

                radial-gradient(
                    circle at 15% 20%,
                    rgba(115, 50, 180, 0.22),
                    transparent 30%
                ),

                radial-gradient(
                    circle at 85% 15%,
                    rgba(45, 90, 180, 0.18),
                    transparent 30%
                ),

                radial-gradient(
                    circle at 70% 80%,
                    rgba(180, 70, 180, 0.10),
                    transparent 35%
                ),

                linear-gradient(
                    135deg,
                    #08051A 0%,
                    #10082B 50%,
                    #070519 100%
                ) !important;

        }


        /* ==================================================
           STAR FIELD
           ================================================== */

        [data-testid="stAppViewContainer"]::before {

            content: "";

            position: fixed;

            top: 0;
            left: 0;

            width: 100%;
            height: 100%;

            pointer-events: none;

            z-index: 1;

            opacity: 0.65;

            background-image:

                radial-gradient(
                    2px 2px at 8% 12%,
                    #FFFFFF,
                    transparent
                ),

                radial-gradient(
                    1px 1px at 18% 30%,
                    #D6A4FF,
                    transparent
                ),

                radial-gradient(
                    2px 2px at 28% 18%,
                    #F6D77A,
                    transparent
                ),

                radial-gradient(
                    1px 1px at 38% 42%,
                    #FFFFFF,
                    transparent
                ),

                radial-gradient(
                    2px 2px at 48% 15%,
                    #D6A4FF,
                    transparent
                ),

                radial-gradient(
                    1px 1px at 58% 35%,
                    #FFFFFF,
                    transparent
                ),

                radial-gradient(
                    2px 2px at 68% 12%,
                    #F6D77A,
                    transparent
                ),

                radial-gradient(
                    1px 1px at 78% 28%,
                    #D6A4FF,
                    transparent
                ),

                radial-gradient(
                    2px 2px at 88% 18%,
                    #FFFFFF,
                    transparent
                ),

                radial-gradient(
                    1px 1px at 94% 48%,
                    #F6D77A,
                    transparent
                ),

                radial-gradient(
                    1px 1px at 12% 65%,
                    #D6A4FF,
                    transparent
                ),

                radial-gradient(
                    2px 2px at 25% 80%,
                    #FFFFFF,
                    transparent
                ),

                radial-gradient(
                    1px 1px at 42% 70%,
                    #F6D77A,
                    transparent
                ),

                radial-gradient(
                    2px 2px at 60% 85%,
                    #D6A4FF,
                    transparent
                ),

                radial-gradient(
                    1px 1px at 82% 72%,
                    #FFFFFF,
                    transparent
                );

        }

        </style>
        """,
        unsafe_allow_html=True,
    )

# ======================================================
# Mystical Effects
# ======================================================

def apply_mystical_effects():

    st.markdown(
        """
        <style>

        /* ==================================================
           GLOWING HEADINGS
           ================================================== */

        .stApp h1 {

            text-shadow:
                0 0 12px
                rgba(246, 215, 122, 0.35),

                0 0 25px
                rgba(183, 112, 255, 0.20);

        }


        .stApp h2,
        .stApp h3 {

            text-shadow:
                0 0 10px
                rgba(183, 112, 255, 0.35);

        }


        /* ==================================================
           IMAGE GLOW
           ================================================== */

        [data-testid="stImage"] {

            border-radius:
                18px !important;

            padding:
                5px !important;

            background:
                linear-gradient(
                    135deg,
                    rgba(246, 215, 122, 0.35),
                    rgba(183, 112, 255, 0.35)
                ) !important;

            box-shadow:
                0 0 25px
                rgba(183, 112, 255, 0.22) !important;

        }


        /* ==================================================
           EXPANDERS
           ================================================== */

        [data-testid="stExpander"] {

            background:
                linear-gradient(
                    135deg,
                    rgba(35, 17, 67, 0.95),
                    rgba(14, 9, 32, 0.95)
                ) !important;

            border:
                1px solid
                rgba(183, 112, 255, 0.40) !important;

            border-radius:
                15px !important;

        }


        [data-testid="stExpander"] summary {

            color:
                #F6D77A !important;

        }


        /* ==================================================
           ALERT BOX GLOW
           ================================================== */

        [data-testid="stAlert"] {

            box-shadow:
                0 0 18px
                rgba(183, 112, 255, 0.12) !important;

        }


        /* ==================================================
           GOLD ACCENT
           ================================================== */

        .cosmic-gold {

            color:
                #F6D77A !important;

            text-shadow:
                0 0 10px
                rgba(246, 215, 122, 0.45);

        }


        /* ==================================================
           MYSTICAL BADGE
           ================================================== */

        .mystical-badge {

            display:
                inline-block;

            padding:
                7px 16px;

            border-radius:
                30px;

            background:
                linear-gradient(
                    135deg,
                    rgba(106, 27, 154, 0.65),
                    rgba(42, 18, 75, 0.75)
                );

            border:
                1px solid
                rgba(246, 215, 122, 0.45);

            color:
                #F6D77A;

            font-size:
                13px;

            font-weight:
                600;

            letter-spacing:
                1px;

            box-shadow:
                0 0 15px
                rgba(183, 112, 255, 0.20);

        }

        </style>
        """,
        unsafe_allow_html=True,
    )

# ======================================================
# Planets & Mystical Decorations
# ======================================================

def add_cosmic_decorations():

    st.markdown(
        """
        <!-- Moon -->
        <div class="cosmic-moon">☾</div>

        <!-- Planets -->
        <div class="cosmic-planet planet-one"></div>
        <div class="cosmic-planet planet-two"></div>

        <!-- Decorative Stars -->
        <div class="cosmic-star star-one">✦</div>
        <div class="cosmic-star star-two">✧</div>
        <div class="cosmic-star star-three">✦</div>
        <div class="cosmic-star star-four">✧</div>

        <style>

        /* ==================================================
           DECORATION BASE
           ================================================== */

        .cosmic-moon,
        .cosmic-planet,
        .cosmic-star {

            position: fixed;

            pointer-events: none;

            z-index: 5;

        }


        /* ==================================================
           MOON
           ================================================== */

        .cosmic-moon {

            top: 110px;

            right: 55px;

            font-size: 72px;

            color: #D6A4FF;

            opacity: 0.30;

            text-shadow:
                0 0 25px
                rgba(183, 112, 255, 0.80);

        }


        /* ==================================================
           PLANET ONE
           ================================================== */

        .planet-one {

            top: 150px;

            left: 420px;

            width: 85px;

            height: 85px;

            border-radius: 50%;

            background:
                radial-gradient(
                    circle at 30% 30%,
                    #D6A4FF,
                    #7145A5 45%,
                    #24113F 100%
                );

            opacity: 0.32;

            box-shadow:
                0 0 35px
                rgba(150, 90, 255, 0.40);

        }


        /* ==================================================
           PLANET TWO
           ================================================== */

        .planet-two {

            right: 125px;

            bottom: 90px;

            width: 55px;

            height: 55px;

            border-radius: 50%;

            background:
                radial-gradient(
                    circle at 35% 30%,
                    #F6D77A,
                    #8C5B28 50%,
                    #2A1420 100%
                );

            opacity: 0.28;

            box-shadow:
                0 0 25px
                rgba(246, 215, 122, 0.30);

        }


        /* ==================================================
           DECORATIVE STARS
           ================================================== */

        .cosmic-star {

            color: #F6D77A;

            opacity: 0.70;

            font-size: 20px;

            text-shadow:
                0 0 12px
                rgba(246, 215, 122, 0.80);

        }


        .star-one {

            top: 160px;

            right: 220px;

        }


        .star-two {

            top: 280px;

            right: 80px;

            color: #D6A4FF;

        }


        .star-three {

            top: 470px;

            left: 390px;

        }


        .star-four {

            bottom: 180px;

            right: 260px;

            color: #D6A4FF;

        }


        /* ==================================================
           SMALL SCREEN
           ================================================== */

        @media (max-width: 900px) {

            .cosmic-moon,
            .cosmic-planet {

                opacity: 0.12;

            }

            .cosmic-star {

                opacity: 0.35;

            }

        }

        </style>
        """,
        unsafe_allow_html=True,
    )

# ======================================================
# Golden Palmistry Decoration
# ======================================================

def add_palmistry_decoration():

    st.html(
        """
<div class="golden-palmistry">

    <div class="palm-glow">
        🖐
    </div>

    <div class="palm-line palm-line-one"></div>

    <div class="palm-line palm-line-two"></div>

    <div class="palm-line palm-line-three"></div>

    <div class="palm-line palm-line-four"></div>

</div>

<style>

.golden-palmistry {

    position: fixed;

    right: 35px;

    bottom: 55px;

    width: 250px;

    height: 300px;

    pointer-events: none;

    z-index: 5;

    opacity: 0.18;

}


.palm-glow {

    position: absolute;

    right: 35px;

    top: 25px;

    font-size: 170px;

    color: #F6D77A;

    filter:
        drop-shadow(
            0 0 18px
            rgba(246, 215, 122, 0.65)
        );

    opacity: 0.35;

}


.palm-line {

    position: absolute;

    height: 2px;

    background: #F6D77A;

    border-radius: 50%;

    box-shadow:
        0 0 8px
        rgba(246, 215, 122, 0.75);

}


.palm-line-one {

    width: 110px;

    right: 48px;

    top: 145px;

    transform:
        rotate(12deg);

}


.palm-line-two {

    width: 95px;

    right: 45px;

    top: 170px;

    transform:
        rotate(-8deg);

}


.palm-line-three {

    width: 80px;

    right: 58px;

    top: 195px;

    transform:
        rotate(10deg);

}


.palm-line-four {

    width: 65px;

    right: 65px;

    top: 220px;

    transform:
        rotate(-12deg);

}


@media (max-width: 1000px) {

    .golden-palmistry {

        opacity: 0.08;

        right: 5px;

    }

}

</style>
        """,
        
    )

# ======================================================
# Premium Sidebar + Upload Styling
# ======================================================

def apply_sidebar_theme():

    st.markdown(
        """
        <style>

        /* ==================================================
           SIDEBAR
           ================================================== */

        section[data-testid="stSidebar"] {

            background:
                linear-gradient(
                    180deg,
                    #09051A 0%,
                    #13082A 50%,
                    #080417 100%
                ) !important;

            border-right:
                1px solid
                rgba(183, 112, 255, 0.40) !important;

            box-shadow:
                8px 0 35px
                rgba(86, 35, 140, 0.22) !important;

        }


        /* ==================================================
           SIDEBAR TEXT
           ================================================== */

        section[data-testid="stSidebar"] label {

            color:
                #EDE2F7 !important;

            font-weight:
                500 !important;

        }


        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {

            color:
                #F6D77A !important;

            text-shadow:
                0 0 10px
                rgba(246, 215, 122, 0.25);

        }


        /* ==================================================
           SIDEBAR DIVIDERS
           ================================================== */

        section[data-testid="stSidebar"] hr {

            border-color:
                rgba(183, 112, 255, 0.25) !important;

        }


        /* ==================================================
           SIDEBAR TEXT INPUT
           ================================================== */

        section[data-testid="stSidebar"]
        .stTextInput input {

            background:
                #130C2B !important;

            color:
                #FFFFFF !important;

            border:
                1px solid
                rgba(183, 112, 255, 0.55) !important;

            border-radius:
                12px !important;

        }


        section[data-testid="stSidebar"]
        .stTextInput input::placeholder {

            color:
                #A99BB8 !important;

        }


        /* ==================================================
           FILE UPLOADER
           ================================================== */

        section[data-testid="stSidebar"]
        section[data-testid="stFileUploader"] {

            background:
                rgba(25, 14, 50, 0.95) !important;

            border:
                1px solid
                rgba(183, 112, 255, 0.45) !important;

            border-radius:
                16px !important;

            padding:
                8px !important;

        }


        /* Upload drop zone */

        section[data-testid="stSidebar"]
        [data-testid="stFileUploaderDropzone"] {

            background:
                rgba(18, 10, 38, 0.95) !important;

            border:
                1px dashed
                rgba(246, 215, 122, 0.50) !important;

            border-radius:
                14px !important;

        }


        /* Upload text */

        section[data-testid="stSidebar"]
        section[data-testid="stFileUploader"] span {

            color:
                #EDE2F7 !important;

            opacity:
                1 !important;

        }


        /* Upload button */

        section[data-testid="stSidebar"]
        section[data-testid="stFileUploader"] button {

            background:
                linear-gradient(
                    135deg,
                    #6A1B9A,
                    #32105B
                ) !important;

            color:
                #FFFFFF !important;

            border:
                1px solid
                rgba(246, 215, 122, 0.55) !important;

            border-radius:
                10px !important;

            opacity:
                1 !important;

        }


        /* Upload button text */

        section[data-testid="stSidebar"]
        section[data-testid="stFileUploader"] button span {

            color:
                #FFFFFF !important;

            opacity:
                1 !important;

        }


        /* File type information */

        section[data-testid="stSidebar"]
        section[data-testid="stFileUploader"] small {

            color:
                #C9B8D9 !important;

            opacity:
                1 !important;

        }


        /* ==================================================
           ANALYZE BUTTON
           ================================================== */

        section[data-testid="stSidebar"]
        .stButton > button {

            min-height:
                52px !important;

            background:
                linear-gradient(
                    135deg,
                    #7B1FA2,
                    #42105F
                ) !important;

            color:
                #FFFFFF !important;

            border:
                1px solid
                rgba(246, 215, 122, 0.65) !important;

            border-radius:
                15px !important;

            font-size:
                16px !important;

            font-weight:
                700 !important;

            box-shadow:
                0 0 22px
                rgba(123, 31, 162, 0.35) !important;

        }


        section[data-testid="stSidebar"]
        .stButton > button:hover {

            background:
                linear-gradient(
                    135deg,
                    #9C27B0,
                    #5E177F
                ) !important;

            border-color:
                #F6D77A !important;

            box-shadow:
                0 0 30px
                rgba(183, 112, 255, 0.45) !important;

        }


        /* ==================================================
           MOBILE RESPONSIVE DESIGN
           ================================================== */

        @media (max-width: 700px) {
            
            /* Main content */
            .main.block-container {

                width: 100% !important;
                max-width: 100% !important;
                padding-left: 12px !important;
                padding-right: 12px !important;
                padding-top: 1rem !important;
                padding-bottom: 2rem !important;

                margin: 0 !important;

            }


            /* Prevent horizontal overflow */
            .stApp,
            [data-testid="stAppViewContainer"],
            [data-testid="stAppViewBlockContainer"] {

                max-width: 100% !important;

                overflow-x: hidden !important;

            }

            /* Sidebar */
            section[data-testid="stSidebar"] {
                    
                max-width: 85vw !important;
                box-shadow: none !important;
            
            }

            /* Headings */

            .stApp h1 {
                font-size: 1.8rem !important;

            }

            .stApp h2 {
                font-size: 1.45rem !important;
    
            }

            .stApp h3 {
                font-size: 1.15rem !important;

            }

            /* Header and buttons */
            button {

                max-width: 100% !important;

                box-sizing: border-box !important;
            
            }


            /* Text inputs */

            input,
            textarea {
                 max-width: 100% !important;
                 box-sizing: border-box !important;
            }
            
            /* Images */
            img {

                 max-width: 100% !important;
                 height: auto !important;

            }

            /* Expanders */

            [data-testid="stExpander"] {

                max-width: 100% !important;
                box-sizing: border-box !important;

            }

           
            /* Columns */
            [data-testid="stHorizontalBlock"] { 

                width: 100% !important;
                max-width: 100% !important;
                box-sizing: border-box !important;

            }

            /* Column contents */

            [data-testid="column"] {

                min-width: 0 !important;

                max-width: 100% !important;

                box-sizing: border-box !important;

            }

            /* Metrics */

            div[data-testid="metric-container"] {

                max-width: 100% !important;

                box-sizing: border-box !important;

            }

        }

        </style>
        """,
        unsafe_allow_html=True

    )
 
# ======================================================
# Mystical Header
# ======================================================

def add_mystical_header():

    st.html(

        """
<div class="mystical-header">

    <div class="mystical-orb">
        🔮
    </div>

    <div class="mystical-header-text">

        <div class="mystical-title">
             PALMISTRY ASSISTANT
        </div>

        <div class="mystical-subtitle">
            ✦ Palmistry Knowledge ✦
        </div>

    </div>

    <div class="mystical-stars">
        ✦ &nbsp; ✧ &nbsp; ✦ &nbsp; ✧ &nbsp; ✦
    </div>

</div>

<style>

.mystical-header {

    position: relative;

    display: flex;

    align-items: center;

    justify-content: center;

    gap: 22px;

    padding: 24px 30px;

    margin-bottom: 25px;

    border-radius: 24px;

    background:
        linear-gradient(
            135deg,
            rgba(42, 18, 78, 0.95),
            rgba(12, 7, 31, 0.95)
        );

    border:
        1px solid
        rgba(214, 164, 255, 0.35);

    box-shadow:
        0 0 30px
        rgba(122, 56, 184, 0.20);

    overflow: hidden;

}


.mystical-header::before {

    content: "";

    position: absolute;

    width: 280px;

    height: 280px;

    top: -180px;

    left: 15%;

    background:
        radial-gradient(
            circle,
            rgba(183, 112, 255, 0.25),
            transparent 70%
        );

    pointer-events: none;

}


.mystical-orb {

    width: 68px;

    height: 68px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 50%;

    font-size: 38px;

    background:
        radial-gradient(
            circle at 35% 30%,
            #D6A4FF,
            #6A1B9A 45%,
            #17082F 100%
        );

    border:
        1px solid
        rgba(246, 215, 122, 0.60);

    box-shadow:
        0 0 20px
        rgba(183, 112, 255, 0.55);

}


.mystical-title {

    color: #F6D77A;

    font-size: 28px;

    font-weight: 800;

    letter-spacing: 2px;

}


.mystical-subtitle {

    margin-top: 5px;

    color: #D6A4FF;

    font-size: 14px;

    letter-spacing: 1px;

}


.mystical-stars {

    position: absolute;

    top: 12px;

    right: 25px;

    color: #F6D77A;

    font-size: 13px;

    opacity: 0.65;

}


@media (max-width: 700px) {

    .mystical-header {

        flex-direction: column;

        text-align: center;

    }

    .mystical-title {

        font-size: 21px;

    }

    .mystical-stars {

        display: none;

    }

}

</style>
        """
        
    )

# ======================================================
# Premium Dashboard Theme
# ======================================================

def apply_dashboard_theme():

    st.markdown(
        """
        <style>

        /* ==================================================
           DASHBOARD METRIC CARDS
           ================================================== */

        div[data-testid="metric-container"] {

            position: relative;

            overflow: hidden;

            min-height: 125px;

            background:
                linear-gradient(
                    145deg,
                    rgba(42, 22, 76, 0.96),
                    rgba(15, 10, 38, 0.96)
                ) !important;

            border:
                1px solid
                rgba(183, 112, 255, 0.45) !important;

            border-radius:
                18px !important;

            padding:
                20px !important;

            box-shadow:
                0 0 25px
                rgba(139, 74, 255, 0.20) !important;

            transition:
                transform 0.25s ease,
                box-shadow 0.25s ease;

        }


        /* ==================================================
           CARD STAR
           ================================================== */

        div[data-testid="metric-container"]::before {

            content:
                "✦";

            position:
                absolute;

            top:
                8px;

            right:
                12px;

            color:
                #D6A4FF;

            opacity:
                0.45;

            font-size:
                14px;

        }


        /* ==================================================
           CARD GLOW
           ================================================== */

        div[data-testid="metric-container"]::after {

            content:
                "";

            position:
                absolute;

            bottom:
                -50px;

            left:
                -20px;

            width:
                120px;

            height:
                80px;

            background:
                radial-gradient(
                    circle,
                    rgba(183, 112, 255, 0.18),
                    transparent 70%
                );

            pointer-events:
                none;

        }


        /* ==================================================
           HOVER EFFECT
           ================================================== */

        div[data-testid="metric-container"]:hover {

            transform:
                translateY(-5px);

            box-shadow:
                0 0 30px
                rgba(183, 112, 255, 0.35) !important;

        }


        /* ==================================================
           METRIC VALUE
           ================================================== */

        div[data-testid="stMetricValue"] {

            color:
                #F6D77A !important;

            font-size:
                32px !important;

            font-weight:
                800 !important;

            text-shadow:
                0 0 10px
                rgba(246, 215, 122, 0.25);

        }


        /* ==================================================
           METRIC LABEL
           ================================================== */

        div[data-testid="stMetricLabel"] {

            color:
                #D6A4FF !important;

            font-size:
                14px !important;

            font-weight:
                600 !important;

        }


        /* ==================================================
           DASHBOARD DIVIDER
           ================================================== */

        .dashboard-divider {

            height:
                1px;

            margin:
                15px 0 25px 0;

            background:
                linear-gradient(
                    90deg,
                    transparent,
                    rgba(183, 112, 255, 0.55),
                    rgba(246, 215, 122, 0.45),
                    transparent
                );

        }

        </style>
        """,
        unsafe_allow_html=True,
    )

