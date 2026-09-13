import streamlit as st

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Kanushi Taneja | E-Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# LINKS
# ---------------------------------------------------------
LINKEDIN = "https://www.linkedin.com/in/kanushi-taneja/"
GITHUB = "https://github.com/27-kanushitaneja-ctrl"
EMAIL = "mailto:kanushitaneja.work@gmail.com"

AGRAMI_REPO = "https://github.com/27-kanushitaneja-ctrl/FMCG-Live-Project"
NYKAA_REPO = "https://github.com/27-kanushitaneja-ctrl/Nykaa-Spec-Campaign-WhoTaughtYou"
FAE_REPO = "https://github.com/27-kanushitaneja-ctrl/FAE-YOUR-WAY"
COIL_REPO = "https://github.com/27-kanushitaneja-ctrl/COIL-International-Insights"

NYKAA_CANVA = "https://www.canva.com/design/DAHQfzF2gDQ/AtFCNZ3-0Mh1-qb2Iew47A/view"

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

html {
    scroll-behavior: smooth;
}

.stApp {
    background: #F7F4EF;
    color: #29241F;
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Hide Streamlit chrome */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* Typography */
h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: #29241F !important;
}

h1 {
    font-size: 4rem !important;
    line-height: 1.05 !important;
}

h2 {
    font-size: 2.4rem !important;
}

h3 {
    font-size: 1.35rem !important;
}

/* Navigation */
.nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem 0 2rem 0;
    border-bottom: 1px solid #DDD5CC;
    margin-bottom: 4rem;
}

.nav-name {
    font-family: 'Playfair Display', serif;
    font-size: 1.25rem;
    font-weight: 600;
}

.nav-right {
    font-size: 0.9rem;
    color: #6F655D;
}

/* Hero */
.hero {
    padding: 2rem 0 5rem 0;
}

.eyebrow {
    text-transform: uppercase;
    letter-spacing: 3px;
    font-size: 0.72rem;
    font-weight: 700;
    color: #8A6D55;
    margin-bottom: 1rem;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 4.3rem;
    line-height: 1.03;
    margin: 0;
    color: #29241F;
}

.hero-subtitle {
    font-size: 1.2rem;
    color: #716860;
    margin-top: 1.2rem;
    line-height: 1.7;
}

.hero-description {
    font-size: 1rem;
    color: #625A54;
    line-height: 1.8;
    max-width: 650px;
    margin-top: 1.5rem;
}

.photo {
    border-radius: 50%;
    border: 8px solid #E7E0D8;
}

/* Buttons */
.btn {
    display: inline-block;
    padding: 0.75rem 1.25rem;
    border-radius: 5px;
    text-decoration: none !important;
    font-weight: 600;
    font-size: 0.88rem;
    margin-right: 0.5rem;
    margin-top: 1.3rem;
}

.btn-primary {
    background: #29241F;
    color: white !important;
}

.btn-secondary {
    background: transparent;
    color: #29241F !important;
    border: 1px solid #B9AEA4;
}

/* Sections */
.section {
    padding: 4.5rem 0;
    border-top: 1px solid #DDD5CC;
}

.section-label {
    text-transform: uppercase;
    letter-spacing: 2.5px;
    font-size: 0.7rem;
    font-weight: 700;
    color: #8A6D55;
    margin-bottom: 0.7rem;
}

/* Cards */
.card {
    background: #FCFAF7;
    border: 1px solid #E3DBD2;
    border-radius: 8px;
    padding: 1.8rem;
    height: 100%;
    box-sizing: border-box;
}

.project-number {
    font-size: 0.72rem;
    letter-spacing: 2px;
    color: #9A8A7B;
    font-weight: 700;
}

.project-type {
    text-transform: uppercase;
    font-size: 0.68rem;
    letter-spacing: 1.5px;
    color: #8A6D55;
    font-weight: 700;
    margin-top: 0.8rem;
}

.project-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.7rem;
    margin: 0.5rem 0;
}

.project-role {
    font-size: 0.88rem;
    font-weight: 600;
    color: #514840;
    margin-bottom: 1rem;
}

.project-text {
    color: #6B625B;
    font-size: 0.9rem;
    line-height: 1.65;
}

.tag {
    display: inline-block;
    background: #EEE7DF;
    color: #66594F;
    border-radius: 20px;
    padding: 0.35rem 0.65rem;
    margin: 0.25rem 0.2rem 0.25rem 0;
    font-size: 0.7rem;
}

/* Evidence */
.evidence {
    background: #EEE7DF;
    border-radius: 8px;
    padding: 1.3rem;
    margin-top: 1.3rem;
}

