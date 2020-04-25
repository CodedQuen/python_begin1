def search(sequence, number, lower, upper):
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower+upper)//2
        if number > sequence[middle]:
            return search(sequence, number, middle+1, upper)
        else:
            return search(sequence, number, lower, middle)

seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
print(search(seq, 34, 0, 7))
