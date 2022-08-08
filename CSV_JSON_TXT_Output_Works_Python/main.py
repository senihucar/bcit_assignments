import reports

def main():
    again = input(f"\nWelcome to 'TEXT,CSV,JSON' report software. Do you want get report? \n 1- Yes \n 2- No\n")
    if again == "1" or again == "y" or again == "Y" or again == "yes" or again == "Yes":
        while again == "1" or again == "y" or again == "Y" or again == "yes" or again == "Yes":
            print(f'Please, select device')
            reports.select_device()
            print(f'\nPlease, select output report style')
            reports.select_report()
            again = input(f"\nDo you want get another report \n 1- Yes \n 2- No\n")
            if again == "1" or again == "y" or again == "Y" or again == "yes" or again == "Yes":
                continue
            else:
                print("Thanks using report system\n\n\t\t\t\t Senih Ucar")
                break
    else:
        print("Thanks using report system\n\n\t\t\t\t Senih Ucar")
    return


if __name__ == '__main__':
    main()
