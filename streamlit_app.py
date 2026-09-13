import streamlit as st

# =========================================================
# PAGE SETUP
# =========================================================

st.set_page_config(
    page_title="Kanushi Taneja | E-Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# LINKS
# =========================================================

LINKEDIN = "https://www.linkedin.com/in/kanushi-taneja/"
GITHUB = "https://github.com/27-kanushitaneja-ctrl"
EMAIL = "mailto:kanushitaneja.work@gmail.com"

AGRAMI = "https://github.com/27-kanushitaneja-ctrl/FMCG-Live-Project"
NYKAA = "https://github.com/27-kanushitaneja-ctrl/Nykaa-Spec-Campaign-WhoTaughtYou"
FAE = "https://github.com/27-kanushitaneja-ctrl/FAE-YOUR-WAY"
COIL = "https://github.com/27-kanushitaneja-ctrl/COIL-International-Insights"

NYKAA_PRESENTATION = (
    "https://www.canva.com/design/DAHQfzF2gDQ/"
    "AtFCNZ3-0Mh1-qb2Iew47A/view"
)

# =========================================================
# CUSTOM CSS
# =========================================================

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
    padding-top: 1.5rem;
    padding-bottom: 4rem;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: #29241F !important;
}

h1 {
    font-size: 4rem !important;
    line-height: 1.05 !important;
}

h2 {
    font-size: 2.5rem !important;
}

h3 {
    font-size: 1.4rem !important;
}

.top-line {
    border-bottom: 1px solid #DDD5CC;
    padding-bottom: 1.2rem;
    margin-bottom: 4rem;
}

.name {
    font-family: 'Playfair Display', serif;
    font-size: 1.3rem;
    font-weight: 600;
}

.top-role {
    color: #776D65;
    font-size: 0.85rem;
    text-align: right;
    padding-top: 0.3rem;
}

.eyebrow {
    text-transform: uppercase;
    letter-spacing: 3px;
    font-size: 0.7rem;
    font-weight: 700;
    color: #8A6D55;
    margin-bottom: 1rem;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 4.2rem;
    line-height: 1.05;
    color: #29241F;
    margin-bottom: 1rem;
}

.hero-role {
    font-size: 1.2rem;
    color: #756B63;
    line-height: 1.6;
}

.hero-text {
    color: #625A54;
    font-size: 1rem;
    line-height: 1.85;
    max-width: 680px;
    margin-top: 1.2rem;
}

.profile-image {
    border-radius: 50%;
}

.section {
    padding-top: 4rem;
    margin-top: 4rem;
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

.section-description {
    color: #6B625B;
    line-height: 1.8;
    max-width: 760px;
}

.project-card {
    background: #FCFAF7;
    border: 1px solid #E3DBD2;
    border-radius: 9px;
    padding: 1.7rem;
    margin-bottom: 1.5rem;
}

.project-number {
    color: #9A8A7B;
    font-size: 0.7rem;
    letter-spacing: 2px;
    font-weight: 700;
}

.project-type {
    color: #8A6D55;
    font-size: 0.68rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    font-weight: 700;
    margin-top: 0.7rem;
}

.project-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.75rem;
    margin: 0.4rem 0;
    color: #29241F;
}

.project-role {
    font-weight: 600;
    font-size: 0.85rem;
    color: #514840;
    margin-bottom: 1rem;
}

.project-text {
    color: #6B625B;
    font-size: 0.88rem;
    line-height: 1.7;
}

.small-heading {
    color: #8A6D55;
    font-size: 0.68rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    font-weight: 700;
    margin-top: 0.9rem;
}

.tag {
    display: inline-block;
    background: #EEE7DF;
    color: #66594F;
    border-radius: 20px;
    padding: 0.3rem 0.65rem;
    margin: 0.2rem 0.15rem 0.2rem 0;
    font-size: 0.68rem;
}

.evidence-box {
    background: #EEE7DF;
    border-radius: 7px;
    padding: 1rem;
    margin-top: 1rem;
}

.evidence-title {
    font-size: 0.68rem;
    text-transform: uppercase;
    letter-spacing: 1.3px;
    font-weight: 700;
    color: #66594F;
}

.skill-card {
    background: #FCFAF7;
    border: 1px solid #E3DBD2;
    border-radius: 8px;
    padding: 1.4rem;
    min-height: 170px;
}

.skill-title {
    font-weight: 700;
    margin-bottom: 0.7rem;
}

.skill-text {
    color: #6B625B;
    font-size: 0.86rem;
    line-height: 1.8;
}

.contact-card {
    background: #29241F;
    border-radius: 10px;
    padding: 2.8rem;
}

.contact-card h2 {
    color: white !important;
}

.contact-text {
    color: #DCD3CA;
    line-height: 1.8;
}

.disclaimer {
    color: #8A8179;
    font-size: 0.7rem;
    line-height: 1.6;
    margin-top: 1rem;
}

