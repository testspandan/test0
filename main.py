from flask import Flask, request, jsonify, send_from_directory
from elevenlabs import generate, play
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/generate_audio', methods=['POST'])
def generate_audio():
    try:
        # Get the text from the POST request
        text = request.json.get('text')

        # Generate audio using elevenlabs
        audio_data = generate(text=text, voice="Arnold", model='eleven_multilingual_v1')

        # Save the audio data to a WAV file
        audio_file_path = "generated_audio.wav"
        with open(audio_file_path, 'wb') as wf:
            wf.write(audio_data)

        # Return the path to the hosted audio file
        return jsonify({'audio_url': f'http://89729e1f-c451-4f96-84cd-3edd795e24be-00-o1vf1nwn7gw5.pike.replit.dev/get_audio/{audio_file_path}'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_audio/<filename>')
def get_audio(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    # Run the Flask application on host 0.0.0.0 and port 81
    app.run(host='0.0.0.0', port=81, debug=True)
