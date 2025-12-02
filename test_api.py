"""
Test script for AI Text Summarizer API
Run this after starting the server to test all endpoints
"""

import requests
import json
from typing import Dict, Any


API_URL = "http://localhost:8000"


def print_response(title: str, response: Dict[Any, Any]):
    """Pretty print API response"""
    print("\n" + "="*70)
    print(f"📊 {title}")
    print("="*70)
    print(json.dumps(response, indent=2))
    print("="*70 + "\n")


def test_health_check():
    """Test the health check endpoint"""
    print("🔍 Testing Health Check...")
    response = requests.get(f"{API_URL}/health")
    print_response("Health Check", response.json())


def test_basic_summarization():
    """Test basic text summarization"""
    print("🔍 Testing Basic Summarization (Concise Style)...")
    
    text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to 
    the natural intelligence displayed by humans and animals. Leading AI textbooks define 
    the field as the study of intelligent agents: any device that perceives its environment 
    and takes actions that maximize its chance of successfully achieving its goals. 
    Colloquially, the term "artificial intelligence" is often used to describe machines 
    (or computers) that mimic "cognitive" functions that humans associate with the human 
    mind, such as "learning" and "problem solving".
    """
    
    response = requests.post(
        f"{API_URL}/summarize",
        json={
            "text": text.strip(),
            "style": "concise",
            "max_tokens": 150,
            "temperature": 0.7
        }
    )
    print_response("Concise Summary", response.json())


def test_bullet_summarization():
    """Test bullet point summarization"""
    print("🔍 Testing Bullet Point Summarization...")
    
    text = """
    Climate change refers to long-term shifts in temperatures and weather patterns. 
    These shifts may be natural, such as through variations in the solar cycle. 
    But since the 1800s, human activities have been the main driver of climate change, 
    primarily due to burning fossil fuels like coal, oil and gas. Burning fossil fuels 
    generates greenhouse gas emissions that act like a blanket wrapped around the Earth, 
    trapping the sun's heat and raising temperatures. Examples of greenhouse gas emissions 
    that are causing climate change include carbon dioxide and methane.
    """
    
    response = requests.post(
        f"{API_URL}/summarize",
        json={
            "text": text.strip(),
            "style": "bullet",
            "max_tokens": 200,
            "temperature": 0.5
        }
    )
    print_response("Bullet Points Summary", response.json())


def test_context_summarization():
    """Test context-aware summarization"""
    print("🔍 Testing Context-Aware Summarization...")
    
    text = """
    Quantum computing is a type of computation that harnesses the collective properties 
    of quantum states, such as superposition, interference, and entanglement, to perform 
    calculations. The devices that perform quantum computations are known as quantum 
    computers. Though current quantum computers are too small to outperform usual 
    (classical) computers for practical applications, they are believed to be capable 
    of solving certain computational problems, such as integer factorization, 
    substantially faster than classical computers.
    """
    
    # Test 1: For a 5-year-old
    response1 = requests.post(
        f"{API_URL}/summarize/context",
        json={
            "text": text.strip(),
            "context": "for a 5-year-old child",
            "max_tokens": 150
        }
    )
    print_response("Summary for a 5-year-old", response1.json())
    
    # Test 2: For technical audience
    response2 = requests.post(
        f"{API_URL}/summarize/context",
        json={
            "text": text.strip(),
            "context": "technical audience with computer science background",
            "max_tokens": 200
        }
    )
    print_response("Summary for Technical Audience", response2.json())


def test_key_points_extraction():
    """Test key points extraction"""
    print("🔍 Testing Key Points Extraction...")
    
    text = """
    Machine learning (ML) is a field of inquiry devoted to understanding and building 
    methods that 'learn', that is, methods that leverage data to improve performance 
    on some set of tasks. It is seen as a part of artificial intelligence. Machine 
    learning algorithms build a model based on sample data, known as training data, 
    in order to make predictions or decisions without being explicitly programmed to 
    do so. Machine learning algorithms are used in a wide variety of applications, 
    such as in medicine, email filtering, speech recognition, and computer vision, 
    where it is difficult or unfeasible to develop conventional algorithms to perform 
    the needed tasks.
    """
    
    response = requests.post(
        f"{API_URL}/summarize/keypoints",
        json={
            "text": text.strip(),
            "num_points": 5
        }
    )
    print_response("Key Points (Top 5)", response.json())


def test_detailed_summarization():
    """Test detailed summarization"""
    print("🔍 Testing Detailed Summarization...")
    
    text = """
    The Internet of Things (IoT) describes physical objects (or groups of such objects) 
    with sensors, processing ability, software and other technologies that connect and 
    exchange data with other devices and systems over the Internet or other communications 
    networks. Internet of Things has been considered a misnomer because devices do not 
    need to be connected to the public internet, they only need to be connected to a 
    network and be individually addressable. The field has evolved due to the convergence 
    of multiple technologies, including ubiquitous computing, commodity sensors, 
    increasingly powerful embedded systems, and machine learning. Traditional fields of 
    embedded systems, wireless sensor networks, control systems, automation (including 
    home and building automation), independently and collectively enable the Internet of Things.
    """
    
    response = requests.post(
        f"{API_URL}/summarize",
        json={
            "text": text.strip(),
            "style": "detailed",
            "max_tokens": 300,
            "temperature": 0.7
        }
    )
    print_response("Detailed Summary", response.json())


def run_all_tests():
    """Run all test cases"""
    print("\n" + "🚀 " + "="*68)
    print("🤖 AI TEXT SUMMARIZER API - TEST SUITE")
    print("="*70)
    
    try:
        # Test if server is running
        test_health_check()
        
        # Run all tests
        test_basic_summarization()
        test_bullet_summarization()
        test_detailed_summarization()
        test_context_summarization()
        test_key_points_extraction()
        
        print("\n✅ All tests completed successfully!")
        print("="*70 + "\n")
        
    except requests.exceptions.ConnectionError:
        print("\n❌ ERROR: Cannot connect to API server!")
        print("Make sure the server is running with: python main.py")
        print("="*70 + "\n")
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        print("="*70 + "\n")


if __name__ == "__main__":
    run_all_tests()
