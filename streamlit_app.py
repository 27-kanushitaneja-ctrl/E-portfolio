import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

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
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* -------------------------------------------------------
   FONTS
------------------------------------------------------- */

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@400;500;600&display=swap');


/* -------------------------------------------------------
   GLOBAL
------------------------------------------------------- */

html {
    scroll-behavior: smooth;
}

.stApp {
    background: #F5F1EB;
    color: #191817;
}

.block-container {
    max-width: 1180px;
    padding-top: 1.5rem;
    padding-bottom: 5rem;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}


/* -------------------------------------------------------
   GENERAL TYPE
------------------------------------------------------- */

h1, h2, h3, p {
    font-family: 'DM Sans', sans-serif;
}

.serif {
    font-family: 'Playfair Display', serif;
}


/* -------------------------------------------------------
   NAVIGATION
------------------------------------------------------- */

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 10px 0 22px 0;

    border-bottom: 1px solid #D6CEC3;
}

.nav-logo {
    font-family: 'DM Sans', sans-serif;
    font-weight: 700;
    font-size: 18px;
    letter-spacing: -0.5px;
}

.nav-text {
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    letter-spacing: 1.8px;
    color: #746D65;
    font-weight: 600;
}


/* -------------------------------------------------------
   HERO
------------------------------------------------------- */

.hero {
    padding: 85px 0 75px 0;
}

.hero-kicker {
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #7A7167;
    font-weight: 700;
    margin-bottom: 25px;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(58px, 8vw, 104px);
    line-height: 0.92;
    letter-spacing: -4px;
    font-weight: 500;
    color: #181716;
}

.hero-title em {
    font-style: italic;
}

.hero-intro {
    font-family: 'DM Sans', sans-serif;
    font-size: 20px;
    line-height: 1.55;
    color: #48433D;
    max-width: 720px;
    margin-top: 35px;
}

.hero-intro strong {
    color: #171615;
    font-weight: 600;
}

.hero-detail {
    font-family: 'DM Sans', sans-serif;
    font-size: 15px;
    line-height: 1.75;
    color: #746D65;
    max-width: 660px;
    margin-top: 18px;
}

.hero-rule {
    width: 75px;
    height: 2px;
    background: #191817;
    margin-top: 38px;
}


/* -------------------------------------------------------
   PROFILE IMAGE
------------------------------------------------------- */

.profile-frame {
    border-radius: 0px;
    overflow: hidden;
    background: #DED7CD;
    margin-top: 25px;
}


/* -------------------------------------------------------
   BUTTONS
------------------------------------------------------- */

.stLinkButton > a {
    border-radius: 0px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
}


/* -------------------------------------------------------
   PROOF STRIP
------------------------------------------------------- */

.proof-strip {
    border-top: 1px solid #D1C8BC;
    border-bottom: 1px solid #D1C8BC;

    padding: 28px 0;

    margin: 10px 0 100px 0;
}

.proof-number {
    font-family: 'Playfair Display', serif;
    font-size: 34px;
    line-height: 1;
}

.proof-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 10px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #81786E;
    margin-top: 7px;
}


/* -------------------------------------------------------
   SECTION LABELS
------------------------------------------------------- */

.section-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2.2px;
    text-transform: uppercase;
    color: #83796E;
    margin-bottom: 14px;
}

.section-heading {
    font-family: 'Playfair Display', serif;
    font-size: 51px;
    line-height: 1;
    font-weight: 500;
    letter-spacing: -1px;
    margin-bottom: 50px;
}


/* -------------------------------------------------------
   PROJECTS
------------------------------------------------------- */

.project-card {
    border-top: 1px solid #CFC6BA;
    padding: 30px 0 42px 0;
}

.project-number {
    font-family: 'DM Sans', sans-serif;
    font-size: 10px;
    letter-spacing: 1.5px;
    color: #8B8177;
    font-weight: 700;
}

.project-name {
    font-family: 'Playfair Display', serif;
    font-size: 43px;
    line-height: 1;
    margin-top: 8px;
    margin-bottom: 12px;
}

