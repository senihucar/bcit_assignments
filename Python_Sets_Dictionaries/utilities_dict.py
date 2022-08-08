#PART B
def display_all(this_dict):
    for key, value in this_dict.items():
        print(f"'{value}' is the capital city of '{key}'")
    return
def get_capital_city(province_name,this_dict):
    province_name = province_name.title()
    if province_name in this_dict.keys():
        print(f"The capital city of '{province_name}' is '{this_dict.get(province_name)}'.")
    return
def add_element(province_name,capital_city,this_dict):
    province_name = province_name.title()
    capital_city = capital_city.title()
    this_dict[province_name] = capital_city
    return
def remove_item(province_name,this_dict):
    province_name = province_name.title()
    del this_dict[province_name]
    return

#PART C
def get_total_population(this_dict):
    sum = 0
    for details in this_dict.values():
        for population in details.values():
            if isinstance(population, int) == True:
                sum = (sum + population)
    return sum
def get_another_capital_city(province_name, this_dict):
    province_name = str(province_name.title())
    if province_name in this_dict.keys():
        capital_var = this_dict[province_name]['capital']
        return capital_var
    else:
        return ''
def get_largest_city(province_name,this_dict):
    province_name = str(province_name.title())
    if province_name in this_dict.keys():
        capital_var = this_dict[province_name]['largest']
        return capital_var
    else:
        return ''
def get_smallest_province(this_dict):
    min_value = float("inf")
    province_and_population = []
    for province in this_dict.keys():
        population = (this_dict[province]['population'])
        if population == min_value:
            province_and_population.append(province)
            province_and_population.append(population)
        if population < min_value:
            min_value = population
            province_and_population = []
            province_and_population.append(province)
            province_and_population.append(population)
    return province_and_population
def get_largest_province(this_dict):
    max_value = float("-inf")
    province_and_population = []
    for province in this_dict.keys():
        population = (this_dict[province]['population'])
        if population == max_value:
            province_and_population.append(province)
            province_and_population.append(population)
        if population > max_value:
            max_value = population
            province_and_population = []
            province_and_population.append(province)
            province_and_population.append(population)
    return province_and_population
def get_province_description(province_name,this_dict):
    province_name = str(province_name.title())
    if province_name in this_dict.keys():
        capital_var = this_dict[province_name]['capital']
        largest_var = this_dict[province_name]['largest']
        population_var = this_dict[province_name]['population']
        display = f"{province_name} has a population of {population_var} whose capital is {capital_var} and largest city is {largest_var}."
        return display
    else:
        return ''
