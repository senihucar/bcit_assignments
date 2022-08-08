def add_element_dict(category,item,this_dict):
    this_dict[category] = item
    return

def adress_creator(y):
    for x in range((len(y) - 4)):
        return y[x]

def dict_creator(filename="listings.txt"):
    with open(filename, "r") as f:
        lines = f.readlines()
        i = 0
        while i == len(lines):
            for line in lines:
                details_dict = {}
                x = line.split(",")
                y = x[1].split(" ")
                adress = ' '.join(y[0:-4])
                city = (f"{y[-4]}")
                province = (f"{y[-3]}")
                post_code = (f"{y[-2]} {y[-1]}")
                add_element_dict('adress',adress,details_dict)
                add_element_dict('city', city ,details_dict)
                add_element_dict('province', province ,details_dict)
                add_element_dict('post_code', post_code ,details_dict)
                add_element_dict('price',x[2],details_dict)
                add_element_dict('bedroom',x[3], details_dict)
                add_element_dict('bathroom',x[4],details_dict)
                add_element_dict('property_type',x[5],details_dict)
                add_element_dict('listing_day',x[6],details_dict)
                i = i + 1
        i = 0
        while i == len(lines):
            for line in lines:
                house_dict_2 = {}
                x = line.split(",")
                house_dict[x[i]] = details_dict
                i = i + 1
            return house_dict_2

print(dict_creator())

house_dict = {
    'R2507956': {'adress': '2242 Grant Street', 'city': 'Vancouver', 'province': 'BC', 'post_code': 'V5L 2Z7',
                 'price': 1699000, 'bedroom': 5, 'bathroom': 2, 'property_type': 'House','listing_day': 13},
    'R2500627': {'adress': '305-1006 Beach Avenue', 'city': 'Vancouver', 'province': 'BC', 'post_code': 'V6E 1T7',
                 'price': 981000, 'bedroom': 2, 'bathroom': 2, 'property_type': 'Condo','listing_day': 34},
    'R2512107': {'adress': '680 W 6th Avenue', 'city': 'Vancouver', 'province': 'BC', 'post_code': 'V5Z 1A3',
                 'price': 989000, 'bedroom': 2, 'bathroom': 2, 'property_type': 'Townhouse','listing_day': 1},
    'R2512000': {'adress': '208-607 E 8th Avenue', 'city': 'Vancouver', 'province': 'BC', 'post_code': 'V5T 1T2',
                 'price': 574900, 'bedroom': 1, 'bathroom': 1, 'property_type': 'Condo','listing_day': 1},
    'R2511923': {'adress': '2146 W 14th Avenue', 'city': 'Vancouver', 'province': 'BC', 'post_code': 'V6K 2V7',
                 'price': 2248000, 'bedroom': 3, 'bathroom': 3, 'property_type': 'House','listing_day': 31},
    'R2511301': {'adress': '2638 Charles Street', 'city': 'Vancouver', 'province': 'BC', 'post_code': 'V5K 3A5',
                 'price': 1890000, 'bedroom': 8, 'bathroom': 8, 'property_type': 'House','listing_day': 18},
    'R2511809': {'adress': '307-2080 E Kent Avenue', 'city': 'Vancouver', 'province': 'BC', 'post_code': 'V5P 4X2',
                 'price': 449000, 'bedroom': 1, 'bathroom': 1, 'property_type': 'Condo','listing_day': 2},
    'R2511747': {'adress': '1408-1775 Quebec Street', 'city': 'Vancouver', 'province': 'BC', 'post_code': 'V5T 0E3',
                 'price': 679900, 'bedroom': 1, 'bathroom': 1, 'property_type': 'Condo','listing_day': 5},
    'R2511972': {'adress': '306-7180 Linden Avenue', 'city': 'Burnaby', 'province': 'BC', 'post_code': 'V5E 3G6',
                 'price': 448800, 'bedroom': 1, 'bathroom': 1, 'property_type': 'Condo','listing_day': 30},
    'R2511059': {'adress': '7760 Berkley Street', 'city': 'Burnaby', 'province': 'BC', 'post_code': 'V5E 2J7',
                 'price': 1150000, 'bedroom': 2, 'bathroom': 1, 'property_type': 'House','listing_day': 20},
    'R2511262': {'adress': '1106-9222 University Crescent', 'city': 'Burnaby', 'province': 'BC', 'post_code': 'V5A 0A6',
                 'price': 629800, 'bedroom': 2, 'bathroom': 2, 'property_type': 'Condo','listing_day': 4},
    'R2510818': {'adress': '5190 Fulwell Street', 'city': 'Burnaby', 'province': 'BC', 'post_code': 'V5G 1P2',
                 'price': 1390000, 'bedroom': 7, 'bathroom': 4, 'property_type': 'House','listing_day': 15},
    'R2510183': {'adress': '5712 Grant Street', 'city': 'Burnaby', 'province': 'BC', 'post_code': 'V5B 2K4',
                 'price': 1698000, 'bedroom': 3, 'bathroom': 4, 'property_type': 'House','listing_day': 18},
    'R2512071': {'adress': '8154 Gilley Avenue', 'city': 'Burnaby', 'province': 'BC', 'post_code': 'V5J 4Y5',
                 'price': 2488000, 'bedroom': 9, 'bathroom': 9, 'property_type': 'House','listing_day': 1},
    'R2510573': {'adress': '5059 Norfolk Street', 'city': 'Burnaby', 'province': 'BC', 'post_code': 'V5G 1E9',
                 'price': 1299000, 'bedroom': 4, 'bathroom': 4, 'property_type': 'House','listing_day': 7},
    'R2512173': {'adress': '11226-236 Street', 'city': 'Maple Ridge', 'province': 'BC', 'post_code': 'V2W 0C8',
                 'price': 900000, 'bedroom': 4, 'bathroom': 4, 'property_type': 'House','listing_day': 35},
    'R2512052': {'adress': '21560 Ashbury Court', 'city': 'Maple Ridge', 'province': 'BC', 'post_code': 'V2X 8Z7',
                 'price': 775000, 'bedroom': 3, 'bathroom': 2, 'property_type': 'House','listing_day': 43},
    'R2508895': {'adress': '227-12258 224 Street', 'city': 'Maple Ridge', 'province': 'BC', 'post_code': 'V2X 8Y7',
                 'price': 474900, 'bedroom': 2, 'bathroom': 2, 'property_type': 'Condo','listing_day': 12},
    'R2512451': {'adress': '102 Croteau Court', 'city': 'Coquitlam', 'province': 'BC', 'post_code': 'V3K 6E2',
                 'price': 948000, 'bedroom': 4, 'bathroom': 2, 'property_type': 'House','listing_day': 20},
    'R2512494': {'adress': '1803-1185 The High Street', 'city': 'Coquitlam', 'province': 'BC', 'post_code': 'V3B 0A9',
                 'price': 968000 , 'bedroom': 3, 'bathroom': 2,'property_type': 'Condo','listing_day': 10},
    }
