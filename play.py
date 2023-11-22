from pytube import YouTube 

yt = YouTube(str(input("Enter the youtube video link: ")))

# https://www.youtube.com/watch?v=5RJA20ShC14

print(yt.title)
# print(yt.streams.filter(only_audio=True, abr="128kbps"))
# stream = yt.streams.get_by_itag(140)
# print(stream)

# stream1 = yt.streams.filter(only_audio=True, abr="128kbps").first()
# print(stream1)
stream = yt.streams.filter(only_audio=True).first()
filename = yt.title+".mp3"
stream.download(filename=filename)

print("Download completed")