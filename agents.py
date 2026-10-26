
import re

# Agent 1: Extract skills from text
class ResumeAgent:
    def extract_skills(self, text):
        skills_list = [
            "Python", "Java", "C", "C++",
            "HTML", "CSS", "JavaScript",
            "SQL", "DBMS", "Machine Learning",
            "Artificial Intelligence", "Data Structures",
            "Communication", "Git", "Flask"
        ]

        found_skills = []

        for skill in skills_list:
            pattern = r"\b" + re.escape(skill) + r"\b"
            if re.search(pattern, text, re.IGNORECASE):
                found_skills.append(skill)

        return found_skills


# Agent 2: Compare resume with job requirements
class JobMatchingAgent:
    def compare_skills(self, resume_skills, job_description):
        job_skills = ResumeAgent().extract_skills(job_description)

        matched = [
            skill for skill in resume_skills
            if skill.lower() in [s.lower() for s in job_skills]
        ]

        missing = [
            skill for skill in job_skills
            if skill.lower() not in [s.lower() for s in resume_skills]
        ]

        if job_skills:
            score = round(len(matched) / len(job_skills) * 100)
        else:
            score = 0

        return matched, missing, score


# Agent 3: Generate career advice
class CareerAdviceAgent:
    def generate_advice(self, missing_skills):
        if not missing_skills:
            return [
                "Your resume contains all the skills detected in the job description.",
                "Add measurable achievements to strengthen your resume."
            ]

        advice = [
            "Consider learning or demonstrating these skills:"
        ]

        for skill in missing_skills:
            advice.append(f"• {skill}")

        advice.append(
            "Add relevant projects and certifications where applicable."
        )

        return advice
