# 🚀 Deploy to Render - Complete Guide

## Overview

Render is a free cloud platform where you can host your API. This guide will walk you through every step.

---

## 📋 Prerequisites

Before you start:

- ✅ GitHub account (create at github.com if you don't have one)
- ✅ Render account (sign up at render.com - it's FREE)
- ✅ Your Gemini API key (you already have this: )
- ✅ All your project files working locally

---

## 🔧 Step 1: Prepare Your Project for Deployment

### 1.1 Create a `.python-version` file

This tells Render which Python version to use (we'll use 3.11 instead of 3.14 for better compatibility).

**Create file:** `.python-version`

```
3.11.7
```

**How to create it:**

```powershell
# In VS Code, create a new file named .python-version
# Add just this one line: 3.11.7
```

### 1.2 Update `requirements.txt`

**Make sure your `requirements.txt` looks like this:**

```txt
google-generativeai==0.8.5
python-dotenv==1.2.1
fastapi==0.123.0
uvicorn[standard]==0.38.0
```

**Note:** Added `[standard]` to uvicorn - this includes extra features needed for production.

### 1.3 Create a `render.yaml` file (Optional but Recommended)

This file tells Render how to build and run your app.

**Create file:** `render.yaml`

```yaml
services:
  - type: web
    name: text-summarizer-api
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.7
      - key: GEMINI_API_KEY
        sync: false
      - key: GEMINI_MODEL
        value: gemini-2.0-flash-exp
```

### 1.4 Remove the `py314_fix.py` dependency

Since we're using Python 3.11 on Render (not 3.14), we need to make the fix optional.

**Edit `main.py`:** Change line 7 to:

```python
# Import Python 3.14 fix only if on 3.14
import sys
if sys.version_info >= (3, 14):
    import py314_fix
```

### 1.5 Update the server startup command

**Edit `main.py`:** Change the last section (around line 170) to:

```python
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))  # Use Render's port or 8000
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=False  # Don't use reload in production
    )
```

---

## 🐙 Step 2: Push Your Code to GitHub

### 2.1 Initialize Git (if not already done)

```powershell
# Navigate to your project folder
cd C:\Users\Splashray-Tayo\Documents\Ai-Automation\Text-summarizer

# Initialize git
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: AI Text Summarizer API"
```

### 2.2 Create GitHub Repository

1. Go to https://github.com
2. Click the **"+"** icon (top right)
3. Select **"New repository"**
4. **Repository name:** `text-summarizer-api`
5. **Description:** "AI-powered text summarizer using Google Gemini"
6. **Visibility:** Choose Public or Private (free tier works with both)
7. **DO NOT** check "Initialize with README" (you already have files)
8. Click **"Create repository"**

### 2.3 Push Your Code

GitHub will show you commands like this:

```powershell
# Add the GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/text-summarizer-api.git

# Push your code
git branch -M main
git push -u origin main
```

**Replace `YOUR_USERNAME`** with your actual GitHub username.

### 2.4 Verify Upload

- Refresh your GitHub repository page
- You should see all your files (main.py, requirements.txt, etc.)
- ✅ Make sure `.env` is **NOT** there (it's protected by `.gitignore`)

---

## ☁️ Step 3: Deploy to Render

### 3.1 Sign Up for Render

1. Go to https://render.com
2. Click **"Get Started"**
3. Sign up with **GitHub** (easiest option)
4. Authorize Render to access your GitHub repositories

### 3.2 Create a New Web Service

1. On Render dashboard, click **"New +"**
2. Select **"Web Service"**
3. Choose **"Build and deploy from a Git repository"**
4. Click **"Connect account"** if needed
5. Find your repository: `text-summarizer-api`
6. Click **"Connect"**

### 3.3 Configure Your Service

Fill in these settings:

| Setting            | Value                                          | Notes                           |
| ------------------ | ---------------------------------------------- | ------------------------------- |
| **Name**           | `text-summarizer-api`                          | This becomes your URL subdomain |
| **Region**         | Oregon (US West)                               | Or closest to you               |
| **Branch**         | `main`                                         | Your main branch                |
| **Root Directory** | (leave blank)                                  | Files are at root               |
| **Runtime**        | Python 3                                       | Auto-detected                   |
| **Build Command**  | `pip install -r requirements.txt`              | Installs packages               |
| **Start Command**  | `uvicorn main:app --host 0.0.0.0 --port $PORT` | Starts server                   |
| **Instance Type**  | Free                                           | $0/month                        |

### 3.4 Add Environment Variables

**CRITICAL:** Scroll down to **"Environment Variables"**

Click **"Add Environment Variable"** and add these:

| Key              | Value                  |
| ---------------- | ---------------------- |
| `GEMINI_API_KEY` | ``                     |
| `GEMINI_MODEL`   | `gemini-2.0-flash-exp` |
| `PYTHON_VERSION` | `3.11.7`               |

**Why:** Render doesn't have access to your `.env` file (which is good for security!). You must manually add these secrets.

### 3.5 Deploy!

1. Click **"Create Web Service"** at the bottom
2. Render will now:
   - Clone your GitHub repo
   - Install Python 3.11
   - Run `pip install -r requirements.txt`
   - Start your server with `uvicorn main:app...`

**This takes 2-5 minutes.**

### 3.6 Monitor the Deployment

You'll see a live log that looks like this:

```
==> Cloning from https://github.com/YOUR_USERNAME/text-summarizer-api...
==> Downloading Python 3.11.7...
==> Installing dependencies...
Successfully installed fastapi-0.123.0 uvicorn-0.38.0...
==> Starting service...
INFO:     Application startup complete.
==> Your service is live 🎉
```

---

## ✅ Step 4: Test Your Deployed API

### 4.1 Get Your API URL

After deployment succeeds, Render gives you a URL like:

```
https://text-summarizer-api.onrender.com
```

### 4.2 Test in Browser

Visit:

```
https://text-summarizer-api.onrender.com
```

You should see:

```json
{
  "message": "Welcome to the AI Text Summarizer API",
  "endpoints": {...}
}
```

### 4.3 Access API Documentation

Visit:

```
https://text-summarizer-api.onrender.com/docs
```

You'll see the **Swagger UI** - same as localhost, but now on the internet! 🌍

### 4.4 Test Summarization

In the Swagger UI:

1. Click **POST /summarize**
2. Click **"Try it out"**
3. Enter this JSON:

```json
{
  "text": "Artificial intelligence is intelligence demonstrated by machines. It includes learning, reasoning, and problem-solving capabilities.",
  "style": "concise",
  "max_tokens": 150,
  "temperature": 0.7
}
```

4. Click **"Execute"**
5. You should get a summary! ✅

---

## 🔒 Step 5: Security Best Practices

### 5.1 Protect Your API Key

- ✅ Never commit `.env` to GitHub
- ✅ Only add secrets via Render's dashboard
- ✅ Regenerate API keys if accidentally exposed

### 5.2 Monitor Usage

- Check Render logs: Dashboard → Your Service → Logs
- Monitor Gemini usage: https://aistudio.google.com/app/apikey
- Free tier limits: 60 requests/minute

---

## 🎯 Step 6: Make Updates

When you change your code:

```powershell
# 1. Make changes to your files
# 2. Commit changes
git add .
git commit -m "Describe what you changed"

# 3. Push to GitHub
git push

# 4. Render auto-deploys! ✨
```

Render watches your GitHub repo and **automatically redeploys** when you push!

---

## 🐛 Troubleshooting

### Problem: Build fails with "Module not found"

**Solution:** Check `requirements.txt` includes all packages

### Problem: Server starts but returns 500 errors

**Solution:**

- Check Render logs for errors
- Verify environment variables are set correctly
- Make sure `GEMINI_API_KEY` is valid

### Problem: "Application startup failed"

**Solution:**

- Check start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- Verify `main.py` doesn't have syntax errors
- Check Render logs for specific error

### Problem: Slow first request after inactivity

**Explanation:** Free tier "spins down" after 15 minutes of no requests. First request after that takes ~30 seconds to wake up. This is normal for free tier.

**Solution:** Upgrade to paid tier ($7/month) for always-on service.

---

## 📊 Free Tier Limits

| Resource          | Limit                   |
| ----------------- | ----------------------- |
| **RAM**           | 512 MB                  |
| **CPU**           | Shared                  |
| **Bandwidth**     | 100 GB/month            |
| **Build minutes** | 500/month               |
| **Spin-down**     | After 15 min inactivity |

**For learning:** Free tier is PERFECT! ✅

---

## 🎉 Success Checklist

- ✅ Code pushed to GitHub
- ✅ Render service created
- ✅ Environment variables set
- ✅ Deployment succeeded (green checkmark)
- ✅ API accessible at https://your-app.onrender.com
- ✅ `/docs` shows Swagger UI
- ✅ Can summarize text via API

---

## 🔗 Your Deployed API Endpoints

Once deployed, share these URLs:

```
Base URL: https://text-summarizer-api.onrender.com

📖 Documentation: /docs
❤️  Health Check:  /health
✍️  Summarize:     POST /summarize
🎯 With Context:   POST /summarize/context
🔑 Key Points:     POST /summarize/keypoints
```

---

## 💡 Next Steps

1. **Share your API:** Send the URL to friends/portfolio
2. **Monitor logs:** Check for errors or high usage
3. **Add features:** New endpoints, different AI models
4. **Set up custom domain:** (Optional, requires paid plan)
5. **Add rate limiting:** Prevent abuse
6. **Add analytics:** Track usage statistics

---

## 📞 Support Resources

- **Render Docs:** https://render.com/docs
- **Render Community:** https://community.render.com
- **FastAPI Docs:** https://fastapi.tiangolo.com
- **Gemini API Docs:** https://ai.google.dev/docs

---

**You're now a deployed developer! 🚀**