.evidence-title {
    font-weight: 700;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Skills */
.skill-box {
    background: #FCFAF7;
    border: 1px solid #E3DBD2;
    padding: 1.3rem;
    border-radius: 7px;
    margin-bottom: 1rem;
}

.skill-title {
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.skill-text {
    color: #6B625B;
    font-size: 0.88rem;
    line-height: 1.6;
}

/* Contact */
.contact-box {
    background: #29241F;
    color: white;
    border-radius: 10px;
    padding: 3rem;
}

.contact-box h2 {
    color: white !important;
}

.contact-box p {
    color: #DDD4CC;
    line-height: 1.7;
}

/* Footer */
.footer {
    text-align: center;
    color: #81766D;
    font-size: 0.75rem;
    padding-top: 3rem;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# NAVIGATION
# ---------------------------------------------------------
st.markdown("""
<div class="nav">
    <div class="nav-name">Kanushi Taneja</div>
    <div class="nav-right">Marketing · Strategy · Content</div>
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# HERO
# ---------------------------------------------------------
hero_left, hero_right = st.columns([2.3, 1], gap="large")

with hero_left:

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">E-Portfolio</div>

        <div class="hero-title">
            Building brands<br>
            people remember.
        </div>

        <div class="hero-subtitle">
            Marketing · Brand Strategy · Digital & Content
        </div>

        <div class="hero-description">
            I am a marketing student interested in understanding people,
            translating insights into ideas, and building strategic brand
            communication across digital and social platforms.
        </div>

        <a class="btn btn-primary"
           href="#projects">
           Explore My Work
        </a>

        <a class="btn btn-secondary"
           href="https://www.linkedin.com/in/kanushi-taneja/"
           target="_blank">
           LinkedIn
        </a>

        <a class="btn btn-secondary"
           href="https://github.com/27-kanushitaneja-ctrl"
           target="_blank">
           GitHub
        </a>
    </div>
    """, unsafe_allow_html=True)

with hero_right:
    st.image("profile.png", use_container_width=True)


# ---------------------------------------------------------
# ABOUT
# ---------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown("""
<div class="section-label">01 — About</div>
<h2>About Me</h2>
""", unsafe_allow_html=True)

about_left, about_right = st.columns([1.5, 1], gap="large")

with about_left:
    st.markdown("""
    <p style="line-height:1.9; color:#625A54;">
    I approach marketing at the intersection of <b>strategy, consumer
    understanding and creative communication</b>.
    </p>

    <p style="line-height:1.9; color:#625A54;">
    My project experience spans live brand work, speculative campaigns,
    social media strategy and cross-cultural qualitative research.
    </p>

    <p style="line-height:1.9; color:#625A54;">
    I enjoy moving from a business or consumer problem to a clear insight,
    a strong idea and an executable communication plan.
    </p>
    """, unsafe_allow_html=True)

with about_right:
    st.markdown("""
    <div class="card">
        <div class="project-type">What I bring</div>
        <h3>Strategy with a creative lens</h3>
        <p class="project-text">
        Consumer-first thinking, campaign conceptualisation, social
        strategy, research and structured problem solving.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ---------------------------------------------------------
# PROJECTS
# ---------------------------------------------------------
st.markdown('<div class="section" id="projects">', unsafe_allow_html=True)

st.markdown("""
<div class="section-label">02 — Selected Work</div>
<h2>Projects</h2>
<p style="color:#6B625B; max-width:700px; line-height:1.7;">
A selection of live, academic and speculative projects demonstrating
strategy, research, campaign thinking and digital execution.
</p>
""", unsafe_allow_html=True)


# ---------------- AGRAMI ----------------
st.markdown("### 01", unsafe_allow_html=True)

agr_left, agr_right = st.columns([1.5, 1], gap="large")

with agr_left:
    st.markdown("""
    <div class="card">
        <div class="project-type">Live FMCG Project</div>
        <div class="project-title">AGRAMI — Integrated Brand & Social Strategy</div>
        <div class="project-role">My Role: Content & Social Strategy</div>

        <p class="project-text">
        Developed content and social components for AGRAMI, including
        content pillars, sample creative concepts, launch planning and
        influencer, PR and community strategy.
        </p>

        <div>
            <span class="tag">Content Strategy</span>
            <span class="tag">Social Media</span>
            <span class="tag">Campaign Planning</span>
            <span class="tag">Influencer Marketing</span>
            <span class="tag">PR & Community</span>
        </div>

        <div class="evidence">
            <div class="evidence-title">My Contribution</div>
            <p class="project-text">
            Created the content pillars and sample creative mapping,
            contributed to launch strategy, and developed influencer,
            PR and community activation ideas.
            </p>
        </div>

        <a class="btn btn-primary"
           href="https://github.com/27-kanushitaneja-ctrl/FMCG-Live-Project"
           target="_blank">
           View Evidence
        </a>
    </div>
    """, unsafe_allow_html=True)

with agr_right:
    st.markdown("""
    <div class="card">
        <div class="project-type">Purpose</div>
        <h3>Build trust through content</h3>
        <p class="project-text">
        The strategy focused on helping consumers understand AGRAMI's
        sourcing, ingredients, purity and food usage.
        </p>

        <div class="project-type">Process</div>
        <p class="project-text">
        Content pillars → creative concepts → launch sequence →
        creator/PR/community strategy.
        </p>

        <div class="project-type">Outcome</div>
        <p class="project-text">
        A structured social content and activation framework covering
        education, transparency, recipes and community participation.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ---------------- NYKAA ----------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 02", unsafe_allow_html=True)

ny_left, ny_right = st.columns([1.5, 1], gap="large")

with ny_left:
    st.markdown("""
    <div class="card">
        <div class="project-type">Speculative Brand Campaign</div>
        <div class="project-title">Nykaa — “Who Taught You?”</div>
        <div class="project-role">My Role: Campaign Strategy & Concept Development</div>

        <p class="project-text">
        Developed a social campaign built around the idea that beauty
        knowledge is passed from one person to another.
        </p>

        <div>
            <span class="tag">Consumer Insight</span>
            <span class="tag">Brand Strategy</span>
            <span class="tag">Campaign Concept</span>
            <span class="tag">UGC</span>
            <span class="tag">Social Strategy</span>
        </div>

        <div class="evidence">
            <div class="evidence-title">My Contribution</div>
            <p class="project-text">
            Audited Nykaa's Instagram presence, identified the opportunity
            to shift from “brand teaches” to “community teaches community,”
            and developed the campaign insight, platform, content mechanics,
            rollout and KPIs.
            </p>
        </div>

        <a class="btn btn-primary"
           href="https://github.com/27-kanushitaneja-ctrl/Nykaa-Spec-Campaign-WhoTaughtYou"
           target="_blank">
           GitHub
        </a>

        <a class="btn btn-secondary"
           href="https://www.canva.com/design/DAHQfzF2gDQ/AtFCNZ3-0Mh1-qb2Iew47A/view"
           target="_blank">
           View Presentation
        </a>
    </div>
    """, unsafe_allow_html=True)

with ny_right:
    st.markdown("""
    <div class="card">
        <div class="project-type">Purpose</div>
        <h3>Turn beauty knowledge into community</h3>
        <p class="project-text">
        Explore how Nykaa could move beyond teaching consumers to
        enabling consumers to teach and credit one another.
        </p>

        <div class="project-type">Process</div>
        <p class="project-text">
        Instagram audit → consumer insight → campaign platform →
        content formats → four-week rollout → KPIs.
        </p>

        <div class="project-type">Outcome</div>
        <p class="project-text">
        A social-first campaign framework designed to create
        participation, UGC and “handoff chains” between consumers.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ---------------- FAE ----------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 03", unsafe_allow_html=True)

fae_left, fae_right = st.columns([1.5, 1], gap="large")

with fae_left:
    st.markdown("""
    <div class="card">
        <div class="project-type">Speculative Beauty Campaign</div>
        <div class="project-title">FAE Beauty — FAE YOUR WAY</div>
        <div class="project-role">My Role: Campaign Concept & Social Strategy</div>

        <p class="project-text">
        Developed a mood-led campaign platform based on the insight
        that consumers do not have one fixed beauty aesthetic.
        </p>

        <div>
            <span class="tag">Consumer Insight</span>
            <span class="tag">Campaign Strategy</span>
            <span class="tag">Creative Strategy</span>
            <span class="tag">Social Media</span>
            <span class="tag">UGC Strategy</span>
        </div>

        <div class="evidence">
            <div class="evidence-title">Campaign Idea</div>
            <p class="project-text">
            “Your face. Your mood. Your rules.” The campaign connects
            Mood → Look → Product → FAE and uses creator and UGC
            participation to make the platform social.
            </p>
        </div>

        <a class="btn btn-primary"
           href="https://github.com/27-kanushitaneja-ctrl/FAE-YOUR-WAY"
           target="_blank">
           View Evidence
        </a>
    </div>
    """, unsafe_allow_html=True)

with fae_right:
    st.markdown("""
    <div class="card">
        <div class="project-type">Purpose</div>
        <h3>Move from one aesthetic to self-expression</h3>
        <p class="project-text">
        The concept explores how FAE can position beauty around
        individual moods rather than one predefined aesthetic.
        </p>

        <div class="project-type">Process</div>
        <p class="project-text">
        Human insight → four mood territories → campaign platform →
        social content loop → creator & UGC strategy.
        </p>

        <div class="project-type">Outcome</div>
        <p class="project-text">
        A complete social campaign concept spanning Hero Reel,
        Stories, Carousel, Creator Content and UGC.
        </p>

        <p style="font-size:0.72rem; color:#8A8179; margin-top:1.2rem;">
        Speculative / student concept. Mockup engagement figures
        are illustrative and not actual campaign results.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ---------------- COIL ----------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 04", unsafe_allow_html=True)

coil_left, coil_right = st.columns([1.5, 1], gap="large")

with coil_left:
    st.markdown("""
    <div class="card">
        <div class="project-type">International Collaborative Research</div>
        <div class="project-title">COIL — Globalization in Action</div>
        <div class="project-role">My Role: India FGD Moderator</div>

        <p class="project-text">
        A cross-cultural qualitative research project comparing US and
        Indian student perspectives on the skills required for future careers.
        </p>

        <div>
            <span class="tag">Qualitative Research</span>
            <span class="tag">FGD Moderation</span>
            <span class="tag">Cross-Cultural Research</span>
            <span class="tag">Interviewing</span>
            <span class="tag">Insight Generation</span>
        </div>

        <div class="evidence">
            <div class="evidence-title">My Contribution</div>
            <p class="project-text">
            Moderated the India-side Focus Group Discussion, facilitated
            participant conversations, probed responses and contributed
            qualitative perspectives to the US–India comparison.
            </p>
        </div>

        <a class="btn btn-primary"
           href="https://github.com/27-kanushitaneja-ctrl/COIL-International-Insights"
           target="_blank">
           View Evidence
        </a>
    </div>
    """, unsafe_allow_html=True)

with coil_right:
    st.markdown("""
    <div class="card">
        <div class="project-type">Purpose</div>
        <h3>Understand future-career skills</h3>
        <p class="project-text">
        The research explored perceptions of technical and soft skills,
        AI literacy, adaptability and employability across the US and India.
        </p>

        <div class="project-type">Process</div>
        <p class="project-text">
        Focus groups → in-depth interviews → secondary research →
        US–India comparison → findings.
        </p>

        <div class="project-type">Outcome</div>
        <p class="project-text">
        The research identified broad agreement on the importance of
        technical and soft skills, with differences in emphasis across contexts.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ---------------------------------------------------------
# SKILLS
# ---------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown("""
<div class="section-label">03 — Capabilities</div>
<h2>Skills & Tools</h2>
""", unsafe_allow_html=True)

skill1, skill2, skill3 = st.columns(3)

with skill1:
    st.markdown("""
    <div class="skill-box">
        <div class="skill-title">Strategy</div>
        <div class="skill-text">
        Brand Strategy<br>
        Consumer Insight<br>
        Campaign Planning<br>
        Positioning<br>
        Creative Strategy
        </div>
    </div>
    """, unsafe_allow_html=True)

with skill2:
    st.markdown("""
    <div class="skill-box">
        <div class="skill-title">Digital & Content</div>
        <div class="skill-text">
        Social Media Strategy<br>
        Content Strategy<br>
        UGC Strategy<br>
        Influencer Marketing<br>
        PR & Community
        </div>
    </div>
    """, unsafe_allow_html=True)

with skill3:
    st.markdown("""
    <div class="skill-box">
        <div class="skill-title">Research</div>
        <div class="skill-text">
        Qualitative Research<br>
        Focus Group Moderation<br>
        Interviewing<br>
        Cross-Cultural Research<br>
        Insight Generation
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

tools1, tools2 = st.columns(2)

with tools1:
    st.markdown("""
    <div class="skill-box">
        <div class="skill-title">Tools</div>
        <div class="skill-text">
        Canva · GitHub · Streamlit · Microsoft Office
        </div>
    </div>
    """, unsafe_allow_html=True)

with tools2:
    st.markdown("""
    <div class="skill-box">
        <div class="skill-title">Working Style</div>
        <div class="skill-text">
        Consumer-first · Structured · Collaborative ·
        Research-led · Creative
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ---------------------------------------------------------
# CONTACT
# ---------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown("""
<div class="contact-box">
    <div class="section-label">04 — Contact</div>
    <h2>Let's connect.</h2>
    <p>
    I am open to conversations around marketing, brand strategy,
    digital content and opportunities where consumer insight can
    translate into meaningful brand work.
    </p>

    <a class="btn btn-secondary"
       style="background:white;"
       href="mailto:kanushitaneja.work@gmail.com">
       Email Me
    </a>

    <a class="btn btn-secondary"
       style="background:white;"
       href="https://www.linkedin.com/in/kanushi-taneja/"
       target="_blank">
       LinkedIn
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown("""
<div class="footer">
    © 2026 Kanushi Taneja · Marketing · Brand Strategy · Digital & Content
</div>
""", unsafe_allow_html=True)
