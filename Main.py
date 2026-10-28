import Menus

def main():
    Menus.show_welcome_screen()
    input()
        
    while True:
        Menus.show_main_menu()
        choice = Menus.menu_choice()
        
        match choice:
            case 1:
                Menus.show_encycl_menu()
                choice = Menus.menu_choice()

                match choice:
                    case 1:
                        continue
                    case 2:
                        continue
                    case 3:
                        categories = Menus.menu_flavor()
                        choice = Menus.menu_choice()
                        selected_category = sorted(categories)[choice - 1]
                        print(selected_category)                
            case 2:
                continue
            case 3:
                continue
                
            case 0:
                print("Bedankt voor je bezoek!")
                break


if __name__ == "__main__":
    main()
