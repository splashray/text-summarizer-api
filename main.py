"""
AI Text Summarizer API
A FastAPI application that provides text summarization using Google Gemini
"""

# Fix for Python 3.14 compatibility (only needed for Python 3.14+)
import sys
if sys.version_info >= (3, 14):
    import py314_fix

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Literal
from services.summarize_service import SummarizeService
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="AI Text Summarizer API",
    description="Summarize text using Google Gemini with various styles and options",
    version="1.0.0"
)

# Initialize summarization service
summarizer = SummarizeService()


# Request Models
class SummarizeRequest(BaseModel):
    """Request model for basic text summarization"""
    text: str = Field(..., min_length=10, description="The text to summarize (minimum 10 characters)")
    style: Literal["concise", "detailed", "bullet"] = Field(
        default="concise",
        description="Summarization style: concise (2-3 sentences), detailed (comprehensive), or bullet (key points)"
    )
    max_tokens: int = Field(
        default=150,
        ge=50,
        le=1000,
        description="Maximum tokens in the summary (50-1000)"
    )
    temperature: float = Field(
        default=0.7,
        ge=0.0,
        le=2.0,
        description="Creativity level (0.0-2.0, lower = more focused)"
    )


class ContextSummarizeRequest(BaseModel):
    """Request model for context-aware summarization"""
    text: str = Field(..., min_length=10)
    context: str = Field(
        ...,
        description="Context for summarization (e.g., 'for a 5-year-old', 'technical audience', 'executive summary')"
    )
    max_tokens: int = Field(default=200, ge=50, le=1000)


class KeyPointsRequest(BaseModel):
    """Request model for extracting key points"""
    text: str = Field(..., min_length=10)
    num_points: int = Field(
        default=5,
        ge=1,
        le=10,
        description="Number of key points to extract (1-10)"
    )


# API Endpoints
@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Welcome to AI Text Summarizer API",
        "version": "1.0.0",
        "endpoints": {
            "POST /summarize": "Basic text summarization with style options",
            "POST /summarize/context": "Context-aware summarization",
            "POST /summarize/keypoints": "Extract key points from text",
            "GET /health": "Health check endpoint"
        },
        "documentation": "/docs"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "AI Text Summarizer API"
    }


@app.post("/summarize")
async def summarize_text(request: SummarizeRequest):
    """
    Summarize text with specified style
    
    - **text**: The text to summarize (minimum 10 characters)
    - **style**: 'concise' (2-3 sentences), 'detailed' (comprehensive), or 'bullet' (key points)
    - **max_tokens**: Maximum length of summary (50-1000 tokens)
    - **temperature**: Creativity level (0.0 = focused, 2.0 = creative)
    """
    
    result = summarizer.summarize_text(
        text=request.text,
        style=request.style,
        max_tokens=request.max_tokens,
        temperature=request.temperature
    )
    
    if not result.get("success"):
        raise HTTPException(
            status_code=500,
            detail=f"Summarization failed: {result.get('error')}"
        )
    
    return result


@app.post("/summarize/context")
async def summarize_with_context(request: ContextSummarizeRequest):
    """
    Summarize text with specific context
    
    - **text**: The text to summarize
    - **context**: Target audience or style (e.g., "for a 5-year-old", "technical audience", "executive summary")
    - **max_tokens**: Maximum length of summary
    
    Examples of context:
    - "for a 5-year-old" - Simple, easy-to-understand language
    - "technical audience" - Include technical details and jargon
    - "executive summary" - Brief, business-focused summary
    - "social media post" - Short, engaging format
    """
    
    result = summarizer.summarize_with_context(
        text=request.text,
        context=request.context,
        max_tokens=request.max_tokens
    )
    
    if not result.get("success"):
        raise HTTPException(
            status_code=500,
            detail=f"Summarization failed: {result.get('error')}"
        )
    
    return result


@app.post("/summarize/keypoints")
async def extract_key_points(request: KeyPointsRequest):
    """
    Extract key points from text
    
    - **text**: The text to analyze
    - **num_points**: Number of key points to extract (1-10)
    
    Returns a numbered list of the most important points from the text
    """
    
    result = summarizer.extract_key_points(
        text=request.text,
        num_points=request.num_points
    )
    
    if not result.get("success"):
        raise HTTPException(
            status_code=500,
            detail=f"Key point extraction failed: {result.get('error')}"
        )
    
    return result


# Run the application
if __name__ == "__main__":
    import os
    
    # Use PORT from environment (Render sets this) or default to 8000 for local dev
    port = int(os.environ.get("PORT", 8000))
    
    # Disable reload in production (when PORT env var is set)
    is_production = "PORT" in os.environ
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=not is_production  # Auto-reload only in development
    )
