import streamlit as st

# -----------------------
# CONFIG
# -----------------------
st.set_page_config(
    page_title="George Iordanous | Data & Finance Portfolio",
    page_icon="💳",
    layout="wide",
)

GITHUB_USERNAME = "negroniO"
LINKEDIN_URL = "https://www.linkedin.com/in/george-iordanous"
EMAIL = "george.iordanous@hotmail.com"

PAYMENT_RECOVERY_REPO = "https://github.com/negroniO/payment-recovery-ml"
PAYMENT_RECOVERY_APP = "https://payment-recovery-ml.streamlit.app"


# -----------------------
# CUSTOM CSS (VISUAL UPGRADE)
# -----------------------
CUSTOM_CSS = """
<style>

/* ---------------- GLOBAL TEXT COLOR ---------------- */
* {
    color: #f8fafc !important;
}

/* ---------------- BACKGROUND ---------------- */
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top, #1e293b 0%, #0f172a 60%);
}

.block-container {
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

/* ---------------- CARD UI ---------------- */
.card {
    background: rgba(30, 41, 59, 0.88);
    border-radius: 1.1rem;
    padding: 1.3rem 1.5rem;
    border: 1px solid rgba(148, 163, 184, 0.4);
    box-shadow: 0 18px 40px rgba(0,0,0,0.4);
    margin-bottom: 1.5rem;
}

/* ---------------- TAGS ---------------- */
.tag {
    display: inline-block;
    padding: 0.15rem 0.6rem;
    border-radius: 999px;
    font-size: 0.75rem;
    margin-right: 0.25rem;
    margin-bottom: 0.25rem;
    color: #f1f5f9 !important;
    border: 1px solid rgba(148, 163, 184, 0.7);
    background: rgba(15, 23, 42, 0.9);
}

/* Tag color accents */
.tag-ml {
    border-color: rgba(34, 197, 94, 0.9);
}

.tag-finance {
    border-color: rgba(59, 130, 246, 0.9);
}

.tag-app {
    border-color: rgba(244, 114, 182, 0.9);
}

.tag-sql {
    border-color: rgba(250, 204, 21, 0.9);
}

/* ---------------- SIDEBAR ---------------- */
[data-testid="stSidebar"] {
    background: #0f172a;
    border-right: 1px solid rgba(71, 85, 105, 0.8);
}

/* ---------------- SIDEBAR NAV BUTTON STYLING ---------------- */

/* Make each radio label look like a full-width button */
[data-testid="stSidebar"] div[role="radiogroup"] > label {
    background-color: #1e293b !important;
    padding: 10px 14px !important;
    padding-left: 16px !important;  /* adjust after removing circle */
    border-radius: 8px !important;
    margin: 6px 0 !important;
    border: 1px solid #475569 !important;
    cursor: pointer !important;
    width: 100%;
    transition: all 0.15s ease-in-out;
    color: #e2e8f0 !important;
}

/* Hover effect */
[data-testid="stSidebar"] div[role="radiogroup"] > label:hover {
    background-color: #334155 !important;
    border-color: #64748b !important;
}

/* Selected button */
[data-testid="stSidebar"] div[role="radiogroup"] > label[data-selected="true"] {
    background-color: #0ea5e9 !important;
    border-color: #38bdf8 !important;
    color: white !important;
    font-weight: 600 !important;
}

/* Remove the radio SVG icons (Streamlit's new radio circles) */
[data-testid="stSidebar"] svg {
    display: none !important;
}

</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# -----------------------
# SIDEBAR NAVIGATION
# -----------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Projects", "Skills & Experience", "Finance Use Cases", "Contact"],
)


# -----------------------
# SESSION ANALYTICS
# -----------------------
if "page_views" not in st.session_state:
    st.session_state["page_views"] = {}

st.session_state["page_views"][page] = st.session_state["page_views"].get(page, 0) + 1
total_views = sum(st.session_state["page_views"].values())

# Show analytics in the sidebar
st.sidebar.markdown("---")
st.sidebar.subheader("📊 Session Analytics")
st.sidebar.write(f"Total page views: **{total_views}**")

for p, v in st.session_state["page_views"].items():
    st.sidebar.write(f"- {p}: {v}")

st.sidebar.markdown("---")
st.sidebar.markdown("**Connect with me:**")
st.sidebar.markdown(f"[GitHub](https://github.com/{GITHUB_USERNAME})")
st.sidebar.markdown(f"[LinkedIn]({LINKEDIN_URL})")
st.sidebar.markdown(f"[Email](mailto:{EMAIL})")


# -----------------------
# TAG HELPER
# -----------------------
def render_tags(tags_with_classes):
    html = ""
    for label, extra_cls in tags_with_classes:
        html += f"<span class='tag {extra_cls}'>{label}</span>"
    st.markdown(html, unsafe_allow_html=True)


# -----------------------
# HOME
# -----------------------
def render_home():

    # Banner
    st.markdown(
        """
        <p align="center">
          <img src="https://raw.githubusercontent.com/negroniO/payment-recovery-ml/main/assets/banner.png" width="80%" />
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<h1 style='margin-bottom: 0.3rem;'>Hi, I'm George 👋</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-weight: 400;'>Data & Finance Analytics • FP&A • Machine Learning</h3>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.write(
        """
I combine **finance**, **SQL**, and **machine learning** to build tools that improve
collections, forecasting, and decision-making.

I recently finished a **Master’s in Data Analytics in Accounting & Finance** and I'm working as an **FP&A analyst**, applying
analytics directly to meaningful business problems.
        """
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Years in Finance / Analytics", "5+")
    col2.metric("ML / Analytics Projects", "5+")
    col3.metric("Tech Stack", "Python • SQL • BI")

    st.markdown("---")
    st.markdown("### 🔍 Portfolio Overview")

    st.write(
        """
This portfolio showcases projects where I:

- Build **SQL data models**  
- Develop **machine learning pipelines**  
- Deploy **Streamlit apps** for real users  
- Focus on **finance analytics**: DSO, collections, recovery, AR  
        """
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # Page view count
    st.caption(f"👀 This page viewed **{st.session_state['page_views'].get('Home', 1)}** times this session.")


# -----------------------
# PROJECTS
# -----------------------
def render_projects():
    st.title("Projects")

    # ---- Project 1 ----
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 1️⃣ Payment Recovery ML (End-to-End System)")

    render_tags([
        ("ML", "tag-ml"),
        ("Finance", "tag-finance"),
        ("Streamlit App", "tag-app"),
        ("SQL", "tag-sql"),
    ])

    st.write(
        """
Predict which failed transactions will be recovered and prioritize outreach by **expected revenue**.

- End-to-end ML pipeline  
- Logistic Regression with calibration  
- PR AUC, Brier score, lift analysis  
- Deployed as a Streamlit scoring app  
        """
    )

    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown(f"[🔗 GitHub Repo]({PAYMENT_RECOVERY_REPO})")
        st.markdown(f"[🌐 Live App]({PAYMENT_RECOVERY_APP})")
    with c2:
        st.markdown(
            """
<p align="center">
  <img src="https://raw.githubusercontent.com/negroniO/payment-recovery-ml/main/assets/demo.gif" width="95%" />
</p>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)

    # ---- Project 2 ----
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 2️⃣ Finance Collections & DSO Forecasting")

    render_tags([
        ("Time Series", "tag-ml"),
        ("Finance", "tag-finance"),
        ("DSO", "tag-finance"),
    ])

    st.write(
        """
Forecast collections and DSO using **Prophet** to support planning and treasury.

- Cash flow expectations  
- DSO forecasting  
- Trend detection  
        """
    )

    st.info("➡ Add GitHub link when ready.")
    st.markdown("</div>", unsafe_allow_html=True)

    # ---- Project 3 ----
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 3️⃣ SQL Analytics & BI Dashboards")

    render_tags([
        ("SQL", "tag-sql"),
        ("BI", "tag-app"),
        ("Finance", "tag-finance"),
    ])

    st.write(
        """
SQL-based dashboards for AR, collections, and operational analysis.

- Window functions  
- Cohort logic  
- Tableau / Power BI dashboards  
        """
    )

    st.info("➡ Add BI/SQL repo here later.")
    st.markdown("</div>", unsafe_allow_html=True)


# -----------------------
# SKILLS & EXPERIENCE
# -----------------------
def render_skills_experience():
    st.title("🛠 Skills & Experience")

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Technical Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.write(
            """
**Languages & Core:**
- Python  
- SQL (PostgreSQL, Presto)  
- R (basic)

**ML & Stats:**
- scikit-learn  
- Time series forecasting  
- Model evaluation (PR AUC, Brier, Lift)  
- Calibration  
            """
        )

    with col2:
        st.write(
            """
**Data & Engineering:**
- Pandas, NumPy  
- ETL & data cleaning  
- SQL feature engineering  
- API automation  

**Apps & BI:**
- Streamlit  
- Tableau  
- Power BI  
- Excel (advanced)  
            """
        )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Finance & Business Experience")

    st.write(
        """
- FP&A: budgeting, variance analysis, forecasting  
- Credit control & collections  
- Payment operations: card payments, settlement, chargebacks  
- Finance reporting and KPI dashboards  
        """
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Education")

    st.write(
        """
- **IBM Data Science Certificate**  
- **MSc – Data Analytics in Accounting & Finance**  
- **BSc – Economics**  
        """
    )

    st.markdown("</div>", unsafe_allow_html=True)


# -----------------------
# FINANCE USE CASES
# -----------------------
def render_finance_use_cases():
    st.title("💼 Finance & Analytics Use Cases")

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.write(
        """
### 1️⃣ Payment Recovery & Collections  
- ML scoring  
- Expected value ranking  
- Prioritized outreach  

### 2️⃣ DSO & Cash Flow Forecasting  
- DSO modeling  
- Cash inflow forecasts  
- Help treasury & FP&A  

### 3️⃣ Credit Control & Risk  
- Behavior segmentation  
- Early risk detection  

### 4️⃣ BI & Self-Service Reporting  
- Automating Excel  
- Tableau/Power BI dashboards  
- SQL analytics  
        """
    )

    st.markdown("</div>", unsafe_allow_html=True)


# -----------------------
# CONTACT
# -----------------------
def render_contact():
    st.title("Contact & Links")

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.write("If you'd like to connect:")

    st.write(f"- **GitHub:** [@{GITHUB_USERNAME}](https://github.com/{GITHUB_USERNAME})")
    st.write(f"- **LinkedIn:** [George Iordanous]({LINKEDIN_URL})")

    if EMAIL:
        st.write(f"- **Email:** {EMAIL}")

    st.markdown("---")
    st.write("If you viewed this portfolio, feel free to reach out or star a project you liked 🙂")

    st.markdown("</div>", unsafe_allow_html=True)


# -----------------------
# ROUTING
# -----------------------
if page == "Home":
    render_home()
elif page == "Projects":
    render_projects()
elif page == "Skills & Experience":
    render_skills_experience()
elif page == "Finance Use Cases":
    render_finance_use_cases()
elif page == "Contact":
    render_contact()
