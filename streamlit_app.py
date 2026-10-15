import streamlit as st

st.set_page_config(
    page_title="Kanushi Taneja | Marketing Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# LINKS
# =========================================================

LINKEDIN = "https://www.linkedin.com/in/kanushi-taneja/"
EMAIL = "mailto:kanushitaneja.work@gmail.com"

RESUME = "https://raw.githubusercontent.com/27-kanushitaneja-ctrl/E-portfolio/main/Kanushi%20Taneja_RESUME_.pdf"

AGRAMI = "https://github.com/27-kanushitaneja-ctrl/FMCG-Live-Project"
NYKAA = "https://github.com/27-kanushitaneja-ctrl/Nykaa-Spec-Campaign-WhoTaughtYou"
FAE = "https://github.com/27-kanushitaneja-ctrl/FAE-YOUR-WAY"
COIL = "https://github.com/27-kanushitaneja-ctrl/COIL-International-Insights"


# =========================================================
# GLOBAL CSS
# =========================================================

st.html("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap');

:root {
    --cream: #F7F3ED;
    --paper: #FCFAF7;
    --ink: #28221F;
    --muted: #766B62;
    --line: #DED3C7;
    --burgundy: #773C48;
    --blush: #EADCD8;
    --sand: #E7DED2;
}

html {
    scroll-behavior: smooth;
}

body,
.stApp {
    background: var(--cream);
    color: var(--ink);
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1160px;
    padding: 28px 34px 70px;
}

#MainMenu,
footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

p {
    color: var(--muted);
}

/* NAVIGATION */

.navbar {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
    padding: 15px 0 23px;
    border-bottom: 1px solid var(--line);
}

.logo {
    font-family: 'Playfair Display', serif;
    font-size: 27px;
    font-weight: 600;
    color: var(--burgundy);
    letter-spacing: -1px;
}

.nav-right {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    color: var(--muted);
}

/* HERO */

.hero {
    padding: 75px 0 35px;
}

.kicker,
.section-label,
.contact-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2.1px;
    text-transform: uppercase;
    color: var(--burgundy);
}

.kicker {
    margin-bottom: 24px;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(52px, 6.3vw, 80px);
    line-height: 1.02;
    letter-spacing: -2.8px;
    font-weight: 400;
    color: var(--ink);
}

.hero-title em,
.about-heading em,
.thinking-title em,
.contact-title em,
.visual-title em {
    color: var(--burgundy);
    font-weight: 400;
}

.hero-intro {
    font-size: 19px;
    line-height: 1.7;
    color: #51463F;
    max-width: 660px;
    margin-top: 28px;
}

.hero-intro strong,
.about-copy strong {
    color: var(--ink);
    font-weight: 600;
}

.hero-detail {
    font-size: 14px;
    line-height: 1.85;
    color: var(--muted);
    max-width: 600px;
    margin-top: 15px;
}

.hero-line {
    width: 58px;
    height: 2px;
    background: var(--burgundy);
    margin-top: 30px;
}

/* PROFILE */

.profile-card {
    background: var(--sand);
    padding: 10px;
    margin-top: 70px;
    border: 1px solid #D8CBBE;
}

.profile-card img {
    display: block;
    width: 100%;
    border-radius: 2px;
}

.profile-caption {
    font-size: 9px;
    letter-spacing: 1.7px;
    text-transform: uppercase;
    color: var(--muted);
    margin-top: 13px;
}

/* BUTTONS */

.stLinkButton a {
    border: 1px solid #C7B5A8 !important;
    border-radius: 2px !important;
    background: transparent !important;
    color: var(--burgundy) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 10px !important;
    font-weight: 700 !important;
    letter-spacing: 1.1px !important;
    transition: background 180ms ease, color 180ms ease;
}

.stLinkButton a:hover {
    background: var(--burgundy) !important;
    color: #FFFFFF !important;
    border-color: var(--burgundy) !important;
}

/* STATISTICS */

.proof {
    border-top: 1px solid var(--line);
    border-bottom: 1px solid var(--line);
    padding: 24px 0;
    margin: 20px 0 80px;
}

.proof-number {
    font-family: 'Playfair Display', serif;
    font-size: 36px;
    line-height: 1.2;
    color: var(--burgundy);
}

.proof-label {
    font-size: 9px;
    line-height: 1.6;
    letter-spacing: 1.3px;
    text-transform: uppercase;
    color: var(--muted);
    margin-top: 7px;
}

/* SECTION HEADINGS */

.section-label {
    margin-bottom: 13px;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(38px, 4.2vw, 50px);
    line-height: 1.12;
    font-weight: 400;
    letter-spacing: -1.2px;
    color: var(--ink);
    margin-bottom: 38px;
}

/* PROJECT VISUALS */

.project-visual {
    min-height: 315px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 35px;
    border: 1px solid rgba(80, 60, 50, 0.08);
}

.agrami {
    background: #E7DED0;
}

.nykaa {
    background: #EADBD9;
}

.fae {
    background: #E4DED7;
}

.coil {
    background: #DFE1DF;
}

.visual-label {
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--burgundy);
    margin-bottom: 16px;
}

