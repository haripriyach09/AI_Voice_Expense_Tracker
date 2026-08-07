# 🎙️ AI Voice Expense Tracker

An AI-powered expense tracking application that converts voice recordings into structured expense reports.

Simply upload an audio recording describing your expenses, and the application will automatically:

- 🎤 Convert speech to text
- 🤖 Extract expenses using AI
- 📂 Categorize each expense
- 📊 Generate interactive charts
- 📁 Export expense reports as CSV

---

## ✨ Features

- 🎙 Upload MP3, WAV, and M4A audio files
- 📝 Automatic Speech-to-Text Transcription
- 🤖 AI-Based Expense Extraction
- 📂 Smart Expense Categorization
- 📊 Interactive Expense Analytics
- 💰 Total Expense Summary
- 📈 Category-wise Visualization
- 📥 Export Expenses to CSV
- 🎨 Clean and Professional Streamlit UI

---

## 🛠 Tech Stack

### Frontend
- Streamlit
- HTML/CSS
- Plotly

### AI Services
- AssemblyAI (Speech Recognition)
- Groq API
- Llama 3.3 70B Versatile

### Data Processing
- Pandas
- JSON

---

## 📁 Project Structure

```
AI_Voice_Expense_Tracker/
│
├── app.py
├── styles.css
├── requirements.txt
├── .env
│
├── modules/
│   ├── speech_to_text.py
│   ├── llm_extract.py
│   ├── csv_generator.py
│
├── output/
│   ├── expenses.csv
│   └── summary.csv
│
└── temp/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Voice-Expense-Tracker.git

cd AI-Voice-Expense-Tracker
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
ASSEMBLYAI_API_KEY=YOUR_ASSEMBLYAI_KEY
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📷 Workflow

1. Upload an expense audio recording.
2. Speech is converted into text.
3. AI extracts expense details.
4. Expenses are categorized.
5. Analytics dashboard is generated.
6. Download expense reports in CSV format.

---

## 📊 Output

The application generates:

- Expense Table
- Category Summary
- Pie Chart
- Bar Chart
- Expenses CSV
- Summary CSV

---

## 📌 Supported Categories

- Food
- Groceries
- Transport
- Shopping
- Clothing
- Medical
- Bills
- Education
- Entertainment
- Electronics
- Others

---

## 🚀 Future Improvements

- OCR Receipt Scanner
- Voice Recording inside the App
- Monthly Expense Dashboard
- PDF Report Export
- User Authentication
- Database Integration
- Expense History
- Budget Alerts
- Multi-language Support

---

## 👩‍💻 Author

**Kavana BV**

GitHub: https://github.com/yourusername

---

## ⭐ If you found this project useful, don't forget to star the repository.
