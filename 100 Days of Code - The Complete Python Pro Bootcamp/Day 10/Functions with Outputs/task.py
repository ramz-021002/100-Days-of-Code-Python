def format_name(firstname, lastname):
    return firstname.title(), lastname.title()
    # first_name = firstname[0].capitalize()
    # first_name += firstname[1:len(firstname)].lower()
    # last_name = lastname[0].capitalize()
    # last_name += lastname[1:len(lastname)].lower()
    # return first_name, last_name

f_name = "angelia"
l_name = "yun"
final_first, final_last = format_name(f_name,l_name)
print(final_first, final_last)