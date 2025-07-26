import json

def envie_de_caca(dominant_emotion):
    """
    Retourne True ou False selon l'émotion dominante.
    C'est une logique humoristique basée sur des interprétations légères.
    """
    logique = {
        "angry": True,      # Trop de pression, intestins tendus
        "disgust": True,    # Peut signaler un besoin urgent
        "fear": True,       # Peur soudaine peut activer le transit
        "happy": False,     # Trop détendu
        "sad": True,        # Se vider soulage l’esprit
        "surprise": True,   # Surprise peut provenir de crampes inattendues
        "neutral": False    # Rien d'alarmant
    }
    return logique.get(dominant_emotion, False)


# def envie_de_caca(result):
#     emotion = result.get('dominant_emotion', '').lower()
#     age = result.get('age', 30)
#     gender = result.get('gender', '').lower()
    
#     # Base de score envie (0-10)
#     score = 5
    
#     # Emotion
#     if emotion in ['sad', 'angry', 'fear']:
#         score -= 3
#     elif emotion == 'surprise':
#         score -= 4
#     elif emotion in ['happy', 'neutral']:
#         score += 1
    
#     # Age influence
#     if age < 20:
#         score += 2
#     elif age > 50:
#         score -= 2
    
#     # Genre influence
#     if gender == 'man':
#         score += 1
#     elif gender == 'woman':
#         score -= 1
    
#     # Clamp score entre 0 et 10
#     score = max(0, min(score, 10))
    
#     # On décide que score >= 5 veut dire "envie de caca"
#     envie = score >= 5
    
#     return envie, score
