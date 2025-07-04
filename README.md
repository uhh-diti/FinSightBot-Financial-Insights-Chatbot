# FinSightBot-Financial-Insights-Chatbot
Your AI-powered assistant for decoding 10-K reports and visualizing financial health
Financial Metrics Chatbot + Dashboard (2022–2024)

This project was developed as part of the BCG GenAI Consulting Team job simulation on Forage, where I built an AI-powered financial assistant capable of interpreting SEC filings and delivering user-friendly insights via chatbot and dashboard interfaces.

🔍 Features

Extracted key financial figures from 10-K and 10-Q reports for Apple, Microsoft, and Tesla

Calculated YoY growth for:

Total Revenue

Net Income

Total Assets

Total Liabilities

Operating Cash Flow

Developed a rule-based Python chatbot using Flask for web deployment

Visualized trends and chatbot responses interactively using Power BI with Python scripting

Ensured users could query financial metrics easily through either a browser or dashboard UI

📊 Technologies Used

Python: pandas, Flask

Power BI: DAX, Python script integration

Jupyter Notebook: Financial data cleaning & metric engineering

HTML (Jinja2): For chatbot web interface

📁 Folder Structure

financial-chatbot-dashboard/
│
├── data/
│   ├── 10k_reports_raw/            # 10-K and 10-Q excerpts (2022–2024)
│   └── processed_financials.csv     # Structured data with growth metrics
│
├── chatbot/
│   ├── app.py                     # Flask web app with chatbot
│   ├── templates/
│   │   └── index.html          # Chat UI page
│   └── requirements.txt
│
├── powerbi/
│   ├── chatbot_powerbi.pbix       # Power BI dashboard with embedded Python script
│   └── screenshots/
│       └── demo_ui.png            # Example chatbot in Power BI
│
├── notebooks/
│   └── financial_analysis.ipynb   # Jupyter notebook with metric calculations
│
└── README.md

🚀 Run the Chatbot App Locally

cd chatbot/
pip install -r requirements.txt
python app.py

Open in your browser: http://127.0.0.1:5000

📊 View Dashboard in Power BI

Open powerbi/chatbot_powerbi.pbix

Enable Python scripting under Power BI options

Use slicers to select questions and view automated responses

🙋‍♀️ About Me

Aditi MararAspiring AI/ML Engineer | Python + BI Enthusiast 
: https://www.linkedin.com/in/aditi-marar-901943290

Project built as part of BCG GenAI Virtual Experience via Forage.

I'm always open to collaboration or feedback!
