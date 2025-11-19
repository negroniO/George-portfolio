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
/* Global text color for good contrast on dark theme */
* {
    color: #f8fafc !important;
}

/* Adjust body background */
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top, #1e293b 0%, #0f172a 60%);
}

/* Improve content visibility */
.block-container {
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

/* Card UI */
.card {
    background: rgba(30, 41, 59, 0.88);
    border-radius: 1.1rem;
    padding: 1.3rem 1.5rem;
    border: 1px solid rgba(148, 163, 184, 0.4);
    box-shadow: 0 18px 40px rgba(0,0,0,0.4);
    margin-bottom: 1.5rem;
}

/* Tag chips */
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

/* Sidebar */
[data-testid="stSidebar"] {
    background: #0f172a;
    border-right: 1px solid rgba(71, 85, 105, 0.8);
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
# SIMPLE SESSION ANALYTICS
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
    """
    tags_with_classes: list of (label, extra_class) pairs,
    e.g. [("ML", "tag-ml"), ("Finance", "tag-finance")]
    """
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


    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.write(
            """
I combine **finance**, **SQL**, and **machine learning** to build tools that improve
collections, forecasting, and decision-making.

I recently finished a **Master’s in Data Analytics in Accounting & Finance** and I'm working as an **FP&A analyst**, applying
analytics directly to real business problems.
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
This portfolio highlights projects where I:

- Build **SQL data models** and feature views  
- Train and calibrate **ML models** for real business use cases  
- Deploy **Streamlit apps** for interactive analytics  
- Focus on **finance and payment analytics** (DSO, collections, recovery, AR)
            """
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # Optional: show current page view count on home
    st.caption(
        f"👀 This page viewed **{st.session_state['page_views'].get('Home', 1)}** times this session."
    )


# -----------------------
# PROJECTS
# -----------------------
def render_projects():
    st.title("Projects")

    # ---- Project 1: Payment Recovery ML ----
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 1️⃣ Payment Recovery ML (End-to-End System)")
    render_tags(
        [
            ("ML", "tag-ml"),
            ("Finance", "tag-finance"),
            ("Streamlit App", "tag-app"),
            ("SQL", "tag-sql"),
        ]
    )

    st.write(
        """
**Goal:** Predict which failed / unpaid transactions will be recovered within 30 days and
prioritize outreach based on **expected recovered revenue**.

- End-to-end ML pipeline (SQL → features → model → scoring → app)  
- Calibrated Logistic Regression with PR AUC, Brier Score, lift analysis  
- Expected value ranking: `amount × probability`  
- Deployed Streamlit app for interactive scoring  
        """
    )

    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown(
            f"[🔗 View GitHub Repo]({PAYMENT_RECOVERY_REPO})  \n"
            f"[🌐 Open Live App]({PAYMENT_RECOVERY_APP})"
        )
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

    # ---- Project 2: Finance Collections & DSO Forecasting ----
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 2️⃣ Finance Collections & DSO Forecasting")
    render_tags(
        [
            ("Time Series", "tag-ml"),
            ("Finance", "tag-finance"),
            ("DSO", "tag-finance"),
        ]
    )

    st.write(
        """
**Goal:** Forecast collections and **Days Sales Outstanding (DSO)** over time.

- Time series modeling using **Prophet / time series tools**  
- Uses AR / collections and invoice data  
- Produces charts for expected cash inflows and DSO trends  
- Helps finance teams anticipate cash flow and risk
        """
    )
    st.info("➡ Add GitHub link for this project here once the repo is ready.")
    st.markdown("</div>", unsafe_allow_html=True)

    # ---- Project 3: SQL Analytics & BI Dashboards ----
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 3️⃣ SQL Analytics & BI Dashboards")
    render_tags(
        [
            ("SQL", "tag-sql"),
            ("BI", "tag-app"),
            ("Finance", "tag-finance"),
        ]
    )

    st.write(
        """
**Goal:** Build analytical views and dashboards for AR, collections, and operations.

- Complex SQL with **window functions, aggregations, cohort logic**  
- Data sources integrated into **Tableau / Power BI**  
- Focus on: aging buckets, collection performance, payment behavior segmentation.
        """
    )
    st.info("➡ You can link to a 'sql-analytics' or 'bi-dashboards' repo here later.")
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
- Time series (Prophet / forecasting)
- Model evaluation (PR AUC, Brier, lift)
- Probability calibration
            """
        )
    with col2:
        st.write(
            """
**Data & Engineering:**
- Pandas, NumPy
- ETL & data cleaning
- SQL feature engineering
- APIs & automation scripts

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
- **FP&A / Finance Analytics**: budgeting, variance analysis, forecasting  
- **Credit control and collections**: failed payments, recovery strategies, DSO reduction  
- **Payment operations**: card payments, providers, settlement, chargebacks  
- **Reporting**: building dashboards and KPIs for senior stakeholders
        """
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Education")
    st.write(
        """
- **IBM Data Science Certificate (via Coursera)**  
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
I focus on problems at the intersection of **finance operations** and **analytics**:

### 1️⃣ Payment Recovery & Collections
- Prioritizing failed card payments using ML  
- Estimating probability of recovery and expected value  
- Helping teams focus on the *right* customers

### 2️⃣ DSO & Cash Flow Forecasting
- Modeling DSO (Days Sales Outstanding) over time  
- Projecting collections and expected cash inflows  
- Supporting treasury and planning decisions

### 3️⃣ Credit Control & Risk
- Segmenting customers by payment behavior  
- Identifying high-risk accounts early  
- Building reporting around overdue balances

### 4️⃣ BI & Self-Service Reporting
- Automating manual Excel reports using Python + SQL  
- Tableau / Power BI dashboards for AR, invoices, and collections  
- Enabling non-technical stakeholders to explore data easily
        """
    )
    st.markdown("</div>", unsafe_allow_html=True)


# -----------------------
# CONTACT
# -----------------------
def render_contact():
    st.title("Contact & Links")

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write(
        """
If you’d like to connect, collaborate, or discuss data/ML roles in finance and analytics:
        """
    )
    st.write(
        f"""
- **GitHub:** [@{GITHUB_USERNAME}](https://github.com/{GITHUB_USERNAME})  
- **LinkedIn:** [George Iordanous]({LINKEDIN_URL})  
        """
    )

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
