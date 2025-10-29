from to_do import TODO


def task7(deliveries: list[int]) -> str:

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    highest_value = deliveries[0]

    result = 0

    for index, delivery in enumerate(deliveries[:5]):
        if delivery > highest_value:
            highest_value = delivery
            result = index

    return weekdays[result]

if __name__ == "__main__":

    #deliveries = [5,16,9,14,13,20,25] ---> [Tuesday]
    print(task7(deliveries=[5,16,9,14,13,20,25]))
    #deliveries = [15,6,9,14,13,20,25] ---> [Monday]
    print(task7(deliveries=[15,6,9,14,13,20,25]))
