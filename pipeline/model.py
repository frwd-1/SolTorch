import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# test
# Example data
solidity_codes = ["code_with_reentrancy", "safe_code", ...]
labels = [1, 0, ...]  # 1 for vulnerable, 0 for not vulnerable

# Vectorize the Solidity code
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(solidity_codes)
y = np.array(labels)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train a simple Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train, y_train)

# test
# Evaluate the model
predictions = model.predict(X_test)
print(classification_report(y_test, predictions))
