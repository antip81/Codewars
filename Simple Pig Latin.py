# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.
#
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

# def pig_it(text):
#     #your code here

# test.assert_equals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
# test.assert_equals(pig_it('This is my string'),'hisTay siay ymay tringsay')

# "O tempora o mores !" -> 'Oay emporatay oay oresmay !'

def pig_it(text):
    result = ""
    for i in text.split(" "):
        if len(i) > 1:
            result += i[1:] + i[0] + "ay "
        elif i in ",.?!":
            result += i + " "
        else:
            result += i + "ay "
    return result.strip()
