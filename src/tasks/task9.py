from to_do import TODO


def task9(username: str) -> bool:

    if len(username) <= 5 and len(username) >= 12:
        return False

    for index,letter in enumerate(username):

        if index == 0 and username.isalpha():
            return True
        elif letter == username.isupper() >1:
            return True
        elif letter == username.islower() >1:
            return True
        elif letter == username.isdigit() >1:
            return True
        elif username == "_" not in username[-1]:
            return True
        else:
            return False

if __name__ == "__main__":

    #username = Alex_9 ---> True
    print(task9(username="Alex_9"))
    #username = 9alexA ---> False
    print(task9(username="9alexA"))