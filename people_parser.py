from itertools import zip_longest 

def people_sorted(name_file, hobby_file, sorted_file):
    with open(name_file, 'r', encoding='utf-8') as name, \
        open(hobby_file, 'r', encoding='utf-8') as hobby, \
        open(sorted_file, 'a', encoding='utf-8') as sorted:

        for user_name, hobbies in zip_longest(name, hobby):
            if user_name is None:
                exit(1)
            else:
                user_name = user_name.strip()
                if hobbies is not None:
                    hobbies = hobbies.strip()
                sorted.write(f'{user_name}: {hobbies}\n')


people_sorted('name.csv', 'hobby.csv', 'sorted_people.csv')