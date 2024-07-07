from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report


clf = MultinomialNB()
clf.fit(X_train_counts, y_train)


y_pred = clf.predict(X_test_counts)
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
print(classification_report(y_test, y_pred))
