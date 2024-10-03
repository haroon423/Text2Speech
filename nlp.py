"""from gtts import gTTS
tts = gTTS('hello', lang='en')
tts.save('hello.mp3')"""





"""from gtts import gTTS
tts = gTTS('hello', lang='en', tld='com.au')
tts.save('11hello.mp3')"""




"""from gtts import gTTS
tts_en = gTTS('hello', lang='en')
tts_fr = gTTS('bonjour', lang='fr')

with open('hello_bonjour.mp3', 'wb') as f:
    tts_en.write_to_fp(f)
    tts_fr.write_to_fp(f)"""






"""from gtts import gTTS
from io import BytesIO

mp3_fp = BytesIO()
tts = gTTS('hello', lang='en')
tts.write_to_fp(mp3_fp)"""





"""from gtts.tokenizer import Tokenizer, tokenizer_cases, pre_processors
import gtts.tokenizer.symbols as symbols

# Add custom substitution to the symbol pairs
symbols.SUB_PAIRS.append(('sub.', 'submarine'))

# Example text
test_text = "Have you seen the Queen's new sub.?"

# Apply pre-processor substitution
processed_text = pre_processors.word_sub(test_text)
print(processed_text)  # Expected: "Have you seen the Queen's new submarine?"

# Create a Tokenizer object with specific cases
tokenizer = Tokenizer([
    tokenizer_cases.tone_marks,
    tokenizer_cases.period_comma,
    tokenizer_cases.other_punctuation
])

# Run tokenizer on the processed text
tokenizer.run(processed_text)"""








from gtts import gTTS

# Function to convert text file into speech
def text_to_speech(file_path, output_file):
    # Open and read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Convert text to speech using gTTS
    tts = gTTS(text=text, lang='en')

    # Save the converted audio to a file
    tts.save(output_file)
    print(f"Speech saved to {output_file}")

# Example usage
file_path = 'speech-tester-document.txt'  # Path to your text document
output_file = 'output_audio.mp3'  # Output audio file

text_to_speech(file_path, output_file)

