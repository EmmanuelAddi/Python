
def translate(phrase) :
    translation = ""

    for letter in phrase:
        if letter.lower() in "aeiou" :
            if letter.isupper():
                translation = translation + "BA"
            else:
                translation = translation + "ba"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))