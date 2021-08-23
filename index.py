from fetch import Fetch
from movie import Movie


title_art = r""" _____              ______ _ _
░██████╗████████╗██████╗░███████╗░█████╗░███╗░░░███╗██╗░░██╗
██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗████╗░████║╚██╗██╔╝
╚█████╗░░░░██║░░░██████╔╝█████╗░░███████║██╔████╔██║░╚███╔╝░
░╚═══██╗░░░██║░░░██╔══██╗██╔══╝░░██╔══██║██║╚██╔╝██║░██╔██╗░
██████╔╝░░░██║░░░██║░░██║███████╗██║░░██║██║░╚═╝░██║██╔╝╚██╗
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝
                                    """
print(title_art+'\n')


def main():
    search_result = True
    movie_list = None
    print("Enter the movie name \n")
    while search_result:
        movie_name = input(" ")
        print(f'Searching for "{movie_name}" \n')
        movie = Fetch()
        movie_list = movie.Fetch_data(f"list_movies.json?query_term={movie_name}")
        if movie_list['data']['movie_count'] >= 1:
            search_result = False
        else:
            print("Movie Not Found. Please try with different movie name. \n")

    handle_movie = Movie(movie_list)
    handle_movie.display_movies()

    while handle_movie.valid_index:
        print(f"Please Enter the index of the movie which you want to stream\download")
        user_choice = input()
        print(f"Press 1 to stream or Press 2 to download the movie")
        stream_choice = input()
        if(int(stream_choice) > 1):
            handle_movie.download = True
        handle_movie.handle_movie_stream(user_choice)


main()