def compare_string(string, strings):
    verification = False
    new_string = ''
    for i in range(len(strings)):
        print(strings[i])
        if strings[i].lower() == string.lower():
            new_string = strings[i]
            verification = True
    return verification, new_string