from statistics import median
import data
import datetime

global device_list, report_list, timestamp, phones, tablets, laptops
dateTimeObj = datetime.datetime.now()

def minute():
    """
    If the current minute is less than 10, it adds 0 digits before minute.
    :return: str(0+minute)
    """
    if dateTimeObj.minute < 10:
        dateTimeObj.minute = '0' + dateTimeObj.minute
    return dateTimeObj.minute

timestamp = f"{dateTimeObj.year}-{dateTimeObj.month}-{dateTimeObj.day} {dateTimeObj.hour}:{dateTimeObj.minute}"
phones = data.get_phone_info_list()
tablets = data.get_tablet_info_list()
laptops = data.get_laptop_info_list()

def phone_lists():
    """
    It creates lists of the phone list in the data py file according to text, csv and json formats.
    :return: phones price list.
    """
    global phone_price_list, phone_ram_list, phone_os_list_txt, phone_os_list_csv, phone_os_list_json
    phone_1 = (phones[0].split(","))
    phone_2 = (phones[1].split(","))
    phone_3 = (phones[2].split(","))
    phone_4 = (phones[3].split(","))
    phone_5 = (phones[4].split(","))
    phone_6 = (phones[5].split(","))
    phone_7 = (phones[6].split(","))
    phone_8 = (phones[7].split(","))
    phone_9 = (phones[8].split(","))
    phone_10 = (phones[9].split(","))
    phone_price_list = [float(phone_1[6]), float(phone_2[6]), float(phone_3[6]), float(phone_4[6]),
                        float(phone_5[6]), float(phone_6[6]), float(phone_7[6]), float(phone_8[6]),
                        float(phone_9[6]), float(phone_10[6])]
    phone_ram_list = [int(phone_1[3]), int(phone_2[3]), int(phone_3[3]), int(phone_4[3]), int(phone_5[3]),
                      int(phone_6[3]), int(phone_7[3]), int(phone_8[3]), int(phone_9[3]), int(phone_10[3])]
    os_list_phone = [phone_1[4]+" "+phone_1[5], phone_2[4]+" "+phone_2[5], phone_3[4]+" "+phone_3[5],
                     phone_4[4]+" "+phone_4[5], phone_5[4]+" "+phone_5[5], phone_6[4]+" "+phone_6[5],
                     phone_7[4]+" "+phone_7[5], phone_8[4]+" "+phone_8[5], phone_9[4]+" "+phone_9[5],
                     phone_10[4]+" "+phone_10[5]]
    phone_os_list_txt = f"{os_list_phone[0]}, {os_list_phone[1]}, {os_list_phone[2]}, {os_list_phone[3]}, {os_list_phone[4]}, " \
                        f"{os_list_phone[5]}, {os_list_phone[6]}, {os_list_phone[7]}, {os_list_phone[8]}, {os_list_phone[9]}"
    phone_os_list_csv = f"{os_list_phone[0]}/{os_list_phone[1]}/{os_list_phone[2]}/{os_list_phone[3]}/{os_list_phone[4]}/ " \
                        f"{os_list_phone[5]}/{os_list_phone[6]}/{os_list_phone[7]}/{os_list_phone[8]}/{os_list_phone[9]}"
    phone_os_list_json = f' [\n\t\t"{os_list_phone[0]}",\n\t\t"{os_list_phone[1]}",\n\t\t"{os_list_phone[2]}"\n\t\t"{os_list_phone[3]}" ' \
                         f'\n\t\t"{os_list_phone[4]}",\n\t\t"{os_list_phone[5]}",\n\t\t"{os_list_phone[6]}"\n\t\t"{os_list_phone[7]}" ' \
                         f'\n\t\t"{os_list_phone[8]}",\n\t\t"{os_list_phone[9]}"\n]'
    return phone_price_list

