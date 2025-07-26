from PIL import Image
from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("patrickjohncyh/fashion-clip")
processor = CLIPProcessor.from_pretrained("patrickjohncyh/fashion-clip")

def comment_outfit(image_path):
    image = Image.open(image_path).convert("RGB").resize((224,224))
    texts = [
       "casual streetwear",
       "tenue chic",
       "look élégant",
       "outfit raté résidu années 2000"
    ]
    inputs = processor(text=texts, images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    probs = outputs.logits_per_image.softmax(dim=1).tolist()[0]
    best = max(zip(texts, probs), key=lambda x: x[1])
    return {"text": best[0], "score": best[1]}

# Exemple
result = comment_outfit("photo.jpg")
print(result)
