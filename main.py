# this program's function is to take a number from the user and for each character increase
# the value by one.
# ex: 12345 -> 23456
# 998 -> 10109

dict_num = {
    '0': '1',
    '1': '2',
    '2': '3',
    '3': '4',
    '4': '5',
    '5': '6',
    '6': '7',
    '7': '8',
    '8': '9',
    '9': '10',

}


def num_converter(num):
    temp_num = ""
    print("Num: " + str(num) + ".")
    for char in num:
        temp_num += (dict_num[char])
    print("Num: " + temp_num + ".")


while True:
    # loops until the user enters a numeric number only.
    while True:
        user_input = input("Please enter your number: ")
        try:
            if int(user_input):
                break
        except ValueError:
            print("Must enter a number!")

    num_converter(user_input)

    print("Thanks")
    break
