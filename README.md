# reddit-clone-app

A social news aggregation app with a Django backend and React frontend
  
## API Endpoints

### Register

----

Allows a user to register and stores their details in the database

*  **URL**  

/auth/register/ 

*  **Method:**

`POST`

*  **Data Params**

**Required:**

**Content:**  `{ "username" : <username>, "email": <email>, "password": <password> }`

*  **Success Response:**

*  **Code:** 200 OK

**Content:**  `{ "message" : "User successfully registered." }`

*  **Error Response:**

 *  **Code:** 400 BAD REQUEST

**Content:**  

 * Duplicate email - `{  "email":  [  "This email is already in use."  ]  }`
 * Duplicate username - `{  "username":  [  "This username is already in use."  ]  }`
 * Invalid email address - `{ "email": [ "Enter a valid email address." ] }`
 * Username too long - `{  "username":  [  "Ensure this field has no more than 150 characters."  ]  }`
 * Non-matching passwords - `{  "password":  [  "Password fields didn't match."  ]  }`
 * Too short password - `{  "password":  [  "This password is too short. It must contain at least 8 characters." ]  }`
 * Common password - `{  "email":  [  "Enter a valid email address."  ]  }`
 * Empty field - `{  <field>:  [  "This field may not be blank."  ]  }`

**Sample Call:**

```curl -H "Content-type: application/json" -d '{ "username" : "testusername", "email": "test@email.com", "password": "testpassword123, "confirm_password": "testpassword123"}`' 'http://127.0.0.1:8000/auth/register/'```


### Login

----

Returns an access token (valid for 300s) and refresh token cookie (valid for 7 days) to authenticate user for future requests
 
*  **URL**  

/auth/login/ 

*  **Method:**

`POST`

*  **Data Params**

**Required:**

**Content:**  `{ "username" : <username>, "password": <password> }`

*  **Success Response:**

*  **Code:** 200 OK

**Content:**  `{ "access": <access_token> }`

*  **Error Response:**

 *  **Code:** 400 BAD REQUEST

**Content:**  

 * Empty field - `{ <field>: [ "This field is required." ] }`

*  **Error Response:**

 *  **Code:** 401 UNAUTHORIZED

**Content:**  

 * Invalid credentials - `{ "detail": "No active account found with the given credentials" }`

**Sample Call:**

```curl -H "Content-type: application/json" -d '{ "username" : "testusername", "password": "testpassword123"}`' 'http://127.0.0.1:8000/auth/login/'```


### Login (refresh)

----

Returns a new access token (valid for 300s) to authenticate user given a valid refresh token
 

*  **URL**  

/auth/login/refresh/

*  **Method:**

`GET`

*  **Cookie Params**

**Required:**

**Content:**  `{ "refresh" : <refresh_token> }`

*  **Success Response:**

*  **Code:** 200 OK

**Content:**  `{ "access": <access_token> }`

*  **Error Response:**

 *  **Code:** 400 BAD REQUEST

**Content:**  `{ "refresh": [ "This field is required." ] }`

 *  **Code:** 401 UNAUTHORIZED

**Content:**  `{ "detail": "Token is invalid or expired", "code": "token_not_valid" }`

**Sample Call:**

```curl -XGET -H 'Authorization: Bearer <refresh_token>' 'http://127.0.0.1:8000/auth/login/refresh/'```


### Profile

----

Returns a logged in user's profile
 

*  **URL**  

/api/profile/

*  **Method:**

`GET`

*  **Authorization Params**

**Required:**

**Content:**  `Bearer <access_token> }`

*  **Success Response:**

*  **Code:** 200 OK

**Content:**  `{ "username": <username>, "date_joined": <date_joined>, "last_login": <last_login>, "avatar": <avatar> }`

*  **Error Response:**

 *  **Code:** 401 UNAUTHORIZED

**Content:**  

 * No credentials provided - `{ "detail": "Authentication credentials were not provided." }`
 
 * Invalid token provided - `{ "detail": "Given token not valid for any token type", "code": "token_not_valid", "messages": [ { "token_class": "AccessToken", "token_type": "access", "message": "Token is invalid or expired" } ] }`

**Sample Call:**

```curl -XGET -H 'Authorization: Bearer <access_token>' 'http://127.0.0.1:8000/api/profile/'```