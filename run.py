def toString(lst):
    return ''.join(lst)

def permute(a, l, r, valid_passwords):
    if l == r:
        perm_str = ''.join(a)
        if perm_str[0].isalpha() and not perm_str[0].isdigit():
            valid_passwords.append(perm_str)

    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r, valid_passwords)
            a[l], a[i] = a[i], a[l]  # backtrack

def permutations(password):
    # Convert the input password to a list of characters
    password_list = list(password)

    # Generate all permutations of the password
    valid_passwords = []
    permute(password_list, 0, len(password_list), valid_passwords)

    # Filter the valid passwords
    valid_passwords = set(valid_passwords)
    
    # Sort in the specified order
    sorted_passwords = sorted(valid_passwords, key=lambda x: (x.isdigit(), x.isupper(), x))

    # Print all valid permutations separated by space
    print(" ".join(sorted_passwords))

def main():
    user_input = input()
    permutations(user_input)

main()
