from parsivar import Normalizer, Tokenizer
from joblib import load

vectorizer = load('vectorizer.joblib')

def preprocess(text, stop_words):

    normalizer = Normalizer(pinglish_conversion_needed=True)
    tokenizer = Tokenizer()

    normalized_text = normalizer.normalize(text)

    sentences = tokenizer.tokenize_sentences(normalized_text)

    filtered_sentences = []
    for sentence in sentences:
        words = sentence.split()
        filtered_words = [word for word in words if word not in stop_words]
        filtered_sentence = ' '.join(filtered_words)
        filtered_sentences.append(filtered_sentence)

    final_text = ' '.join(filtered_sentences)
    
    processed_text_vector = vectorizer.transform([final_text])

    return processed_text_vector