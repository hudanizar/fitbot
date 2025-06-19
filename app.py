# app.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import scipy.cluster.hierarchy as sch
from PIL import Image

# ===== PAGE CONFIGURATION =====
st.set_page_config(page_title="📊 Financial Ratios with Dr. Nurhuda", layout="wide")
st.title("🔮 Learn with Dr. Nurhuda!")

# ===== TAB NAVIGATION =====
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "About Me", "📘 Intro & Guide", "💬 Chatbot", 
    "🧮 Ratio Calculator", "🧠 Quiz", "📈 Visualization", "✉️ Feedback"
])

# ===== SIDEBAR PROFILE =====
image = Image.open("nurhuda_photo.png")
st.sidebar.image(image, width=200)
st.sidebar.markdown("## Dr. Nurhuda Nizar")
st.sidebar.markdown("Senior Lecturer in Finance, UiTM Puncak Alam")


# ============ TAB1: ABOUT ME TAB  ============
with tab1:
    col1, col2 = st.columns([1, 3])
    with col1:
        st.subheader("👤 About Dr. Nurhuda Nizar, PhD")
        st.markdown("""
**Senior Lecturer in Finance, UiTM Puncak Alam.**

🏛️ **Teaching Focus**
- Financial Market and Banking Services
- Business Analytics and Financial Modelling
- Ar-Rahnu, Financial Management, Insurance

🎓 **Education**
- PhD in Finance, UKM (2019)
- Master’s in Finance, UiTM (2010)
- Master’s in TVET, UTHM (2006)
- BBA in Finance, UiTM (2005)

📝 **Academic Contributions**
- MQA Assessor Panels (2020–2024)
- Guest Lecturer (2023)
- FIN435 & FIN534 Resource Person
- Journal Reviewer and Editorial Roles
        """)

        st.markdown("""
<div style='text-align: center; font-size: 14px; color: grey; margin-top: 50px;'>
    <strong>Dr. Nurhuda Nizar</strong><br>
    Department of Economic and Financial Studies | UiTM Puncak Alam<br>
    hudanizar@uitm.edu.my
</div>
""", unsafe_allow_html=True)


# ============ TAB2: INTRO & GUIDE TAB ============
with tab2:
    st.title(":blue_book: Welcome to the FinBot: Interactive Chatbot for Learning Financial Ratios")
    st.markdown("""
**Purpose**: Help you learn, calculate, and test your understanding of financial ratios. 

:point_right: Try asking in the Chatbot:
- *What is the current ratio?*
- *How do I calculate ROE?*

This tool is designed for **students, lecturers, and anyone learning finance**.
    """)

    with st.expander(":bulb: FAQ"):
        st.write("""
        This chatbot uses a predefined knowledge base on key financial ratios, 
        such as liquidity, profitability, leverage, efficiency, and market value ratios.
        """)


