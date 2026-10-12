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

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@400;500;600&display=swap');

html {
    scroll-behavior: smooth;
}

body {
    background: #F5F1EB;
}

.stApp {
    background: #F5F1EB;
    color: #191817;
}

.block-container {
    max-width: 1180px;
    padding-top: 25px;
    padding-bottom: 80px;
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


/* NAVIGATION */

.navbar {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 12px 0 22px;

    border-bottom: 1px solid #D5CDC2;
}

.logo {
    font-family: 'DM Sans', sans-serif;
    font-size: 18px;
    font-weight: 700;
}

.nav-right {
    font-family: 'DM Sans', sans-serif;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 2px;
    color: #766E65;
}


/* HERO */

.hero {
    padding: 75px 0 45px;
}

.kicker {
    font-family: 'DM Sans', sans-serif;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #7D746A;
    margin-bottom: 25px;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 82px;
    line-height: .94;
    letter-spacing: -4px;
    font-weight: 500;
}

.hero-title em {
    font-style: italic;
}

.hero-intro {
    font-family: 'DM Sans', sans-serif;
    font-size: 20px;
    line-height: 1.6;
    color: #48433D;
    max-width: 700px;
    margin-top: 32px;
}

.hero-intro strong {
    color: #191817;
}

.hero-detail {
    font-family: 'DM Sans', sans-serif;
    font-size: 15px;
    line-height: 1.75;
    color: #746D65;
    max-width: 650px;
    margin-top: 16px;
}

.hero-line {
    width: 70px;
    height: 2px;
    background: #191817;
    margin-top: 35px;
}


/* PROFILE */

.profile-card {
    background: #DDD6CC;
    padding: 12px;
    margin-top: 65px;
}

.profile-caption {
    font-family: 'DM Sans', sans-serif;
    font-size: 9px;
    letter-spacing: 1.6px;
    text-transform: uppercase;
    color: #81786E;
    margin-top: 12px;
}


/* PROOF */

.proof {
    border-top: 1px solid #D1C8BC;
    border-bottom: 1px solid #D1C8BC;

    padding: 28px 0;

    margin: 20px 0 100px;
}

.proof-number {
    font-family: 'Playfair Display', serif;
    font-size: 34px;
}

.proof-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 9px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #81786E;
    margin-top: 7px;
}


/* SECTIONS */

.section-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2.2px;
    text-transform: uppercase;
    color: #83796E;
    margin-bottom: 13px;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 52px;
    line-height: 1;
    font-weight: 500;
    margin-bottom: 45px;
}


/* PROJECT VISUALS */

.project-visual {
    height: 315px;

    display: flex;
    align-items: center;
    justify-content: center;

    padding: 40px;
}

.agrami {
    background: #D8D0C1;
}

.nykaa {
    background: #E7D9D8;
}

.fae {
    background: #DDD8D0;
}

.coil {
    background: #D8DCE0;
}

.visual-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 15px;
}

.visual-title {
    font-family: 'Playfair Display', serif;
    font-size: 48px;
    line-height: .95;
}

.visual-title em {
    font-style: italic;
}


/* PROJECT INFO */

.project {
    border-top: 1px solid #CEC5B9;
    padding: 28px 0 35px;
}

.project-number {
    font-family: 'DM Sans', sans-serif;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: #8A8177;
}

.project-name {
    font-family: 'Playfair Display', serif;
    font-size: 42px;
    margin-top: 8px;
}

.project-tag {
    display: inline-block;

    font-family: 'DM Sans', sans-serif;
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 1.5px;

    padding: 6px 9px;

    border: 1px solid #BBB2A7;

    margin: 5px 0 17px;
}

.project-description {
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    line-height: 1.7;
    color: #625B53;
}

.project-role {
    font-family: 'DM Sans', sans-serif;
    font-size: 12px;
    line-height: 1.7;

    color: #302D2A;

    margin-top: 20px;
}

.role-label {
    font-size: 9px;
    letter-spacing: 1.5px;
    font-weight: 700;
    color: #82786E;
    margin-bottom: 3px;
}


/* ABOUT */

.about {
    margin-top: 120px;
}

.about-heading {
    font-family: 'Playfair Display', serif;
    font-size: 39px;
    line-height: 1.2;
}

.about-heading em {
    font-style: italic;
}

.about-copy {
    font-family: 'DM Sans', sans-serif;
    font-size: 16px;
    line-height: 1.85;
    color: #5D5750;
}

.about-copy strong {
    color: #24211E;
}

.about-side {
    border-left: 1px solid #CFC6BA;
    padding-left: 35px;
}

.side-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    color: #82786E;
}

.side-title {
    font-family: 'Playfair Display', serif;
    font-size: 30px;
    line-height: 1.2;
    margin-top: 14px;
}

.side-copy {
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    line-height: 1.7;
    color: #6F675F;
    margin-top: 18px;
}


/* THINKING */

