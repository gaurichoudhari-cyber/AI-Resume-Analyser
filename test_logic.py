def test_simple_check():
    
    app_name = "AI Resume Analyser"
    assert "AI" in app_name

def test_math_logic():
   
    resume_score = 80
    assert resume_score >= 0 and resume_score <= 100
