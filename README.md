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

  

*  **Code:** 200 CREATED

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


  

*  **Sample Call:**

  

```curl

curl -H "Content-type: application/json" -d '{ "username" : "testusername", "email": "test@email.com", "password": "testpassword123, "confirm_password": "testpassword123"}`' 'http://127.0.0.1:8000/auth/register/'```