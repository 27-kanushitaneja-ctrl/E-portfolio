import streamlit as st
import textwrap

# =========================================================
# PAGE SETUP
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
# HTML HELPER
# =========================================================

def render_html(html):
    st.markdown(
        textwrap.dedent(html).strip(),
        unsafe_allow_html=True
    )


# =========================================================
# DESIGN / CSS
# =========================================================

render_html("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@400;500;600&display=swap');

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


/* =====================================================
   NAV
===================================================== */

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0 22px 0;
    border-bottom: 1px solid #D6CEC3;
}

.nav-logo {
    font-family: 'DM Sans', sans-serif;
    font-size: 18px;
    font-weight: 700;
    letter-spacing: -0.5px;
}

.nav-text {
    font-family: 'DM Sans', sans-serif;
    font-size: 10px;
    letter-spacing: 2px;
    color: #746D65;
    font-weight: 600;
}


/* =====================================================
   HERO
===================================================== */

.hero {
    padding: 75px 0 55px 0;
}

.hero-kicker {
    font-family: 'DM Sans', sans-serif;
    font-size: 10px;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #7A7167;
    font-weight: 700;
    margin-bottom: 24px;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(55px, 7.5vw, 98px);
    line-height: 0.94;
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
    margin-top: 32px;
}

.hero-intro strong {
    color: #171615;
}

.hero-detail {
    font-family: 'DM Sans', sans-serif;
    font-size: 15px;
    line-height: 1.75;
    color: #746D65;
    max-width: 650px;
    margin-top: 17px;
}

.hero-rule {
    width: 70px;
    height: 2px;
    background: #191817;
    margin-top: 35px;
}


/* =====================================================
   PROFILE
===================================================== */

.profile-card {
    background: #DED7CD;
    padding: 12px;
    margin-top: 55px;
}

.profile-caption {
    font-family: 'DM Sans', sans-serif;
    font-size: 9px;
    letter-spacing: 1.5px;
    color: #81786E;
    text-transform: uppercase;
    margin-top: 12px;
}


/* =====================================================
   BUTTONS
===================================================== */

.stLinkButton > a {
    border-radius: 0px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 10px !important;
    font-weight: 700 !important;
    letter-spacing: 1.2px !important;
}


/* =====================================================
   PROOF STRIP
===================================================== */

.proof-strip {
    border-top: 1px solid #D1C8BC;
    border-bottom: 1px solid #D1C8BC;
    padding: 28px 0;
    margin: 15px 0 95px 0;
}

.proof-number {
    font-family: 'Playfair Display', serif;
    font-size: 34px;
    line-height: 1;
}

.proof-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 9px;
    letter-spacing: 1.4px;
    text-transform: uppercase;
    color: #81786E;
    margin-top: 8px;
}


/* =====================================================
   SECTIONS
===================================================== */

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
    margin-bottom: 48px;
}


/* =====================================================
   PROJECTS
===================================================== */

.project-visual {
    min-height: 310px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 45px;
}

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
    font-size: 48px;
    line-height: 0.95;
}

.visual-title em {
    font-style: italic;
}

.project-card {
    border-top: 1px solid #CFC6BA;
    padding: 30px 0 38px 0;
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
    font-family: 'DM Sans', sans-serif;
    font-size: 9px;
    letter-spacing: 1.4px;
    font-weight: 700;
    color: #82786E;
    margin-bottom: 4px;
}


/* =====================================================
   ABOUT
===================================================== */

.about-section {
    margin-top: 115px;
}

