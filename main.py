import json
import os
from pytube import YouTube
from moviepy.editor import AudioFileClip

if not os.path.isdir('audio_files'):
    os.makedirs('audio_files')

if not os.path.isdir('cut_files'):
    os.makedirs('cut_files')

if __name__ == '__main__':
    # Load data from json file
    data = json.load(open('urls.json', 'r'))
    # Iterate over entries
    for entry in data['urls']:
        yt_url = entry['url']
        vid = YouTube(yt_url)
        audio_stream = vid.streams.filter(only_audio=True).first()
        audio_dir = 'audio_files/'
        audio_path = entry['name'] + '.mp3'
        audio_stream.download(output_path=audio_dir[:-1], filename=audio_path)
        cut_dir = 'cut_files/'
        tbcut_audio = AudioFileClip(audio_dir + audio_path)
        cut_audio = tbcut_audio.subclip(entry['begin'], entry['end'])
        cut_audio.write_audiofile(cut_dir + audio_path)
