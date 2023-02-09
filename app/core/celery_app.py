from celery import Celery
from dotenv import load_dotenv
import os


load_dotenv()

celery_app = Celery(
    "worker",
    broker=os.environ.get("MESSAGE_BROCKER_URL"),
    backend=os.environ.get("CELERY_POSTGRES_URL"),
)
