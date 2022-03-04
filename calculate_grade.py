# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
# Refactored.
import math


def display_grade_stat(read_inputs):
    """Gathers stats and print them out."""
    grade_list = read_inputs
    # Calculate the mean and standard deviation of the grades
    mean, standard_deviation = calculate_stat(grade_list)
    # print out the mean and standard deviation in a nice format.
    print_stat(mean, standard_deviation)
    return mean, round(standard_deviation, 3)


def calculate_stat(grade_list):
    """Calculate the mean and standard deviation of the grades."""
    total = 0
    for grade in grade_list:
        total = total + grade
    mean = total / len(grade_list)
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list))  # standard deviation
    return mean, sd


def print_stat(mean, sd):
    """print out the mean and standard deviation in a nice format."""
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')


display_grade_stat([12, 13, 41, 2, 3])
