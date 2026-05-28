from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_resume(name, role, skills, experience):
    prompt = f"""Create a professional resume for:
Name: {name} | Target Role: {role}
Skills: {skills} | Experience: {experience}

Format with sections: Summary, Skills, Experience, Education
Make it ATS-friendly and impactful."""
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    resume = response.choices[0].message.content
    with open(f"{name.replace(' ','_')}_resume.md", 'w') as f:
        f.write(resume)
    print("Resume generated!")
    return resume

generate_resume("John Doe", "AI Engineer", 
               "Python, ML, OpenCV", "1 year internship")