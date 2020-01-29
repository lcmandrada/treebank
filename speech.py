import os

import speech_recognition as sr

from pydub import AudioSegment
from pydub.silence import split_on_silence


def speech_to_text(path, length=1000, thresh=-16):
    text = str()
    audio = AudioSegment.from_wav(path)
    # print(audio.dBFS)

    # split track where silence is 0.5 seconds
    # or more and get chunks
    # consider it silent if quieter than -16 dBFS
    # adjust this per requirement
    chunks = split_on_silence(audio, min_silence_len=length,
                              silence_thresh=thresh)

    # create a directory to store the audio chunks.
    if not os.path.exists('audio_chunks'):
        os.mkdir('audio_chunks')

    i = 0
    # process each chunk
    for chunk in chunks:
        # Create 0.5 seconds silence chunk
        chunk_silent = AudioSegment.silent(duration=500)

        # add 0.5 sec silence to beginning and
        # end of audio chunk. This is done so that
        # it doesn't seem abruptly sliced.
        audio_chunk = chunk_silent + chunk + chunk_silent

        # export audio chunk and save it in
        # the current directory.
        # specify the bitrate to be 192 k
        audio_chunk.export(f'audio_chunks/chunk{i}.wav',
                           bitrate='192k', format='wav')
        # print(f'saving chunk{i}.wav')

        # the name of the newly created chunk
        filename = f'audio_chunks/chunk{i}.wav'
        # print('Processing chunk '+str(i))

        # get the name of the newly created chunk
        # in the AUDIO_FILE variable for later use.
        file = filename

        # create a speech recognition object
        r = sr.Recognizer()

        # recognize the chunk
        with sr.AudioFile(file) as source:
            # remove this if it is not working correctly.
            # r.adjust_for_ambient_noise(source)
            audio_listened = r.listen(source)

        try:
            # try converting it to text
            rec = r.recognize_sphinx(audio_listened)
            # write the output to the file.
            text += rec + '. '
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))

        i += 1

    return text


if __name__ == '__main__':
    text = speech_to_text('harvard.wav', length=2000, thresh=-32)
    print(text)
