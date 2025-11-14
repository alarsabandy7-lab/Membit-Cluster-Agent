KEYWORDS = {
    "scam": 1.0,
    "fraud": 1.0,
    "hack": 0.9,
    "exploit": 0.9,
    "phish": 0.9,
    "airdrop": -0.6,
    "reward": -0.5
}

def local_score(text):
    t = text.lower()
    score = 0
    for k, w in KEYWORDS.items():
        if k in t:
            score += w
    return round(score, 2)