.footer {
    text-align: center;
    color: #81766D;
    font-size: 0.72rem;
    padding-top: 3rem;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TOP BAR
# =========================================================

top1, top2 = st.columns([2, 1])

with top1:
    st.markdown(
        '<div class="name">Kanushi Taneja</div>',
        unsafe_allow_html=True
    )

with top2:
    st.markdown(
        '<div class="top-role">Marketing · Strategy · Content</div>',
        unsafe_allow_html=True
    )

st.markdown(
    '<div class="top-line"></div>',
    unsafe_allow_html=True
)

# =========================================================
# HERO
# =========================================================

hero1, hero2 = st.columns([1.8, 1], gap="large")

with hero1:

    st.markdown(
        '<div class="eyebrow">E-Portfolio</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-title">'
        'Building brands<br>people remember.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-role">'
        'Marketing · Brand Strategy · Digital & Content'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-text">'
        'I am a marketing student interested in understanding people, '
        'translating insights into ideas, and building strategic brand '
        'communication across digital and social platforms.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'''
        <a href="{LINKEDIN}" target="_blank"
        style="display:inline-block;
        margin-top:1.3rem;
        margin-right:0.6rem;
        padding:0.7rem 1.1rem;
        background:#29241F;
        color:white;
        text-decoration:none;
        border-radius:5px;
        font-weight:600;
        font-size:0.85rem;">
        LinkedIn
        </a>

        <a href="{GITHUB}" target="_blank"
        style="display:inline-block;
        margin-top:1.3rem;
        padding:0.7rem 1.1rem;
        border:1px solid #B9AEA4;
        color:#29241F;
        text-decoration:none;
        border-radius:5px;
        font-weight:600;
        font-size:0.85rem;">
        GitHub
        </a>
        ''',
        unsafe_allow_html=True
    )

with hero2:

    try:
        st.image("profile.png", use_container_width=True)
    except:
        st.info("Profile photo")

# =========================================================
# ABOUT
# =========================================================

st.markdown(
    '<div class="section"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-label">01 — About</div>',
    unsafe_allow_html=True
)

st.markdown("## About Me")

about1, about2 = st.columns([1.5, 1], gap="large")

with about1:

    st.markdown(
        """
        <p class="hero-text">
        I approach marketing at the intersection of
        <b>strategy, consumer understanding and creative communication.</b>
        </p>

        <p class="hero-text">
        My project experience spans live brand work, speculative campaigns,
        social media strategy and cross-cultural qualitative research.
        </p>

        <p class="hero-text">
        I enjoy moving from a business or consumer problem to a clear insight,
        a strong idea and an executable communication plan.
        </p>
        """,
        unsafe_allow_html=True
    )

with about2:

    st.markdown(
        """
        <div class="project-card">
        <div class="project-type">What I bring</div>

        <h3>Strategy with a creative lens</h3>

        <p class="project-text">
        Consumer-first thinking, campaign conceptualisation,
        social strategy, research and structured problem solving.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# PROJECTS
# =========================================================

st.markdown(
    '<div class="section"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-label">02 — Selected Work</div>',
    unsafe_allow_html=True
)

st.markdown("## Projects")

st.markdown(
    '<p class="section-description">'
    'A selection of live, academic and speculative projects demonstrating '
    'strategy, research, campaign thinking and digital execution.'
    '</p>',
    unsafe_allow_html=True
)

# =========================================================
# AGRAMI
# =========================================================

st.markdown(
    """
    <div class="project-card">

    <div class="project-number">01</div>

    <div class="project-type">Live FMCG Project</div>

    <div class="project-title">
    AGRAMI — Integrated Brand & Social Strategy
    </div>

    <div class="project-role">
    My Role: Content & Social Strategy
    </div>

    <p class="project-text">
    Developed content and social components for AGRAMI, including
    content pillars, sample creative concepts, launch planning and
    influencer, PR and community strategy.
    </p>

    <span class="tag">Content Strategy</span>
    <span class="tag">Social Media</span>
    <span class="tag">Campaign Planning</span>
    <span class="tag">Influencer Marketing</span>
    <span class="tag">PR & Community</span>

    <div class="evidence-box">
    <div class="evidence-title">My Contribution</div>

    <p class="project-text">
    Created content pillars and sample creative mapping, contributed
    to launch strategy, and developed influencer, PR and community
    activation ideas.
    </p>
    </div>

    </div>
    """,
    unsafe_allow_html=True
)

st.link_button("View AGRAMI Evidence →", AGRAMI)

# =========================================================
# NYKAA
# =========================================================

st.markdown(
    """
    <div class="project-card">

    <div class="project-number">02</div>

    <div class="project-type">Speculative Brand Campaign</div>

    <div class="project-title">
    Nykaa — “Who Taught You?”
    </div>

    <div class="project-role">
    My Role: Campaign Strategy & Concept Development
    </div>

    <p class="project-text">
    Developed a social campaign built around the idea that beauty
    knowledge is passed from one person to another.
    </p>

    <span class="tag">Consumer Insight</span>
    <span class="tag">Brand Strategy</span>
    <span class="tag">Campaign Concept</span>
    <span class="tag">UGC</span>
    <span class="tag">Social Strategy</span>

    <div class="evidence-box">
    <div class="evidence-title">My Contribution</div>

    <p class="project-text">
    Audited Nykaa's Instagram presence, identified the opportunity
    to shift from brand-led teaching to community-led teaching,
    and developed the campaign insight, platform, content mechanics,
    rollout and KPIs.
    </p>
    </div>

    </div>
    """,
    unsafe_allow_html=True
)

ny1, ny2 = st.columns(2)

with ny1:
    st.link_button("View Nykaa GitHub →", NYKAA)

with ny2:
    st.link_button("View Presentation →", NYKAA_PRESENTATION)

# =========================================================
# FAE
# =========================================================

st.markdown(
    """
    <div class="project-card">

    <div class="project-number">03</div>

    <div class="project-type">Speculative Beauty Campaign</div>

    <div class="project-title">
    FAE Beauty — FAE YOUR WAY
    </div>

    <div class="project-role">
    My Role: Campaign Concept & Social Strategy
    </div>

    <p class="project-text">
    Developed a mood-led campaign platform based on the insight
    that consumers do not have one fixed beauty aesthetic.
    </p>

    <span class="tag">Consumer Insight</span>
    <span class="tag">Campaign Strategy</span>
    <span class="tag">Creative Strategy</span>
    <span class="tag">Social Media</span>
    <span class="tag">UGC Strategy</span>

    <div class="evidence-box">
    <div class="evidence-title">Campaign Idea</div>

    <p class="project-text">
    “Your face. Your mood. Your rules.”
    The campaign connects Mood → Look → Product → FAE
    and uses creator and UGC participation to make the platform social.
    </p>
    </div>

    <div class="disclaimer">
    Speculative / student concept. Any engagement figures appearing
    in creative mockups are illustrative concept figures and not
    actual campaign results.
    </div>

    </div>
    """,
    unsafe_allow_html=True
)

st.link_button("View FAE Evidence →", FAE)

# =========================================================
# COIL
# =========================================================

st.markdown(
    """
    <div class="project-card">

    <div class="project-number">04</div>

    <div class="project-type">
    International Collaborative Research
    </div>

    <div class="project-title">
    COIL — Globalization in Action
    </div>

    <div class="project-role">
    My Role: India FGD Moderator
    </div>

    <p class="project-text">
    A cross-cultural qualitative research project comparing US and
    Indian student perspectives on the skills required for future careers.
    </p>

    <span class="tag">Qualitative Research</span>
    <span class="tag">FGD Moderation</span>
    <span class="tag">Cross-Cultural Research</span>
    <span class="tag">Interviewing</span>
    <span class="tag">Insight Generation</span>

    <div class="evidence-box">
    <div class="evidence-title">My Contribution</div>

    <p class="project-text">
    Moderated the India-side Focus Group Discussion, facilitated
    participant conversations, probed responses and contributed
    qualitative perspectives to the US–India comparison.
    </p>
    </div>

    </div>
    """,
    unsafe_allow_html=True
)

st.link_button("View COIL Evidence →", COIL)

# =========================================================
# SKILLS
# =========================================================

st.markdown(
    '<div class="section"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-label">03 — Capabilities</div>',
    unsafe_allow_html=True
)

st.markdown("## Skills & Tools")

s1, s2, s3 = st.columns(3)

with s1:
    st.markdown(
        """
        <div class="skill-card">
        <div class="skill-title">Strategy</div>
        <div class="skill-text">
        Brand Strategy<br>
        Consumer Insight<br>
        Campaign Planning<br>
        Positioning<br>
        Creative Strategy
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with s2:
    st.markdown(
        """
        <div class="skill-card">
        <div class="skill-title">Digital & Content</div>
        <div class="skill-text">
        Social Media Strategy<br>
        Content Strategy<br>
        UGC Strategy<br>
        Influencer Marketing<br>
        PR & Community
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with s3:
    st.markdown(
        """
        <div class="skill-card">
        <div class="skill-title">Research</div>
        <div class="skill-text">
        Qualitative Research<br>
        Focus Group Moderation<br>
        Interviewing<br>
        Cross-Cultural Research<br>
        Insight Generation
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

tool1, tool2 = st.columns(2)

with tool1:
    st.markdown(
        """
        <div class="skill-card">
        <div class="skill-title">Tools</div>
        <div class="skill-text">
        Canva · GitHub · Streamlit · Microsoft Office
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with tool2:
    st.markdown(
        """
        <div class="skill-card">
        <div class="skill-title">Working Style</div>
        <div class="skill-text">
        Consumer-first · Structured · Collaborative ·
        Research-led · Creative
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# CONTACT
# =========================================================

st.markdown(
    '<div class="section"></div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="contact-card">

    <div class="section-label">04 — Contact</div>

    <h2>Let's connect.</h2>

    <p class="contact-text">
    I am open to conversations around marketing, brand strategy,
    digital content and opportunities where consumer insight can
    translate into meaningful brand work.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

c1, c2 = st.columns(2)

with c1:
    st.link_button("Email Me →", EMAIL)

with c2:
    st.link_button("LinkedIn →", LINKEDIN)

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
    © 2026 Kanushi Taneja · Marketing · Brand Strategy · Digital & Content
    </div>
    """,
    unsafe_allow_html=True
)
