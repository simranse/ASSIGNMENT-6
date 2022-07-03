#Program5:

def sort_hyphen(str):
    l=str.split("-")
    l.sort()
    return "-".join(l)
string=input("Enter any string: ")
print(sort_hyphen(string))
