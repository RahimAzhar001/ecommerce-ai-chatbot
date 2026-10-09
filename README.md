# E-commerce AI Customer Support Chatbot

An AI-powered customer support chatbot built with Python, Streamlit, and the Google Gemini API. It helps customers find answers to product, shipping, and return-policy questions using store-specific information.

## Features

* AI-powered conversational interface
* Store information loaded from JSON
* Product, shipping, and return-policy assistance
* Conversation history during the current session
* Environment-variable-based API key configuration
* Error handling for failed API requests

## Tech Stack

* Python
* Streamlit
* Google Gemini API
* Google Gen AI Python SDK
* JSON
* python-dotenv

## Project Structure

```
ecommerce-ai-chatbot/
├── app.py
├── test_gemini.py
├── store_data.json
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

The `.env` file is local only and must not be committed to GitHub.

## Getting Started

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd ecommerce-ai-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

Obtain an API key through [Google AI Studio](https://aistudio.google.com/). API access is subject to the provider's availability, quotas, and pricing terms.

### 5. Run the chatbot

```bash
streamlit run app.py
```

### 6. Test the API connection

```bash
python test_gemini.py
```

## Example Use Cases

* Answering frequently asked customer questions
* Explaining product details and prices
* Providing shipping and return-policy information
* Demonstrating AI integration in an e-commerce application

## Future Improvements

* Retrieval-augmented generation (RAG) for PDF and document search
* Product database integration
* Authenticated order tracking
* Improved answer evaluation and safeguards
* Deployment and production monitoring

## Disclaimer

This is an educational portfolio project using fictional store data. It is not affiliated with any real online store. AI responses should be tested before use in customer-facing production systems.

## Author

Developed as a portfolio project to explore AI chatbot development and API integration.
