from to_do import TODO

def task2(votes: str) -> str:

    count_a = votes.count("A")
    count_b = votes.count("B")
    count_c = votes.count("C")
    count_d = votes.count("D")

    if count_a > count_b and count_a > count_c and count_a > count_d:
        result = "Alice"
    elif count_b > count_a and count_b > count_c and count_b > count_d:
        result = "Bob"
    elif count_c > count_a and count_c > count_b and count_c > count_d:
        result = "Carol"
    else:
        result = "David"

    return result

if __name__ == "__main__":

    #votes = "CBBDAAB" ---> "Bob"
    print(task2(votes="CBBDAB"))
    #votes = "AABOD" ---> "Alice"
    print(task2(votes="AABOD"))