# ============ TAB3: CHATBOT (Categorized, Text-Based) ============
with tab3:
    st.title("💬 Financial Ratios Chatbot")
    st.markdown("Type any financial ratio name or question (e.g., **What is ROE?**, **Explain Quick Ratio**)")

    ratio_data = {
        # Liquidity
        "current ratio": {
            "category": "Liquidity",
            "formula": "Current Assets / Current Liabilities",
            "description": "Measures a company’s ability to pay short-term obligations."
        },
        "quick ratio": {
            "category": "Liquidity",
            "formula": "(Current Assets − Inventories) / Current Liabilities",
            "description": "Also called the acid-test ratio, it measures immediate short-term liquidity."
        },
        "cash ratio": {
            "category": "Liquidity",
            "formula": "Cash / Current Liabilities",
            "description": "The most conservative liquidity ratio. Only includes cash."
        },

        # Leverage
        "debt-to-equity": {
            "category": "Leverage",
            "formula": "Total Liabilities / Shareholders’ Equity",
            "description": "Indicates the proportion of equity and debt used to finance assets."
        },
        "debt ratio": {
            "category": "Leverage",
            "formula": "Total Liabilities / Total Assets",
            "description": "Shows the percentage of assets financed with debt."
        },
        "interest coverage": {
            "category": "Leverage",
            "formula": "EBIT / Interest Expense",
            "description": "Assesses a company’s ability to meet interest payments."
        },

        # Efficiency
        "inventory turnover": {
            "category": "Efficiency",
            "formula": "COGS / Average Inventory",
            "description": "Shows how often inventory is sold and replaced."
        },
        "asset turnover": {
            "category": "Efficiency",
            "formula": "Revenue / Total Assets",
            "description": "Measures efficiency in using assets to generate sales."
        },
        "receivables turnover": {
            "category": "Efficiency",
            "formula": "Net Credit Sales / Avg. Accounts Receivable",
            "description": "Measures effectiveness in collecting receivables."
        },
        "payables turnover": {
            "category": "Efficiency",
            "formula": "COGS / Avg. Accounts Payable",
            "description": "Shows how quickly a company pays its suppliers."
        },

        # Profitability
        "gross profit margin": {
            "category": "Profitability",
            "formula": "(Revenue − COGS) / Revenue",
            "description": "Measures the % of revenue retained after direct costs."
        },
        "net profit margin": {
            "category": "Profitability",
            "formula": "Net Income / Revenue",
            "description": "Shows overall profitability after all expenses."
        },
        "return on assets": {
            "category": "Profitability",
            "formula": "Net Income / Total Assets",
            "description": "Indicates how efficient a company is in using assets."
        },
        "return on equity": {
            "category": "Profitability",
            "formula": "Net Income / Shareholders’ Equity",
            "description": "Shows the return generated on shareholders’ investments."
        },

        # Market Value
        "eps": {
            "category": "Market Value",
            "formula": "Net Income / Shares Outstanding",
            "description": "Earnings per share – a key indicator of profitability."
        },
        "p/e ratio": {
            "category": "Market Value",
            "formula": "Price per Share / EPS",
            "description": "Shows how much investors pay per RM of earnings."
        },
        "market-to-book": {
            "category": "Market Value",
            "formula": "Market Value per Share / Book Value per Share",
            "description": "Compares market value of equity to its book value."
        },
        "dividend yield": {
            "category": "Market Value",
            "formula": "Dividends per Share / Price per Share",
            "description": "Shows cash return from owning the stock."
        }
    }

    # Input box
    query = st.text_input("Ask about any financial ratio:")

    if query:
        matched = None
        for key in ratio_data:
            if key in query.lower():
                matched = ratio_data[key]
                break

        if matched:
            st.markdown(f"### 📘 {key.title()} ({matched['category']} Ratio)")
            st.markdown(f"**Formula:** `{matched['formula']}`")
            st.markdown(f"**Use:** {matched['description']}")
        else:
            st.warning("🤖 I couldn’t find that ratio. Try asking about ROE, P/E, or Current Ratio.")



# ============ TAB 4: RATIO CALCULATOR ============
with tab4:
    st.title("🧮 Financial Ratio Calculator")

    uploaded_file = st.file_uploader("📂 Upload your Excel file (e.g., Statement of Financial Position)", type=["xlsx"])
    
    if uploaded_file:
        # Try to read after skipping multi-row header
        df = pd.read_excel(uploaded_file, header=5)  # skip first 5 rows as in your screenshot
        st.subheader("📊 Data Preview")
        st.dataframe(df.head())

        # Clean and prepare the DataFrame
        df.columns = df.columns.map(str)
        df.rename(columns={df.columns[0]: "Item"}, inplace=True)
        df["Item"] = df["Item"].str.strip()
        df.set_index("Item", inplace=True)

        # Define the years you want to evaluate
        years = ["2019", "2020", "2021", "2022", "2023"]

        # Extract relevant rows
        try:
            current_assets = df.loc["Total current assets", years]
            total_assets = df.loc["Total assets", years]
            cash = df.loc.get("Cash and bank balances", pd.Series([0]*len(years), index=years))
            inventories = df.loc.get("Inventories", pd.Series([0]*len(years), index=years))
            receivables = df.loc.get("Trade and other receivables", pd.Series([0]*len(years), index=years))

            # If you have total liabilities and equity from other sheets, adjust here
            # For demo, assume:
            total_liabilities = pd.Series([4000000, 4200000, 4500000, 4700000, 4300000], index=years)
            total_equity = total_assets - total_liabilities  # estimated

            # === Calculate Ratios ===
            ratios = pd.DataFrame(index=years)

            # Liquidity
            ratios["Current Ratio"] = current_assets / total_liabilities
            ratios["Quick Ratio"] = (current_assets - inventories) / total_liabilities

            # Leverage
            ratios["Debt Ratio"] = total_liabilities / total_assets
            ratios["Debt-to-Equity"] = total_liabilities / total_equity

            # Efficiency (basic approximation)
            ratios["Asset Turnover"] = receivables / total_assets  # proxy

            # Profitability (requires Net Income - assumed dummy here)
            net_income = pd.Series([300000, 350000, 370000, 390000, 360000], index=years)
            ratios["ROA"] = net_income / total_assets
            ratios["ROE"] = net_income / total_equity

            # Market Value (dummy EPS)
            net_income_total = net_income
            shares_outstanding = pd.Series([100000]*5, index=years)
            ratios["EPS"] = net_income_total / shares_outstanding

            st.subheader("✅ Financial Ratios Summary")
            st.dataframe(ratios.style.format("{:.2f}"))

        except KeyError as e:
            st.error(f"❌ Missing expected row: {e}")
        except Exception as e:
            st.error(f"⚠️ Error processing the file: {e}")

        st.session_state.ratios = ratios



