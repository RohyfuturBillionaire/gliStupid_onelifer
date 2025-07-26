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

def analyze_face(image_path):
    try:
        result = DeepFace.analyze(img_path=image_path, actions=["age", "gender", "emotion", "race"])
        return result
    except Exception as e:
        return {"error": str(e)}

