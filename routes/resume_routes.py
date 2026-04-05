from flask import Blueprint, render_template, request
import os

from utils.resume_parser import extract_text
from utils.skill_matcher import match_skills
from models.placement_model import predict_placement
from utils.recommendation import recommend_skills

resume_bp = Blueprint("resume", __name__)


@resume_bp.route("/")
def home():
    return render_template("index.html")


@resume_bp.route("/upload", methods=["POST"])
def upload_resume():

    file = request.files["resume"]

    filepath = os.path.join("uploads", file.filename)
    file.save(filepath)

    resume_text = extract_text(filepath)

    score = match_skills(resume_text)

    placement = predict_placement(score)

    skills = recommend_skills(resume_text)

    return render_template(
        "dashboard.html",
        score=score,
        placement=placement,
        skills=skills
    )