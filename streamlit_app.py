import streamlit as st

# ---------------------------------------------------------
# PAGE SETTINGS
# ---------------------------------------------------------

st.set_page_config(
    page_title="Kanushi Taneja | E-Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# CUSTOM STYLING
# ---------------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #FAF8F5;
    color: #222222;
}

.block-container {
    max-width: 1180px;
    padding-top: 3rem;
    padding-bottom: 4rem;
}

/* Hide Streamlit branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Main headings */

.hero-name {
    font-family: 'Playfair Display', serif;
    font-size: 4.8rem;
    line-height: 1.05;
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: #171717;
}

.hero-role {
    font-size: 1.25rem;
    color: #8A5A44;
    font-weight: 600;
    letter-spacing: 0.5px;
    margin-bottom: 1.2rem;
}

.hero-text {
    font-size: 1.1rem;
    line-height: 1.8;
    max-width: 760px;
    color: #555555;
}

/* Section headings */

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.4rem;
    font-weight: 600;
    margin-top: 4rem;
    margin-bottom: 0.7rem;
    color: #171717;
}

.section-line {
    width: 55px;
    height: 3px;
    background: #B77B5A;
    margin-bottom: 2rem;
}

/* Project cards */

.project-card {
    background: #FFFFFF;
    border: 1px solid #E9E2DC;
    border-radius: 18px;
    padding: 2rem;
    margin-bottom: 1.5rem;
    min-height: 320px;
    box-shadow: 0 8px 30px rgba(40, 30, 20, 0.05);
}

.project-number {
    font-size: 0.8rem;
    color: #B77B5A;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.project-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    font-weight: 600;
    color: #171717;
    margin: 0.5rem 0;
}

.project-type {
    font-size: 0.85rem;
    color: #777777;
    font-weight: 600;
    margin-bottom: 1rem;
}

.project-description {
    color: #555555;
    line-height: 1.7;
    font-size: 0.95rem;
}

.project-role {
    margin-top: 1.2rem;
    font-size: 0.9rem;
    line-height: 1.7;
    color: #333333;
}

.skill-pill {
    display: inline-block;
    background: #EFE7E1;
    color: #694633;
    padding: 0.45rem 0.85rem;
    border-radius: 30px;
    margin: 0.25rem;
    font-size: 0.85rem;
    font-weight: 500;
}

.info-box {
    background: #F1EBE6;
    border-radius: 18px;
    padding: 2rem;
    margin-top: 1.5rem;
}

.contact-box {
    background: #222222;
    color: white;
    border-radius: 20px;
    padding: 2.5rem;
    margin-top: 3rem;
}

