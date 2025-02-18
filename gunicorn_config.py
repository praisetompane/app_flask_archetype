import os


workers = int(os.environ.get("GUNICORN_PROCESSES", "2"))

threads = int(os.environ.get("GUNICORN_THREADS", "4"))

# timeout = int(os.environ.get('GUNICORN_TIMEOUT', '120'))

bind = os.environ.get("GUNICORN_BIND", "0.0.0.0:8080")

wsgi_app = "src.app_flask_archetype.app:create_app()"

forwarded_allow_ips = "*"

secure_scheme_headers = {"X-Forwarded-Proto": "https"}
