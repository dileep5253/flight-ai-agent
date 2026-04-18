# ✈️ AI Flight Booking Agent

An intelligent flight booking assistant that understands natural language queries and automatically selects and books flights based on user preferences (cheapest or most expensive). Includes a chatbot UI built using Streamlit.

---

## 🚀 Features

- 🧠 Natural language input  
- 💰 Selects cheapest or most expensive flight  
- 📧 Sends booking details via email  
- 🤖 Rule-based AI logic  
- 🌐 Interactive web UI using Streamlit  
- 🧩 Modular Python project  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- SMTP (Email)  
- Basic NLP (rule-based)  

---

## 📂 Project Structure


flight-ai-agent/
│── app.py
│── ai_agent_llm.py
│── agent.py
│── flight.py
│── email_service.py
│── requirements.txt
│── README.md


---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/dileep5253/flight-ai-agent.git
cd flight-ai-agent
2. Create Virtual Environment (optional)
python -m venv .venv
.venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
▶️ Run the Application
streamlit run app.py
💡 Usage

Enter your request like:

Book cheapest flight to Delhi tomorrow
Book expensive flight to Bangalore next Monday
I want to travel to Mumbai
📧 Email Setup

Edit email_service.py:

sender_email = "your_email@gmail.com"
password = "your_app_password"

⚠️ Use Gmail App Password, not your normal password.

🔐 Security Note
Do NOT upload real passwords or API keys
Use environment variables for production
🧠 How It Works
User enters request
System extracts destination and date
Flights are generated (mock data)
Agent selects:
Cheapest OR expensive flight
Ticket is created
Email is sent
📈 Future Improvements
Real flight API integration
Budget filtering (under ₹5000)
Chat history
Deployment
