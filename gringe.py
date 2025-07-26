from transformers import pipeline

# Pipeline d'analyse de sentiment
analyzer = pipeline("sentiment-analysis")

# Liste de mots ou patterns cringe (tu peux enrichir ça)
cringe_keywords = ["bébé", "je peux avoir ton snap", "tu fais quoi de beau", "t ki", "cc", "tu dors ?","baby", "bae", "mon roi", "ma queen", "trop mimi", "l’amour de ma vie", 
    "mon soleil", "forever and always", "âmes sœurs", "mon petit cœur","sava"]

def cringe_score(phrase, analyzer, cringe_keywords):
    sentiment = analyzer(phrase)[0]
    score = 0.0
    max_score = 5.0  # Score maximal possible pour normaliser ensuite

    # Bonus de cringe si c’est TROP positif de manière non naturelle
    if sentiment['label'] == 'POSITIVE' and sentiment['score'] > 0.95:
        score += 1.0

    # Chaque mot-clé cringe ajoute 2 points (évite les répétitions inutiles)
    for mot in cringe_keywords:
        if mot.lower() in phrase.lower():
            score += 2.0

    # On plafonne à max_score pour éviter un taux > 1
    taux = min(score / max_score, 1.0)

    return round(taux, 2)


def commentaire_cringe(taux):
    if taux >= 0.8:
        return " Cringe absolu, c’est trop."
    elif taux >= 0.5:
        return " Un peu trop mielleux, fais gaffe."
    elif taux >= 0.2:
        return " Doux mais supportable."
    else:
        return " Rien de cringe, tu gères."


def detect_cringe(phrase):
     sentiment = analyzer(phrase)[0]
     score = 0.0
     max_score = 5.0  # Score maximal possible pour normaliser ensuite

    # Bonus de cringe si c’est TROP positif de manière non naturelle
     if sentiment['label'] == 'POSITIVE' and sentiment['score'] > 0.95:
        score += 1.0

    # Chaque mot-clé cringe ajoute 2 points (évite les répétitions inutiles)
     for mot in cringe_keywords:
        if mot.lower() in phrase.lower():
            score += 2.0
    
     return commentaire_cringe(score)


# Test
if __name__=="__main__":
    print(detect_cringe("bien ou quoi"))
    print(detect_cringe("Salut"))
