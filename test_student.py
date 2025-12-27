from student import student_details
def test_student_details():
    name="Anusha"
    usn="0E318"
    div="E"
    age=20
    expected_output=(
    "student name:Anusha\n"
    "student usn:0E318\n"
    "student div:E\n"
    "student age:20\n"
    )
    assert student_details(name, usn, div,age) == expected_output
