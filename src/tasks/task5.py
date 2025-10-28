from to_do import TODO

def task5(scores: list[int]) -> list[int]:

        if len(scores) == 0:
            return [-1]

        result = []

        for index in range(len(scores)):
            if index < len(scores) - 1:
                result.append(scores[index] + scores[index + 1])
            else:
                result.append(scores[index] * scores[index])

        return result


if __name__ == "__main__":

    #scores = [3,5,7,2] ---> [8,12,9,4]
    print(task5(scores=[3,5,7,2]))
    #scores = [2,5,7,3] ---> [10,35,14,9]
    print(task5(scores=[2,5,7,3]))
    #scores = [] ---> [-1]
    print(task5(scores=[]))

