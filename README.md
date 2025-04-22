# JFlix - Netflix Clone

A Netflix clone built with Django.

## Local Development

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ProjetoNetflix
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with the following content:
   ```
   SECRET_KEY=your-secret-key
   DEBUG=True
   ```

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Visit http://127.0.0.1:8000/ in your browser.

## Deploying to Heroku

1. Create a Heroku account if you don't have one: https://signup.heroku.com/

2. Install the Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli

3. Login to Heroku:
   ```
   heroku login
   ```

4. Create a new Heroku app:
   ```
   heroku create your-app-name
   ```

5. Add a PostgreSQL database:
   ```
   heroku addons:create heroku-postgresql:mini
   ```

6. Configure environment variables:
   ```
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   ```

7. Push your code to Heroku:
   ```
   git push heroku main
   ```

8. Run migrations on Heroku:
   ```
   heroku run python manage.py migrate
   ```

9. Create a superuser on Heroku:
   ```
   heroku run python manage.py createsuperuser
   ```

10. Open your app:
    ```
    heroku open
    ```

## Media Files

For production, you should use a service like AWS S3 to store media files. Heroku has an ephemeral filesystem, which means any uploaded files will be lost when the dyno restarts.

## Troubleshooting

If you encounter any issues with static files, try running:
```
python manage.py collectstatic
```

### Case Sensitivity in Static Files

Heroku's file system is case-sensitive, unlike Windows. Make sure that the file names in your templates match exactly with the actual file names in your static directories, including the correct capitalization. For example, if your file is named `JFlix.png`, referencing it as `jflix.png` or `Jflix.png` will work locally on Windows but fail on Heroku.

For more information on deploying Django applications to Heroku, see the [Heroku Django documentation](https://devcenter.heroku.com/articles/django-app-configuration).
