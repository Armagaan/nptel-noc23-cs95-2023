# Matching round braces

def matched(my_string):
    counter = 0
    # iterate over the characters
    for char in my_string:
        # if character == (
        if char == "(":
            # increment counter
            counter += 1
        # if character == )
        elif char == ")":
            # decrement counter
            counter -= 1
            if counter < 0:
                return False
    if counter == 0:
        return True
    else:
        return False


print(matched("zb%78"))
print(matched("(7)(a"))
print(matched("a)*(?"))
print(matched("((jkl)78(A)&l(8(dd(FJI:),):)?)"))
print(matched("(( apple"))
print(matched(")hello("))