# ============ TAB 5: QUIZ ============ 
with tab5:
    st.title("🧠 Quick Quiz")

    st.subheader("Test your understanding of financial ratios:")

    # Question 1 – Liquidity
    q1 = st.radio("1. What does the Current Ratio measure?", 
                  ["Profitability", "Liquidity", "Leverage"])
    if q1:
        if q1 == "Liquidity":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. It measures Liquidity.")

    # Question 2 – Leverage
    q2 = st.radio("2. Which ratio indicates how much debt a company uses to finance its assets?",
                  ["Return on Equity", "Debt Ratio", "Inventory Turnover"])
    if q2:
        if q2 == "Debt Ratio":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. The correct answer is Debt Ratio.")

    # Question 3 – Profitability
    q3 = st.radio("3. Return on Equity (ROE) tells you how much...", 
                  ["Equity is available", "Net income is earned per unit of equity", "Debt is used"])
    if q3:
        if q3 == "Net income is earned per unit of equity":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. ROE measures net income per unit of equity.")

    # Question 4 – Efficiency
    q4 = st.radio("4. Which ratio reflects how efficiently a firm uses its assets to generate sales?",
                  ["Asset Turnover", "Current Ratio", "Debt-to-Equity"])
    if q4:
        if q4 == "Asset Turnover":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. Asset Turnover measures efficiency.")

    # Question 5 – Market Value
    q5 = st.radio("5. What does the Price/Earnings (P/E) Ratio represent?",
                  ["Profitability", "Market expectation", "Liquidity"])
    if q5:
        if q5 == "Market expectation":
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect. It reflects market expectations of earnings.")



# ============ TAB 6: VISUALIZATION ============
with tab6:
    st.title("📈 Ratio Trend Visualization")

    if "ratios" in st.session_state:
        ratios = st.session_state.ratios.copy()
        ratios.reset_index(inplace=True)
        ratios = pd.melt(ratios, id_vars="index", var_name="Ratio", value_name="Value")
        ratios.rename(columns={"index": "Year"}, inplace=True)

        selected_ratios = st.multiselect(
            "📌 Select ratios to visualize:", 
            sorted(ratios["Ratio"].unique()), 
            default=["Current Ratio", "Debt Ratio"]
        )

        if selected_ratios:
            filtered = ratios[ratios["Ratio"].isin(selected_ratios)]

            fig = px.line(
                filtered, x="Year", y="Value", color="Ratio",
                markers=True, title="📊 Financial Ratio Trends Over Years"
            )
            fig.update_layout(legend_title_text='Ratio', xaxis_title="Year", yaxis_title="Value")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("☝️ Please select at least one ratio to visualize.")
    else:
        st.warning("⚠️ Please calculate ratios first in the Ratio Calculator tab.")


# ============ TAB 7: FEEDBACK ============
with tab7:
    st.title("✉️ Feedback")
    st.markdown("We’d love to hear your thoughts!")

    name = st.text_input("Your Name")
    feedback = st.text_area("Your Feedback")
    if st.button("Submit"):
        if feedback:
            st.success("✅ Thank you for your feedback!")
        else:
            st.error("⚠️ Please enter feedback before submitting.")