def tablet_lists():
    """
    It creates lists of the tablet list in the data py file according to text, csv and json formats.
    :return: tablets price list
    """
    global tablet_price_list, tablet_ram_list, tablet_os_list_txt, tablet_os_list_csv, tablet_os_list_json
    tablet_1 = (tablets[0].split(","))
    tablet_2 = (tablets[1].split(","))
    tablet_3 = (tablets[2].split(","))
    tablet_4 = (tablets[3].split(","))
    tablet_5 = (tablets[4].split(","))
    tablet_6 = (tablets[5].split(","))
    tablet_7 = (tablets[6].split(","))
    tablet_8 = (tablets[7].split(","))
    tablet_9 = (tablets[8].split(","))
    tablet_10 = (tablets[9].split(","))
    tablet_11 = (tablets[10].split(","))
    tablet_price_list = [float(tablet_1[6]), float(tablet_2[6]), float(tablet_3[6]), float(tablet_4[6]),
                        float(tablet_5[6]), float(tablet_6[6]), float(tablet_7[6]), float(tablet_8[6]),
                        float(tablet_9[6]), float(tablet_10[6]), float(tablet_11[6])]
    tablet_ram_list = [int(tablet_1[3]), int(tablet_2[3]), int(tablet_3[3]), int(tablet_4[3]), int(tablet_5[3]),
                       int(tablet_6[3]), int(tablet_7[3]), int(tablet_8[3]), int(tablet_9[3]), int(tablet_10[3]),
                       int(tablet_11[3])]
    os_list_tablet = [tablet_1[4]+" "+tablet_1[5], tablet_2[4]+" "+tablet_2[5], tablet_3[4]+" "+tablet_3[5],
                     tablet_4[4]+" "+tablet_4[5], tablet_5[4]+" "+tablet_5[5], tablet_6[4]+" "+tablet_6[5],
                     tablet_7[4]+" "+tablet_7[5], tablet_8[4]+" "+tablet_8[5], tablet_9[4]+" "+tablet_9[5],
                     tablet_10[4]+" "+tablet_10[5], tablet_11[4]+" "+tablet_11[5]]
    tablet_os_list_txt = f"{os_list_tablet[0]}, {os_list_tablet[1]}, {os_list_tablet[2]}, {os_list_tablet[3]}, " \
                         f"{os_list_tablet[4]}, {os_list_tablet[5]}, {os_list_tablet[6]}, {os_list_tablet[7]}, " \
                         f"{os_list_tablet[8]}, {os_list_tablet[9]}, {os_list_tablet[10]}"
    tablet_os_list_csv = f"{os_list_tablet[0]}/{os_list_tablet[1]}/{os_list_tablet[2]}/{os_list_tablet[3]}/{os_list_tablet[4]}/ " \
                         f"{os_list_tablet[5]}/{os_list_tablet[6]}/{os_list_tablet[7]}/{os_list_tablet[8]}/{os_list_tablet[9]}/ " \
                         f"{os_list_tablet[10]}"
    tablet_os_list_json = f' [\n\t\t"{os_list_tablet[0]}",\n\t\t"{os_list_tablet[1]}",\n\t\t"{os_list_tablet[2]}"\n\t\t"{os_list_tablet[3]}" ' \
                          f'\n\t\t"{os_list_tablet[4]}",\n\t\t"{os_list_tablet[5]}",\n\t\t"{os_list_tablet[6]}"\n\t\t"{os_list_tablet[7]}" ' \
                          f'\n\t\t"{os_list_tablet[8]}",\n\t\t"{os_list_tablet[9]}",\n\t\t"{os_list_tablet[10]}"\n]'
    return tablet_price_list

