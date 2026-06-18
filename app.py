import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="AI Deal Research Assistant",
    page_icon="📊",
    layout="wide"
)


def detect_business_signals(notes: str) -> list[str]:
    text = str(notes).lower()
    signals = []

    signal_keywords = {
        "AI / automation": ["ai", "automation", "automated", "machine learning", "llm"],
        "Enterprise growth": ["enterprise", "large clients", "b2b", "corporate"],
        "Hiring / team growth": ["hiring", "recruiting", "team growth", "sales staff"],
        "Product launch": ["launched", "new product", "new feature", "dashboard"],
        "Market expansion": ["expanded", "expansion", "new market", "international"],
        "Compliance / regulation": ["compliance", "regulatory", "reporting", "transaction reporting"],
        "Integration activity": ["integration", "integrations", "api", "connected"],
        "Analytics / data": ["analytics", "data", "dashboard", "insights"],
    }

    for signal, keywords in signal_keywords.items():
        if any(keyword in text for keyword in keywords):
            signals.append(signal)

    return signals if signals else ["No clear signal detected"]


def calculate_priority(sector: str, notes: str, signals: list[str]) -> tuple[str, int]:
    score = 0
    text = f"{sector} {notes}".lower()

    high_value_terms = [
        "ai", "automation", "compliance", "regulatory", "enterprise",
        "reporting", "analytics", "b2b", "workflow"
    ]

    for term in high_value_terms:
        if term in text:
            score += 1

    if len(signals) >= 3:
        score += 2
    elif len(signals) == 2:
        score += 1

    if score >= 6:
        return "High", score
    if score >= 3:
        return "Medium", score
    return "Low", score


def create_company_summary(company_name: str, sector: str, country: str, notes: str, signals: list[str]) -> str:
    signal_text = ", ".join(signals)
    return (
        f"{company_name} is a {sector} company based in {country}. "
        f"The available notes suggest the following signals: {signal_text}. "
        f"Summary note: {notes}"
    )


def suggest_next_action(priority: str, signals: list[str]) -> str:
    signal_text = " ".join(signals).lower()

    if priority == "High":
        return "Review in detail and prepare a short outreach or research note."
    if "compliance" in signal_text or "regulation" in signal_text:
        return "Check regulatory use case and compare with similar companies."
    if "hiring" in signal_text or "market expansion" in signal_text:
        return "Monitor growth signals and look for recent company updates."
    if priority == "Medium":
        return "Keep on watchlist and collect more information."
    return "Low priority for now, revisit if stronger signals appear."


def create_outreach_note(company_name: str, sector: str, signals: list[str]) -> str:
    signal_text = ", ".join(signals)
    return (
        f"Hi, I noticed {company_name} is active in the {sector} space, "
        f"with signals around {signal_text}. It would be interesting to learn more "
        f"about the company's current growth plans and product direction."
    )


def process_companies(df: pd.DataFrame) -> pd.DataFrame:
    required_columns = ["company_name", "sector", "country", "website", "notes"]

    for column in required_columns:
        if column not in df.columns:
            df[column] = ""

    results = []

    for _, row in df.iterrows():
        company_name = str(row["company_name"]).strip()
        sector = str(row["sector"]).strip()
        country = str(row["country"]).strip()
        website = str(row["website"]).strip()
        notes = str(row["notes"]).strip()

        signals = detect_business_signals(notes)
        priority, score = calculate_priority(sector, notes, signals)
        summary = create_company_summary(company_name, sector, country, notes, signals)
        next_action = suggest_next_action(priority, signals)
        outreach_note = create_outreach_note(company_name, sector, signals)

        results.append({
            "company_name": company_name,
            "sector": sector,
            "country": country,
            "website": website,
            "business_signals": ", ".join(signals),
            "priority": priority,
            "priority_score": score,
            "summary": summary,
            "next_action": next_action,
            "outreach_note": outreach_note
        })

    return pd.DataFrame(results)


st.title("AI Deal Research Assistant")
st.write(
    "A lightweight internal-tool style MVP for organising company information, "
    "summarising business signals, and generating structured decision-support outputs."
)

st.sidebar.header("Upload company data")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

st.sidebar.markdown("Expected columns:")
st.sidebar.code("company_name, sector, country, website, notes")

if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    st.info("No CSV uploaded. Using sample company data.")
    input_df = pd.read_csv("sample_companies.csv")

st.subheader("Input company data")
st.dataframe(input_df, use_container_width=True)

processed_df = process_companies(input_df)

st.subheader("Generated research outputs")
st.dataframe(processed_df, use_container_width=True)

st.subheader("Company summaries")

for _, row in processed_df.iterrows():
    with st.expander(f"{row['company_name']} - {row['priority']} priority"):
        st.write(f"**Sector:** {row['sector']}")
        st.write(f"**Country:** {row['country']}")
        st.write(f"**Website:** {row['website']}")
        st.write(f"**Business signals:** {row['business_signals']}")
        st.write(f"**Priority score:** {row['priority_score']}")
        st.write(f"**Summary:** {row['summary']}")
        st.write(f"**Suggested next action:** {row['next_action']}")
        st.write(f"**Draft outreach note:** {row['outreach_note']}")

csv_output = processed_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download generated research output as CSV",
    data=csv_output,
    file_name="deal_research_output.csv",
    mime="text/csv"
)