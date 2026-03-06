#!/usr/bin/env python
import sys
import warnings
from pathlib import Path

from dotenv import load_dotenv
from datetime import datetime

from debate.crew import Debate

# Load .env from workspace root
load_dotenv(Path(__file__).resolve().parents[4] / ".env")

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'motion': 'There needs to be strict laws to regulate LLMs',
    }
    
    try:
        result = Debate().crew().kickoff(inputs=inputs)
        print(result.raw)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")