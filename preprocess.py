#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from parsivar import Normalizer, Tokenizer

with open('Pesian_Stop_Words_List.txt', 'r', encoding='utf-8') as file:
    stop_words = [line.strip() for line in file]

def preprocess(texts):
    processed_texts = []

    normalizer = Normalizer(pinglish_conversion_needed=True)
    tokenizer = Tokenizer()

    for text in texts:
        normalized_text = normalizer.normalize(text)

        sentences = tokenizer.tokenize_sentences(normalized_text)

        filtered_sentences = []
        for sentence in sentences:
            words = sentence.split()  
            filtered_words = [word for word in words if word not in stop_words]
            filtered_sentence = ' '.join(filtered_words)
            filtered_sentences.append(filtered_sentence)

        final_text = ' '.join(filtered_sentences)

        processed_texts.append(final_text)

    return 'dfdsfdsfdsfsdfdsfsd' #processed_texts


# %%
