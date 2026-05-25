from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

messages = [
    "You won a free mobile phone",
    "Claim your cash reward now",
    "Free recharge available today",
    "Project meeting at 5 PM",
    "Send me the assignment file",
    "Your order is delivered"
]

labels = [
    "spam",
    "spam",
    "spam",
    "normal",
    "normal",
    "normal"
]

model = Pipeline([
    ("text", TfidfVectorizer()),
    ("ai_model", MultinomialNB())
])

model.fit(messages, labels)

test_messages = [
    "Congratulations! Free laptop waiting",
    "Let's play cricket in evening"
]

print("\nMessage Checking System\n")

for text in test_messages:

    output = model.predict([text])[0]

    if output == "spam":
        status = "Spam Message 🚫"
    else:
        status = "Normal Message ✅"

    print("Message:", text)
    print("Result:", status)
    print()