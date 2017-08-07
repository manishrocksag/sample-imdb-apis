# IMDB Movie APIs

This project exposes apis to retrive 
movies. The movies can be searched through
their names , genres, director name and popularity.

/admin ~ reference to the admin site page where CRUD operations 
    can be performed on models.
    
/movie ~ Returns the list of all the movies.

/movie?id={0} ~ Returns the movie with the given id

/genre ~ Returns the list of all the genres.

# todo 

/movie/{id}?genre={name} ~ Returns the genre list of the given movie.

/movie/{id}?director={name} ~ Returns the director name of the given movie.

/movie/popularity?score={number} ~ Returns the list of the movies which has a popularity
    greater than or equal to the given score.
    
/movie/rating?rating={number} ~ Returns the list of the movies which has a ratings
    greater than or equal to the given score.

movie/genre?{name} ~ Returns the movie list which belongs to the given genre.    

# todo 
adding permission and authentication.


More features coming soon.
