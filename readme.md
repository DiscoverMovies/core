# DiscoverMovies API documentation

The api is divided into segments that interact with specific models

### Core

Core handles and interacts with users and sessions. It handles:

*   Creating login token
    ```
        POST /user/auth
        {username,password}
    ```
*   Creating users
    ```
        POST /user/create
        {username,password,email,phone}
    ```
*   Updating user profile
    ```
        POST /user/update
        {token,name,sex,dob,country,state}
    ```````
*   Check user exists
    ```
        GET /user/check
        {username}
    ```
*   Search user 
    ```
        GET /user/check
        {username}
    ```
*   Send verification code
    ```
        HTTP /user/verify/<username>
    ```
    

### Forums

*   Create forum
    ```
        POST /forum/create
        {token, title, text}
    ```
*   Get forum details
    ```
        HTTP /forum/get/<forum_id>
    ```
*   Search forums
    ```
        GET /forum/search
        {q}
    ```
*   Get all forum topics
    ```
        HTTP /forum/all
    ```
*   Delete forum
    ```
        POST /forum/delete/<forum_id>
        {token}
    ```
    if the forum_topic author and user deleting is not same, error will be raised

*   Get all replies to the forum
    ```
        HTTP /forum/replies/<forum_id>
    ```
*   Post reply to a forum
    ```
        POST /forum/reply/post/<forum_id>
        {token, text}
    ```

### Movies

*   Get movie details
    ```
        HTML /movie/get/<movie_id>
    ```

*   Search movie data
    ```
        GET /movie/search
        {q}
    ```

*   Get popular movies of a genre
    ```
        HTML /movie/popular/<genre_id>
    ```

*   Get details of all genre
    ```
        HTML /movie/genre/all
    ```

### Recommendation
 
*   Rate a movie
    ```
        POST /rate/movie/<movie_id>
        {token, rating}
    ```

*   Get all rating provided by a single user
    ```
        HTTP /rating/user/all/<token>
    ```

*   Remove a rating by user
    ```
        HTTP /rating/user/remove/<movie_id>/<token>
    ```

*   Get movies like another movie
    ```
        HTTP /recommendation/movie/<movie_id>
    ```