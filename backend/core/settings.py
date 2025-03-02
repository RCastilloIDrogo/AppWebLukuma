from pathlib import Path
import environ
import pymysql
pymysql.install_as_MySQLdb()


# Definir BASE_DIR antes de cargar las variables de entorno
BASE_DIR = Path(__file__).resolve().parent.parent

# Cargar variables del archivo .env
env = environ.Env()
environ.Env.read_env(BASE_DIR / ".env")

# Seguridad: Obtener SECRET_KEY desde .env
SECRET_KEY = env("SECRET_KEY", default='django-insecure-default-key')

# Configuración de Debug segura
DEBUG = env.bool("DEBUG", default=True)

# Hosts permitidos
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps del sistema
    'productos',  # Gestión del menú y productos
    'mesas',      # Gestión de mesas y QR
    'pedidos',    # Gestión de pedidos
    'usuarios',   # Gestión de usuarios y roles

    # API
    'rest_framework',
    'corsheaders',
]

AUTH_USER_MODEL = 'usuarios.Usuario'

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Habilita CORS
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Permitir comunicación con Angular
CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",
]

# Para permitir todos los orígenes en desarrollo (Opcional)
CORS_ALLOW_ALL_ORIGINS = True  # ⚠️ Desactiva esto en producción

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Base de datos (Usar PostgreSQL en producción)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST", default="localhost"),
        'PORT': env("DB_PORT", default="3306"),
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        },
    }
}


# Validadores de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configuración de idioma y zona horaria
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = 'static/'

# Configuración de clave primaria automática
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
