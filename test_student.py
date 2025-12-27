from student.py import student_details

def test_student_details():
    expected_output=(
        "student name=Anusha\n"
        "student usn=0E318\n"
        "student div=E\n"
        "student age=20\n"
    )
    
    assert student_details("Anusha","0E318","E",20)==expected output