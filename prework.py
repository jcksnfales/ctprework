print("hello world")

# Question 1: hello_name(user_name)
def hello_name(user_name):
    print("hello_%s" % user_name)


# Question 2: first_odds()
def first_odds():
    found_odds = []

    for i in range(100): # loop through all numbers 'i' from 0-100
        # add any odd values of 'i' to the list 'found_odds'
        if(i % 2 == 1): found_odds.append(i)
            
    print(found_odds) # print the final value of 'found_odds'


# Question 3: max_num_in_list(a_list)
def max_num_in_list(a_list):
    max_num = 0 # tracks the currently-found maximum
    
    for n in a_list: # loop through all values 'n' in 'a_list'
        # replace max_num with any greater values if found
        if(max_num < n): max_num = n 
    
    return max_num # return final value of 'max_num'


# Question 4: is_leap_year(year)
def is_leap_year(year):
    # return True when the given year is either:
    #   divisible by 4 and NOT divisible by 100
    #       OR
    #   divisible by 400     
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)


# Question 5: is_consecutive(a_list)
def is_consecutive(a_list):
    index = 1 # tracks the current index, starting from the second value of 'a_list'
    
    while(index < len(a_list)):
        if(a_list[index] == (a_list[index - 1] + 1)): # if the current index value is 1 greater than the previous index value, increment 'index' and continue 
            index = index + 1
        else: return False # if the current index value is ever not 1 greater than the previous index value, the list can't be continuous; return False

    return True # if a discontinuity is never found, return True


# Test cases
# Q1
hello_name("Jack")
# Q2
first_odds()
# Q3
q3_test_list = [4,8,15,16,28,42,42,69,13,2,6,3,6,9,4,17,6]
print("Q3: In the list {0}, the greatest value is {1}".format(q3_test_list, max_num_in_list(q3_test_list)))
# Q4
q4_year = 2000
print("Q4: Is {0} a leap year? {1}".format(q4_year, is_leap_year(q4_year)))
# Q5
q5_consecutive_list = [2,3,4,5,6,7]
q5_nonconsecutive_list = [1,2,4,5]
print("Q5: Is {0} continuous? {1}".format(q5_consecutive_list, is_consecutive(q5_consecutive_list)))
print("Q5: Is {0} continuous? {1}".format(q5_nonconsecutive_list, is_consecutive(q5_nonconsecutive_list)))