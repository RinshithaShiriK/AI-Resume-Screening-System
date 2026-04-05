import os

class Config:
    SECRET_KEY = "resume_ai_secret_key"
    UPLOAD_FOLDER = "uploads"
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB file limit