# config.py
# Central configuration for enabling/disabling reviews
from dotenv import load_dotenv
load_dotenv()

ENABLED_REVIEWS = {
    "LOGIC": True,
    "EDGE": True,
    "PERFORMANCE": False,
    "READABILITY": True,
}
