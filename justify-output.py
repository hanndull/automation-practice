import os

terminal_width = os.get_terminal_size().columns

user_input = input("What do you want to say? ")

print(user_input.center(terminal_width).title())
print(user_input.ljust(terminal_width).title())
print(user_input.rjust(terminal_width).title())