import os

from shutil import rmtree

import speech_recognition as sr

from pydub import AudioSegment
from pydub.silence import split_on_silence


HOUNDIFY_CLIENT_ID = os.getenv('HOUNDIFY_CLIENT_ID', '')
HOUNDIFY_CLIENT_KEY = os.getenv('HOUNDIFY_CLIENT_KEY', '')


def speech_to_text(path, min_length=1000, db_threshold=-32,
                   speech_api: str = 'sphinx'):
    if path.endswith('.wav'):
        audio = AudioSegment.from_wav(path)
    elif path.endswith('.mp3'):
        audio = AudioSegment.from_mp3(path)
    else:
        raise Exception('Unsupported audio file.')
    # print(audio.dBFS)

    # By default,
    # Split track where silence is 1 second or more and get chunks.
    # Consider it silent if quieter than -32 dBFS.
    chunks = split_on_silence(audio, min_silence_len=min_length,
                              silence_thresh=db_threshold)

    if os.path.exists('audio'):
        rmtree('audio')
    os.mkdir('audio')

    text = list()
    for index, chunk in enumerate(chunks, 1):
        # Create 0.5 seconds silence chunk.
        chunk_silent = AudioSegment.silent(duration=500)

        # Add 0.5 sec silence to beginning and end of audio chunk.
        # This is done so that it doesn't seem abruptly sliced.
        audio_chunk = chunk_silent + chunk + chunk_silent

        # Export audio chunk and save it in the current directory.
        # Specify the bitrate to be 192k.
        chunk_path = f'audio/chunk_{index}.wav'
        audio_chunk.export(chunk_path, bitrate='192k', format='wav')

        r = sr.Recognizer()

        with sr.AudioFile(chunk_path) as source:
            # r.adjust_for_ambient_noise(source)
            audio_listened = r.listen(source)

        try:
            if speech_api == 'houndify':
                rec = r.recognize_houndify(audio_listened,
                                           client_id=HOUNDIFY_CLIENT_ID,
                                           client_key=HOUNDIFY_CLIENT_KEY)
            else:
                rec = r.recognize_sphinx(audio_listened)

            text.append((rec.capitalize(), chunk_path))
        except sr.UnknownValueError:
            print('Speech API could not understand the audio')
        except sr.RequestError as e:
            print(f'Speech API error: {e}')

    return text


if __name__ == '__main__':
    text = speech_to_text('test/test.wav', min_length=1000, db_threshold=-32,
                          speech_api='houndify')
    print(text)
