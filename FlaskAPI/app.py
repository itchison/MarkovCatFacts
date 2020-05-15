from flask import Flask
import os
import markovify

app = Flask(__name__)


# Get raw text as string.
with open("catfacts/catfacts.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

@app.route("/")
def hello():
    return text_model.make_sentence()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)