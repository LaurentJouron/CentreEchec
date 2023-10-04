def display_menu(menu_dict):
    menu_options = " | ".join([f" {option}. {label} " for option, label in menu_dict.items()])
    print(f"\n {menu_options.center(106, '*')}\n")
