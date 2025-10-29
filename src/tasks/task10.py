from to_do import TODO

def task10(classroom: list[str], student: str) -> int:

    
    result = 0

    for index, name in enumerate(classroom):
        if name.lower() == student.lower():
            result += index

    return result

if __name__ == "__main__":

    #classroom = ["Anna","Bob","anna","Eve","Anna"],student ="anna" ---> 6
    print(task10(classroom=["Anna","Bob","anna","Eve","Anna"],student="anna"))
    #classroom = ["Bob","BOb","anna","Eve"],student = "Bob" ---> 1
    print(task10(classroom=["Bob","BOb","anna","Eve"], student="Bob"))
    #classroom = ["Anna","Bob","anna","Anna"] student ="Eve" ---> 0
    print(task10(classroom=["Anna","Bob","anna","Anna"], student="Eve"))