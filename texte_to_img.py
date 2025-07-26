from diffusers import StableDiffusionPipeline
import torch

# Charge le modèle avec précision float16 (GPU requis)


# Envoie le modèle sur le GPU si disponible
device = "cuda" if torch.cuda.is_available() else "cpu" 
pipe = pipe.to(device)

# Prompt texte
prompt = "a 25-year-old Asian man looking stressed while sitting on the toilet"

# Génère l’image
with torch.autocast("cuda"):
    image = pipe(prompt).images[0]

# Sauvegarde
image.save("sortie.png")
print("✅ Image générée et sauvegardée dans sortie.png")
