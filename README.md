# Autonomous Insurance Claims Processing Agent

## Overview

This project implements a lightweight autonomous agent that processes FNOL (First Notice of Loss) documents and automatically:

- Extracts key insurance claim fields  
- Identifies missing mandatory data  
- Classifies claims  
- Routes claims to the correct workflow  
- Provides reasoning for routing decisions  

The solution is designed around ACORD-style automobile FNOL forms and simulates a real-world insurance intake pipeline.

---

## Features

- PDF FNOL text extraction  
- Rule-based field parsing  
- Mandatory field validation  
- Automated claim routing  
- Structured JSON output  
- Simple and extensible Python architecture  

---

## Architecture
FNOL PDF
↓
PDF Text Extraction (pdfplumber)
↓
Regex Field Parser
↓
Missing Field Validator
↓
Routing Engine
↓
JSON Output


---

## Tech Stack

- Python 3.10+
- pdfplumber
- Regex (re)
- JSON

---

## Project Structure

fnol-agent/
│
├── main.py
├── sample_fnol.pdf
└── README.md


---

## Installation

### Clone Repository

bash
git clone https://github.com/yourusername/fnol-agent.git
cd fnol-agent

## Install Dependencies
pip install pdfplumber


## Running the Agent
Place your FNOL PDF in the project directory (default: sample_fnol.pdf).

Run:
python main.py

## Sample Output
{
  "extractedFields": {
    "policy_number": "abc123",
    "policyholder": "john doe",
    "date_of_loss": "01/12/2025",
    "location": "pune",
    "description": "rear collision",
    "estimated_damage": "18000",
    "claim_type": "vehicle"
  },
  "missingFields": [],
  "recommendedRoute": "Fast-track",
  "reasoning": "Low value claim"
}

## Routing Rules
Condition	                                      Route
Estimated damage < 25,000	                    Fast-track
Mandatory fields missing	                    Manual Review
Keywords: fraud / staged / inconsistent	      Investigation Flag
Claim type = injury	                          Specialist Queue


## Priority:

Investigation → Specialist → Manual → Fast-track

## Approach

Extract text from FNOL PDF
Parse required fields using regex
Validate mandatory fields
Apply rule-based routing
Output structured JSON

## Future Enhancements

LLM-powered extraction
OCR support for scanned PDFs
Confidence scoring
ML-based fraud detection
REST API (FastAPI)
Web dashboard
Docker deployment

License
MIT

Author
Saurav Singh
