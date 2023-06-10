
from pytube import Playlist

link = str(input("Insira Link do Vídeo: "))

# Usando a biblioteca:
yt_playList = Playlist(link)

# Aqui esta o 'Pulo do gato':
for video in yt_playList.videos:
    # Aqui você escolhe a qualidade do vídeo a ser baixado, como;
    # ".get_lowest_resolution()" , ".get_by_resolution()" , Etc...
    video.streams.get_highest_resolution().download()
    print("Video Baixado", video.title)

print("Todos os videos foram baixados !")


'''
Use ->  "pip3 install pytube"  Para instalar a biblioteca
 no seu ambiente virtual

'''
