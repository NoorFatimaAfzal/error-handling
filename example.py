elt = [[['peter', 'parker'], [10.0, 5.0, 85.0]], 
[['bruce', 'wayne'], [10.0, 8.0, 74.0]],
[['captain', 'america'], [8.0,10.0,96.0]],
[['deadpool'], []]]
def get_stats(class_list):
    new_stats = []
    try:
        for elt in class_list:
            new_stats.append([elt[0], elt[1], avg(elt[1])])
    except Exception as a:
        print(a)
        return new_stats
    else:
        print("avg 0 nahi howa")
        return new_stats 
    finally: 
        print("is nahi chlna he chalna")
        return new_stats
def avg(grades):
    return sum(grades)/len(grades)

print(get_stats(elt))