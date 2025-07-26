from flask import Flask, request, jsonify
from flask_cors import CORS
from disquette import get_random_disquette
from emotions import analyze_face
from outfit import comment_outfit
from gringe import detect_cringe
from werkzeug.utils import secure_filename
import os
from convert import convert_numpy

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
 
 
@app.route('/test', methods=['POST']) 
def test():     
    data = request.get_json()     
    print("Données reçues :", data)     
    return jsonify({"message": "Message reçu avec succès depuis le backend !","status": "success"})
# test
@app.route('/test', methods=['GET'])
def test_get():    
    return jsonify({"message": "Test","status": "success"    })

# disquette
@app.route("/disquette", methods=["GET"])
def disquette():    
    result = get_random_disquette()    
    return jsonify(result)



@app.route('/upload-photo', methods=['POST'])
def upload_photo():    
    if 'photo' not in request.files:        
        return jsonify({'error': 'Aucune photo reçue'}), 400
    photo = request.files['photo']    
    print(f"Nom du fichier : {photo.filename}")
    filename = secure_filename(photo.filename)    
    filepath = os.path.join("uploads", filename)    
    os.makedirs("uploads", exist_ok=True)    
    photo.save(filepath)
    # Analyse de l’image avec DeepFace    
    print(f"Photo sauvegardée à : {filepath}")    
    result = analyze_face(filepath)    
    print(f"Résultat de l'analyse : {result}")
    result_clean = convert_numpy(result)
    return jsonify(result_clean)


@app.route('/upload-outfit', methods=['POST'])
def upload_outfit():
    if 'photo' not in request.files:
        return jsonify({'error': 'Aucune photo reçue'}), 400

    photo = request.files['photo']
    print(f"Nom du fichier : {photo.filename}")
    filename = secure_filename(photo.filename)
    filepath = os.path.join("uploads", filename)
    os.makedirs("uploads", exist_ok=True)
    photo.save(filepath)

    print(f"Photo sauvegardée à : {filepath}")
    result = comment_outfit(filepath)
    print(f"Résultat de l'analyse : {result}")
    result_clean = convert_numpy(result)
    return jsonify(result_clean)


# @app.route("/texte", methods=["POST"])
# def recevoir_texte():    
#        data = request.get_json()    
#        texte = data.get("message")
#        if not texte:        
#         return jsonify({"error": "Aucun texte fourni"}), 400
        
#        print(f"Texte reçu : {texte}") 
#        return jsonify({"reponse": f"Tu as envoyé : {texte}"}), 200

# # teste
# @app.route("/testPost", methods=["POST"])
# def recevoir_texte2():    
#      data = request.get_json()    
#      texte = data.get("message")
#      if not texte:        
#         return jsonify({"error": "Aucun texte fourni"}), 400
#     # Traitement du texte    
#      print(f"Texte reçu : {texte}")    
#      return jsonify({"reponse": f"Tu as envoyé : {texte}"}), 200


@app.route("/cringe", methods=["POST"])
def detect_cringe_route():
    data = request.get_json()
    texte = data.get("message")
    if not texte:
        return jsonify({"error": "Aucun texte fourni"}), 400
    print(f"Texte reçu : {texte}")
    reponse=detect_cringe(texte)
    return jsonify({"reponse": f"Tu as envoyé : {reponse}"}), 200

# port par defaut 5000# 
# if __name__ == '__main__':#     app.run(debug=True)
if __name__ == '__main__':    
    app.run(debug=True, host='0.0.0.0')

