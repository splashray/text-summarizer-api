# 🤖 AI Text Summarizer API

Fast API for text summarization using **Google Gemini** (FREE tier available!).

## 🚀 Quick Setup

### 1. Get Gemini API Key (Free!)

1. Go to https://aistudio.google.com/app/apikey
2. Click "Create API Key"
3. Copy your key (starts with `AIza...`)

### 2. Add API Key to Project

Open `.env` file and add your key:

```env
GEMINI_API_KEY=AIzaSy...YOUR_KEY_HERE
GEMINI_MODEL=gemini-1.5-flash
```

### 3. Start the Server

```powershell
python main.py
```

### 4. Test the API

Open browser: **http://localhost:8000/docs**

---

## 📚 API Endpoints

### `POST /summarize`

Basic text summarization

**Styles:** `concise` | `detailed` | `bullet`

```json
{
  "text": "Your long text here...",
  "style": "concise",
  "max_tokens": 150,
  "temperature": 0.7
}
```

### `POST /summarize/context`

Context-aware summarization

```json
{
  "text": "Your text...",
  "context": "for a 5-year-old"
}
```

### `POST /summarize/keypoints`

Extract key points

```json
{
  "text": "Your text...",
  "num_points": 5
}
```

---

## 🧪 Quick Test (PowerShell)

```powershell
$body = @{
    text = "Python is a high-level programming language known for its simplicity and readability. It's widely used in web development, data science, and automation."
    style = "concise"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/summarize" -Method Post -Body $body -ContentType "application/json"
```

Or run the test script:

```powershell
python test_api.py
```

---

## 💰 Pricing

**Gemini 1.5 Flash:** FREE (60 requests/minute)  
**Gemini 1.5 Pro:** FREE up to quota, then paid

Perfect for learning - no credit card required for free tier!

---

## 📁 Project Structure

```
Text-summarizer/
├── main.py                    # FastAPI app
├── services/
│   └── summarize_service.py   # Gemini integration
├── test_api.py                # Test script
├── sample_texts.py            # Sample data
├── .env                       # Your API key
└── requirements.txt           # Dependencies
```

---

## 🛠️ Installed Packages

- `google-generativeai` - Gemini SDK
- `fastapi` - Web framework
- `uvicorn` - Web server
- `python-dotenv` - Environment variables

---

## 🎯 What You'll Learn

✅ Google Gemini API integration  
✅ REST API development with FastAPI  
✅ Prompt engineering  
✅ Token management  
✅ Python best practices

---

## 🐛 Troubleshooting

**"Invalid API key"**

- Get key from https://aistudio.google.com/app/apikey
- Add to `.env` file
- Starts with `AIza`

**"Module not found"**

```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Server won't start**

```powershell
python main.py
```

Then open http://localhost:8000/docs

---

## 🔗 Resources

- Gemini API Docs: https://ai.google.dev/docs
- Get API Key: https://aistudio.google.com/app/apikey
- FastAPI Docs: https://fastapi.tiangolo.com

---
