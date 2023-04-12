# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Name: Mad Libs
Purpose: A mad lib project to refresh the basics. Based on the Kylie Ying
         tutorial at https://www.youtube.com/watch?v=8ext9G7xspg&t=100s.
Version: 20230411
License: MIT

Developer(s): Alan Redding (GitHub: alnrddng)
'''

def get_user_input():
    ''' request user input for the mad lib '''

    adj = str(input("Adjective: "))
    verb1 = str(input("Verb: "))
    verb2 = str(input("Verb: "))
    famous_person = str(input("Famous Person: "))

    return [adj, verb1, verb2, famous_person]

def main():
    ''' display the results of the mad lib '''

    madlib_input = get_user_input()

    print(f"Computer programming is so {madlib_input[0]}! It makes me so \
excited all the time because I love to {madlib_input[1]}. Stay hydrated \
and {madlib_input[2]} like you are {madlib_input[3]}!")

if __name__ == "__main__":
    main()
