get=input("Please enter an e-mail adress:")
def is_valid(e_mail):
    at_symbol=0
    dot_symbol=0
    for symbol in e_mail:
        if symbol=="@":
            at_symbol+=1
        elif symbol==".":
            dot_symbol+=1
    if at_symbol>=1 and dot_symbol>=1:
        return True
    else:
        return False
print(is_valid(get))