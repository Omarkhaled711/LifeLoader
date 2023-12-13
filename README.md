# LifeLoader

**LifeLoader: Loading moments, Sharing lives...**

  *Welcome to LifeLoader, your destination for blogging and social networking. Connect with others, share your thoughts, and explore a vibrant community.*

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [API Endpoints](#api-endpoints)
- [Demo Video](#demo-video)
- [Installation](#installation)
- [License](#license)

## Introduction

LifeLoader is an engaging platform where every moment is loaded with shared experiences, share your thoughts, engage in discussions, and build connections.

### Technologies used

- Django: The backend is powered by Django, providing a secure and scalable web framework.
- Bootstrap: Ensuring a responsive and visually appealing user interface.
- jQuery: Empowering the client to handle dynamic content loading, significantly optimizing server resources.
- RESTful API: Streamlining communication between the frontend and backend for optimal performance.
- HTML, CSS: Crafting the foundation for a dynamic and aesthetically pleasing user interface.
- SQLite: Serving as the database engine

## Features

### User Authentication

1. **Registration:**
   - Seamless user registration process with a clear and intuitive interface.
   <details>
     <summary>Click to view screenshot</summary>
    
     *Registering process.*
     ![User Registration Screenshot](images/register_1.png).
    <summary>Click to view screenshot</summary>
 
     *Account created successfully*
     ![User Registration Screenshot](images/register_2.png)
   </details>

2. **Login:**
   - Secure login functionality with robust password protection.
   <details>
     <summary>Click to view screenshots</summary>

     *Entering username and password.*
     ![Login Page Screenshot](images/login_1.png)

     *User successfully logged in, showing the dashboard.*
     ![Dashboard Screenshot](images/login_2.png)
   </details>

3. **Password Reset:**
   - Effortless password reset mechanism for user convenience.
   <details>
     <summary>Click to view screenshot</summary>

     *Request password reset.*
     ![Password Reset Screenshot](images/reset_1.png)

     *Email for creating new password has been sent*
     ![Password Reset Screenshot](images/reset_2.png)
     
     *Create new password.*
     ![Password Reset Screenshot](images/reset_3.png)
   </details>

### Social Networking

1. **Post Creation:**
   - Intuitive interface for creating and publishing posts.
   <details>
     <summary>Click to view screenshot</summary>
    
     *Write Post*
     ![Post Creation Screenshot](images/post_1.png)

     *Published successfully*
     ![Post Creation Screenshot](images/post_2.png)
   </details>

2. **Interaction:**
   - User-friendly features for liking and commenting on posts.
   <details>
     <summary>Click to view screenshot</summary>
     
     *Writing a comment*
     ![Post Interaction Screenshot](images/comment.png)

     *Liking a post*
     ![Post Interaction Screenshot](images/like.png)
   </details>

3. **Sorting Options:**
   - Explore posts based on latest, top likes, and top comments.
   <details>
     <summary>Click to view screenshot</summary>
     
     *Latest*
     ![Sorting Options Screenshot](images/order_1.png)

     *Top Comments*
     ![Sorting Options Screenshot](images/order_2.png)
     
     *Top Likes*
     ![Sorting Options Screenshot](images/order_3.png)
   </details>


### Profile Management

1. **Update Information:**
   - Easily update profile picture, email, username, and bio.
   <details>
     <summary>Click to view screenshot</summary>

     *The profile before any changes*
     ![Update Information Screenshot](images/profile_1.png)

     *Making Edits*
     ![Update Information Screenshot](images/profile_2.png)
     
     *Profile updated successfully*
     ![Update Information Screenshot](images/profile_3.png)

   </details>

2. **View Others' Profiles:**
   - Explore and view profiles of other users in the community.
   <details>
     <summary>Click to view screenshot</summary>
     
     ![View Others' Profiles Screenshot](images/view_1.png)
   </details>

### Search Functionality

1. **User Search:**
   - Efficient search functionality to find specific users.
   <details>
     <summary>Click to view screenshot</summary>
     
     ![User Search Screenshot](images/search_1.png)
   </details>

2. **Posts of a specific user:**
   - Find posts written by a specefic user
   <details>
     <summary>Click to view screenshot</summary>
     
     ![Post Search Screenshot](images/search_2.png)
   </details>

### Landing Page

- Having a visually good-looking landing page that describes the features of the website.
    <details>
     <summary>Click to view screenshot</summary>
     
     ![Landing Page Screenshot](images/landing.png)
    </details>

## API Endpoints

These APIs are seamlessly integrated with jQuery, optimizing backend server performance by enabling efficient retrieval of JSON data, which is then presented on the client frontend.

### 1. View Posts Ordered by Latest

- **Endpoint:** `/api/v1/posts/`
- **Description:** Fetches posts ordered by the latest.
- <details>
  <summary>Click to view screenshot</summary>

  ![View Latest Posts Screenshot](images/api_1.png)
</details>


### 2. View Posts Ordered by Top Likes

- **Endpoint:** `/api/v1/posts/top_likes/`
- **Description:** Fetches posts ordered by top likes.
- <details>
  <summary>Click to view screenshot</summary>

  ![View Top Likes Screenshot](images/api_2.png)
</details>

### 3. View Posts Ordered by Top Comments

- **Endpoint:** `/api/v1/posts/top_comments/`
- **Description:** Fetches posts ordered by top comments.
- <details>
  <summary>Click to view screenshot</summary>

  ![View Top Comments Screenshot](images/api_3.png)
</details>

### 4. View Comments on a Specific Post

- **Endpoint:** `/api/v1/posts/{post_id}/comments/`
- **Description:** Fetches comments on a specific post.
- <details>
  <summary>Click to view screenshot</summary>

  ![View Comments on Post Screenshot](images/api_7.png)
</details>

### 5. View Likes on a Specific Post

- **Endpoint:** `/api/v1/posts/{post_id}/likes/`
- **Description:** Fetches likes on a specific post.
- <details>
  <summary>Click to view screenshot</summary>

  ![View Likes on Post Screenshot](images/api_6.png)
</details>

### 6. Fetch Data of All Users Profiles

- **Endpoint:** `/api/v1/users/`
- **Description:** Fetches data of all user profiles.
- <details>
  <summary>Click to view screenshot</summary>

  ![Fetch User Profiles Screenshot](images/api_4.png)
</details>

### 7. View a Specific User Profile

- **Endpoint:** `/api/v1/users/{user_id}/`
- **Description:** Fetches data of a specific user profile.
- <details>
  <summary>Click to view screenshot</summary>

  ![View User Profile Screenshot](images/api_5.png)
</details>

### 8. Post Comment on a Specific Post (if logged in)

- **Endpoint:** `/api/v1/posts/{post_id}/comments/`
- **Description:** Allows the user to post a comment on a specific post (requires authentication).
- <details>
  <summary>Click to view screenshot</summary>

  *Adding a comment*
  ![Post Comment on Post Screenshot](images/api_8.png)

  *Added successfully*
    ![Post Comment on Post Screenshot](images/api_9.png)
</details>

## Demo Video

Check out the demo video to see the features in action:

[![Demo Video](images/landing.png)](demo_video/LifeLoader_demo.mp4)

Click on the image above to watch the demo video.

## Installation

Follow these steps to get your project up and running.

### Prerequisites

Before you begin, make sure you have the following installed:

- [Python](https://www.python.org/) (version 3)
- [Pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/your-username/your-project.git
```

### Navigate to the Project Directory

```bash
git clone https://github.com/your-username/your-project.git
```

### Create a Virtual Environment (Optional but recommended)

```bash
python -m venv venv
```

### Activate the Virtual Environment

- On Windows:
  
  ```bash
   venv\Scripts\activate
  ```

- On macOS/Linux:
  
  ```bash
  source venv/bin/activate
  ```

### Apply migrations

```bash
python manage.py migrate
```

### Create a Superuser (Optional but recommended)

```bash
python manage.py createsuperuser
```

### Run the Development Server

```bash
python manage.py runserver
```

Visit http://localhost:8000/ in your browser to see the application.

### License

This project is licensed under the MIT - see the LICENSE.md file for details.