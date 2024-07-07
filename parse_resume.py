import openai
import json

openai.api_key = 'YOUR_OPENAI_API_KEY'

def parse_resume(resume_text):
    prompt = f"""
    You are a resume parser. Given the following resume text, convert it into a JSON format with keys: "name," "contact_information," "summary," "experience," "education," "skills," and "projects." Ensure each key has an appropriate and structured value. Here's the resume:

    {resume_text}
    """

    response = openai.Completion.create(
      engine="text-davinci-004",
      prompt=prompt,
      max_tokens=1500,
      n=1,
      stop=None,
      temperature=0.5,
    )

    parsed_resume = response.choices[0].text.strip()
    try:
        return json.loads(parsed_resume)
    except json.JSONDecodeError:
        return {"error": "Failed to parse resume into JSON"}

resume_text = """
John Doe
john.doe@example.com
123-456-7890

Summary:
Experienced software developer with a background in AI and machine learning. Skilled in Python, Java, and database management.

Experience:
Software Developer at TechCorp (Jan 2020 - Present)
- Developed AI models for data analysis
- Collaborated with cross-functional teams

Education:
B.S. in Computer Science, XYZ University (2016 - 2020)

Skills:
- Python
- Java
- Machine Learning
- SQL

Projects:
- MentorApp: Developed using FlutterFlow and Firebase
- MedQuest: Involved in database/SQL development
- Chatbot Development: Used Dialogflow for customer service bot
"""

parsed_resume = parse_resume(resume_text)
print(json.dumps(parsed_resume, indent=2))

