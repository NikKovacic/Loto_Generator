# -*- coding: utf-8 -*-

import random


def generate_loto_num(loto_num):
    num_list = []

    while True:
        if len(num_list) == loto_num:
            break

        loto_number = random.randint(1, 50)

        if loto_number not in num_list:
            num_list.append(loto_number)

    return num_list


def main():
    print "Welcome to the Lottery numbers generator. "
    loto_num_question = raw_input("Please enter how many random numbers would you like to have: ")

    try:
        loto_numbers = int(loto_num_question)
        print generate_loto_num(loto_numbers)
    except ValueError:
        print ("Error! Please enter a number. ")

    print "END"


if __name__ == "__main__":
    main()
