def main(full_name):
    split_name = full_name.split()
    initials = [part[0].upper() + "." for part in split_name]
    return "".join(initials)
name = input("Enter Full Name: ")
print(main(name))

# Matthew Beekman
# 10/23/2024
# Program 1