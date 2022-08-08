def get_total_items(set):
    return len(set)

def display_all_items(set):
    for val in set:
            print(val)
    return

def add_item(item,set):
    return set.add(item)

def remove_item(item,set):
    return set.discard(item)

def get_the_union_of(set1,set2):
    return set1.union(set2)
