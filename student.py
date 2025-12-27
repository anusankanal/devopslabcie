def student_details(name,usn,div,age):
    result=(
        f"student name:{name}\n"
        f"student usn:{usn}\n"
        f"student div:{div}\n"
        f"student age:{age}\n"
    )
    return result
    if __name=="__main__":
        name="Anusha"
        usn="0E318"
        div="E"
        age=20
        print(student_details(name,usn,div,age))