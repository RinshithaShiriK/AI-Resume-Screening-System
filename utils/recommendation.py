skills_required = [
    "python",
    "java",
    "machine learning",
    "sql",
    "data structures",
    "javascript",
    "react",
    "node"
]

def recommend_skills(resume_text):

    resume_text = resume_text.lower()

    missing_skills = []

    for skill in skills_required:
        if skill not in resume_text:
            missing_skills.append(skill)

    return missing_skills