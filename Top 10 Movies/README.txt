1. I create an SQLite database with SQLAlchemy. The database contain a "Movie" Table. This table contain: id, title, year, description, rating, ranking, review, img_url. I added 10 entries to the database.
2. I'm able to edit a Movie's Rating and Review
   Edit button (on the back of the movie card) -> If I click on it I can change the rating and the review.
   I use WTForm to create the RateMovieForm. I use this to create a Quick Form to be rendered in edit.html
3. I am able to delete movies from the Database
   On the back of each movie card there is also a Delete button. This button allow the movie entry to be deleted from the Database
4. I am able to add new movies via the Add Page
   The Add page render when I click on the Add Movie button on the Home page
   The Add page show a WTF quick from that only contains 1 field - the title of the movie
5. When a user types a movie title and clicks "Add Movie", the Flask server receive the movie title. Next, I use the requests library to make a request and search The Movie Database API for all movies that match that title. 
    I sign up for a free account on The Movie Database
    Settings -> API and I get an API Key. Copy that API key into my project.
6. Using the data I get from the API, I render a select.html page and add all movie title and year of release on to the page. This way, the user can choose the movie they want to add. There are usually quite a few movies under similar names. 
   Once the user selects a particular film from select.html page, the id of the movie is used to hit up another path in the Movie Database API, which will fetch all the data they have on that movie.
   It is used the id of the movie that the user selected to make a request to the get-movie-details path.
   The data I get from API populate the database with a new entry. 
   Once the entry is added, redirect to the home page and it display the new movie as a card. 
7. The movies are displayed according to the rating. If the user added another movie and it had the highest rating among the movies, then it should be ranked according to it's rating.

