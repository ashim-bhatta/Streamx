import requests
import subprocess
import sys

title_art = r""" _____              ______ _ _
|_   _|             |  ___| (_)
  | | ___  _ __ _ __| |_  | |___  __
  | |/ _ \| '__| '__|  _| | | \ \/ /
  | | (_) | |  | |  | |   | | |>  <
  \_/\___/|_|  |_|  \_|   |_|_/_/\_\
                                    """
title_art = r""" _____              ______ _ _
|_   _|             |  ___| (_)
  | | ___  _ __ _ __| |_  | |___  __
  | |/ _ \| '__| '__|  _| | | \ \/ /
  | | (_) | |  | |  | |   | | |>  <
  \_/\___/|_|  |_|  \_|   |_|_/_/\_\
                                    """
print(title_art+'\n')

BASE_URL = 'https://yts.mx/api/v2/'

def Fetch_data(url):
    return requests.get(url=url).json()


def main():
    movie_name = input("Enter the movie name:\n")
    print(f"Searching for {movie_name}")
    movie_list_url = f"{BASE_URL}list_movies.json?query_term={movie_name}"
    torrent_results = Fetch_data(movie_list_url)
    index = 1
    magnets = []
    count = 1
    for result in torrent_results['data']['movies']:
        torrentInfo = result['torrents']
        print(f"{count}. {result['title']}---------{torrentInfo[0]['size']}")
        count+=1
        mg = f'magnet:?xt=urn:btih:{torrentInfo[0]["hash"]}&dn={result["title"]}&tr=udp://open.demonii.com:1337/announce&tr=udp://tracker.openbittorrent.com:80&tr=udp://tracker.coppersurfer.tk:6969&tr=udp://glotorrents.pw:6969/announce&tr=udp://tracker.opentrackr.org:1337/announce&tr=udp://torrent.gresille.org:80/announce&tr=udp://p4p.arenabg.com:1337&tr=udp://tracker.leechers-paradise.org:6969'
        magnets.append(mg)

    print('\r')
    print('\r')
    print(f"Please Enter the index of the movie which you want to stream\download")
    selectedMovie = input()
    print('\r')
    print('\r')
    if magnets:
        try:
            magnet = magnets[int(selectedMovie) - 1]
            download = False  # Default is streaming
            stream_choice = int(
                input("Press 1 to stream or Press 2 to download the movie\n"))
            if stream_choice == 2:
                download = True

            webtorrent_stream(magnet, download)
        except IndexError:
            print("Incorrect Index entered")
    else:
        print(f"No results found for {movie_name}")


# Handle Streaming
def webtorrent_stream(magnet_link: str, download: bool):
    cmd = ""
    cmd= cmd + "webtorrent"
    cmd=cmd+" download "
    cmd=cmd+'"{}"'.format(magnet_link)
    if not download:
        print('streamming...')
        cmd=cmd+' --vlc'

    if sys.platform.startswith('linux'):
        subprocess.call(cmd)
    elif sys.platform.startswith('win32'):
        subprocess.call(cmd, shell=True)


if __name__ == "__main__":
    main()
