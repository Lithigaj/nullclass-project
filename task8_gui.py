<code>
import json

# Placeholder for the OCR model
class OCRModel:
    def __init__(self):
        pass

    def extract_text(self, image):
        # In a real implementation, this would use an OCR model to extract text from the image.
        # Since we can't load a real model, we'll return a dummy text or None.
        # For demonstration purposes, let's assume it recognizes "hello world" and returns None for anything else.
        if image == "image_with_hello_world":
            return "hello world"
        else:
            return None

# Placeholder for the language detection model
class LanguageDetectionModel:
    def __init__(self):
        pass

    def detect_language(self, text):
        # In a real implementation, this would use a language detection model to identify the language of the text.
        # Since we can't load a real model, we'll assume it's English.
        return "en"  # English

# Placeholder for the translation model
class TranslationModel:
    def __init__(self, tamil_dict):
        self.tamil_dict = tamil_dict

    def translate(self, text):
        words = text.lower().split()
        translated_words = [self.tamil_dict.get(word, word) for word in words]
        return ' '.join(translated_words)

def load_translation_dict(file_path):
    """
    Loads the translation dictionary from a JSON file.
    """
    with open(file_path, 'r') as f:
        return json.load(f)

# Example usage (without GUI)
if __name__ == '__main__':
    # Load translation dictionary
    tamil_dict = load_translation_dict('tamil_dict.json')

    # Create OCR, language detection, and translation models
    ocr_model = OCRModel()
    language_model = LanguageDetectionModel()
    translation_model = TranslationModel(tamil_dict)

    # Simulate image input
    image_input = "image_with_hello_world"  # Replace with actual image input

    # Extract text from the image
    extracted_text = ocr_model.extract_text(image_input)

    if extracted_text:
        # Detect the language of the extracted text
        language = language_model.detect_language(extracted_text)

        if language == "en":
            # Translate to Tamil
            tamil_text = translation_model.translate(extracted_text)
            print(f"English: {extracted_text}, Tamil: {tamil_text}")
        else:
            print("The extracted text is not in English.")
    else:
        print("Could not extract text from the image.")
</code>