.project-type {
    display: inline-block;

    font-family: 'DM Sans', sans-serif;
    font-size: 9px;
    letter-spacing: 1.5px;
    font-weight: 700;

    padding: 6px 9px;

    border: 1px solid #BDB4A9;

    margin-bottom: 17px;
}

.project-description {
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    line-height: 1.7;
    color: #625B53;
    max-width: 520px;
}

.project-role {
    font-family: 'DM Sans', sans-serif;
    font-size: 12px;
    line-height: 1.7;
    color: #302D2A;
    margin-top: 20px;
}

.project-role-title {
    font-size: 9px;
    letter-spacing: 1.4px;
    font-weight: 700;
    color: #82786E;
}


/* -------------------------------------------------------
   PROJECT VISUALS
------------------------------------------------------- */

.project-visual {
    min-height: 310px;

    display: flex;
    align-items: center;
    justify-content: center;

    padding: 45px;

    margin-bottom: 5px;
}

.visual-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 9px;
    letter-spacing: 2px;
    font-weight: 700;
    text-transform: uppercase;

    margin-bottom: 15px;
}

.visual-title {
    font-family: 'Playfair Display', serif;
    font-size: 49px;
    line-height: 0.95;
}

.visual-title em {
    font-style: italic;
}


/* Individual visual worlds */

.agrami {
    background: #D8D0C1;
}

.nykaa {
    background: #E7D9D8;
}

.fae {
    background: #DCD7CF;
}

.coil {
    background: #D8DCE0;
}


/* -------------------------------------------------------
   ABOUT
------------------------------------------------------- */

.about-section {
    margin-top: 115px;
}

.about-big {
    font-family: 'Playfair Display', serif;
    font-size: 38px;
    line-height: 1.22;
}

.about-big em {
    font-style: italic;
}

.about-body {
    font-family: 'DM Sans', sans-serif;
    font-size: 16px;
    line-height: 1.85;
    color: #5D5750;
}

.about-body strong {
    color: #24211E;
    font-weight: 600;
}

.about-side {
    border-left: 1px solid #CFC6BA;
    padding-left: 35px;
}

.about-side-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 9px;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    font-weight: 700;
    color: #82786E;
}

.about-side-title {
    font-family: 'Playfair Display', serif;
    font-size: 30px;
    line-height: 1.2;
    margin-top: 13px;
}

.about-side-copy {
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    line-height: 1.7;
    color: #6F675F;
    margin-top: 18px;
}


/* -------------------------------------------------------
   THINKING
------------------------------------------------------- */

.thinking-section {
    margin-top: 115px;
    padding: 60px 0;

    border-top: 1px solid #CEC5B9;
    border-bottom: 1px solid #CEC5B9;
}

.thinking-intro {
    font-family: 'Playfair Display', serif;
    font-size: 39px;
    line-height: 1.2;
}

.thinking-intro em {
    font-style: italic;
}

.thinking-step {
    padding: 18px 0;
    border-bottom: 1px solid #D8D0C5;

    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    line-height: 1.6;
}

.thinking-step span {
    font-size: 10px;
    letter-spacing: 1px;
    color: #8A8177;
    margin-right: 10px;
}


/* -------------------------------------------------------
   TOOLKIT
------------------------------------------------------- */

.toolkit-section {
    margin-top: 110px;
}

.toolkit-box {
    border-top: 1px solid #CEC5B9;
    padding: 23px 0 28px 0;
}

.toolkit-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    color: #81776D;
}

.toolkit-content {
    font-family: 'DM Sans', sans-serif;
    font-size: 15px;
    line-height: 1.7;
    margin-top: 9px;
    color: #37332F;
}


/* -------------------------------------------------------
   CONTACT
------------------------------------------------------- */

.contact-section {
    background: #191817;
    color: #F5F1EB;

    margin-top: 110px;

    padding: 70px 65px;
}

.contact-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 9px;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 700;
    color: #AAA39A;
}

