# 🏗️ Project Architecture

## Overview

AI Text Summarizer API built with **FastAPI** and **Google Gemini**.

---

## 🎯 Core Components

### 1. **main.py** - API Layer

FastAPI application with REST endpoints

**Responsibilities:**

- Define API routes
- Handle HTTP requests/responses
- Validate input data with Pydantic
- Route requests to service layer

**Endpoints:**

- `GET /` - API info
- `GET /health` - Health check
- `POST /summarize` - Basic summarization
- `POST /summarize/context` - Context-aware summarization
- `POST /summarize/keypoints` - Key points extraction

### 2. **services/summarize_service.py** - Business Logic

Gemini integration and summarization logic

**Responsibilities:**

- Initialize Gemini client
- Create prompts for different styles
- Call Gemini API
- Handle API responses and errors

**Methods:**

- `summarize_text()` - Main summarization with style options
- `summarize_with_context()` - Context-aware summarization
- `extract_key_points()` - Extract numbered key points

### 3. **.env** - Configuration

Environment variables for API keys

**Contains:**

- `GEMINI_API_KEY` - Your Gemini API key
- `GEMINI_MODEL` - Model to use (gemini-1.5-flash or gemini-1.5-pro)

---

## 📊 Request Flow

```
User Request
    ↓
FastAPI (main.py)
    ↓
Pydantic Validation
    ↓
SummarizeService (service layer)
    ↓
Google Gemini API
    ↓
Response Processing
    ↓
JSON Response to User
```

### Example: POST /summarize

1. **User sends request:**

```json
{
  "text": "Long text...",
  "style": "concise",
  "max_tokens": 150,
  "temperature": 0.7
}
```

2. **FastAPI validates** with `SummarizeRequest` model

3. **Calls** `summarizer.summarize_text()`

4. **Service creates prompt:**

```python
prompt = "Provide a brief, concise summary in 2-3 sentences.\n\nSummarize: {text}"
```

5. **Gemini generates** summary

6. **Returns:**

```json
{
  "success": true,
  "summary": "Generated summary...",
  "model": "gemini-1.5-flash",
  "style": "concise"
}
```

---

## 🔧 Technology Stack

### Backend

- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation

### AI/ML

- **Google Gemini** - LLM for text generation
- **google-generativeai** - Python SDK

### Configuration

- **python-dotenv** - Environment variable management

---

## 📂 File Structure

```
Text-summarizer/
│
├── main.py                          # FastAPI app & routes
│   ├── FastAPI instance
│   ├── Pydantic request models
│   ├── API endpoints
│   └── Server initialization
│
├── services/
│   ├── __init__.py
│   └── summarize_service.py         # Gemini integration
│       ├── SummarizeService class
│       ├── summarize_text()
│       ├── summarize_with_context()
│       └── extract_key_points()
│
├── .env                             # API keys (gitignored)
├── requirements.txt                 # Python dependencies
├── test_api.py                      # Test suite
└── sample_texts.py                  # Sample data
```

---

## 🔐 Security

### API Key Protection

- Stored in `.env` file
- `.env` in `.gitignore`
- Loaded via `python-dotenv`
- Never hardcoded in source

### Input Validation

- Pydantic models validate all inputs
- Min/max length constraints
- Type checking
- Enum for style choices

---

## 🎨 Design Patterns

### 1. **Service Layer Pattern**

Separates business logic from API routes

- `main.py` = presentation layer
- `services/` = business logic layer

### 2. **Dependency Injection**

Service instance created once, reused for all requests

```python
summarizer = SummarizeService()  # Singleton-like
```

### 3. **Configuration Management**

Environment-based configuration

- Dev: `gemini-1.5-flash` (fast, free)
- Prod: `gemini-1.5-pro` (higher quality)

---

## 🚀 Key Features

### Multiple Summarization Styles

- **Concise** - 2-3 sentences
- **Detailed** - Comprehensive summary
- **Bullet** - Key points list

Implemented via prompt engineering:

```python
style_prompts = {
    "concise": "Provide a brief, concise summary in 2-3 sentences.",
    "detailed": "Provide a comprehensive summary...",
    "bullet": "Summarize the main points in bullet point format."
}
```

### Temperature Control

Controls randomness/creativity (0.0 - 2.0):

- **0.0-0.3** - Focused, deterministic
- **0.7-1.0** - Balanced (default)
- **1.5-2.0** - Creative, varied

### Token Management

`max_tokens` parameter controls output length:

- Concise: 100-150 tokens
- Detailed: 200-300 tokens
- Key points: 200-300 tokens

---

## 📈 Scalability Considerations

### Current Architecture

- Synchronous request handling
- Single Gemini model instance
- No caching

### Future Enhancements

1. **Async Processing** - Handle concurrent requests
2. **Caching** - Redis for repeated summaries
3. **Rate Limiting** - Prevent API abuse
4. **Batch Processing** - Summarize multiple texts
5. **Database** - Store summaries for history

---

## 🧪 Testing Strategy

### Manual Testing

- Interactive docs: `/docs`
- Test script: `test_api.py`
- Sample data: `sample_texts.py`

### Test Coverage

- All 3 endpoints
- Multiple styles
- Different contexts
- Error handling

---

## 💡 Prompt Engineering

### System Design

Each endpoint uses tailored prompts:

**Basic Summarization:**

```
"Provide a {style} summary.\n\nSummarize: {text}"
```

**Context-Aware:**

```
"Summarize for: {context}\n\n{text}"
```

**Key Points:**

```
"Extract exactly {num} key points. Format as numbered list.\n\n{text}"
```

### Best Practices

- Clear, specific instructions
- Examples when needed
- Temperature tuning per use case
- Token limits to control cost/length

---

## 🔄 Error Handling

### Service Layer

```python
try:
    response = self.model.generate_content(...)
    return {"success": True, "summary": response.text}
except Exception as e:
    return {"success": False, "error": str(e)}
```

### API Layer

```python
if not result.get("success"):
    raise HTTPException(status_code=500, detail=result.get("error"))
```

---

## 📊 API Response Format

### Success Response

```json
{
  "success": true,
  "summary": "The generated summary text...",
  "model": "gemini-1.5-flash",
  "style": "concise"
}
```

### Error Response

```json
{
  "detail": "Error message here"
}
```

---

## 🎯 Learning Outcomes

This architecture demonstrates:

✅ **Clean separation** - API vs Business Logic  
✅ **Type safety** - Pydantic validation  
✅ **Environment config** - .env pattern  
✅ **Error handling** - Try/except with user-friendly messages  
✅ **API design** - RESTful endpoints  
✅ **LLM integration** - Gemini SDK usage  
✅ **Prompt engineering** - Different styles via prompts

---

## 🔗 External Dependencies

### Google Gemini API

- **Endpoint:** Google AI Studio
- **Authentication:** API Key
- **Rate Limits:** 60 requests/minute (free tier)
- **Models:** gemini-1.5-flash, gemini-1.5-pro

### FastAPI Auto-Docs

- **Swagger UI:** `/docs`
- **ReDoc:** `/redoc`
- Auto-generated from code

---

**Simple, scalable, and production-ready! 🚀**
