web: gunicorn djangochat.wsgi --preload --log-file -
web: daphne djangochat.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v2
chatworker: python manage.py runworker --settings=chat.settings -v2


