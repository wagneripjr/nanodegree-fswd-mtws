#creates a list of my prefered moviews to generate the website
import movie

kungfuPanda = movie.Movie("Kung Fu Panda"
        , "A young panda that becomes one with himself"
        ,"http://upload.wikimedia.org/wikipedia/en/thumb/7/76/Kungfupanda.jpg/220px-Kungfupanda.jpg"
        ,"www.youtube.com/watch?v=PXi3Mv6KMzY"
        , [ "Jack Black", "Ian McShane", "Angelina Jolie"]
        , "2008-06-06"
        , "USA"
        , "Mark Osborne")

avatar = movie.Movie("Avatar"
        , "A marine on an alien planet"
        ,"http://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg"
        ,"https://www.youtube.com/watch?v=5PSNL1qE6VY"
        , ["Sam Worthington", "Zoe Saldana", "Sigourney Weaver"]
        , "2009-12-18"
        , "USA"
        , "James Cameron")

gladiator = movie.Movie("Gladiator"
        ,"A roman soldier lost everything and fight as a gladiator to take revenge"
        ,"http://upload.wikimedia.org/wikipedia/en/thumb/8/8d/Gladiator_ver1.jpg/220px-Gladiator_ver1.jpg"
        ,"https://www.youtube.com/watch?v=Q-b7B8tOAQU"
        , ["Russell Crowe", "Joaquin Phoenix", "Connie Nielsen"]
        , "2000-05-05"
        , "USA"
        , "Ridley Scott")

matrix = movie.Movie("The Matrix"
        ,"A hacker in a journey to discover the truth"
        ,"http://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg"
        ,"https://www.youtube.com/watch?v=_Ls19O-9p3s"
        , ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"]
        , "1999-03-31"
        , "USA"
        , "The Wachowski Brothers")

braveheart = movie.Movie("Braveheart"
        ,"William Wallace begins a revolt and leads Scottish warriors against the cruel English tyrant who rules Scotland with an iron fist"
        ,"http://upload.wikimedia.org/wikipedia/en/thumb/5/55/Braveheart_imp.jpg/220px-Braveheart_imp.jpg"
        ,"https://www.youtube.com/watch?v=d8eiuEa7ZHE"
        , ["Mel Gibson", "Sophie Marceau", "Patrick McGoohan"]
        , "1995-05-24"
        , "USA"
        , "Mel Gibson")

#list of my prefered movies
def movies():
        return [braveheart, gladiator, kungfuPanda, matrix, avatar]

