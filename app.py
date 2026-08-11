import os
import streamlit as st
import plotly.express as px

from modules.speech_to_text import transcribe
from modules.llm_extract import extract_expenses
from modules.csv_generator import generate_csv

st.set_page_config(
    page_title="AI Voice Expense Tracker",
    page_icon="🎙️",
    layout="wide"
)

# Load CSS
with open("styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# Hero Section
st.markdown("""
<h1 style='text-align:center;color:#2563eb;'>
🎙️ AI Voice Expense Tracker
</h1>

<p style='text-align:center;font-size:18px;color:gray;'>
Upload your weekly or monthly expense recording and let AI automatically organize every expense.
</p>

<br>
""", unsafe_allow_html=True)

# Upload
st.markdown("## 📂 Upload Audio File")

audio = st.file_uploader(
    "",
    type=["mp3", "wav", "m4a"]
)

if audio:

    os.makedirs("temp", exist_ok=True)
    os.makedirs("output", exist_ok=True)

    audio_path = os.path.join("temp", audio.name)

    with open(audio_path, "wb") as f:
        f.write(audio.read())

    st.audio(audio)

    if st.button("🚀 Analyze Expenses", use_container_width=True):

        with st.spinner("🎤 Transcribing Audio..."):
            transcript = transcribe(audio_path)

        st.success("Transcript Generated")

        st.text_area(
            "Transcript",
            transcript,
            height=220
        )

        with st.spinner("🤖 Extracting Expenses..."):
            expenses = extract_expenses(transcript)

        df, summary = generate_csv(expenses)

        total = summary["Amount"].sum()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "💰 Total Expense",
                f"₹{total:.2f}"
            )

        with col2:
            st.metric(
                "📂 Categories",
                len(summary)
            )

        with col3:
            st.metric(
                "🧾 Transactions",
                len(df)
            )

        st.markdown("---")

        st.subheader("📋 Expense Details")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("---")

        st.subheader("📊 Expense Analytics")

        left, right = st.columns(2)

        with left:

            fig = px.pie(
                summary,
                names="Category",
                values="Amount",
                hole=0.45
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with right:

            fig = px.bar(
                summary,
                x="Category",
                y="Amount"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.markdown("---")

        c1, c2 = st.columns(2)

        with c1:

            with open("output/expenses.csv", "rb") as f:

                st.download_button(
                    "⬇ Download Expenses CSV",
                    f,
                    "expenses.csv",
                    use_container_width=True
                )

        with c2:

            with open("output/summary.csv", "rb") as f:

                st.download_button(
                    "⬇ Download Summary CSV",
                    f,
                    "summary.csv",
                    use_container_width=True
                )