import webbrowser

class Movie():
    """ This class provides a way to store my prefered movie related information """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_stars, released, country, movie_director):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.stars = movie_stars
        self.release_date = released
        self.country = country
        self.director = movie_director

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
