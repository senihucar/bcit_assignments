import listings

def open_and_write_txt_file(substring):
    f = open("report.txt", "a+")
    f.write(f"{substring}\n")
    f.close()
    return

def output_csv(mls):
    for houses in listings.house_dict.keys():
        if mls == houses:
            output = f"{houses},{listings.house_dict[houses]['adress']} {listings.house_dict[houses]['city']} " \
                     f"{listings.house_dict[houses]['province']} {listings.house_dict[houses]['post_code']}," \
                     f"{listings.house_dict[houses]['price']},{listings.house_dict[houses]['bedroom']}," \
                     f"{listings.house_dict[houses]['bathroom']},{listings.house_dict[houses]['property_type']}," \
                     f"{listings.house_dict[houses]['listing_day']}"
            return output

def search_by_city_and_bedroom_number(city_name,number_of_bedrooms):
    city_name = str(city_name.title())
    number_of_bedrooms = int(number_of_bedrooms)
    for houses in listings.house_dict.keys():
        city_dict = (listings.house_dict[houses]['city'])
        bedroom_dict = (listings.house_dict[houses]['bedroom'])
        if city_name == city_dict and number_of_bedrooms == bedroom_dict:
            open_and_write_txt_file(output_csv(houses))
    return

def search_by_price_range(minimum_price,maximum_price):
    minimum_price = int(minimum_price)
    maximum_price = int(maximum_price)
    for houses in listings.house_dict.keys():
        price = (listings.house_dict[houses]['price'])
        if price > minimum_price and price < maximum_price:
            open_and_write_txt_file(output_csv(houses))
    return

def search_by_city_and_property_type(city_name,property_type):
    city_name = str(city_name.title())
    property_type = str(property_type.title())
    for houses in listings.house_dict.keys():
        city_dict = (listings.house_dict[houses]['city'])
        property_dict = (listings.house_dict[houses]['property_type'])
        if city_name == city_dict and property_type == property_dict:
            open_and_write_txt_file(output_csv(houses))
    return

def reduce_price():
    for houses in listings.house_dict.keys():
        listing_day = (listings.house_dict[houses]['listing_day'])
        price = (listings.house_dict[houses]['price'])
        if listing_day > 30:
            price = price - 10000
            listings.house_dict[houses]['price'] = price
            open_and_write_txt_file(output_csv(houses))
    return

def search_by_postal_code_range(starting_character,ending_number):
    for houses in listings.house_dict.keys():
        post_code_dict = (listings.house_dict[houses]['post_code'])
        if starting_character == post_code_dict[0] and ending_number <= post_code_dict[-1]:
            open_and_write_txt_file(output_csv(houses))
    return

def get_listing(mls):
    for houses in listings.house_dict.keys():
        if mls == houses:
            open_and_write_txt_file("{"
                  f" 'MLS':{houses},'address':'{listings.house_dict[houses]['adress']} {listings.house_dict[houses]['city']}"
                  f" {listings.house_dict[houses]['province']} {listings.house_dict[houses]['post_code']}',"
                  f" 'price':'{listings.house_dict[houses]['price']}','bedrooms':'{listings.house_dict[houses]['bedroom']}',"
                  f" 'bathrooms':'{listings.house_dict[houses]['bathroom']}','property_type':'{listings.house_dict[houses]['property_type']}',"
                  f" 'active_listing_days':'{listings.house_dict[houses]['listing_day']}'" "}")

    return
