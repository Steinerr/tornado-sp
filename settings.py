import os

# Proxy API version
from concurrent.futures import ThreadPoolExecutor

# from application.version import *

CNS_EVA_CODE = os.environ.get('CNS_EVA_CODE', '08')
SERVICE_COST = int(os.environ.get('SERVICE_COST', '5000'))

CONTRACT_ASSIGNMENT_START_ID = int(os.environ.get('CONTRACT_ASSIGNMENT_START_ID', 1))
CONTRACT_NUMBER_INC_LEN = 5
GLOBAL_BANK_OFFICE_ID = '99'

HOST = os.environ.get('HOST', '0.0.0.0')
PORT = int(os.environ.get('PORT', '8888'))

# request timeout
REQUEST_TIMEOUT = int(os.environ.get("REQUEST_TIMEOUT", 60))

# Real Host (e.g. eva.domclick.ru), when working under proxy
# Used to create direct links
REAL_HOST = os.environ.get('REAL_HOST', '')

# POL
# Deal integration
POL_URL = os.environ.get('POL_URL', '')
POL_CHECK_USER_BY_PHONE_URL = 'part/api/v1/deal/getByClient'
POL_CHECK_USER_BY_PASSPORT_URL = 'part/api/v2/deal/assessmentReport'
POL_SEND_REPORT_BY_PASSPORT_URL = 'part/api/v2/deal/assessmentReport'
POL_SEND_REPORT_BY_PHONE_URL = 'part/api/v1/deal/assessmentReport'
POL_DEBUG_RESPONSE = os.environ.get('POL_DEBUG', False)

# MIK / CIK integration
POL_REQUEST_BASE = 'part/api/v1/organization/'
POL_REQUEST_USER_METHOD = POL_REQUEST_BASE + 'getMIKs'
POL_REQUEST_OFFICE_METHOD = POL_REQUEST_BASE + 'getBankOffices'
POL_MAX_LIMIT = 200

# filegenerator integration
FILEGEN_API_HOST = os.environ.get('FILEGEN_API_HOST', 'http://api-filegenerator:8000/')

FILEGEN_API_URL = FILEGEN_API_HOST + 'api/v1/reports/'
FILEGEN_API_CONTRACT_ASSIGNMENT = FILEGEN_API_HOST + 'api/v1/contract_assignment'
FILEGEN_API_CONTRACT_COMPANY = FILEGEN_API_HOST + 'api/v1/contract_company'

# DaData

DATATA_URL = os.environ.get('DATATA_URL', 'https://suggestions.dadata.ru')

DADATA_ADDRESS_SUGGEST = os.environ.get('DADATA_ADDRESS_SUGGEST', '/suggestions/api/4_1/rs/suggest/address')
DADATA_INN_SUGGEST = os.environ.get('DADATA_ADDRESS_SUGGEST', '/suggestions/api/4_1/rs/suggest/party')
DADATA_BANK_SUGGEST = os.environ.get('DADATA_BANK_SUGGEST', '/suggestions/api/4_1/rs/suggest/bank')

DADATA_DEFAULT_COUNT = os.environ.get('DADATA_DEFAULT_COUNT', 10)

DADATA_API_KEY = os.environ.get('DADATA_API_KEY', '')

# Tornado debug settings (http://www.tornadoweb.org/en/stable/guide/running.html#debug-mode-and-automatic-reloading)
DEBUG = os.environ.get('DEBUG', False)

# Database connection string
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgres://user:dbpass@pg:5432/proxy_prj_db')

# Project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Changelog settings
CHANGELOG_SERVER = os.environ.get('CHANGELOG_SERVER', 'http://changelog:8000')

CHANGELOG_TABLELOG_URL = CHANGELOG_SERVER + os.environ.get('CHANGELOG_TABLELOG_URL', '/api/v1/tablelogs/')

# Filestorage settings
FILESTORAGE_SERVER = os.environ.get('FILESTORAGE_SERVER', 'http://storage:8000')

FILESTORAGE_DOCUMENT_URL = FILESTORAGE_SERVER + os.environ.get('FILESTORAGE_DOCUMENT_URL', '/api/v1/document/')

