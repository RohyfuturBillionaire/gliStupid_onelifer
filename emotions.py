# # from deepface import DeepFace

# # result = DeepFace.analyze(img_path="photo.jpg", actions=["age", "gender", "emotion", "race"])
# # print(result)
# import ssl
# import urllib3

# # Désactive la vérification SSL (dangereux pour la sécurité, à utiliser juste pour tests locaux)
# ssl._create_default_https_context = ssl._create_unverified_context
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# from deepface import DeepFace

# result = DeepFace.analyze(img_path="photo1.jpeg", actions=["age", "gender", "emotion", "race"])
# # result = DeepFace.analyze(img_path="photo.jpg", actions=["emotion"])
# print(result)
# import ssl
# import urllib3
# from deepface import DeepFace
# from logiqueCaca import envie_de_caca

# # Sécurité désactivée temporairement
# ssl._create_default_https_context = ssl._create_unverified_context
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# # Analyse avec DeepFace
# result = DeepFace.analyze(img_path="photo.jpg", actions=["emotion"])
# dominant_emotion = result[0]["dominant_emotion"]

# # Décision "humoristique"
# if envie_de_caca(dominant_emotion):
#     print(f"Dominant emotion: {dominant_emotion}  Envie de faire caca")
# else:
#     print(f"Dominant emotion: {dominant_emotion}  Pas envie de faire caca")

# # result = DeepFace.analyze(img_path="photo.jpg", actions=["age", "gender", "emotion", "race"])
# # envie, score = envie_de_caca(result)

# # print(f"Envie de faire caca ? {'Oui' if envie else 'Non'}, score: {score}")

import ssl
import urllib3
from deepface import DeepFace

# Désactive la vérification SSL (à éviter en prod)
ssl._create_default_https_context = ssl._create_unverified_context
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def traduire_emotion(emotion_en):
    traductions = {
        'angry': 'colère',
        'disgust': 'dégoût',
        'fear': 'peur',
        'happy': 'joie',
        'sad': 'tristesse',
        'surprise': 'surprise',
        'neutral': 'neutre'
    }
    return traductions.get(emotion_en.lower(), emotion_en)


def generer_commentaire(face_data):
    age = face_data['age']
    genre = face_data['dominant_gender']
    emotion = face_data['dominant_emotion']
    origine = face_data['dominant_race']

    # Réflexions positives sur les origines (sans les nommer explicitement)
    compliments_origine = {
        'asian': "Il y a souvent une forme de sagesse tranquille et de persévérance chez ceux qui viennent d’un héritage culturel aussi ancien.",
        'indian': "Certaines personnes issues de ce type d’héritage combinent naturellement profondeur spirituelle, intelligence et ambition.",
        'black': "Il y a une force créative et une résilience marquante chez ceux dont les racines sont aussi riches culturellement.",
        'white': "Ceux qui viennent de ce genre de parcours ont souvent une grande capacité d’adaptation et un esprit indépendant.",
        'middle eastern': "On retrouve souvent une fierté profonde et un lien fort à la famille dans les cultures de ce type.",
        'latino hispanic': "Beaucoup de personnes ayant un tel fond culturel rayonnent de chaleur, d’énergie et de joie de vivre contagieuse."
    }

    # Conseils selon l’émotion dominante
    conseils_emotion = {
        'angry': "La colère peut arriver, c’est humain — le tout, c’est de la canaliser intelligemment.",
        'disgust': "Si quelque chose te dégoûte en ce moment, c’est peut-être un signal qu’il faut changer ton environnement.",
        'fear': "La peur est souvent un indicateur de croissance — elle montre que tu sors de ta zone de confort.",
        'happy': "Tu rayonnes de bonheur — continue à transmettre cette lumière autour de toi.",
        'sad': "La tristesse ne veut pas dire faiblesse. Autorise-toi à la ressentir, mais n’oublie pas que tu peux te relever.",
        'surprise': "La surprise est un moteur de découverte. Accueille-la avec curiosité.",
        'neutral': "Rester calme et posé, c’est une force. Mais pense aussi à te reconnecter à ce que tu ressens vraiment."
    }
    gr=""
    # Conseils liés à l’âge
    if age < 18:
        conseil_age = "Tu es encore en train de te construire — prends le temps de découvrir ce qui te fait vibrer."
        clause_rizz = ""
    else:
        conseil_age = f"À {age} ans, tu es à un moment fort de ta vie — c’est le moment de bâtir, d’oser et de te réaliser."
        clause_rizz = "Et au passage… maintenant que tu es majeur·e : on ne drague plus les mineurs. Faut rester dans ta tranche d’âge 😌."
    if genre=="man": 
            gr='homme'
    else:
           gr='femme'
    # Construction du message
    commentaire = (
       
        f"Tu as l’air d’un·e {gr} de {age} ans avec une vraie présence. "
        f"{compliments_origine.get(origine, '')}\n\n"
        f"En ce moment, tu sembles ressentir de la {traduire_emotion(emotion)} — et c’est totalement légitime. "
        f"{conseils_emotion.get(emotion, '')}\n\n"
        f"{conseil_age}\n\n"
        f"{clause_rizz}"
    )

    return commentaire


def analyze_face(image_path):
    try:
        result = DeepFace.analyze(img_path=image_path, actions=["age", "gender", "emotion", "race"])
        return generer_commentaire(result[0])
    except Exception as e:
        return {"error": str(e)}
    
if __name__=="__main__":
    res=analyze_face("outfitTest.jpeg")
    print(res)

# print(analyze_face("photo.jpg"))
