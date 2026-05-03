import PyPDF2

# Important skills for placement
required_skills = [
    "python",
    "java",
    "sql",
    "machine learning",
    "data structures",
    "communication",
    "teamwork",
    "problem solving"
]

print("===== AI Resume Analyzer with PDF Upload =====")

# PDF file path input
file_path = input("Enter your Resume PDF file path: ")

try:
    # Open PDF file
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        resume_text = ""

        # Read all pages
        for page in reader.pages:
            resume_text += page.extract_text()

    resume_text = resume_text.lower()

    found_skills = []
    missing_skills = []

    # Skill checking
    for skill in required_skills:
        if skill in resume_text:
            found_skills.append(skill)
        else:
            missing_skills.append(skill)

    # Output
    print("\n===== Resume Analysis Result =====")

    print("\nSkills Found:")
    for skill in found_skills:
        print("-", skill)

    print("\nMissing Skills:")
    for skill in missing_skills:
        print("-", skill)

    # Score
    score = (len(found_skills) / len(required_skills)) * 100
    print("\nResume Score:", int(score), "/100")

    # Feedback
    if score >= 80:
        print("Excellent Resume for Placement!")
    elif score >= 50:
        print("Good Resume, but needs improvement.")
    else:
        print("Resume needs major improvement.")

except FileNotFoundError:
    print("File not found. Please check the path.")

except Exception as e:
    print("Error:", e)
    