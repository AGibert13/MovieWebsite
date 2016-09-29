import webbrowser

class Movie():
    """This class provides a way to store movie related information."""
    
    def __init__(self, movie_title, movie_director, movie_storyline, poster_image, trailer_youtube, year_released, movie_rating):
        self.title = movie_title
        self.director = movie_director
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = year_released
        self.rating = movie_rating
