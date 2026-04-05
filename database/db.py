from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["resume_ai_system"]

students = db["students"]
resumes = db["resumes"]
predictions = db["predictions"]