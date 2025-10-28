from to_do import TODO

def task3(temperatures: list[int]) -> str:

    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    min_temp = temperatures[0]
    min_index = 0

    for number in range(len(temperatures)):
        if temperatures[number] < min_temp:
            min_temp = temperatures[number]
            min_index = number

    result = months[min_index]
    return result

if __name__ == "__main__":

    # temperatures = [-2,0, 5, 9, 15, 20, 22, 21, 16, 10, 4, -1] ---> January
    print(task3(temperatures=[-2,0, 5, 9, 15, 20, 22, 21, 16, 10, 4, -1]))
    # temperature = [4,0, 5, 9, 15, 20, 22, 21, 16, 10, 4, -1] ---> December
    print(task3(temperatures=[4,0, 5, 9, 15, 20, 22, 21, 16, 10, 4, -1]))
