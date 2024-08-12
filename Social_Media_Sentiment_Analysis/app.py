from flask import Flask, request, jsonify
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the vectorizer
with open(r'E:\Social_Media_Sentiment_Analysis\Notebook\vectorizer.pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

@app.route('/vectorize', methods=['POST'])
def vectorize():
    data = request.get_json(force=True)
    text = data['text']
    text_vectorized = vectorizer.transform([text]).toarray()
    return jsonify({'vectorized_text': text_vectorized.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
