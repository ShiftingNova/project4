def second_largest(numbers):
    '''
    this function finds the second largest number un the list
    numbers:
        is a list that
    :return:
        returns the index of the second largest value in the list in a variable called second
    '''
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
    '''
    between returns all of the values from the list that are inbetween the paramaters (inclusive)
     numbers:
        a list
     lower:
        the lower value
    upper:
        the upper value
    :return:
    a list with the numbers inbetween the lower and upper paramaters(inbclusive) called bet
    '''
    bet = []
    for index in numbers:
        if index >=lower and index <=upper:
            bet.append(index)
    return bet
def no_duplicates(numbers):
    '''
    deletes all of the duplicates in the list "numbers"
     numbers:
        is the list that gets modified
    :return:
        a list called 'copy'
    '''
    copy = []
    for index in numbers:
        if not(index in copy):
            copy.append(index)
    return copy
def del_duplicate_adjacents(numbers):
    '''
    this function only deletes the duplicate numbers that are next to each other in the list 'numbers'
    :param numbers:
        is the list that gets modified
    :return:
     none
    '''
    index = len(numbers)-1
    while index >0:
        if numbers[index] == numbers[index-1]:
            del numbers[index]
            index = index -1
        index = index - 1
    #return numbers
def sum_sublists(lists):
    '''
    adds tha values off all the sub-0lists together
    :param lists:
        is the 2D list that gets its values added up and put into another list
    :return:
        the list of sums called "results"
    '''
    results=[]
    for index in lists:
        count = 0
        for endex in index:
            count = count + endex
        results.append(count)
    return results
def flatten(lists):
    '''
    this function turns the 2D list into a a single list
    :param lists:
        is the 2d list
    :return:
     a list of all of the values called "results"
    '''
    results = []
    for index in lists:
        for endex in index:
            results.append(endex)
    return results
def is_median(number, target):
    '''
    this function findses if the target value is the median
    :param number:
        the list that is used to find the median
    :param target:
        is what the function is trying to see if the median is this value
    :return:
    True or False depending if "target" is equal to the median
    '''
    index = 0
    half = (len(number)-1)/2
    while index <len(number):
        if index == (half):
            if number[index]==target:
                return True
        index = index +1
    return False

def differences(numbers):
    '''
    this function creates a list based off of how the values in the list differ from one another
    :param numbers:
    the list of values
    :return:
    returns a list called "results" where values came from numbers
    '''
    results = []
    index = 0
    while index < len(numbers)-1:
        dif = numbers[index+1] - numbers[index]
        index +=1
        results.append(dif)
    return results
def odds_or_evens(numbers):
    '''
    this function counts the total odd and even values in hte list "numbers" and puts them all into their own respective lists
    :param numbers:
        is the list where the list "odd" and the list "even" gets their names from
    :return:
    which ever list (odd or even) depending on whice one is lager and if they are the same length it returns even
    '''
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
    '''
    this function keeps a running total if all the values in a list then adds those values to another list
    :param numbers:
    its the list where all of the values are added up then added to another list
    :return:
    the list "results" where all of the numbers are added up
    '''
    results = []
    count = 0
    for index in numbers:
        count = count + index
        results.append(count)
    return results
def comma_separated(numbers):
    '''
    this function turns a list into a string with the commas incuded
    :param numbers:
    the list that gets turned into a string
    :return:
         a string value called "results" and is based of of the list "numbers"
    '''
    results=""
    results= str(numbers)
    return results

