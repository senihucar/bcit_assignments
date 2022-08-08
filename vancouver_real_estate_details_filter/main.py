import functions

if __name__ == '__main__':
    functions.open_and_write_txt_file('\\\\\search by city and bedroom number (Vancouver,3)\\\\\\\ \n')
    functions.search_by_city_and_bedroom_number('Vancouver', 3)
    functions.open_and_write_txt_file('\n\\\\\search by price range(550000,1000000 )\\\\\\\ \n')
    functions.search_by_price_range(550000, 1000000)
    functions.open_and_write_txt_file('\n\\\\\search by city and property type(Burnaby,House)\\\\\\\ \n')
    functions.search_by_city_and_property_type('Burnaby', 'House')
    functions.open_and_write_txt_file('\n\\\\\ reduce price\\\\\\\ \n')
    functions.reduce_price()
    functions.open_and_write_txt_file('\n\\\\\search_by_postal_code_range(V,7)\\\\\\\ \n')
    functions.search_by_postal_code_range('V', '7')
    functions.open_and_write_txt_file('\n\\\\\Details of the MLS : R2508895 : are\\\\\\\ \n')
    functions.get_listing('R2508895')
