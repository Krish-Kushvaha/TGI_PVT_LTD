from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

training_messages = [
    "Win a free iPhone now!",
    "Click here to claim your prize",
    "Free money is waiting for you",
    "Meeting scheduled at 3 PM tomorrow",
    "Can you review my project code?",
    "Your package has been shipped successfully"
]

training_labels = [
    "spam",
    "spam",
    "spam",
    "ham",
    "ham",
    "ham"
]

spam_detector = Pipeline([
    ("vectorizer", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

spam_detector.fit(training_messages, training_labels)

sample_messages = [
    "Congratulations! You won a lottery",
    "Let's have lunch together at noon"
]

print("\nSpam Detection Results:\n")

for message in sample_messages:
    prediction = spam_detector.predict([message])[0]

    if prediction == "spam":
        result = "SPAM 🚫"
    else:
        result = "HAM ✅"

    print(f"Message: {message}")
    print(f"Prediction: {result}\n")