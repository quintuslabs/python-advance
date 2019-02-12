def single_letter_count(string,letter):
    return string.lower(). count(letter.lower())
print(single_letter_count('sangram','A'))

def multiple_letter_count(string):

    return {letter: string.count(letter) for letter in string}
print(multiple_letter_count('sojoeijeoaioie'))


def multiple_letter_count1(stringg):

    return [stringg.count(letterr) for letterr in stringg]
print(multiple_letter_count1('sojoeijeoaioie'))