.visual-title {
    font-family: 'Playfair Display', serif;
    font-size: 46px;
    line-height: 1.02;
    color: var(--ink);
}

/* PROJECT IMAGES */

div[data-testid="stImage"] {
    width: 100%;
    margin-bottom: 0;
}

div[data-testid="stImage"] img {
    display: block;
    width: 100%;
    height: 315px;
    object-fit: cover;
    border-radius: 2px;
}

/* PROJECT INFORMATION */

.project {
    border-top: 1px solid var(--line);
    padding: 25px 0 30px;
}

.project-number {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.7px;
    color: var(--burgundy);
}

.project-name {
    font-family: 'Playfair Display', serif;
    font-size: clamp(32px, 3.5vw, 42px);
    line-height: 1.15;
    letter-spacing: -0.8px;
    color: var(--ink);
    margin-top: 8px;
}

.project-tag {
    display: inline-block;
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 1.2px;
    color: var(--burgundy);
    padding: 6px 9px;
    border: 1px solid #CDB6B0;
    margin: 12px 0 16px;
}

.project-description {
    font-size: 14px;
    line-height: 1.85;
    color: #655A51;
}

.project-role {
    font-size: 12px;
    line-height: 1.8;
    color: #39312D;
    margin-top: 19px;
}

.role-label {
    font-size: 9px;
    letter-spacing: 1.5px;
    font-weight: 700;
    color: var(--burgundy);
    margin-bottom: 6px;
}

/* ABOUT */

.about {
    margin-top: 100px;
}

.about-heading {
    font-family: 'Playfair Display', serif;
    font-size: clamp(32px, 3.5vw, 40px);
    line-height: 1.25;
    color: var(--ink);
}

.about-copy {
    font-size: 15px;
    line-height: 1.9;
    color: #655A51;
}

.about-side {
    border-left: 2px solid #D4B7B1;
    padding: 8px 0 8px 28px;
}

.side-label {
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    color: var(--burgundy);
}

.side-title {
    font-family: 'Playfair Display', serif;
    font-size: 29px;
    line-height: 1.3;
    color: var(--ink);
    margin-top: 14px;
}

.side-title em {
    color: var(--burgundy);
}

.side-copy {
    font-size: 13px;
    line-height: 1.85;
    color: var(--muted);
    margin-top: 16px;
}

/* HOW I THINK */

.thinking {
    margin-top: 100px;
    padding: 48px 0;
    border-top: 1px solid var(--line);
    border-bottom: 1px solid var(--line);
}

.thinking-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(31px, 3.5vw, 40px);
    line-height: 1.3;
    color: var(--ink);
}

.thinking-step {
    padding: 17px 0;
    border-bottom: 1px solid var(--line);
    font-size: 13px;
    line-height: 1.8;
    color: #655A51;
}

.thinking-step:last-child {
    border-bottom: none;
}

.thinking-step strong {
    color: var(--ink);
    font-weight: 700;
}

.thinking-number {
    color: var(--burgundy);
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-right: 10px;
}

/* MARKETING TOOLKIT */

.toolkit {
    margin-top: 90px;
}

.toolkit-box {
    border-top: 1px solid var(--line);
    padding: 22px 0 26px;
}

.toolkit-label {
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    color: var(--burgundy);
}

.toolkit-text {
    font-size: 14px;
    line-height: 1.9;
    color: #51463F;
    margin-top: 9px;
}

/* INTERNSHIP EXPERIENCE */

.internship-card {
    display: grid;
    grid-template-columns: 42px minmax(0, 1fr);
    gap: 19px;
    padding: 29px 0;
    border-top: 1px solid var(--line);
}

