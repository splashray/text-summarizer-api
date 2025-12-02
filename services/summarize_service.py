"""
Text Summarization Service using Google Gemini API
This service provides various summarization methods with different approaches
"""

import google.generativeai as genai
from typing import Literal
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class SummarizeService:
    """Service for summarizing text using Google Gemini models"""
    
    def __init__(self):
        """Initialize the Gemini client with API key from environment"""
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model_name = os.getenv("GEMINI_MODEL")
        self.model = genai.GenerativeModel(model_name)
        self.model_name = model_name
    
    def summarize_text(
        self,
        text: str,
        style: Literal["concise", "detailed", "bullet"] = "concise",
        max_tokens: int = 150,
        temperature: float = 0.7
    ) -> dict:
        """
        Summarize text using Google Gemini API
        
        Args:
            text: The text to summarize
            style: Summarization style - 'concise', 'detailed', or 'bullet'
            max_tokens: Maximum tokens in the summary (controls length)
            temperature: Creativity level (0.0-2.0, lower = more focused)
            
        Returns:
            dict: Contains 'summary' and 'model' information
        """
        
        # Create style-specific prompts
        style_prompts = {
            "concise": "Provide a brief, concise summary in 2-3 sentences.",
            "detailed": "Provide a comprehensive summary with key details and context.",
            "bullet": "Summarize the main points in bullet point format."
        }
        
        try:
            # Create prompt
            prompt = f"{style_prompts[style]}\n\nSummarize the following text:\n\n{text}"
            
            # Generate response
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=max_tokens,
                    temperature=temperature
                )
            )
            
            return {
                "success": True,
                "summary": response.text,
                "model": self.model_name,
                "style": style
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "summary": None
            }
    
    def summarize_with_context(
        self,
        text: str,
        context: str,
        max_tokens: int = 200
    ) -> dict:
        """
        Summarize text with additional context (e.g., "for a 5-year-old", "technical audience")
        
        Args:
            text: The text to summarize
            context: Additional context for summarization style
            max_tokens: Maximum tokens in the summary
            
        Returns:
            dict: Summary with metadata
        """
        
        try:
            prompt = f"Summarize the following text for: {context}\n\n{text}"
            
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=max_tokens,
                    temperature=0.7
                )
            )
            
            return {
                "success": True,
                "summary": response.text,
                "context": context,
                "model": self.model_name
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def extract_key_points(self, text: str, num_points: int = 5) -> dict:
        """
        Extract key points from text
        
        Args:
            text: The text to analyze
            num_points: Number of key points to extract
            
        Returns:
            dict: List of key points with metadata
        """
        
        try:
            prompt = f"Extract exactly {num_points} key points from the following text. Format as a numbered list.\n\n{text}"
            
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=300,
                    temperature=0.5
                )
            )
            
            return {
                "success": True,
                "key_points": response.text,
                "num_points_requested": num_points,
                "model": self.model_name
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
