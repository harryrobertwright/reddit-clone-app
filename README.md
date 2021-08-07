# reddit-clone-app
A social news aggregation app with a Django backend and React frontend

## API Endpoints
### Register
----
  Allows a user to register and stores their details in the database

* **URL**

  /auth/register/

* **Method:**

  `POST`

* **Data Params**

   **Required:**
 
   **Content:** `{ "username" : <username>, "email": <email>, "password": <password>  }`

* **Success Response:**

  * **Code:** 200 CREATED
    **Content:** ``{ "email" : <email>, "username": <username>  }``
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST

* **Sample Call:**

  ```curl
  curl -H "Content-type: application/json" -d '{ "username" : "testusername", "email": "test@email.com", "password": "testpassword123, "confirm_password": "testpassword123"}`' 'http://127.0.0.1:8000/auth/register/'```
  