.thinking {
    margin-top: 120px;

    padding: 60px 0;

    border-top: 1px solid #CEC5B9;
    border-bottom: 1px solid #CEC5B9;
}

.thinking-title {
    font-family: 'Playfair Display', serif;
    font-size: 40px;
    line-height: 1.2;
}

.thinking-title em {
    font-style: italic;
}

.thinking-step {
    padding: 18px 0;

    border-bottom: 1px solid #D8D0C5;

    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    line-height: 1.6;
}

.thinking-number {
    color: #8A8177;
    font-size: 10px;
    letter-spacing: 1px;
    margin-right: 10px;
}


/* TOOLKIT */

.toolkit {
    margin-top: 110px;
}

.toolkit-box {
    border-top: 1px solid #CEC5B9;
    padding: 23px 0 28px;
}

.toolkit-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    color: #81776D;
}

.toolkit-text {
    font-family: 'DM Sans', sans-serif;
    font-size: 15px;
    line-height: 1.7;
    margin-top: 9px;
}


/* CONTACT */

.contact {
    background: #191817;

    color: #F5F1EB;

    margin-top: 110px;

    padding: 70px 60px;
}

.contact-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #AAA39A;
}

.contact-title {
    font-family: 'Playfair Display', serif;
    font-size: 55px;
    line-height: 1.03;

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

    max-width: 520px;

    margin-top: 23px;
}


/* FOOTER */

.footer {
    border-top: 1px solid #CEC5B9;

    margin-top: 45px;
    padding-top: 20px;

    display: flex;
    justify-content: space-between;

    font-family: 'DM Sans', sans-serif;
    font-size: 10px;
    letter-spacing: 1px;
    color: #82786E;
}


/* MOBILE */

@media (max-width: 768px) {

    .hero-title {
        font-size: 55px;
        letter-spacing: -2px;
    }

    .hero-intro {
        font-size: 18px;
    }

    .section-title {
        font-size: 40px;
    }

    .project-name {
        font-size: 36px;
    }

    .visual-title {
        font-size: 39px;
    }

    .about {
        margin-top: 80px;
    }

    .about-side {
        margin-top: 40px;
    }

    .thinking {
        margin-top: 80px;
    }

    .contact {
        padding: 45px 28px;
    }

    .contact-title {
        font-size: 42px;
    }

    .footer {
        display: block;
        line-height: 2;
    }

}

/* INTERNSHIP EXPERIENCE CARDS */

.internship-card {
    display: grid;
    grid-template-columns: 45px minmax(0, 1fr);
    gap: 20px;
    padding: 32px 0;
    border-top: 1px solid #CEC5B9;
}

.internship-number {
    font-family: 'Playfair Display', serif;
    font-size: 30px;
    color: #A49A8E;
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
    font-size: 28px;
    line-height: 1.3;
    color: #191817;
    max-width: 750px;
}

.internship-date {
    font-family: 'DM Sans', sans-serif;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1px;
    color: #82786E;
    padding-top: 8px;
}

.internship-role {
    font-family: 'DM Sans', sans-serif;
    font-size: 12px;
    font-weight: 600;
    color: #82786E;
    margin-top: 8px;
}

.internship-description {
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    line-height: 1.8;
    color: #625B53;
    max-width: 800px;
    margin-top: 18px;
}

.internship-tags {
    font-family: 'DM Sans', sans-serif;
    font-size: 9px;
    font-weight: 700;
    line-height: 1.8;
    letter-spacing: 1px;
    color: #82786E;
    margin-top: 16px;
}

@media (max-width: 768px) {
    .internship-card {
        grid-template-columns: 30px minmax(0, 1fr);
        gap: 12px;
    }

    .internship-company {
        font-size: 23px;
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
        KT.
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
<div class="proof">
""")

p1, p3, p4 = st.columns(3)

with p1:
    st.html("""
    <div class="proof-number">4</div>
    <div class="proof-label">Internship Experiences</div>
    """)

with p3:
    st.html("""
    <div class="proof-number">6+</div>
    <div class="proof-label">Insurance Brands Analysed</div>
    """)

with p4:
    st.html("""
    <div class="proof-number">4</div>
    <div class="proof-label">Featured Projects</div>
    """)

st.html("""
</div>
""")


# =========================================================
# INTERNSHIP EXPERIENCE
# =========================================================

st.html("""
<div style="margin-top:100px; margin-bottom:35px;">
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
    "EXPLORE PROJECT & CREATIVES →",
    "https://github.com/27-kanushitaneja-ctrl/SuperDrinks-Live-Project",
    use_container_width=True
)

st.link_button(
    "VISIT BRAND WEBSITE →",
    "https://superdrinks.in/",
    use_container_width=True
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
            02 / 05
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


# =========================================================
# NYKAA
# =========================================================

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
            03 / 05
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
            04 / 05
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

    st.html("""
    <div class="project-visual coil">

        <div>

            <div class="visual-label">
                INTERNATIONAL RESEARCH
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

    st.html("""
    <div class="project">

        <div class="project-number">
            05 / 05
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
