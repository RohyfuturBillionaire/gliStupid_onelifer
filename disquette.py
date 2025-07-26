import random

def generer_disquettes():
    return [
        "T’as pas une carte ? Je me perds dans ton regard.",
        "Excuse-moi, t’as un pansement ? Je me suis blessé en tombant amoureux.",
        "Tu brilles plus que mon écran à 100% de luminosité.",
        "T’es pas Google, mais t’as tout ce que je recherche.",
        "Ton père est un voleur ? Il a volé les étoiles pour les mettre dans tes yeux.",
        "Tu dois être une mise à jour, parce que mon cœur bug depuis que je t’ai vue.",
        "Ton sourire éclaire ma journée plus que le soleil.",
        "Je ne suis pas photographe, mais je peux nous voir ensemble.",
        "Si la beauté était un crime, tu serais en prison à vie.",
        "Tu dois être une chanson, parce que tu restes dans ma tête toute la journée.",
        "T’as une carte mémoire ? Car j’aimerais sauvegarder nos souvenirs.",
        "Je dois être en train de rêver, ou alors t’es vraiment réelle ?",
        "Tu dois être une app, parce que je veux te lancer tous les jours.",
        "Je t’écrirais bien une poésie, mais je suis trop occupé à t’admirer.",
        "T’as pas un câble ? Mon cœur est à plat sans toi.",
        "Tu dois être un bug, parce que tu fais tout planter chez moi.",
        "Je ne suis pas électricien, mais j’ai ressenti une étincelle.",
        "T’as volé mon attention comme un hacker.",
        "T’es comme une mise à jour : inattendue, mais indispensable.",
        "T’as un mot de passe ? Car je veux accéder à ton cœur.",
        "Je ne suis pas une IA, mais je suis programmé pour t’aimer.",
        "J’ai beau swiper, c’est toi que je veux matcher.",
        "T’as un plan ou t’es venue comme ça, divine ?",
        "T’as les clés de mon cœur dans ton trousseau ?",
        "T’es pas une notification, mais tu me rends heureux d’un coup.",
        "Ton rire est ma sonnerie préférée.",
        "Tu m’as mis en mode avion, je plane.",
        "T’es le bug que je veux pas corriger.",
        "Tu dois être rare comme une PS5 en stock.",
        "J’ai pas besoin d’algorithme, c’est toi la solution.",
        "T’es comme un cheat code, tu rends ma vie plus facile.",
        "T’as le Wi-Fi ? Parce que je ressens une connexion.",
        "Même mes AirPods tombent amoureux de ta voix.",
        "T’es comme un cookie, tu rends tout plus sucré.",
        "Mon cœur t’a likée avant mes yeux.",
        "Je suis tombé amoureux, sans même scroller.",
        "Je suis pas un robot, mais j’ai été programmé pour te trouver.",
        "T’es pas dans ma To-Do, mais je veux passer ma journée avec toi.",
        "Si t’étais une app, t’aurais 5 étoiles.",
        "T’as un pare-feu ? Parce que j’ai chaud près de toi."
    ]


def get_random_disquette():
    index = random.randint(0, len(generer_disquettes()) - 1)
    return generer_disquettes()[index], index


# disquette, index = get_random_disquette()
# print(f"Disquette #{index + 1} : {disquette}")
