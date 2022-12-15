import environ

CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # <-- And here
    ],
}


LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_REDIRECT_URL = 'entry-list'

env = environ.Env()
environ.Env.read_env()
TEST_USER = env('TEST_USER')
TEST_USER_PASSWORD = env('TEST_USER_PASSWORD')