FILESTORAGE_FILE_URL = FILESTORAGE_SERVER + os.environ.get('FILESTORAGE_FILE_URL', '/api/v2/file/')
FILESTORAGE_REMOVE_FILE_URL = FILESTORAGE_SERVER + os.environ.get('FILESTORAGE_REMOVE_FILE_URL', '/api/v1/file/')

MAX_ALLOWED_FILE_SIZE = os.environ.get('MAX_ALLOWED_FILE_SIZE', 50000000)  # 50 Mb

STORAGE_LINK = '/gate/storage/api/v1/file/%s'

# Sentry logging
SENTRY_DSN = os.environ.get('SENTRY_DSN', '')

# Auth
AUTH_SERVER = os.environ.get('AUTH_SERVER', 'http://auth:8000')
AUTH_LOGIN = os.environ.get('AUTH_LOGIN', '')
AUTH_PASS = os.environ.get('AUTH_PASS', '')

# Resizer
RESIZER_SERVER = os.environ.get('RESIZER_SERVER', 'http://resizer:8080/path/')
RESIZED_IMAGE_TPL = '/gate/resizer/s300x-/path/%s'
# Migrate DB
MIGRATION_TOKEN = os.environ.get('MIGRATION_TOKEN', '')

# Mail
POSTMAN_SERVER = os.environ.get('POSTMAN_SERVER', 'http://postman.stat.sberned.ru/')
POSTMAN_LOGIN = os.environ.get('POSTMAN_LOGIN', '')
POSTMAN_PASSWORD = os.environ.get('POSTMAN_PASSWORD', '')
# Mail for "from" field of messages
MAIL_FROM_EMAIL = os.environ.get('MAIL_FROM_EMAIL', 'ocenka@domclick.ru')
MAIL_FROM_TEXT = os.environ.get('MAIL_FROM_TEXT', 'Центр недвижимости от сбербанка')

# Mail Templates
MAIL_TEMPLATE_PATH = os.path.join(BASE_DIR, 'application', 'mail', 'templates')

# Evaluator notification
TPL_SUBJECT_EVALUATOR_NOTIFY = 'subject_notify_evaluator.txt'
TPL_BODY_HTML_EVALUATOR_NOTIFY = 'body_notify_evaluator.html'
TPL_BODY_TEXT_EVALUATOR_NOTIFY = 'body_notify_evaluator.txt'

# Task not found notification
TPL_SUBJECT_TASK_NOT_FOUND = 'subject_task_not_found.txt'
TPL_BODY_HTML_TASK_NOT_FOUND = 'body_task_not_found.html'
TPL_BODY_TEXT_TASK_NOT_FOUND = 'body_task_not_found.txt'

# map for task settings
MAP_WIDTH = int(os.environ.get('MAP_WIDTH', 650))
MAP_HEIGHT = int(os.environ.get('MAP_HEIGHT', 450))
MAP_SCALE = int(os.environ.get('MAP_SCALE', 16))

LOG_CONFIG = {
    'version': 1,
    'formatters': {
        'detailed': {
            'format': '[%(asctime)s %(levelname)s] %(name)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
        },
        'file': {
            'level': 'INFO',
            'filename': '/tmp/task.log',
            'class': 'logging.FileHandler',
            'formatter': 'detailed'
        }
    },
    'loggers': {
        'application': {
            'handlers': ['console', 'file'],
            'propagate': False,
            'level': 'DEBUG' if DEBUG else 'INFO',
        },
        'tornado': {
            'handlers': ['console', 'file'],
            'propagate': False,
            'level': 'DEBUG' if DEBUG else 'INFO',
        },
        'peewee': {
            'handlers': ['console', 'file'],
            'propagate': False,
            'level': 'DEBUG' if DEBUG else 'INFO',
        },
    },
    'root': {
        'propagate': False
    }
}


SIGN_WSDL = os.environ.get('SIGN_WSDL', 'http://10.210.17.77:8102/digitalSignatureBoundary?wsdl')

THREAD_POOL_EXECUTOR = ThreadPoolExecutor()

FILE_API_HOST = os.environ.get('FILE_API_HOST', 'https://qa.domclick.ru/fs')
