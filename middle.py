

def middle(lst):
    new = lst[1:]
    # lst = lst[:-1]
    del new[-1]
    print(new)

lst = [1,2,33,4,5]
middle(lst)