.small-label {
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: 0.75rem;
    font-weight: 700;
    color: #B77B5A;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# HERO SECTION
# ---------------------------------------------------------

st.markdown('<div class="small-label">E-PORTFOLIO</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="hero-name">Kanushi<br>Taneja</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-role">Marketing · Brand Strategy · Digital & Content</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-text">
    I am a management student interested in the intersection of
    <b>consumer understanding, creativity and strategy</b>.
    My work spans live industry projects, brand campaigns, social media
    strategy and cross-cultural research.
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    st.link_button(
        "View GitHub",
        "https://github.com/27-kanushitaneja-ctrl",
        use_container_width=True
    )

with col2:
    st.link_button(
        "View Projects",
        "#featured-projects",
        use_container_width=True
    )


# ---------------------------------------------------------
# ABOUT
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">About Me</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-line"></div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown(
        """
        I enjoy working on problems where <b>consumer insight needs to
        become practical communication</b>.

        Through academic projects, live brand assignments and independent
        campaign concepts, I have worked across research, strategy,
        content development and campaign planning.

        I am particularly interested in understanding why consumers
        behave the way they do and turning those observations into
        relevant brand ideas.
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="info-box">
        <div class="small-label">Areas of Interest</div>
        <br>
        Brand Strategy<br>
        Consumer Insights<br>
        Digital Marketing<br>
        Social Media Strategy<br>
        Content Strategy<br>
        Campaign Planning<br>
        Brand Communication<br>
        Influencer & Creator Marketing
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------------------------
# PROJECTS
# ---------------------------------------------------------

st.markdown(
    '<div id="featured-projects" class="section-title">Featured Projects</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-line"></div>',
    unsafe_allow_html=True
)

st.write(
    "A selection of live, academic and independent projects demonstrating "
    "my approach to strategy, research and creative communication."
)


# ---------------------------------------------------------
# PROJECT 1 — AGRAMI
# ---------------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        """
        <div class="project-card">

        <div class="project-number">01 · LIVE INDUSTRY PROJECT</div>

        <div class="project-title">
        AGRAMI
        </div>

        <div class="project-type">
        FMCG · Brand & Social Media Strategy
        </div>

        <div class="project-description">
        Developed strategic and creative recommendations for AGRAMI,
        focusing on content, social media, launch communication and
        creator/community engagement.
        </div>

        <div class="project-role">
        <b>My contribution</b><br>
        • Developed content pillars<br>
        • Created sample content and creative concepts<br>
        • Contributed to launch strategy<br>
        • Identified relevant influencers and creator opportunities<br>
        • Developed PR and community engagement ideas
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "View AGRAMI Project →",
        "https://github.com/27-kanushitaneja-ctrl/FMCG-Live-Project",
        use_container_width=True
    )


# ---------------------------------------------------------
# PROJECT 2 — NYKAA
# ---------------------------------------------------------

with col2:

    st.markdown(
        """
        <div class="project-card">

        <div class="project-number">02 · SPECULATIVE CAMPAIGN</div>

        <div class="project-title">
        Nykaa — "Who Taught You?"
        </div>

        <div class="project-type">
        Beauty · Social Campaign · Consumer Insight
        </div>

        <div class="project-description">
        A social-first campaign built around the insight that beauty
        knowledge is often passed from one person to another.
        The platform: <b>"Who Taught You? Pass It On."</b>
        </div>

        <div class="project-role">
        <b>My contribution</b><br>
        • Conducted brand and Instagram audit<br>
        • Developed consumer insight<br>
        • Created campaign platform and core idea<br>
        • Developed content formats and mechanics<br>
        • Created rollout and KPI framework
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "View Nykaa Project →",
        "https://github.com/27-kanushitaneja-ctrl/Nykaa-Spec-Campaign-WhoTaughtYou",
        use_container_width=True
    )


# ---------------------------------------------------------
# PROJECT 3 — FAE
# ---------------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        """
        <div class="project-card">

        <div class="project-number">03 · BEAUTY CAMPAIGN</div>

        <div class="project-title">
        FAE Beauty
        </div>

        <div class="project-type">
        Campaign Strategy · Content · Social Media
        </div>

        <div class="project-description">
        A beauty brand campaign project focused on developing a
        campaign concept and social communication approach for
        FAE Beauty.
        </div>

        <div class="project-role">
        <b>Focus areas</b><br>
        • Campaign development<br>
        • Consumer-facing communication<br>
        • Social content<br>
        • Creative direction<br>
        • Brand storytelling
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------------------------
# PROJECT 4 — COIL
# ---------------------------------------------------------

with col2:

    st.markdown(
        """
        <div class="project-card">

        <div class="project-number">04 · INTERNATIONAL PROJECT</div>

        <div class="project-title">
        COIL Programme
        </div>

        <div class="project-type">
        Cross-Cultural Research · International Collaboration
        </div>

        <div class="project-description">
        A collaborative project involving students from India and the
        United States, focused on cross-cultural research and
        employability-related perspectives.
        </div>

        <div class="project-role">
        <b>Skills demonstrated</b><br>
        • Research<br>
        • Cross-cultural collaboration<br>
        • Qualitative insights<br>
        • Comparative analysis<br>
        • Presentation & teamwork
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------------------------
# SKILLS
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">Skills & Capabilities</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-line"></div>',
    unsafe_allow_html=True
)

skills = [
    "Brand Strategy",
    "Consumer Insights",
    "Campaign Planning",
    "Digital Marketing",
    "Social Media Strategy",
    "Content Strategy",
    "Creative Strategy",
    "Brand Communication",
    "Consumer Research",
    "Competitive Analysis",
    "Campaign Conceptualisation",
    "Influencer Marketing",
    "UGC Strategy",
    "Cross-Cultural Research"
]

st.markdown(
    "".join(
        f'<span class="skill-pill">{skill}</span>'
        for skill in skills
    ),
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# TOOLS
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">Tools</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-line"></div>',
    unsafe_allow_html=True
)

tools = [
    "Canva",
    "Microsoft PowerPoint",
    "Microsoft Word",
    "Microsoft Excel",
    "GitHub",
    "Streamlit"
]

st.markdown(
    "".join(
        f'<span class="skill-pill">{tool}</span>'
        for tool in tools
    ),
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# WORKING APPROACH
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">How I Approach Projects</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-line"></div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="info-box">

    <b>01 · Purpose</b><br>
    Understand the business problem, consumer and objective.

    <br><br>

    <b>02 · Process</b><br>
    Research, analyse, identify insights and develop strategic
    or creative solutions.

    <br><br>

    <b>03 · Outcome</b><br>
    Translate the thinking into tangible outputs such as campaigns,
    content, recommendations, presentations or research findings.

    <br><br>

    <b>04 · Contribution</b><br>
    Clearly distinguish my individual contribution from overall
    team outcomes.

    <br><br>

    <b>05 · Evidence</b><br>
    Connect project claims to actual working files and project evidence.

    </div>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# CONTACT
# ---------------------------------------------------------

st.markdown(
    """
    <div class="contact-box">

    <div class="small-label">LET'S CONNECT</div>

    <h2 style="color:white;">
    Interested in working together?
    </h2>

    <p style="color:#DDDDDD; line-height:1.7;">
    I am open to opportunities and conversations around marketing,
    brand strategy, digital communication and creative projects.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.link_button(
        "GitHub",
        "https://github.com/27-kanushitaneja-ctrl",
        use_container_width=True
    )

with col2:
    st.link_button(
        "LinkedIn",
        "#",
        use_container_width=True
    )

with col3:
    st.link_button(
        "Email",
        "mailto:",
        use_container_width=True
    )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.write("")
st.markdown(
    """
    <div style="text-align:center; color:#888888; padding:2rem 0 1rem 0;">
    © 2026 Kanushi Taneja · E-Portfolio
    </div>
    """,
    unsafe_allow_html=True
)
