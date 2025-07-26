from transformers import pipeline

# Pipeline d'analyse de sentiment
analyzer = pipeline("sentiment-analysis")

# Liste de mots ou patterns cringe (tu peux enrichir ça)
cringe_keywords = ["bébé", "je peux avoir ton snap", "tu fais quoi de beau", "t ki", "cc", "tu dors ?"]

def detect_cringe(phrase):
    sentiment = analyzer(phrase)[0]
    score = 0
    
    # Si trop positif et cheesy → potentiel cringe
    if sentiment['label'] == 'POSITIVE' and sentiment['score'] > 0.95:
        score += 1
    
    # Check de mots cringe connus
    for mot in cringe_keywords:
        if mot in phrase.lower():
            score += 2
    
    if score >= 2:
        return "🟥 CRINGE"
    elif score == 1:
        return "🟨 Moyennement cringe"
    else:
        return "🟩 Confiant"

# Test
print(detect_cringe("Cc, t ki ? 😘"))
print(detect_cringe("Salut, j’ai adoré ton style dans ta bio"))
