from to_do import TODO


def task7(deliveries: list[int]) -> str:

    if len(deliveries) <= 7:
        return []

    result = deliveries[0]
    monday_to_friday = deliveries[:-2]
    for days in monday_to_friday:
        if days > result:
            result += days
    return list(result)


if __name__ == "__main__":

    #deliveries = [5,16,9,14,13,20,25] ---> [Tuesday]
    print(task7(deliveries=[5,16,9,14,13,20,25]))
    #deliveries = [15,6,9,14,13,20,25] ---> [Monday]
    print(task7(deliveries=[15,6,9,14,13,20,25]))
    #deliveries = [15,6,9,14,13] ---> []
    print(task7(deliveries=[]))