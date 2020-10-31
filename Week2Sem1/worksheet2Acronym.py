user_input = input(" Please enter the words you want to convert to an acronym ")
def acronym_generator(a):
    print("print by fn ", a)
    a_list = a.split()
    acronym = ""
    for i in range(len(a_list)):
        acronym = acronym + a_list[i][0]
    print(acronym.upper())
acronym_generator(user_input)
