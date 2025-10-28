from to_do import TODO

def task1(weather: str) -> str:

    middle_index = len(weather) // 2
    middle_char = weather[middle_index]

    if middle_char == "S":
        return "Sunny"
    elif middle_char == "C":
        return "Cloudy"
    elif middle_char == "R":
        return "Rainy"
    elif middle_char == "T":
        return "Storm"
    else:
        return "error"

    
if __name__ == "__main__":

    #weather = "SCRTS" ---> Rainy
    print(task1(weather="SCRTS"))
    #weather = "MACON ---> Cloudly
    print(task1(weather="MACON"))



