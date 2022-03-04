def second_largest(numbers):
    largest = 0
    second = 0
    for index in numbers:
        if largest < index:
            largest = index
    for index in numbers:
        if second < index and index < largest:
            second = index
    return second
def between(numbers,lower,upper):
    bet = []
    for index in numbers:
        if index >=lower and index <=upper:
            bet.append(index)
    return bet
def no_duplicates(numbers):
    copy = []
    for index in numbers:
        if not(index in copy):
            copy.append(index)
    return copy
def del_duplicate_adjacents(numbers):
    index = len(numbers)-1
    while index >0:
        if numbers[index] == numbers[index-1]:
            del numbers[index]
            index = index -1
        index = index - 1
    return numbers
def sum_sublists(lists):
    results=[]
    for index in lists:
        count = 0
        for endex in index:
            count = count + endex
        results.append(count)
    return results
def flatten(lists):
    results = []
    for index in lists:
        for endex in index:
            results.append(endex)
    return results
def is_median(number, target):
    index = 0
    half = (len(number)-1)/2
    while index <len(number):
        if number[index]==target:
            if number[index] == (half+1):
                return True
        index = index +1
    return False

def differences(numbers):
    results = []
    index = 0
    while index < len(numbers)-1:
        dif = numbers[index+1] - numbers[index]
        index +=1
        results.append(dif)
    return results
def odds_or_evens(numbers):
    odd = []
    even = []
    for index in numbers:
        if index%2==0:
            even.append(index)
        else:
            odd.append(index)
    if len(even) < len(odd):
        return odd
    else:
        return even
def running_total(numbers):
    results = []
    count = 0
    for index in numbers:
        count = count + index
        results.append(count)
    return results
def comma_separated(numbers):
    results=""
    results= str(numbers)
    return results
