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

def match_skills(resume_text):

    score = 0
    resume_text = resume_text.lower()

    for skill in skills_required:

        if skill in resume_text:
            score += 1

    percentage = (score / len(skills_required)) * 100

    return percentage