.internship-number {
    font-family: 'Playfair Display', serif;
    font-size: 29px;
    color: #B29A91;
    line-height: 1.2;
}

.internship-content {
    min-width: 0;
}

.internship-topline {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 12px;
    flex-wrap: wrap;
}

.internship-company {
    font-family: 'Playfair Display', serif;
    font-size: 27px;
    line-height: 1.3;
    color: var(--ink);
    max-width: 750px;
}

.internship-date {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1px;
    color: var(--burgundy);
    padding-top: 8px;
}

.internship-role {
    font-size: 12px;
    font-weight: 600;
    color: var(--muted);
    margin-top: 7px;
}

.internship-description {
    font-size: 14px;
    line-height: 1.85;
    color: #655A51;
    max-width: 800px;
    margin-top: 16px;
}

.internship-tags {
    font-size: 9px;
    font-weight: 700;
    line-height: 1.8;
    letter-spacing: 1px;
    color: var(--burgundy);
    margin-top: 14px;
}

/* CONTACT */

.contact {
    background: var(--burgundy);
    color: #FFFFFF;
    margin-top: 90px;
    padding: 58px 52px;
}

.contact-label {
    color: #E8D5D0;
}

.contact-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(36px, 4.5vw, 53px);
    line-height: 1.12;
    margin-top: 16px;
    color: #FFFFFF;
}

.contact-title em {
    color: #F0D8D1;
}

.contact-copy {
    font-size: 14px;
    line-height: 1.8;
    color: #F0E4E0;
    max-width: 520px;
    margin-top: 20px;
}

/* FOOTER */

.footer {
    border-top: 1px solid var(--line);
    margin-top: 38px;
    padding-top: 18px;
    display: flex;
    justify-content: space-between;
    gap: 15px;
    font-size: 9px;
    letter-spacing: 1px;
    color: var(--muted);
}

/* MOBILE */

@media (max-width: 768px) {
    .block-container {
        padding: 18px 20px 45px;
    }

    .navbar {
        align-items: flex-start;
        padding-bottom: 17px;
    }

    .logo {
        font-size: 23px;
    }

    .nav-right {
        font-size: 8px;
        letter-spacing: 1px;
        text-align: right;
        line-height: 1.7;
    }

    .hero {
        padding: 48px 0 25px;
    }

    .hero-title {
        font-size: clamp(43px, 10vw, 58px);
        letter-spacing: -1.8px;
    }

    .hero-intro {
        font-size: 17px;
    }

    .profile-card {
        margin-top: 15px;
    }

    .proof {
        margin-bottom: 60px;
        padding: 20px 0;
    }

    .proof-number {
        font-size: 30px;
    }

    .proof-label {
        font-size: 8px;
        letter-spacing: 0.8px;
    }

    .section-title {
        font-size: 38px;
        margin-bottom: 28px;
    }

    .project-visual {
        min-height: 245px;
        padding: 25px;
    }

    .visual-title {
        font-size: 38px;
    }

    .project-name {
        font-size: 34px;
    }

    .about,
    .toolkit {
        margin-top: 70px;
    }

    .about-side {
        margin-top: 30px;
        padding-left: 20px;
    }

    .thinking {
        margin-top: 70px;
        padding: 35px 0;
    }

    .thinking-title {
        font-size: 31px;
    }

    .internship-card {
        grid-template-columns: 30px minmax(0, 1fr);
        gap: 12px;
        padding: 24px 0;
    }

    .internship-number {
        font-size: 24px;
    }

    .internship-company {
        font-size: 23px;
    }

    .contact {
        margin-top: 65px;
        padding: 38px 25px;
    }

    .contact-title {
        font-size: 37px;
    }

    .footer {
        display: block;
        line-height: 2;
    }
}

@media (prefers-reduced-motion: reduce) {
    html {
        scroll-behavior: auto;
    }

    * {
        transition: none !important;
    }
}

</style>
""")


# =========================================================
# NAVIGATION
# =========================================================

st.html("""
<div class="navbar">

    <div class="logo">
        Kanushi Taneja
    </div>

    <div class="nav-right">
        MARKETING · BRAND · DIGITAL
    </div>

