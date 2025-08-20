from yt_dlp import YoutubeDL

def download_audio(yt_url: str):
    """ Downloads the desired youtuve url into the songs folder

    :param yt_url: youtube url to the video to download
    :type yt_url: str
    """
    
    ydl_opts = {
        'format' : 'bestaudio/best',
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192'
        }], 'outtmpl': 'songs/%(title)s' # Save directory and name format
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])

def deleted_playlist_url(yt_url: str) -> str:
    """ Deletes the playlist termination from the url

    :param yt_url: url of the youtube video
    :type yt_url: str
    :return: url without the playlist termination
    :rtype: str
    """
    
    is_playlist = False
    playlist_str = ""

    for i in yt_url:
        if i == '&':
            is_playlist = True

        if is_playlist:
            playlist_str = playlist_str + i

    if is_playlist:
        print("Trimming playlist url termination")
        yt_url = yt_url.replace(playlist_str, "")

    return yt_url

def get_multiple_songs() -> list[str]:
    """ Gets a list with all the urls that the user wants to download

    :return: list with urls to download
    :rtype: list[str]
    """

    asking = True
    yt_links = []
    counter = 0

    while asking:
        new_url = input("Entering multiple youtube urls. Enter \"exit\" to start downloading:\n")
        
        if new_url == "exit":
            asking = False
            
        elif "https://www.youtube.com/watch?v=" not in new_url:
            print(f"\"{new_url}\" is not a valid youtube link. Please try again.")
            
        elif new_url in yt_links:
            print(f"\"{new_url}\" has already been entered. Please try again")
            
        else:
            yt_links.append(new_url)
            counter = counter + 1
            print(f"Song {counter} added.")

    return yt_links

def main():
    
    yt_url = input("Enter the youtube url or \"m\" for multiple songs:\n")
    
    if yt_url == "m": # Case for multiple songs
        yt_links = get_multiple_songs()
        counter = 0
        
        for link in yt_links: # Download each url in the list
            counter = counter + 1
            print(f"Downloading songs {counter}/{len(yt_links)}")
            download_audio(deleted_playlist_url(link))
            
    else: # Case for a single song
        print("Chose to enter a single song")
        download_audio(deleted_playlist_url(yt_url))
    
if __name__ == "__main__":
    main()