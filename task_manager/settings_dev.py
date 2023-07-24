from .settings import *  # noqa: F403


DATABASES = {
    'default': dj_database_url.config(  # noqa: F405
        default='sqlite:///db.sqlite3',
        conn_max_age=600,
    )
}
