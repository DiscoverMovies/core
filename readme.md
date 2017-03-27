#DiscoverMovies API documentation

The api is divided into segments that interact with specific models

###Core

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
    ```
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