.contact-title {
    font-family: 'Playfair Display', serif;
    font-size: 57px;
    line-height: 1.02;
    margin-top: 15px;
}

.contact-title em {
    font-style: italic;
}

.contact-copy {
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    line-height: 1.7;
    color: #C7C0B8;
    max-width: 500px;
    margin-top: 25px;
}


/* -------------------------------------------------------
   FOOTER
------------------------------------------------------- */

.footer {
    border-top: 1px solid #CFC6BA;

    margin-top: 45px;
    padding-top: 20px;

    display: flex;
    justify-content: space-between;

    font-family: 'DM Sans', sans-serif;
    font-size: 10px;
    letter-spacing: 1px;
    color: #82786E;
}


/* -------------------------------------------------------
   MOBILE
------------------------------------------------------- */

@media (max-width: 768px) {

    .block-container {
        padding-left: 20px;
        padding-right: 20px;
    }

    .hero {
        padding: 60px 0;
    }

    .hero-title {
        font-size: 59px;
        letter-spacing: -2px;
    }

    .hero-intro {
        font-size: 18px;
    }

    .section-heading {
        font-size: 40px;
    }

    .project-name {
        font-size: 37px;
    }

    .visual-title {
        font-size: 40px;
    }

    .about-section {
        margin-top: 80px;
    }

    .about-side {
        margin-top: 35px;
    }

    .thinking-section {
        margin-top: 80px;
    }

    .contact-section {
        padding: 45px 28px;
    }

    .contact-title {
        font-size: 43px;
    }

    .footer {
        display: block;
        line-height: 2;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# NAVIGATION
# =========================================================

st.markdown("""
<div class="navbar">
    <div class="nav-logo">KT.</div>

    <div class="nav-text">
        MARKETING · BRAND · DIGITAL
    </div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================

col1, col2 = st.columns([1.7, 0.75], gap="large")

with col1:

    st.markdown("""
    <div class="hero">

        <div class="hero-kicker">
            PGDM Marketing · New Delhi · 2026
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

        <div class="hero-rule"></div>

    </div>
    """, unsafe_allow_html=True)

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


with col2:

    st.markdown(
        '<div class="profile-frame">',
        unsafe_allow_html=True
    )

    st.image(
        "profile.png",
        use_container_width=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div style="
        font-family:'DM Sans', sans-serif;
        font-size:10px;
        letter-spacing:1.5px;
        color:#81786E;
        text-transform:uppercase;
        margin-top:12px;
    ">
        Kanushi Taneja
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# PROOF STRIP
# =========================================================

st.markdown("""
<div class="proof-strip">
""", unsafe_allow_html=True)

p1, p2, p3, p4 = st.columns(4)

with p1:
    st.markdown("""
    <div class="proof-number">4</div>
    <div class="proof-label">Internship Experiences</div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown("""
    <div class="proof-number">30+</div>
    <div class="proof-label">Consumer Interviews</div>
    """, unsafe_allow_html=True)

with p3:
    st.markdown("""
    <div class="proof-number">6+</div>
    <div class="proof-label">Insurance Brands Analysed</div>
    """, unsafe_allow_html=True)

with p4:
    st.markdown("""
    <div class="proof-number">4</div>
    <div class="proof-label">Featured Projects</div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# SELECTED WORK
# =========================================================

st.markdown("""
<div>
    <div class="section-label">01 — Selected Work</div>

    <div class="section-heading">
        Ideas I've built.
    </div>
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# AGRAMI
# ---------------------------------------------------------

left, right = st.columns([1.05, 1], gap="large")

with left:
    st.markdown("""
    <div class="project-visual agrami">

        <div>

            <div class="visual-label">
                Live FMCG Project
            </div>

            <div class="visual-title">
                From farm<br>
                <em>to you.</em>
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)

with right:

    st.markdown("""
    <div class="project-card">

        <div class="project-number">
            01 / 04
        </div>

        <div class="project-name">
            AGRAMI
        </div>

        <div class="project-type">
            LIVE PROJECT
        </div>

        <div class="project-description">
            An integrated FMCG strategy focused on building
            consumer trust through content, transparency,
            education and community.
        </div>

        <div class="project-role">

            <div class="project-role-title">
                MY CONTRIBUTION
            </div>

            Content pillars · Sample creatives · Launch strategy ·
            Influencer strategy · PR & community planning

        </div>

    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "VIEW PROJECT →",
        AGRAMI
    )


# ---------------------------------------------------------
# NYKAA
# ---------------------------------------------------------

left, right = st.columns([1.05, 1], gap="large")

with left:
    st.markdown("""
    <div class="project-visual nykaa">

        <div>

            <div class="visual-label">
                Speculative Campaign
            </div>

            <div class="visual-title">
                Who<br>
                <em>taught you?</em>
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)

with right:

    st.markdown("""
    <div class="project-card">

        <div class="project-number">
            02 / 04
        </div>

        <div class="project-name">
            NYKAA
        </div>

        <div class="project-type">
            SPEC CAMPAIGN
        </div>

        <div class="project-description">
            A social campaign built around a simple insight:
            beauty knowledge is often passed from one person
            to another. The idea turns that behaviour into
            a community-led content platform.
        </div>

        <div class="project-role">

            <div class="project-role-title">
                MY CONTRIBUTION
            </div>

            Instagram audit · Consumer insight · Campaign platform ·
            Content formats · Rollout · KPI framework

        </div>

    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "VIEW PROJECT →",
        NYKAA
    )


# ---------------------------------------------------------
# FAE
# ---------------------------------------------------------

left, right = st.columns([1.05, 1], gap="large")

with left:
    st.markdown("""
    <div class="project-visual fae">

        <div>

            <div class="visual-label">
                Beauty Campaign Concept
            </div>

            <div class="visual-title">
                FAE<br>
                <em>Your Way.</em>
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)

with right:

    st.markdown("""
    <div class="project-card">

        <div class="project-number">
            03 / 04
        </div>

        <div class="project-name">
            FAE BEAUTY
        </div>

        <div class="project-type">
            CAMPAIGN CONCEPT
        </div>

        <div class="project-description">
            A beauty campaign based on the idea that people
            don't have one fixed aesthetic. Different moods
            can create different looks, expressions and
            product journeys.
        </div>

        <div class="project-role">

            <div class="project-role-title">
                PROJECT FOCUS
            </div>

            Consumer insight · Big idea · Social content ·
            Creator / UGC loop · Commerce journey

        </div>

    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "VIEW PROJECT →",
        FAE
    )


# ---------------------------------------------------------
# COIL
# ---------------------------------------------------------

left, right = st.columns([1.05, 1], gap="large")

with left:
    st.markdown("""
    <div class="project-visual coil">

        <div>

            <div class="visual-label">
                International Research
            </div>

            <div class="visual-title">
                What does<br>
                <em>career-ready</em><br>
                mean?
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)

with right:

    st.markdown("""
    <div class="project-card">

        <div class="project-number">
            04 / 04
        </div>

        <div class="project-name">
            COIL
        </div>

        <div class="project-type">
            RESEARCH PROJECT
        </div>

        <div class="project-description">
            A cross-cultural research project comparing student
            perspectives from India and the US on employability,
            technical skills, soft skills, AI literacy and
            career readiness.
        </div>

        <div class="project-role">

            <div class="project-role-title">
                MY ROLE
            </div>

            India-side Focus Group Discussion moderator —
            facilitating conversations, probing responses and
            capturing qualitative perspectives.

        </div>

    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "VIEW PROJECT →",
        COIL
    )


# =========================================================
# ABOUT
# =========================================================

st.markdown("""
<div class="about-section">

    <div class="section-label">
        02 — About Me
    </div>

</div>
""", unsafe_allow_html=True)

left, right = st.columns([1.1, 0.9], gap="large")

with left:

    st.markdown("""
    <div class="about-big">

        Curious about people.<br>
        Serious about <em>ideas.</em>

    </div>

    <div style="height:28px;"></div>

    <div class="about-body">

        I'm currently pursuing my <strong>PGDM in Marketing</strong>,
        building experience across marketing communications,
        campaign planning, market research, competitor analysis
        and client-facing work.

        <br><br>

        What interests me most is understanding the
        <strong>why behind consumer behaviour</strong> —
        the small observation, contradiction or unmet need
        that can become the starting point for a bigger idea.

        <br><br>

        Whether I'm analysing a category, developing a campaign
        platform or creating social content, I like connecting
        the strategic thinking with the actual execution.

    </div>
    """, unsafe_allow_html=True)


with right:

    st.markdown("""
    <div class="about-side">

        <div class="about-side-label">
            What I bring to a brief
        </div>

        <div class="about-side-title">
            A balance of<br>
            <em>thinking + doing.</em>
        </div>

        <div class="about-side-copy">
            Research enough to understand the problem.
            Think enough to find the opportunity.
            Create enough to make the idea tangible.
        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# HOW I THINK
# =========================================================

st.markdown("""
<div class="thinking-section">

    <div class="section-label">
        03 — How I Think
    </div>

    <div style="height:12px;"></div>

    <div class="thinking-intro">
        I don't start with the campaign.<br>
        I start with the <em>tension.</em>
    </div>

</div>
""", unsafe_allow_html=True)

steps = [
    (
        "01",
        "OBSERVE",
        "Understand the consumer, category and context."
    ),
    (
        "02",
        "FIND THE TENSION",
        "Look for the behaviour, contradiction or unmet need."
    ),
    (
        "03",
        "BUILD THE IDEA",
        "Turn the observation into a clear strategic platform."
    ),
    (
        "04",
        "MAKE IT SOCIAL",
        "Translate the idea into content people can understand and participate in."
    ),
    (
        "05",
        "MEASURE",
        "Define what success should look like before execution."
    )
]

for number, title, description in steps:

    st.markdown(f"""
    <div class="thinking-step">

        <span>{number}</span>

        <strong>{title}</strong>

        &nbsp; — &nbsp;

        {description}

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# TOOLKIT
# =========================================================

st.markdown("""
<div class="toolkit-section">

    <div class="section-label">
        04 — Marketing Toolkit
    </div>

    <div class="section-heading">
        What I work with.
    </div>

</div>
""", unsafe_allow_html=True)

left, right = st.columns(2, gap="large")

with left:

    st.markdown("""
    <div class="toolkit-box">

        <div class="toolkit-label">
            Strategy
        </div>

        <div class="toolkit-content">
            Brand Strategy · Campaign Planning ·
            Consumer Insights · Positioning ·
            Marketing Communications
        </div>

    </div>

    <div class="toolkit-box">

        <div class="toolkit-label">
            Content
        </div>

        <div class="toolkit-content">
            Content Strategy · Social Media Strategy ·
            Creative Strategy · Influencer Marketing ·
            PR & Community
        </div>

    </div>
    """, unsafe_allow_html=True)


with right:

    st.markdown("""
    <div class="toolkit-box">

        <div class="toolkit-label">
            Research
        </div>

        <div class="toolkit-content">
            Market Research · Competitor Analysis ·
            Qualitative Research · Focus Group Discussions
        </div>

    </div>

    <div class="toolkit-box">

        <div class="toolkit-label">
            Tools
        </div>

        <div class="toolkit-content">
            Canva · MS PowerPoint · MS Excel ·
            Google Workspace · GitHub
        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# CONTACT
# =========================================================

st.markdown("""
<div class="contact-section">

    <div class="contact-label">
        05 — Let's Connect
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
""", unsafe_allow_html=True)

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

st.markdown("""
<div class="footer">

    <div>
        © 2026 KANUSHI TANEJA
    </div>

    <div>
        MARKETING · BRAND · DIGITAL
    </div>

</div>
""", unsafe_allow_html=True)