def laptop_lists():
    """
    It creates lists of the laptop list in the data py file according to text, csv and json formats.
    :return: laptops price list
    """
    global laptop_price_list, laptop_ram_list, laptop_os_list_txt, laptop_os_list_csv, laptop_os_list_json
    laptop_1 = (laptops[0].split(","))
    laptop_2 = (laptops[1].split(","))
    laptop_3 = (laptops[2].split(","))
    laptop_4 = (laptops[3].split(","))
    laptop_5 = (laptops[4].split(","))
    laptop_6 = (laptops[5].split(","))
    laptop_7 = (laptops[6].split(","))
    laptop_8 = (laptops[7].split(","))
    laptop_9 = (laptops[8].split(","))
    laptop_10 = (laptops[9].split(","))
    laptop_11 = (laptops[10].split(","))
    laptop_12 = (laptops[11].split(","))
    laptop_price_list = [float(laptop_1[6]), float(laptop_2[6]), float(laptop_3[6]), float(laptop_4[6]),
                        float(laptop_5[6]), float(laptop_6[6]), float(laptop_7[6]), float(laptop_8[6]),
                        float(laptop_9[6]), float(laptop_10[6]), float(laptop_11[6]), float(laptop_12[6])]
    laptop_ram_list = [int(laptop_1[3]), int(laptop_2[3]), int(laptop_3[3]), int(laptop_4[3]), int(laptop_5[3]),
                       int(laptop_6[3]), int(laptop_7[3]), int(laptop_8[3]), int(laptop_9[3]), int(laptop_10[3]),
                       int(laptop_11[3]), int(laptop_12[3])]
    os_list_laptop = [laptop_1[4]+" "+laptop_1[5], laptop_2[4]+" "+laptop_2[5], laptop_3[4]+" "+laptop_3[5],
                     laptop_4[4]+" "+laptop_4[5], laptop_5[4]+" "+laptop_5[5], laptop_6[4]+" "+laptop_6[5],
                     laptop_7[4]+" "+laptop_7[5], laptop_8[4]+" "+laptop_8[5], laptop_9[4]+" "+laptop_9[5],
                     laptop_10[4]+" "+laptop_10[5], laptop_11[4]+" "+laptop_11[5], laptop_12[4]+" "+laptop_12[5]]
    laptop_os_list_txt = f"{os_list_laptop[0]}, {os_list_laptop[1]}, {os_list_laptop[2]}, {os_list_laptop[3]}, " \
                         f"{os_list_laptop[4]}, {os_list_laptop[5]}, {os_list_laptop[6]}, {os_list_laptop[7]}, " \
                         f"{os_list_laptop[8]}, {os_list_laptop[9]}, {os_list_laptop[10]}, {os_list_laptop[11]}"
    laptop_os_list_csv = f"{os_list_laptop[0]}/{os_list_laptop[1]}/{os_list_laptop[2]}/{os_list_laptop[3]}/{os_list_laptop[4]}/ " \
                         f"{os_list_laptop[5]}/{os_list_laptop[6]}/{os_list_laptop[7]}/{os_list_laptop[8]}/{os_list_laptop[9]}/ " \
                         f"{os_list_laptop[10]}/{os_list_laptop[11]}"
    laptop_os_list_json = f' [\n\t\t"{os_list_laptop[0]}",\n\t\t"{os_list_laptop[1]}",\n\t\t"{os_list_laptop[2]}"\n\t\t"{os_list_laptop[3]}" ' \
                          f'\n\t\t"{os_list_laptop[4]}",\n\t\t"{os_list_laptop[5]}",\n\t\t"{os_list_laptop[6]}"\n\t\t"{os_list_laptop[7]}" ' \
                          f'\n\t\t"{os_list_laptop[8]}",\n\t\t"{os_list_laptop[9]}",\n\t\t"{os_list_laptop[10]}",\n\t\t"{os_list_laptop[11]}"\n]'
    return laptop_price_list

