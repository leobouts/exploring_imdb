def get_J_Similarity(list_a, list_b):
    
    set_a = set(list_a)
    set_b = set(list_b)

    return (len(set_a.intersection(set_b)) / len(set_a.union(set_b)))