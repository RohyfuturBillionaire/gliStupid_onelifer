from flask import Flask, request, jsonify
from flask_cors import CORS

from disquettes import get_disquette_random


app = Flask(__name__)
CORS(app)  

# @app.route('/test', methods=['POST'])
# def test():
#     data = request.get_json()
#     print("Données reçues :", data)
#     return jsonify({
#         "message": "Message reçu avec succès depuis le backend !",
#         "status": "success"
#     })

# test
@app.route('/test', methods=['GET'])
def test_get():
    return jsonify({
        "message": "Test",
        "status": "success"
    })


# disquette
@app.route("/disquette", methods=["GET"])
def disquette():
    result = get_disquette_random()
    return jsonify(result)

@app.route("/analyze", methods=["POST"])
def analyze():
    if "image" not in request.files:
        return jsonify({"error": "Aucune image fournie"}), 400

    image = request.files["image"]
    if image.filename == "":
        return jsonify({"error": "Nom de fichier vide"}), 400

    # Sauvegarde temporairement l’image
    filename = secure_filename(image.filename)
    filepath = os.path.join("uploads", filename)
    os.makedirs("uploads", exist_ok=True)
    image.save(filepath)

    # Analyse de l’image avec DeepFace
    result = analyze_face(filepath)

    return jsonify(result)

@app.route("/texte", methods=["POST"])
def recevoir_texte():
    data = request.get_json()
    texte = data.get("message")

    if not texte:
        return jsonify({"error": "Aucun texte fourni"}), 400

    # Traitement du texte
    print(f"Texte reçu : {texte}")
    return jsonify({"reponse": f"Tu as envoyé : {texte}"}), 200



# port par defaut 5000
# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

