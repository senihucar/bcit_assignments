import utilities_sets
import utilities_dict

set1 = {"apple","banana", "orange", "peach"}
set2 = {"banana","pineapple", "peach", "watermelon"}
canadian_provinces = {
        'Ontario': 'Toronto',
        'Quebec': 'Quebec City',
        'Nova Scotia': 'Halifax',
        'New Brunswick': 'Fredericton',
        'Manitoba': 'Winnipeg',
        'British Columbia': 'Victoria',
        'Prince Edward Island': 'Charlottetown',
        'Saskatchewan': 'Regina',
        'Alberta': 'Edmonton',
        'Newfoundland': "St.John's",
        'Northwest Territories': 'Yellowknife',
        'Yukon': 'Whitehorse',
        'Nunavut': 'Iqaluit',
    }
canadian_provinces_details = {
        'Ontario': {'capital': 'Toronto', 'largest': 'Toronto', 'population': 14734014},
        'Quebec': {'capital': 'Quebec City', 'largest': 'Montreal', 'population': 8574571},
        'Nova Scotia': {'capital': 'Halifax', 'largest': 'Halifax', 'population': 979351},
        'New Brunswick': {'capital': 'Fredericton', 'largest': 'Moncton', 'population': 781476},
        'Manitoba': {'capital': 'Winnipeg', 'largest': 'Winnipeg', 'population': 1379263},
        'British Columbia': {'capital': 'Victoria', 'largest': 'Vancouver', 'population': 5147712},
        'Prince Edward Island': {'capital': 'Charlottetown', 'largest': 'Charlottetown', 'population': 159625},
        'Saskatchewan': {'capital': 'Regina', 'largest': 'Saskatoon', 'population': 1178681},
        'Alberta': {'capital': 'Edmonton', 'largest': 'Calgary', 'population': 4421876},
        'Newfoundland': {'capital': "St. John's", 'largest': "St. John's", 'population': 522103},
        'Northwest Territories': {'capital': 'Yellowknife', 'largest': 'Yellowknife', 'population': 45161},
        'Yukon': {'capital': 'Whitehorse', 'largest': 'Whitehorse', 'population': 42052},
        'Nunavut': {'capital': 'Iqaluit', 'largest': 'Iqaluit', 'population': 39353},
    }

if __name__ == '__main__':
    #PART A
    print("///////////////////////////////////////\n\t\tPART A \n///////////////////////////////////////\n")
    print("\nThis is Set1 : ",set1,"\nThis is Set2 : ",set2)
    utilities_sets.add_item("strawberry",set1)
    print(f"\nAdded ‘strawberry’ to the Set1 and the resulting Set1 is:\n")
    utilities_sets.display_all_items(set1)
    print("\nTotal items number of Set1:", utilities_sets.get_total_items(set1))
    utilities_sets.add_item("cherry", set2)
    print("\nAdded ‘cherry’ to the Set2 and the resulting Set2 is:\n")
    utilities_sets.display_all_items(set2)
    print("\nTotal items number of Set2:", utilities_sets.get_total_items(set2))
    utilities_sets.remove_item("strawberry", set2)
    print("\nRemoved ‘strawberry’ to the Set1 and the resulting Set1 is:\n")
    utilities_sets.display_all_items(set1)
    print("\nUpdated total items number of Set1:", utilities_sets.get_total_items(set1))
    utilities_sets.remove_item("cherry", set2)
    print("\nRemoved ‘cherry’ to the Set2 and the resulting Set2 is:\n")
    utilities_sets.display_all_items(set2)
    print("\nUpdated total items number of Set2:", utilities_sets.get_total_items(set2))
    print("\nUnion of the Set1 and Set2:\n")
    utilities_sets.display_all_items(utilities_sets.get_the_union_of(set1, set2))
    print("\nTotal items number of union Set1 and Set2:", utilities_sets.get_total_items(utilities_sets.get_the_union_of(set1,set2)))
    # PART B
    print("\n///////////////////////////////////////\n\t\tPART B \n///////////////////////////////////////\n\n")
    print("\nThis is Canadian Provinces Dictionary : ", canadian_provinces,"\n\n")
    utilities_dict.display_all(canadian_provinces)
    utilities_dict.get_capital_city('British Columbia', canadian_provinces)
    f"\n{utilities_dict.add_element('bc', 'vancouver', canadian_provinces)}"
    print(f"\n Added ‘bc’ 'vancouver' to the dictionary and result:\n {canadian_provinces}")
    utilities_dict.remove_item('bc', canadian_provinces)
    print(f"\n Removed ‘bc’ 'vancouver' to the dictionary and result:\n {canadian_provinces}")
    #PART C
    print("\n///////////////////////////////////////\n\t\tPART C \n///////////////////////////////////////\n\n")
    print(f"\nThe total population of all provinces in Canada is {utilities_dict.get_total_population(canadian_provinces_details)}")
    print(utilities_dict.get_another_capital_city('British Columbia', canadian_provinces_details))
    print(utilities_dict.get_largest_city('Quebec', canadian_provinces_details))
    print(utilities_dict.get_smallest_province(canadian_provinces_details))
    print(utilities_dict.get_largest_province(canadian_provinces_details))
    print(utilities_dict.get_province_description('British Columbia', canadian_provinces_details))