</div>
""")


# =========================================================
# HERO
# =========================================================

left, right = st.columns([1.65, 0.75], gap="large")

with left:

    st.html("""
    <div class="hero">

        <div class="kicker">
            PGDM MARKETING · NEW DELHI · 2026
        </div>

        <div class="hero-title">
            Marketing that<br>
            starts with <em>people.</em>
        </div>

        <div class="hero-intro">
            I'm <strong>Kanushi Taneja</strong> — a PGDM Marketing
            candidate interested in the space where
            <strong>consumer behaviour, strategy and creativity</strong>
            come together.
        </div>

        <div class="hero-detail">
            I turn observations into insights, insights into ideas,
            and ideas into campaigns, content and communication
            that have a reason to exist.
        </div>

        <div class="hero-line"></div>

    </div>
    """)

    c1, c2 = st.columns(2)

    with c1:
        st.link_button(
            "VIEW LINKEDIN",
            LINKEDIN,
            use_container_width=True
        )

    with c2:
        st.link_button(
            "DOWNLOAD RESUME",
            RESUME,
            use_container_width=True
        )


with right:

    st.html("""
    <div class="profile-card">
    """)

    st.image(
        "profile.png",
        use_container_width=True
    )

    st.html("""
    </div>

    <div class="profile-caption">
        KANUSHI TANEJA · MARKETING
    </div>
    """)


# =========================================================
# PROOF STRIP
# =========================================================

st.html("""
<div style="
    display:grid;
grid-template-columns:repeat(3,minmax(0,1fr));
max-width:900px;
margin:25px auto 45px;
    background:#F0E7DF;
    border:1px solid #DED0C5;
">

    <div style="padding:27px 24px;border-right:1px solid #D8C7BC;">
        <div style="
            font-family:'Playfair Display',serif;
            font-size:36px;
            color:#773C48;
            line-height:1.1;
        ">04</div>
        <div style="
            font-family:'DM Sans',sans-serif;
            font-size:9px;
            letter-spacing:1.3px;
            line-height:1.7;
            color:#766B62;
            margin-top:10px;
        ">INTERNSHIP EXPERIENCES</div>
    </div>

    <div style="padding:27px 24px;border-right:1px solid #D8C7BC;">
        <div style="
            font-family:'Playfair Display',serif;
            font-size:36px;
            color:#773C48;
            line-height:1.1;
        ">06+</div>
        <div style="
            font-family:'DM Sans',sans-serif;
            font-size:9px;
            letter-spacing:1.3px;
            line-height:1.7;
            color:#766B62;
            margin-top:10px;
        ">INSURANCE BRANDS ANALYSED</div>
    </div>

    <div style="padding:27px 24px;">
        <div style="
            font-family:'Playfair Display',serif;
            font-size:36px;
            color:#773C48;
            line-height:1.1;
        ">06</div>
        <div style="
            font-family:'DM Sans',sans-serif;
            font-size:9px;
            letter-spacing:1.3px;
            line-height:1.7;
            color:#766B62;
            margin-top:10px;
        ">FEATURED PROJECTS</div>
    </div>

</div>

<style>
@media (max-width:600px) {
    div[style*="grid-template-columns:repeat(3"] {
        grid-template-columns:1fr !important;
    }
}
</style>
""")

# =========================================================
# INTERNSHIP EXPERIENCE
# =========================================================

st.html("""
<div style="margin-top:35px; margin-bottom:30px;">
    <div class="section-label">01 — INTERNSHIP EXPERIENCE</div>
    <div class="section-title">Where I've learned by doing.</div>
    <p style="
        font-family:'DM Sans',sans-serif;
        font-size:15px;
        line-height:1.7;
        color:#746D65;
        max-width:650px;
        margin-top:-25px;
    ">
        Experiences that helped me connect research, communication
        and consumer understanding with real-world work.
    </p>
