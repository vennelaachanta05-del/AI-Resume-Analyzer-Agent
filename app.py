
import streamlit as st
from pypdf import PdfReader
from agents import ResumeAgent, JobMatchingAgent, CareerAdviceAgent

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")

st.title("🤖 AI Resume Analyzer Agent")
st.write("Upload your resume and compare it with a job description.")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

job_description = st.text_area(
    "Paste the job description here",
    height=200
)

if st.button("Analyze Resume"):
    if uploaded_file is None:
        st.warning("Please upload your resume PDF.")
    elif not job_description.strip():
        st.warning("Please enter a job description.")
    else:
        try:
            reader = PdfReader(uploaded_file)
            resume_text = "\n".join(
                page.extract_text() or "" for page in reader.pages
            )

            if not resume_text.strip():
                st.error("No readable text found. Try a text-based PDF.")
            else:
                with st.spinner("Agents are analyzing your resume..."):
                    resume_agent = ResumeAgent()
                    matching_agent = JobMatchingAgent()
                    advice_agent = CareerAdviceAgent()

                    skills = resume_agent.extract_skills(resume_text)
                    matched, missing, score = matching_agent.compare_skills(
                        skills, job_description
                    )
                    advice = advice_agent.generate_advice(missing)

                st.subheader("📊 Analysis Results")
                st.metric("Job Skill Match", f"{score}%")

                st.subheader("✅ Skills Found in Your Resume")
                st.write(", ".join(skills) if skills else "No listed skills found.")

                st.subheader("🎯 Matching Skills")
                st.write(", ".join(matched) if matched else "No matching skills found.")

                st.subheader("📚 Skills to Develop")
                st.write(", ".join(missing) if missing else "No missing listed skills.")

                st.subheader("💡 Career Advice")
                for item in advice:
                    st.write(item)

                st.caption(
                    "This is a basic skills-based estimate, not an actual hiring probability."
                )

        except Exception as error:
            st.error(f"Could not analyze the PDF: {error}")
