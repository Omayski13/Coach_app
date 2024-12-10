# ⚽Coach_app

**BG Football Trener** is a dedicated platform created by football coaches, for football coaches. The primary goal of this platform is to foster collaboration and knowledge sharing among coaches, regardless of their experience or level of expertise. 

Whether you're coaching grassroots teams or professional players, BG Football Trener provides the tools and resources you need to **grow as a coach and improve** your training methods.

## 🌐Deployment
You can view the live version of the project here: [Live Demo](https://bg-trener-bbe3fjc8g0aqgsbz.italynorth-01.azurewebsites.net/).

## 🔧Testing User Accounts
| Role | Username | Email | Password |
|----------|----------|----------|----------|
| superuser | admin | admin@admin.com | admin |
| staff | staff1 | staff1@gmail.com | Vrubnica1@ |
|common user| user1| user1@gmail.com | Nadejda1@ |

## 🌟Features
- **Training Session Management:** Share,organize, and discover drills and exercises for *7 age groups* and *6 different focuses* of the training:
- **Community Engagement:** Connect with fellow coaches through *shared content, comments, and likes* on training sessions and posts.
- **Customizable Filters, Sorting and Search:** Discover drills by age, focus, or popularity, with options to *sort by latest, most popular, or most discussed*.
- **User Profiles:** **Create and manage** your coaching profile, *track your shared content*, and interact with other users.
- **Approval System:** Ensure high-quality content by *approving* user-submitted drills.
- **Secure Authentication:** Log in securely with *custom user authentication*.

## 💻Technical Overview
- Built With: **Django Framework (Python)**
- Database: **PostgreSQL**
- Front-End Styling: **Custom CSS** for a unique and responsive user interface
- Authentication: **Custom authentication** backend with **support for email or username login**
- Forms: Built-in Django forms with **custom validation for login and registration**.


# 🚀Project setup

### 1. Clone the repo
   
  ```terminal

    git clone https://github.com/Omayski13/Coach_app.git

  ```

### 2.Create and Activate a Virtual Environment
**Run the following command to create a virtual environment:**

   ```terminal
   python -m venv venv

   ```
**Activate the virtual environment**
- *For Windows:*
   ```
   venv\Scripts\activate
   ```

- *For macOS (or Linux):*
  ```
   source venv/bin/activate
   ```

### 3. Install dependencies
 
   ```terminal
   
     pip install -r requirements.txt
  
   ```

### 4. Change DB settings in settings.py

  ```py
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "your_db_name",
            "USER": "your_username",
            "PASSWORD": "your_pass",
            "HOST": "127.0.0.1",
            "PORT": "5432",
        }
    }
  ```

### 5. Run the migrations

  ```terminal

    python manage.py migrate

  ```

### 6. Run the project

  ```terminal

    python manage.py runserver

  ```
