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
# SIDEBAR NAVIGATION
# -----------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Projects", "Skills & Experience", "Finance Use Cases", "Contact"],
)


# -----------------------
# HOME
# -----------------------
def render_home():
    # Banner (optional local asset)
    st.markdown(
        """
        <p align="center">
          <img src="https://raw.githubusercontent.com/negroniO/payment-recovery-ml/main/assets/banner.png" width="80%" />
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.title("Hi, I'm George 👋")
    st.subheader("Data & Finance Analytics • FP&A • Machine Learning")

    st.write(
        """
I combine **finance**, **SQL**, and **machine learning** to build tools that improve
collections, forecasting, and decision-making.

Recently, I completed a **Master’s in Data Analytics in Accounting & Finance** and I'm working as an **FP&A analyst**, applying
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
This portfolio highlights a selection of projects where I:

- Build **SQL data models** and feature views  
- Train and calibrate **ML models** for real business use cases  
- Deploy **Streamlit apps** for interactive analytics  
- Focus on **finance and payment analytics** (DSO, collections, recovery, AR)
        """
    )


# -----------------------
# PROJECTS
# -----------------------
def render_projects():
    st.title("Projects")

    st.markdown("### 1️⃣ Payment Recovery ML (End-to-End System)")

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
        st.link_button("🔗 View GitHub Repo", PAYMENT_RECOVERY_REPO)
        st.link_button("🌐 Open Live App", PAYMENT_RECOVERY_APP)

    with c2:
        st.markdown(
            """
<p align="center">
  <img src="https://raw.githubusercontent.com/negroniO/payment-recovery-ml/main/assets/demo.gif" width="95%" />
</p>
""",
            unsafe_allow_html=True,
        )

    st.markdown("---")

    st.markdown("### 2️⃣ Finance Collections & DSO Forecasting")

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

    st.markdown("---")

    st.markdown("### 3️⃣ SQL Analytics & BI Dashboards")

    st.write(
        """
**Goal:** Build analytical views and dashboards for AR, collections, and operations.

- Complex SQL with **window functions, aggregations, cohort logic**  
- Data sources integrated into **Tableau / Power BI**  
- Focus on: aging buckets, collection performance, payment behavior segmentation.
        """
    )
    st.info("➡ You can link to a 'sql-analytics' or 'bi-dashboards' repo here later.")


# -----------------------
# SKILLS & EXPERIENCE
# -----------------------
def render_skills_experience():
    st.title("🛠 Skills & Experience")

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

    st.markdown("---")
    st.markdown("### Finance & Business Experience")

    st.write(
        """
- **FP&A / Finance Analytics**: budgeting, variance analysis, forecasting  
- **Credit control and collections**: failed payments, recovery strategies, DSO reduction  
- **Payment operations**: card payments, providers, settlement, chargebacks  
- **Reporting**: building dashboards and KPIs for senior stakeholders
        """
    )

    st.markdown("---")
    st.markdown("### Education")

    st.write(
        """
-  **IBM Data Science Certificate (via Coursera)**  
-  **MSc – Data Analytics in Accounting & Finance**  
-  **BSc – Economics**
        """
    )


# -----------------------
# FINANCE USE CASES
# -----------------------
def render_finance_use_cases():
    st.title("💼 Finance & Analytics Use Cases")

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


# -----------------------
# CONTACT
# -----------------------
def render_contact():
    st.title("Contact & Links")

    st.write(
        """
If you’d like to connect, collaborate, or discuss data/ML roles in finance and analytics:

- **GitHub:** [@%s](https://github.com/%s)
- **LinkedIn:** [%s](%s)
        """
        % (GITHUB_USERNAME, GITHUB_USERNAME, "George Iordanous", LINKEDIN_URL)
    )

    if EMAIL:
        st.write(f"- **Email:** {EMAIL}")

    st.markdown("---")
    st.write("If you viewed this portfolio, feel free to reach out or star a project you liked 🙂")


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