def select_device():
    """
    Organizes report data according to the selected device type
    :return: shows device type
    """
    global device, device_pick, number, minimum_price, maximum_price, average_price, ram
    device_list = ['Phone', 'Tablet', 'Laptop']
    device_pick = int(input(f"\n1 - Phone \n2 - Tablet \n3 - Laptop\nPick device:"))
    while device_pick == 1 or device_pick == 2 or device_pick == 3:
        if device_pick == 1:
            device = device_list[0]
            number = len(phones)
            minimum_price = min(phone_lists())
            maximum_price = max(phone_lists())
            average_price = round(sum(phone_lists())/number, 2)
            ram = median(phone_ram_list)
            break
        elif device_pick == 2:
            device = device_list[1]
            number = len(tablets)
            minimum_price = min(tablet_lists())
            maximum_price = max(tablet_lists())
            average_price = round(sum(tablet_lists())/number, 2)
            ram = median(tablet_ram_list)
            break
        elif device_pick == 3:
            device = device_list[2]
            number = len(laptops)
            minimum_price = min(laptop_lists())
            maximum_price = max(laptop_lists())
            average_price = round(sum(laptop_lists())/number, 2)
            ram = median(laptop_ram_list)
            break
        else:
            print("Wrong number picked! Please enter correct number.")
            continue
    return device

def select_report():
    """
    Chooses the report type
    :return: shows report type
    """
    global report, report_list, report_pick
    report_list = ['Text', 'CSV', 'JSON']
    report_pick = int(input(f"\n1 - Text \n2 - CSV \n3 - JSON\nPick report type:"))
    while report_pick == 1 or report_pick == 2 or report_pick == 3:
        if report_pick == 1:
            print(f'\nPicked {device}-{report_list[0]}\n\n{text_report()}')
            break
        elif report_pick == 2:
            print(f'\nPicked {device}-{report_list[1]}\n\n{csv_report()}')
            break
        elif report_pick == 3:
            print(f'\nPicked {device}-{report_list[2]}\n\n{json_report()}')
            break
        else:
            print("Wrong number picked! Please enter correct number.")
            continue
    return report_pick

def os_systems():
    """
    It determines the OS list according to the selected device and type.
    :return: 'OS list' for selected device and report type
    """
    global operating_system_list
    if device_pick == 1 and report_pick == 1:
        operating_system_list = phone_os_list_txt
    elif device_pick == 1 and report_pick == 2:
        operating_system_list = phone_os_list_csv
    elif device_pick == 1 and report_pick ==3:
        operating_system_list = phone_os_list_json
    elif device_pick == 2 and report_pick == 1:
        operating_system_list = tablet_os_list_txt
    elif device_pick == 2 and report_pick == 2:
        operating_system_list = tablet_os_list_csv
    elif device_pick == 2 and report_pick ==3:
        operating_system_list = tablet_os_list_json
    elif device_pick == 3 and report_pick == 1:
        operating_system_list = laptop_os_list_txt
    elif device_pick == 3 and report_pick == 2:
        operating_system_list = laptop_os_list_csv
    elif device_pick == 3 and report_pick == 3:
        operating_system_list = laptop_os_list_json
    return operating_system_list

def text_report():
    """
    Shows the text report type.
    :return: TEXT REPORT
    """
    text_report = f"Timestamp: {timestamp}\nDevice: {device}\nNumber: {number}" \
                  f"\nAverage Price: ${average_price:.2f}\nMinumum Price: ${minimum_price:.2f}\nMaximum Price: ${maximum_price:.2f}" \
                  f"\nMedian Ram: {ram} GB\nOperating Systems: {os_systems()}}}"
    return text_report

def csv_report():
    """
    Shows the csv report type.
    :return: CSV REPORT
    """
    csv_report = f"{timestamp},{device},{number},{average_price},{minimum_price}," \
                 f"{maximum_price},{ram},{os_systems()}"
    return csv_report

def json_report():
    """
    Shows the json report type.
    :return: JSON REPORT
    """
    json_report = f'{{\n\t"date_time":" {timestamp}",' \
                  f'\n\t"device_type":" {device}",' \
                  f'\n\t"number": {number},' \
                  f'\n\t"average_price": {average_price},' \
                  f'\n\t"min_price": {minimum_price},' \
                  f'\n\t"max_price": {maximum_price}' \
                  f'\n\t"median_ram": {ram},' \
                  f'\n\t"operating_systems": {os_systems()}\n}}'
    return json_report
