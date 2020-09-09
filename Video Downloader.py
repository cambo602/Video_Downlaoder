from pytube import YouTube

link = input("Enter the link: ")
yt = YouTube(link)

ys = yt.streams.get_highest_resolution()

# Title of video
print("Title: ", yt.title)
# Number of views of video
print("Number of views: ", yt.views)
# Length of the video
print("Length of video: ", yt.length, "seconds")
# Rating
print("Ratings: ", yt.rating)

download = input("Download y/n: ")

if download == "y":
    ys.download("R:\Videos")
    print("Downlaod Complete")
