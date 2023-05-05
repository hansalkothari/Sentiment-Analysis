import requests

# Set the API key and movie title
api_key = "10eb8e5a"
movie_title = "The Shawshank Redemption"

# Send a request to the OMDB API to search for the movie
search_url = f"http://www.omdbapi.com/?apikey={api_key}&s={movie_title}"
response = requests.get(search_url)
search_result = response.json()

print(search_resultk)
# Extract the IMDb ID of the movie from the search result
imdb_id = search_result["Search"][0]["imdbID"]

# Send a request to the OMDB API to retrieve the details of the movie, including the reviews
movie_url = f"http://www.omdbapi.com/?apikey={api_key}&i={imdb_id}&plot=full&r=json&tomatoes=true"
response = requests.get(movie_url)
movie_details = response.json()

# Extract the reviews from the movie details
reviews = movie_details["tomatoReviews"]

# Print the reviews
for review in reviews:
    print(review)