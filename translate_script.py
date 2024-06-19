from google.cloud import translate_v2 as translate

def translate_file(input_file, output_file, target_language):
    # Instantiates a client
    translate_client = translate.Client()

    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Translates the text into the target language
    translation = translate_client.translate(text, target_language=target_language)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(translation['translatedText'])

if __name__ == '__main__':
    input_file = 'input_file.txt'  # Replace with your input file path
    output_file = 'output_file.txt'  # Replace with your desired output file path
    target_language = 'fr'  # Replace with your target language code (e.g., 'fr' for French)

    translate_file(input_file, output_file, target_language)