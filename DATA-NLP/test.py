


# 1) Minusculas
#data['text_clean'] = data['comment_text'].str.lower()

# 2) Quitar caracteres especiales
#data['text_clean'] = data['text_clean'].apply(lambda x: re.sub('[^a-z0-9 ]+', ' ', x))



#Otra forma de vectorizar

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

# Bolsas de palabras
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data_clean['comment_text_new'])

# Etiqueta
y = data_clean['sentiment_rating']

# División estratificada
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)



from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix

# # Entrenamos
model = LogisticRegression(solver='liblinear')
model.fit(X_train, y_train)

# # Predecimos
y_pred = model.predict(X_test)
test_pred_prob = model.predict_proba(X_test)
# Métricas
print("Accuracy:", accuracy_score(y_test, y_pred))
print("F1 score:", f1_score(y_test, y_pred))
print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))