#check on emptiness, is palindrome and revert
def revert_string(txt):
    # emptiness check
    while not txt:
        print('String is empty')
        txt = input("Please enter a string to revert, not empty this time: ")
    # palindrome check
    return print('That\'s a palindrome, what did you expected?!')  if txt == txt[::-1] else print(txt[::-1])
###############################
# Asking user to type in string
string = input("Please enter a string to revert: ")

revert_string(string)


