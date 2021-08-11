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

Returns an access and refresh token to authenticate user for future requests
 
*  **URL**  

/auth/login/ 

*  **Method:**

`POST`

*  **Data Params**

**Required:**

**Content:**  `{ "username" : <username>, "password": <password> }`

*  **Success Response:**

*  **Code:** 200 OK

**Content:**  `{ "refresh": <refresh_token>, "access": <access_token> }`

*  **Error Response:**

 *  **Code:** 400 BAD REQUEST

**Content:**  

 * Invalid credentials - `{ "detail": "No active account found with the given credentials" }`
 * Empty field - `{  <field>:  [  "This field may not be blank."  ]  }`

**Sample Call:**

```curl -H "Content-type: application/json" -d '{ "username" : "testusername", "password": "testpassword123, "confirm_password": "testpassword123"}`' 'http://127.0.0.1:8000/auth/login/'```


### Login (refresh)

----

Returns a new access and refresh token to authenticate user given a valid refresh token
 

*  **URL**  

/auth/login/refresh/

*  **Method:**

`POST`

*  **Data Params**

**Required:**

**Content:**  `{ "refresh" : <refresh_token> }`

*  **Success Response:**

*  **Code:** 200 OK

**Content:**  `{ "refresh": <refresh_token>, "access": <access_token> }`

*  **Error Response:**

 *  **Code:** 401 UNAUTHORIZED

**Content:**  `{ "detail": "Token is invalid or expired", "code": "token_not_valid" }`

**Sample Call:**

```curl -H "Content-type: application/json" -d '{ "refresh" : <refresh_token> }`' 'http://127.0.0.1:8000/auth/login/refresh/'```