from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Dataset simple
phrases = [
    "Cc, t ki ? 😘", "Tu dors ?", "Je peux avoir ton snap",  # cringe
    "Salut, j'aime ton style", "Je te trouve sympa",         # normal
    "Tu dégages une belle énergie", "Ta confiance est inspirante"  # charismatique
]
labels = ["cringe", "cringe", "cringe", "neutre", "neutre", "confiant", "confiant"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(phrases)
clf = MultinomialNB()
clf.fit(X, labels)

def predict_style(text):
    x_test = vectorizer.transform([text])
    return clf.predict(x_test)[0]

print(predict_style("Tu veux qu'on se parle sur Snap ?"))
print(predict_style("J’admire la manière dont tu t’exprimes"))
