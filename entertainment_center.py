import media
import fresh_tomatoes


dont_be_a_menace = media.Movie("Don't Be a Menace to South Central While Drinking Your Juice in the Hood" ,
                               "Paris Barclay",
                               "'Don\'t Be a Menace to South Central While Drinking your Juice in the Hood' is a parody of several U.S. films about being in the 'Hood', for instance 'Boyz n the Hood', 'South Central', 'Menace II Society', 'Higher Learning' and 'Juice'.",
                               "https://upload.wikimedia.org/wikipedia/en/f/fd/Dontbeamenace.jpg",
                               "https://www.youtube.com/watch?v=JAAhQwcJ20U",
                               "1996",
                               "R")

suicide_squad = media.Movie("Suicide Squad",
                            "David Ayer",
                            "A secret government agency led by Amanda Waller recruits imprisoned supervillains to execute dangerous black ops missions and save the world from a powerful threat, in exchange for leaner sentences.",
                            "https://upload.wikimedia.org/wikipedia/en/5/50/Suicide_Squad_%28film%29_Poster.png",
                            "https://www.youtube.com/watch?v=CmRih_VtVAs",
                            "2016",
                            "PG-13")
                            
do_the_right_thing = media.Movie("Do the Right Thing",
                                 "Spike Lee",
                                 "The movie tells the story of a Brooklyn neighborhood's simmering racial tension, which comes to a head and culminates in tragedy on the hottest day of summer.",
                                 "https://upload.wikimedia.org/wikipedia/en/0/03/Do_the_Right_Thing_poster.png",
                                 "https://www.youtube.com/watch?v=muc7xqdHudI",
                                 "1989",
                                 "R")
the_nightmare_before_christmas = media.Movie("The Nightmare Before Christmas",
                                             "Henry Selick",
                                             "Jack Skellington, king of Halloween Town, discovers Christmas Town, but doesn't quite understand the concept.",
                                             "https://upload.wikimedia.org/wikipedia/en/9/9a/The_nightmare_before_christmas_poster.jpg",
                                             "https://www.youtube.com/watch?v=8qrB9I3DM80",
                                             "1993",
                                             "PG")

the_spongebob_squarepants_movie = media.Movie("The Spongebob Squarepants Movie",
                                              "Stephen Hillenburg",
                                              "SpongeBob SquarePants takes leave from the town of Bikini Bottom in order to track down King Neptune's stolen crown.",
                                              "https://upload.wikimedia.org/wikipedia/en/3/31/The_SpongeBob_SquarePants_Movie_poster.jpg",
                                              "https://www.youtube.com/watch?v=Tv8xk7BKaNM",
                                              "2004",
                                              "PG")
dope = media.Movie("Dope",
                   "Rick Famuyiwa",
                   "Life changes for Malcolm, a geek who's surviving life in a tough neighborhood, after a chance invitation to an underground party leads him and his friends into a Los Angeles adventure.",
                   "https://upload.wikimedia.org/wikipedia/en/d/d2/DopeTeaserPoster.jpg",
                   "https://www.youtube.com/watch?v=strEm9amZuo",
                   "2015",
                   "R")

shrek = media.Movie("Shrek",
                    "Andrew Adamson",
                    "After his swamp is filled with magical creatures, an ogre agrees to rescue a princess for a villainous lord in order to get his land back.",
                    "https://upload.wikimedia.org/wikipedia/en/3/39/Shrek.jpg",
                    "https://www.youtube.com/watch?v=W37DlG1i61s",
                    "2001",
                    "PG")

a_goofy_movie = media.Movie("A Goofy Movie",
                            "Kevin Lima",
                            "When Max makes an preposterous promise to a girl he has a crush on, his chances to fulfilling it seem hopeless when he is dragged onto a cross-country trip with his embarrassing father, Goofy.",
                            "https://upload.wikimedia.org/wikipedia/en/f/f3/A_Goofy_Movie_poster.jpg",
                            "https://www.youtube.com/watch?v=aFYCQoIpGuE",
                            "1995",
                            "G")

scooby_doo = media.Movie("Scooby Doo",
                         "Raja Gosnell",
                         "After an acrimonious break up, the Mystery Inc. gang are individually brought to an island resort to investigate strange goings on.",
                         "https://upload.wikimedia.org/wikipedia/en/a/ae/Scooby-Doo_poster.jpg",
                         "https://www.youtube.com/watch?v=Bzz4EQ2NmpQ",
                         "2005",
                         "PG")

movies = [suicide_squad, do_the_right_thing, the_nightmare_before_christmas, dont_be_a_menace, the_spongebob_squarepants_movie, dope, shrek, a_goofy_movie,scooby_doo]

#Loads the HTML page for the movies
fresh_tomatoes.open_movies_page(movies)

