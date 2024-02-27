# Exercise 1

def count_vowels(word):
    count=0
    vowels=['a', 'e', 'i', 'o', 'u']
    for letter in word.lower():
        if letter in vowels:
            count+=1 
    print( f'"{word}" has {count} vowels.')

count_vowels("This is a longer response.")


# Exercise 2

def capitalize_names(names):
    new_names = [name.title() for name in names]
    print(new_names)

names1 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']
capitalize_names(names1)


# Bonus challenge :)

def capitalize_some_names(names):
    new_names = [name.title() for name in names if type(name) == str and name.lower() != 'bob' and name.lower() != 'max']
    print(new_names)

names2 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']
capitalize_some_names(names2)