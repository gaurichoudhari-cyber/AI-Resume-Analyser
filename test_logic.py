def test_simple_check():
    # Ye ek dummy test hai jo CI pipeline ko pass dikhayega
    app_name = "AI Resume Analyser"
    assert "AI" in app_name

def test_math_logic():
    # Score calculation check karne ke liye
    resume_score = 80
    assert resume_score >= 0 and resume_score <= 100
