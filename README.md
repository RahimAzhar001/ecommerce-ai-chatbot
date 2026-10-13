# E-commerce AI Customer Support Chatbot 🤖

An AI-powered e-commerce customer support chatbot built with Python, Streamlit, and the Google Gemini API. The chatbot helps customers discover products and get answers to shipping, returns, refunds, and other store-related questions using a custom knowledge base and semantic search.

The project combines large language models (LLMs) with **semantic retrieval** to provide relevant, store-specific responses through an interactive web interface.

## 🚀 Live Demo

**Live App:** https://ecommerce-ai-chatbot-feuybxnr8gyu3s8ywjdaoq.streamlit.app/




## ✨ Features

- **AI-Powered Conversations:** Generate natural-language responses using the Google Gemini API.
- **Semantic Search:** Retrieve relevant information based on the meaning of a customer's question rather than relying only on exact keyword matches.
- **Product Discovery:** Search store products and receive recommendations based on product details and budget.
- **Store-Specific Knowledge Base:** Retrieve information from a custom JSON knowledge base.
- **Shipping Assistance:** Answer questions about standard delivery, express delivery, and free shipping.
- **Return and Refund Support:** Explain return windows, eligibility conditions, and refund processing times.
- **Interactive Chat Interface:** Use a Streamlit-based frontend with conversation history during the current session.
- **Environment-Based Configuration:** Keep API credentials outside the source code.
- **Error Handling:** Handle API failures and other exceptions with user-friendly messages.
- **Automated Retrieval Tests:** Test semantic retrieval for common customer questions.

## 🛠️ Tech Stack

- **Language:** Python
- **Frontend:** Streamlit
- **LLM:** Google Gemini API
- **AI Integration:** Google Gen AI Python SDK
- **Semantic Search:** Sentence Transformers
- **Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2`
- **Numerical Processing:** NumPy
- **Data Storage:** JSON
- **Environment Configuration:** python-dotenv
- **Version Control:** Git and GitHub
- **Deployment:** Streamlit Community Cloud

## 🧠 How It Works

1. **Customer Query:** The user enters a question in the chatbot interface.
2. **Semantic Retrieval:** The question is converted into an embedding using Sentence Transformers.
3. **Similarity Matching:** The system compares the question embedding with knowledge-base embeddings and ranks relevant documents by cosine similarity.
4. **Context Preparation:** Relevant retrieved information is provided as context for the AI response.
5. **LLM Response:** The Google Gemini API generates a natural-language answer using the supplied store information.
6. **Response Display:** The chatbot displays the answer in the Streamlit interface.

This retrieval-based approach helps the chatbot answer questions using information specific to the store.

## 📁 Project Structure

```text
ecommerce-ai-chatbot/
├── app.py
├── retriever.py
├── store_data.json
├── knowledge_base.json
├── test_gemini.py
├── test_retriever.py
├── test_semantic_retriever.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

**File descriptions:**

- `app.py` — Main Streamlit application, chatbot interface, and Gemini integration.
- `retriever.py` — Loads the knowledge base, generates embeddings, and retrieves relevant documents.
- `store_data.json` — Contains store information, product details, shipping policies, and return policies.
- `knowledge_base.json` — Contains searchable store-policy documents for semantic retrieval.
- `test_gemini.py` — Tests connectivity to the Gemini API.
- `test_retriever.py` — Tests document retrieval functionality.
- `test_semantic_retriever.py` — Tests semantic retrieval using natural-language questions.
- `requirements.txt` — Lists the Python dependencies required to run the project.
- `.env` — Stores the local Gemini API key and must not be committed to GitHub.
- `.gitignore` — Excludes sensitive files and unnecessary development artifacts.

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ecommerce-ai-chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API Key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

Get an API key from [Google AI Studio](https://aistudio.google.com/).

**Security:** Never commit your `.env` file or expose your API key in source code, screenshots, or public repositories.

### 5. Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to interact with the chatbot.

### 6. Run the Tests

Test Gemini API connectivity:

```bash
python test_gemini.py
```

Test document retrieval:

```bash
python test_retriever.py
```

Test semantic retrieval:

```bash
python test_semantic_retriever.py
```

API tests require valid credentials and available API quota. Retrieval tests may download the embedding model the first time they run.

## 💬 Example Questions

Try asking the chatbot:

- "What products do you have under $30?"
- "How quickly will an express order arrive?"
- "When should I expect to get my money back?"
- "Can I return an item after delivery?"
- "What is the minimum order amount for free shipping?"

The chatbot uses the sample store's product catalog and policy information to answer relevant questions.

## ☁️ Deployment

The application can be deployed using [Streamlit Community Cloud](https://share.streamlit.io/).

Basic deployment steps:

1. Push the project files to GitHub.
2. Create an app in Streamlit Community Cloud.
3. Select the repository, branch, and `app.py` entry point.
4. Add `GEMINI_API_KEY` to the app's Secrets settings.
5. Deploy the application and test the public URL.

Ensure that `retriever.py`, `knowledge_base.json`, `store_data.json`, and `requirements.txt` are committed to the repository.

The deployed chatbot depends on Gemini API availability and quota limits. When the free-tier quota is exhausted, AI-generated responses may temporarily become unavailable.

## 🔮 Future Improvements

- Expand the knowledge base with additional store documentation.
- Improve retrieval accuracy and evaluate similarity thresholds.
- Add product images and richer product recommendations.
- Integrate a database for dynamic product information.
- Implement authenticated order tracking.
- Add automated evaluation of answer relevance and factual accuracy.
- Improve rate-limit handling, caching, and API usage efficiency.
- Add analytics and production monitoring.

## ⚠️ Disclaimer

This is an educational portfolio project that uses fictional store data. It is not affiliated with a real online store. AI-generated responses may be inaccurate and should be evaluated before any production customer-support deployment.

## 👨‍💻 Author

**Rahim Azhar**

Computer Science Graduate | AI & Computer Vision Developer

Building practical AI applications and exploring large language models, semantic search, and intelligent automation.
