import json
from translate import Translator

# Open and read the JSON file
with open(r'C:\Users\Alfred Karanja\PycharmProjects\pythonProject2\data.json') as file:
    data = json.load(file)

# List of target language codes
languages = ['en', 'sw', 'de', ]  # Add more language codes as needed

# Translate the text from English to other languages
for entry in data:
    if entry["locale"] == "en-US":
        translations = {}
        for lang_code in languages:
            translator = Translator(to_lang=lang_code)
            translation = translator.translate(entry["utt"])
            translations[lang_code] = translation
        entry["translations"] = translations

# Pretty print the translated data and save it to a new JSON file
output_file = 'translated_data.json'
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print(f'Translated data has been saved to {output_file}')