</div>
""")

internships = [
    {
        "number": "01",
        "company": "Aditya Birla Capital",
        "role": "Marketing Communications Intern",
        "date": "APR — JUL 2026",
        "description": (
            "Analysed 6+ insurance brands across four social platforms "
            "and evaluated 100+ content pieces. Conducted 30+ consumer "
            "interviews to understand audience needs and support "
            "marketing communication planning."
        ),
        "tags": "COMPETITOR ANALYSIS · CONSUMER INSIGHTS · CONTENT STRATEGY"
    },
    {
        "number": "02",
        "company": "Office of the Chief Commissioner "
                   "for Persons with Disabilities (CCPD)",
        "role": "Research Intern",
        "date": "JAN 2026",
        "description": (
            "Studied disability frameworks across 20 countries and "
            "updated and verified the directory of State Commissioners "
            "for Persons with Disabilities across 33 States and UTs. "
            "Strengthened research, information verification and "
            "analytical skills through policy-focused work."
        ),
        "tags": "POLICY RESEARCH · COMPARATIVE ANALYSIS · DATA VERIFICATION"
    },
       {
        "number": "03",
        "company": "The Leading Solutions",
        "role": "Marketing Intern",
        "date": "JUL 2023 – OCT 2023",
        "description": (
            "Supported financial product marketing and lead nurturing "
            "by following up with 10–15 client leads. Managed client "
            "communication and assisted in policy-sales conversion."
        ),
        "tags": "FINANCIAL MARKETING · LEAD NURTURING · CLIENT ENGAGEMENT"
    },
    {
        "number": "04",
        "company": "Master's Buddy",
        "role": "Marketing Intern",
        "date": "JUL 2023",
        "description": (
            "Conducted competitor analysis across four brands to "
            "understand their marketing and content approaches. "
            "Identified content gaps and opportunities for "
            "content optimisation."
        ),
        "tags": "COMPETITOR RESEARCH · CONTENT ANALYSIS · DIGITAL MARKETING"
    }
]

for item in internships:
    st.html(f"""
    <div class="internship-card">

        <div class="internship-number">
            {item['number']}
        </div>

        <div class="internship-content">

            <div class="internship-topline">
                <div class="internship-company">
                    {item['company']}
                </div>

                <div class="internship-date">
                    {item['date']}
                </div>
            </div>

            <div class="internship-role">
                {item['role']}
            </div>

            <div class="internship-description">
                {item['description']}
            </div>

            <div class="internship-tags">
                {item['tags']}
            </div>

        </div>

    </div>
    """)

st.html("""
<div style="border-top:1px solid #CEC5B9; margin-bottom:75px;"></div>
""")

# =========================================================
# SELECTED WORK
# =========================================================

st.html("""
<div>

    <div class="section-label">
        01 — SELECTED WORK
    </div>

    <div class="section-title">
        Ideas I've built.
    </div>

