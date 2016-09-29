import webbrowser
import os
import re
import math


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        html {
            background: url(background.jpg);
            background-size: 100% 100%;
            background-repeat: no-repeat;
            height: 100%
        }
        body {
            padding-top: 80px;
            background: none;
            color: white;
        }
        li{
            list-style-type: none;
        }
        #info{
            position: absolute;
            bottom: -50%;
            color: black;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 740px;
            height: 540px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        #myCarousel{
            margin-top: 140px;
        }
        .movie-tile {
            
        }
        .moviePoster:hover {
            background-color: rgba(185, 185, 185, .75);
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            position: absolute;
            border: none;
            width: 100%;
            height: 100%;
            left: 0;
            top: 0;
            background-color: black;
        }
        .modal-content{
            height: 120%;
            width: 100%;
        }
        .item{
            text-align: center;
        }
        img{
            margin: auto;
        }
        .moviePoster{
            display: inline-table;
            width: 30%;
            margin-left: 20px;
        }
        @media only screen and (max-width: 740px){
            html{
                height: initial;
            }
            h2{
                font-size: 1.75rem;
            }
            
            #myCarousel{
            margin-top: 0;
            }

            #trailer .modal-dialog{
                margin-top: 20px;
                height: 150%
            }

            .carousel-indicators{
                padding-left:13px;
                bottom: initial;
                top: 55px
            }
            
            .moviePoster{
                width:50%;
            }
            .carousel-control .icon-prev, .carousel-control .icon-next, .carousel-control .glyphicon-chevron-left, .carousel-control .glyphicon-chevron-right{
                position: fixed;
            }
            .carousel-control .icon-prev, .carousel-control .glyphicon-chevron-left{
                left: initial;
            }
            .carousel-control .icon-next, .carousel-control .glyphicon-chevron-right{
                right: initial;
            }
            .modal-content{
                height: 100%;
                width: 90%;
            }

            #info h2{
                font-size: 2em;
            }
            
            @media only screen and (orientation: portrait){
        
                .modal-content{
                    height: 90%;
                    width: 50%;
                }
                #info{
                    bottom: -100%
                }
                
                #trailer .modal-dialog{
                    margin-top: 140px;
                    height: 75%;
                }

            }

        }
        @media only screen and (min-width: 320px) and (max-width: 740px) and (orientation: landscape){
            .modal-content {
                height: 75%;
                width: 96%;
                margin-left: 2px;
            }
            .scale-media iframe{
                height: 70%
            }
        
            #info{
                bottom: -18%
            }
    </style>
    <script type="text/javascript" charset="utf-8">
         
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer_video").removeAttr("src");
        });
        /* Start playing the video whenever the trailer modal is opened.
        Additionally, it pulls the movie information from the movie clicked, and adds the information to the modal.*/
        $(document).on('click', '.moviePoster', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            var movie_title = $(this).attr('data-title')
            var movie_director = $(this).attr('data-director')
            var movie_summary = $(this).attr('data-summary')
            var movie_rating = $(this).attr('data-rating')
            var movie_year = $(this).attr('data-year')
            $("#trailer_video").attr(
              {type: 'text-html',
              src: sourceUrl,
              frameborder: 0
            });
            $("#title").empty().append((movie_title + " (" + movie_year + ")"));
            $("#rating").empty().append("Rated: "+(movie_rating));
            $("#director").empty().append("Director: "+(movie_director));
            $("#summary").empty().append("Summary: "+(movie_summary));
            
        });
        
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
            <iframe id="trailer_video"></iframe>
            <div id="info">
                <h2 id="title"></h2>
                <ul>
                <li id="rating"></li>
                <li id="director"></li>
                <li id="summary"></li>
                </ul>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Adrien's Favorite Movies</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container" id="movies">
    <!-- Bootstrap Carousel -->
        <div id="myCarousel" class="slide" data-interval="false">
            <!-- Pages -->
            <ol class="carousel-indicators">
                <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
                <li data-target="#myCarousel" data-slide-to="1"></li>
                <li data-target="#myCarousel" data-slide-to="2"></li>
          </ol>

              <!-- Wrapper for slides -->
            <div class="carousel-inner" role="listbox">
                <div class="item active">
                  {first_page}
                 </div>
                 <div class="item">
                 {second_page}
                 </div>
                 <div class="item">
                 {third_page}
                 </div>
              </div>

        <!-- Left and right controls -->
        <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
            <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
        </a>
        <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
            <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
          </a>
        </div>
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="moviePoster" data-trailer-youtube-id="{trailer_youtube_id}" data-title="{video_title}" data-director="{movie_director}" data-summary="{movie_storyline}" data-year="{year_released}" data-rating="{movie_rating}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="80%" height="80%">
    <h2>{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''

    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        '''Stores the informaiton in the tiles element, to be pulled for the modal.'''
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            video_title = movie.title,
            movie_rating = movie.rating,
            movie_director = movie.director,
            year_released = movie.year,
            movie_storyline = movie.storyline
        )
        
    return content

    

def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')
    
    '''Sets the number of movies to appear on the carousel page. As there are 3 movies
        per page, it takes the number of movies, divides by 3, and rounds the number up
        to the closest integer.'''
    movie_length = len(movies)
    pages = int(math.ceil(float(movie_length)/3))
    
    '''This sets the movies to appear on each page. Going page by page, it will push
        3 movies to each page as an array. The information will then be stored in the
        variable "pages_array".'''
    pages_array=[]
    for j in range(pages):
        start = j*3
        page = movies[start:(start+3)]
        pages_array.append(page)
        
    '''This places the movies in each slide. Using the previous block of code, it sets
        the movies based on the information found in each index in "pages_array".'''
    rendered_content = main_page_content.format(
            first_page =create_movie_tiles_content(pages_array[0]),
            second_page =create_movie_tiles_content(pages_array[1]),
            third_page =create_movie_tiles_content(pages_array[2])
            )
    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
