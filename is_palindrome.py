def is_palindrome(string):

    if string == string[::-1]:
     print('this string is pallindrome')
    else:
        print("this string is not pallindrome")

is_palindrome('fnrijegi')

# if spaces exists then
def is_palindrome(string):
    string = string.replace(' ','')
    if string == string[::-1]:
     print('this string is pallindrome')
    else:
        print("this string is not pallindrome")

(is_palindrome('ma da m'))