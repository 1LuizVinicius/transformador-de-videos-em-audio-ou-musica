import moviepy.editor

# Carregar arquivos do vídeo
video = moviepy.editor.VideoFileClip("mia.mp4")

# Extrair apenas o áudio do video
audio_data = video.audio

#salvar o arquivo de áudio extraído do video
audio_data.write_audiofile("audio_mia.mp3")