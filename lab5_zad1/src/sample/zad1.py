class hamming:
    def __init__(self):
        pass
    def distance(a, b):
        if len(a) == len(b):
            result = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    result += 1
                else:
                    pass
            return result
        else:
            raise ValueError("Not equal lengths")