.about-big {
    font-family: 'Playfair Display', serif;
    font-size: 40px;
    line-height: 1.2;
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
    font-size: 31px;
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


/* =====================================================
   THINKING
===================================================== */

.thinking-section {
    margin-top: 115px;
    padding: 60px 0;
    border-top: 1px solid #CEC5B9;
    border-bottom: 1px solid #CEC5B9;
}

.thinking-intro {
    font-family: 'Playfair Display', serif;
    font-size: 40px;
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


/* =====================================================
   TOOLKIT
===================================================== */

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


/* =====================================================
   CONTACT
===================================================== */

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


/* =====================================================
   FOOTER
===================================================== */

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


/* =====================================================
   MOBILE
===================================================== */

@media (max-width: 768px) {

    .block-container {
        padding-left: 20px;
        padding-right: 20px;
    }

    .hero {
        padding: 55px 0;
    }

    .hero-title {
        font-size: 58px;
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
        margin-top: 40px;
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
""")


# =========================================================
# NAVIGATION
# =========================================================

render_html("""
<div class="navbar">

    <div class="nav-logo">
        KT.
    </div>

    <div class="nav-text">
        MARKETING · BRAND · DIGITAL
    </div>

</div>
""")


# =========================================================
# HERO
# =========================================================

left, right = st.columns([1.65, 0.75], gap="large")

with left:

    render_html("""
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

    render_html("""
    <div class="profile-card">
    """)

    st.image(
        "profile.png",
        use_container_width=True
    )

    render_html("""
    </div>

    <div class="profile-caption">
        Kanushi Taneja · Marketing
    </div>
    """)


# =========================================================
# PROOF
# =========================================================

render_html("""
<div class="proof-strip">
""")

p1, p2, p3, p4 = st.columns(4)

with p1:
    render_html("""
    <div class="proof-number">4</div>
    <div class="proof-label">Internship Experiences</div>
    """)

with p2:
    render_html("""
    <div class="proof-number">30+</div>
    <div class="proof-label">Consumer Interviews</div>
    """)

with p3:
    render_html("""
    <div class="proof-number">6+</div>
    <div class="proof-label">Insurance Brands Analysed</div>
    """)

with p4:
    render_html("""
    <div class="proof-number">4</div>
    <div class="proof-label">Featured Projects</div>
    """)

render_html("""
</div>
""")


# =========================================================
# SELECTED WORK
# =========================================================

render_html("""
<div>

    <div class="section-label">
        01 — Selected Work
    </div>

    <div class="section-heading">
        Ideas I've built.
    </div>

</div>
""")


# =========================================================
# PROJECT 01 — AGRAMI
# =========================================================

left, right = st.columns([1.05, 1], gap="large")

with left:

    render_html("""
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
    """)

with right:

    render_html("""
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
    """)

    st.link_button("VIEW PROJECT →", AGRAMI)


# =========================================================
# PROJECT 02 — NYKAA
# =========================================================

left, right = st.columns([1.05, 1], gap="large")

with left:

    render_html("""
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
    """)

with right:

    render_html("""
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
            A social campaign built around the idea that beauty
            knowledge is passed from one person to another —
            turning that behaviour into a community-led
            content platform.
        </div>

        <div class="project-role">

            <div class="project-role-title">
                MY CONTRIBUTION
            </div>

            Instagram audit · Consumer insight · Campaign platform ·
            Content formats · Rollout · KPI framework

        </div>

    </div>
    """)

    st.link_button("VIEW PROJECT →", NYKAA)


# =========================================================
# PROJECT 03 — FAE
# =========================================================

left, right = st.columns([1.05, 1], gap="large")

with left:

    render_html("""
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
    """)

with right:

    render_html("""
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
    """)

    st.link_button("VIEW PROJECT →", FAE)


# =========================================================
# PROJECT 04 — COIL
# =========================================================

left, right = st.columns([1.05, 1], gap="large")

with left:

    render_html("""
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
    """)

with right:

    render_html("""
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
    """)

    st.link_button("VIEW PROJECT →", COIL)


# =========================================================
# ABOUT ME
# =========================================================

render_html("""
<div class="about-section">

    <div class="section-label">
        02 — About Me
    </div>

</div>
""")

left, right = st.columns([1.1, 0.9], gap="large")

with left:

    render_html("""
    <div class="about-big">

        Curious about people.<br>
        Serious about <em>ideas.</em>

    </div>

    <div style="height:28px;"></div>

    <div class="about-body">

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

    render_html("""
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
    """)


# =========================================================
# HOW I THINK
# =========================================================

render_html("""
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
""")

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
        "Define what success should look like."
    )
]

for number, title, description in steps:

    render_html(f"""
    <div class="thinking-step">

        <span>{number}</span>

        <strong>{title}</strong>

        &nbsp; — &nbsp;

        {description}

    </div>
    """)


# =========================================================
# TOOLKIT
# =========================================================

render_html("""
<div class="toolkit-section">

    <div class="section-label">
        04 — Marketing Toolkit
    </div>

    <div class="section-heading">
        What I work with.
    </div>

</div>
""")

left, right = st.columns(2, gap="large")

with left:

    render_html("""
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
    """)

with right:

    render_html("""
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
    """)


# =========================================================
# CONTACT
# =========================================================

render_html("""
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

render_html("""
<div class="footer">

    <div>
        © 2026 KANUSHI TANEJA
    </div>

    <div>
        MARKETING · BRAND · DIGITAL
    </div>

</div>
""")
