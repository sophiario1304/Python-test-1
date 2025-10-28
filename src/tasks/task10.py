from to_do import TODO

def task10(classroom: list[str], student: str) -> int:

    student_name = ["Anna","Eve","Bob"]
    result = []
    length_of_classroom = len(classroom)
    for student in enumerate(classroom):
        if student.count(student_name) in classroom:
            max_name = student_name > 1
            return max_name

if __name__ == "__main__":

    #classroom = ["Anna","Bob","anna","Eve","Anna"],student ="anna" ---> 6
    print(task10(classroom=["Anna","Bob","anna","Eve","Anna"],student="anna"))
    #classroom = ["Bob","BOb","anna","Eve"],student = "Bob" ---> 1
    print(task10(classroom=["Bob","BOb","anna","Eve"], student="Bob"))
    #classroom = ["Anna","Bob","anna","Anna"] student ="Eve" ---> 0
    print(task10(classroom=["Anna","Bob","anna","Anna"], student="Eve"))