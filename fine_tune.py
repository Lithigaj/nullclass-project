<code>
import json

# Placeholder for the pre-trained LSTM model
class LSTMModel:
    def __init__(self, translation_dict):
        self.translation_dict = translation_dict

    def translate(self, sentence):
        words = sentence.lower().split()
        translated_words = [self.translation_dict.get(word, word) for word in words]
        return ' '.join(translated_words)

    def fine_tune(self, new_data):
        # Update the translation dictionary with the new data
        self.translation_dict.update(new_data)
        print("Model fine-tuned with new data.")

def load_translation_dict(file_path):
    """
    Loads the translation dictionary from a JSON file.
    """
    with open(file_path, 'r') as f:
        return json.load(f)

def translate_sentence(model, sentence):
    """
    Translates a sentence using the given model.
    """
    return model.translate(sentence)

if __name__ == '__main__':
    # Load the initial translation dictionary
    translation_dict = load_translation_dict('translation_dict.json')

    # Create an LSTM model with the translation dictionary
    model = LSTMModel(translation_dict)

    # Example sentence to translate
    sentence = "hello world"
    print(f"Original sentence: {sentence}")
    translated_sentence = translate_sentence(model, sentence)
    print(f"Translated sentence: {translated_sentence}")

    # Fine-tune the model with new data
    new_data = {"hello": "नमस्ते (new)", "world": "दुनिया (new)"}
    model.fine_tune(new_data)

    # Translate the sentence again after fine-tuning
    translated_sentence = translate_sentence(model, sentence)
    print(f"Translated sentence after fine-tuning: {translated_sentence}")
</code>