</div>
""")

# =========================================================
# SUPERDRINKS — PROJECT 01
# =========================================================

left, right = st.columns([1.05, 1], gap="large")

with left:
    st.image(
        "superdrinks.png",
        use_container_width=True
    )

with right:
    st.html("""
    <div class="project">

        <div class="project-number">01 / 05</div>

        <div class="project-name">SuperDrinks</div>

        <div class="project-tag">LIVE PROJECT</div>

        <div class="project-description">
            A live brand marketing project exploring how
            consumer insights, product occasions and creative
            communication can create new opportunities for a
            ready-to-drink beverage brand.
        </div>

        <div class="project-role">
            <div class="role-label">MY CONTRIBUTION</div>

            Brand audit and SWOT analysis · WhatsApp promotional
            communication · Coffee 911 launch campaign concept ·
            Proposed campus activation · The Crunch Match
            collaboration pitch
        </div>

    </div>
    """)

   
st.link_button(
    "EXPLORE PROJECT & CREATIVES ↗",
    "https://github.com/27-kanushitaneja-ctrl/SuperDrinks-Live-Project",
    use_container_width=False
)

st.link_button(
    "VISIT BRAND WEBSITE ↗",
    "https://superdrinks.in/",
    use_container_width=False
)



# =========================================================
# AGRAMI
# =========================================================

left, right = st.columns([1.05, 1], gap="large")

with left:
    st.image(
        "agrami.png",
        use_container_width=True
    )

with right:

    st.html("""
    <div class="project">

        <div class="project-number">
            02 / 06
        </div>

        <div class="project-name">
            AGRAMI
        </div>

        <div class="project-tag">
            LIVE PROJECT
        </div>

        <div class="project-description">
            An integrated FMCG strategy focused on building
            consumer trust through content, transparency,
            education and community.
        </div>

        <div class="project-role">

            <div class="role-label">
                MY CONTRIBUTION
            </div>

            Content pillars · Sample creatives · Launch strategy ·
            Influencer strategy · PR & community planning

        </div>

    </div>
    """)

    st.link_button("VIEW PROJECT →", AGRAMI)



# =====================================================
# PROJECT 03 — ABSLI INSIGHTAI
# =====================================================

left, right = st.columns([1.05, 1], gap="large")

with left:
    st.image(
        "absli.png",
        use_container_width=True
    )

with right:
    st.html("""
    <div class="project">

        <div class="project-number">
            03 / 06
        </div>

        <div class="project-name">
            ABSLI InsightAI
        </div>

        <div class="project-tag">
            AI-POWERED MARKETING COMMUNICATIONS DASHBOARD
        </div>

        <div class="project-description">
            An AI-powered dashboard prototype exploring how social media
            and competitor data can be transformed into meaningful
            marketing insights through content classification, sentiment
            analysis, consumer segmentation and engagement analysis.
        </div>

        <div class="project-role">

            <div class="role-label">
                MY CONTRIBUTION
            </div>

            Conceptualised the dashboard workflow · Structured marketing
            analytics modules · Developed the prototype using Lovable
            with ChatGPT supporting prompt development

        </div>

        <div class="project-role">

            <div class="role-label">
                TOOLS
            </div>

            Lovable · ChatGPT

        </div>

    </div>
    """)

    st.link_button(
        "EXPLORE LIVE DASHBOARD →",
        "https://marcom-insight-ai.lovable.app/"
    )


# =====================================================
# PROJECT 04 — NYKAA
# =====================================================


# =====================================================
# PROJECT 04 — NYKAA
# =====================================================

left, right = st.columns([1.05, 1], gap="large")

with left:
    st.image(
        "nykaa.png",
        use_container_width=True
    )

with right:

    st.html("""
    <div class="project">

        <div class="project-number">
            04 / 06
        </div>

        <div class="project-name">
            NYKAA
        </div>

        <div class="project-tag">
            SPEC CAMPAIGN
        </div>

        <div class="project-description">
            A social campaign built around the idea that beauty
            knowledge travels from one person to another —
            turning that behaviour into a community-led
            content platform.
        </div>

        <div class="project-role">

            <div class="role-label">
                MY CONTRIBUTION
            </div>

            Instagram audit · Consumer insight · Campaign platform ·
            Content formats · Rollout · KPI framework

        </div>

    </div>
    """)

    st.link_button("VIEW PROJECT →", NYKAA)


# =========================================================
# FAE
# =========================================================

left, right = st.columns([1.05, 1], gap="large")

with left:
    st.image(
        "fae.png",
        use_container_width=True
    )

with right:

    st.html("""
    <div class="project">

        <div class="project-number">
            05 / 06
        </div>

        <div class="project-name">
            FAE BEAUTY
        </div>

        <div class="project-tag">
            CAMPAIGN CONCEPT
        </div>

        <div class="project-description">
            A beauty campaign based on the idea that people
            don't have one fixed aesthetic. Different moods
            can create different looks, expressions and
            product journeys.
        </div>

        <div class="project-role">

            <div class="role-label">
                PROJECT FOCUS
            </div>

            Consumer insight · Big idea · Social content ·
            Creator / UGC loop · Commerce journey

        </div>

    </div>
    """)

    st.link_button("VIEW PROJECT →", FAE)


# =========================================================
# COIL
# =========================================================

left, right = st.columns([1.05, 1], gap="large")

with left:
    st.image(
        "coil.png",
        use_container_width=True
    )

with right:
    st.html("""
    <div class="project">

        <div class="project-number">
            06 / 06
        </div>

        <div class="project-name">
            COIL
        </div>

        <div class="project-tag">
            RESEARCH PROJECT
        </div>

        <div class="project-description">
            A cross-cultural research project comparing student
            perspectives from India and the US on employability,
            technical skills, soft skills, AI literacy and
            career readiness.
        </div>

        <div class="project-role">

            <div class="role-label">
                MY ROLE
            </div>

            India-side Focus Group Discussion moderator —
            facilitating conversations, probing responses and
            capturing qualitative perspectives.

        </div>

    </div>
    """)

    st.link_button("VIEW PROJECT →", COIL)


# =========================================================
# ABOUT ME
# =========================================================

st.html("""
<div class="about">

    <div class="section-label">
        02 — ABOUT ME
    </div>

