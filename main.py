from pytube import YouTube

def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
      youtubeObject.download()
  except:
    print("Ther has been an error in downloading your youtube videos")
  print("Hurray!!!...This download has completed!")

  link = input("put your youtube link here: URL :")
  Download(link)
      