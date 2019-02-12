def combine_words(word,**kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word +   kwargs['suffix']
    return word
print(combine_words('sangram',prefix = "Mr."))
print(combine_words('Mr D Bijay ',suffix= "Rao"))
print(combine_words("sk sahoo",))