</div>
""")

left, right = st.columns([1.1, 0.9], gap="large")

with left:

    st.html("""
    <div class="about-heading">
        Curious about people.<br>
        Serious about <em>ideas.</em>
    </div>

    <div style="height:28px;"></div>

    <div class="about-copy">

        I'm currently pursuing my <strong>PGDM in Marketing</strong>,
        while building hands-on experience across marketing
        communications, campaign planning, market research,
        competitor analysis and client-facing work.

        <br><br>

        What interests me most is understanding the
        <strong>why behind consumer behaviour</strong> —
        the small observation, contradiction or unmet need
        that can become the starting point for a bigger idea.

        <br><br>

        I enjoy moving between the strategic and the creative:
        understanding the problem, finding the opportunity,
        shaping the idea and thinking about how it can come
        alive through content and communication.

    </div>
    """)

with right:

    st.html("""
    <div class="about-side">

        <div class="side-label">
            WHAT I BRING TO A BRIEF
        </div>

        <div class="side-title">
            A balance of<br>
            <em>thinking + doing.</em>
        </div>

        <div class="side-copy">
            Research enough to understand the problem.
            Think enough to find the opportunity.
            Create enough to make the idea tangible.
        </div>

    </div>
    """)


# =========================================================
# HOW I THINK
# =========================================================

st.html("""
<div class="thinking">

    <div class="section-label">
        03 — HOW I THINK
    </div>

    <div style="height:12px;"></div>

    <div class="thinking-title">
        I don't start with the campaign.<br>
        I start with the <em>tension.</em>
    </div>

</div>
""")

steps = [
    ("01", "OBSERVE", "Understand the consumer, category and context."),
    ("02", "FIND THE TENSION", "Look for the behaviour, contradiction or unmet need."),
    ("03", "BUILD THE IDEA", "Turn the observation into a clear strategic platform."),
    ("04", "MAKE IT SOCIAL", "Translate the idea into content people can understand and participate in."),
    ("05", "MEASURE", "Define what success should look like.")
]

for number, title, description in steps:

    st.html(f"""
    <div class="thinking-step">

        <span class="thinking-number">
            {number}
        </span>

        <strong>
            {title}
        </strong>

        &nbsp; — &nbsp;

        {description}

    </div>
    """)


# =========================================================
# TOOLKIT
# =========================================================

st.html("""
<div class="toolkit">

    <div class="section-label">
        04 — MARKETING TOOLKIT
    </div>

    <div class="section-title">
        What I work with.
    </div>

</div>
""")

left, right = st.columns(2, gap="large")

with left:

    st.html("""
    <div class="toolkit-box">

        <div class="toolkit-label">
            STRATEGY
        </div>

        <div class="toolkit-text">
            Brand Strategy · Campaign Planning ·
            Consumer Insights · Positioning ·
            Marketing Communications
        </div>

    </div>

    <div class="toolkit-box">

        <div class="toolkit-label">
            CONTENT
        </div>

        <div class="toolkit-text">
            Content Strategy · Social Media Strategy ·
            Creative Strategy · Influencer Marketing ·
            PR & Community
        </div>

    </div>
    """)

with right:

    st.html("""
    <div class="toolkit-box">

        <div class="toolkit-label">
            RESEARCH
        </div>

        <div class="toolkit-text">
            Market Research · Competitor Analysis ·
            Qualitative Research · Focus Group Discussions
        </div>

    </div>

    <div class="toolkit-box">

        <div class="toolkit-label">
            TOOLS
        </div>

        <div class="toolkit-text">
            Canva · MS PowerPoint · MS Excel ·
            Google Workspace · GitHub
        </div>

    </div>
    """)


# =========================================================
# CONTACT
# =========================================================

st.html("""
<div class="contact">

    <div class="contact-label">
        05 — LET'S CONNECT
    </div>

    <div class="contact-title">
        Have a brand problem?<br>
        Let's build something <em>interesting.</em>
    </div>

    <div class="contact-copy">
        I'm open to opportunities across marketing, brand,
        digital, content and strategy.
    </div>

</div>
""")

c1, c2, c3 = st.columns(3)

with c1:
    st.link_button(
        "EMAIL ME",
        EMAIL,
        use_container_width=True
    )

with c2:
    st.link_button(
        "LINKEDIN",
        LINKEDIN,
        use_container_width=True
    )

with c3:
    st.link_button(
        "RESUME",
        RESUME,
        use_container_width=True
    )


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="footer">

    <div>
        © 2026 KANUSHI TANEJA
    </div>

    <div>
        MARKETING · BRAND · DIGITAL
    </div>

</div>
""")
