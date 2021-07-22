import os, csv, random
from time import sleep

#class mini_project:

def instructions():
    '''This displays a set of instructions'''
    print() 
    print('##########################################')
    print()

def read_prod_csv():
    try:
        with open('inventory-dict.csv') as file1:
            prod_list = list(csv.DictReader(file1))
            #prod_list = [word.strip() for word in file1.read().split(',') if word] 
            
    except FileNotFoundError:
        prod_list = []
        
    return prod_list

def print_prod_csv():
    prod_result = read_prod_csv()
    if prod_result == []:
        print(f'\nYou have no item in stock')
    elif len(prod_result) == 1:
        print(f'\nYou have {len(prod_result)} item in stock: \n\n{prod_result}\n')
    else:
        print(f'\nYou have {len(prod_result)} items in stock: \n\n{prod_result}\n')

def instructions2():
    '''This displays a set of instructions'''
    print('\nPlease follow the following instructions')
    print()
    print('##########################################')
    print()

def read_cour_csv():   
    try:
        with open('courier-dict.csv') as file2:
            cour_list = list(csv.DictReader(file2))
            
    except FileNotFoundError:
        cour_list = []
    
    return cour_list

def print_cour_csv():
    cour_result = read_cour_csv()       
    if cour_result == []:
        print(f'\nYou have no courier service')
    elif len(cour_result) == 1:
        print(f'\nYou have {len(cour_result)} courier in your service today: \n\n{cour_result}\n')    
    else:
        print(f'\nYou have {len(cour_result)} couriers in your service today: \n\n{cour_result}\n')
    
def instructions3():
    '''This displays a set of instructions'''
    print('\nPlease follow the following instructions')
    print()
    print('##########################################')
    print()

def read_ord_csv():
    try:
        with open('order-dict.csv') as file3:  
            ord_dict = list(csv.DictReader(file3)) 
            
    except FileNotFoundError:
        ord_dict = []
    return ord_dict
    

def main_func():
    use_prod_list = read_prod_csv()
    use_cour_list = read_cour_csv()
    use_ord_dct = read_ord_csv()
    prod_dict = {}
    cour_dict = {}
    
    while True: # Even if user inputs a number out of range the app won't crash but display appropriate set of instructions.
        try:
            user_input = int(input('Input 0 to exit the app and save your progess, 1 to progress to product menu, 2 to courier menu or 3 to order menu: '))
        except Exception:
            print('Please, input an integer')
        
        if user_input == 1:
                        
            def user_input_1():
                print()
                try:
                    user_input_2 = int(input('Input: \n0 to return to main menu \n1 to print product menu \
                                        \n2 to add a new product and display stock \n3 to print index and items in stock, and add new items \
                                        \n4 to remove an item from stock \n5 to clear the screen \
                                        \n6 to clear stock: '))
                except Exception:
                    print('Please, input an integer')
                
                return user_input_2
            
            input_result_prod = user_input_1()
            
            if input_result_prod == 1:
                print()
                if use_prod_list:
                    print(f'You have {use_prod_list} in stock\n')
                else:
                    print(f'You have no product in stock\n')
            
            elif input_result_prod == 2:
                print()
                user_input_3 = input('Type in the name of the item you wish to add: ').lower()
                user_input_3_price = input('Type in the price of the item you wish to add: ')
                prod_dict[user_input_3] = user_input_3_price
                use_prod_list.append(prod_dict)
                print(f'\nYou now have {use_prod_list} in stock\n')
            
            elif input_result_prod == 3:
                
                def if_user_input_is_3():
                    if use_prod_list:
                        print()
                        print('index \t item')
                        for index, items in enumerate(use_prod_list):
                            print(str(index), '\t', str(items))
                        print()
                    else:
                        print('No product in stock yet')
                    try:
                        user_input_ind = int(input(f'you may add a new item to stock \nInput a number between 0 to {len(use_prod_list)-1} for the position of the item you wish to add: '))
                        user_input_item = input('\nPlease, type in an item name you wish to add: ')
                        print()
                        user_input_item_price = input('Please, type in the item price: ')
                        if user_input_item:
                            prod_dict[user_input_item] = user_input_item_price
                            use_prod_list.insert(user_input_ind, prod_dict)
                            print()
                            print(f'You now have {use_prod_list} in stock\n')
                        else:
                            pass
                    except Exception as ex:
                        print(ex)
                if_user_input_is_3()    
                
            elif input_result_prod == 4:
                
                def if_user_input_is_4():
                    if use_prod_list:
                        print()
                        print('index \t item')
                        for index, items in enumerate(use_prod_list):
                            print(str(index), '\t', str(items))
                        print()
                        if len(use_prod_list) == 1: 
                            get_info = f'Input 0 for the product you wish to remove: '
                        else:    
                            get_info = f'Input a number between 0 and {len(use_prod_list)-1} representing the product you wish to remove: '
                        
                        try:
                            new_user_input_ind = int(input(get_info))
                        except IndexError as e:
                            print()
                            print(e)
                        except Exception:
                            print('\nPlease, input an integer')
                            
                        del use_prod_list[new_user_input_ind]
                        if use_prod_list:
                            print()
                            print(f'You now have {use_prod_list} in stock\n')
                        else:
                            print()
                            print(f'You now have no product in stock\n')  
                    else:
                        print('\nYou cannot delete any product as your stock is empty')
                        
                if_user_input_is_4()
                    
            elif input_result_prod == 5:
                os.system('cls || clear')
                
            elif input_result_prod == 6:
                use_prod_list.clear()
                print()
                print(f'Your stock is now empty\n')
                
            elif not input_result_prod: # If the user input 0 above
                print()
                x = instructions()
            else:
                print('\nPlease, type in a number between 0 and 6')
                
        elif user_input == 2:
            print()
            try:
                sub_user_input = int(input('Input: \n0 to return to main menu \n1 to print courier list \
                                        \n2 to add a new courier and print list \n3 to print index and names in your courier and add new courier \
                                        \n4 to remove a courier \n5 to clear the screen \
                                        \n6 to clear courier list: '))
            except Exception:
                print('\nPlease, input an integer')
                continue
            
            if sub_user_input == 1:
                if cour_list:
                    if len(cour_list) == 1:
                        print(f'\nYou have {cour_list} courier at your service\n')
                    else:
                        print(f'\nYou have {cour_list} couriers at your service\n')
                else:
                    print(f'\nYou have no courier service\n')
                
            elif sub_user_input == 2:
                sub_user_input_3 = input('Please, type in a courier name to add to your service: ').title()
                sub_user_input_3_ph = input('Please, type in the courier phone number: ')
                cour_dict[sub_user_input_3] = sub_user_input_3_ph
                cour_list.append(cour_dict)
                #cour_list.append(sub_user_input_3)
                if len(cour_dict) == 1:
                    print(f'You now have {cour_dict} courier at your service\n')
                else:
                    print(f'\nYou now have {cour_dict} couriers at your service\n') 
                
            elif sub_user_input == 3:
                if cour_list:
                    print()
                    print('index \t courier')
                    for index, items in enumerate(cour_list):
                        print(str(index), '\t', str(items))
                    print()   
                else:
                    print('No courier in service yet')  
                try:
                    sub_user_input_ind = int(input(f'you may add a new courier to your service \nInput a number between 0 to {len(cour_list)-1} for the position of the courier you wish to add: '))
                    sub_user_input_name= input('\nType in the courier name you wish to add: ')
                    print()
                    sub_user_input_ph = input('Please, type in the courier phone number: ')
                    if sub_user_input_name:
                        cour_dict[sub_user_input_name] = sub_user_input_ph
                        cour_list.insert(sub_user_input_ind, cour_dict)
                        print()
                        print(f'You now have {cour_list} at your courier service\n')
                    else:
                        pass
                except Exception as ex:
                    print(ex)
                                                        
            elif sub_user_input == 4:   
                if cour_list:
                    print()
                    print('index \t item')
                    for index, items in enumerate(cour_list):
                        print(str(index), '\t', str(items))
                    print()
                    if len(cour_list) == 1: 
                        get_info_cour = f'Input 0 for the courier you wish to remove: '
                    else:    
                        get_info_cour = f'Input a number between 0 and {len(cour_list)-1} representing the courier you wish to remove: '
                    
                    try:
                        new_user_cour_ind = int(input(get_info_cour))
                    except IndexError as e:
                        print()
                        print(e)
                    except Exception:
                        print('\nPlease, input an integer')
                        
                    del cour_list[new_user_cour_ind]
                    if cour_list:
                        print()
                        print(f'You now have {cour_list} at your courier service\n')
                    else:
                        print()
                        print(f'You now have no courier service\n')
                else:
                    print('\nYou cannot delete any courier as you have none')
                
            elif sub_user_input == 5:
                os.system('cls || clear')
            
            elif sub_user_input == 6:
                cour_list.clear()
                print()
                print(f'You now have no courier service\n')
          
            elif not sub_user_input:
                y = instructions2()
            
            else:
                print('\nPlease, type in a number between 0 and 6')   
                
        elif user_input == 3:
            print()
            try:
               ord_user_input_2 = int(input('Input: \n0 to return to main menu \n1 to print list of available orders \
                                    \n2 to add your order \n3 to print index, available orders, and change your order status \
                                    \n4 to change your order \n5 to delete your order \
                                    \n6 to clear the screen: '))
            except Exception:
                print('Please, input an integer')
                continue
                
            if ord_user_input_2 == 1:
                if ord_dict:
                    if len(ord_dict) == 1:
                        print(f'\nYou have this order: {ord_dict}\n')
                    else:
                        print(f'\nYou have  the following orders: {ord_dict}\n')
                else:
                    print(f'\nYou have no order\n')

            elif ord_user_input_2 == 2:
                print()
                ord_user_input_name = input('Please, type in your full name: ').title()
                ord_user_input_add = input('Please, type in your address: ').capitalize()
                ord_user_input_ph = input('Please, type in your phone number: ')
                
                if prod_list:
                    print('\nindex \t product category')
                    for index, items in enumerate(prod_list):
                        print(str(index), '\t', str(items))
                    
                    ord_user_input_item = input(f'Please, choose your order item(s) by inputting the index number between 0 and {len(prod_list)-1} separated by commas from the categories above: ')
                    try:
                        int_ord_user_input_item = [int(i) for i in ord_user_input_item.split(',')]
                    except Exception as e:
                        print(e)
                else:
                    int_ord_user_input_item = None
                    print('\nDue to recent surge in demand we have no product in stock. We will refill in 2 hours and alert you')
                        
                if prod_list:
                    print('index \t couriers')
                    if cour_list:
                        for index, courier in enumerate(cour_list):
                            print(str(index), '\t', str(courier))
                    else:
                        temp_cour_list = random.sample(('Micheal', 'Matthew', 'Cypher', 'Linda', 'Ahmed', 'Ela', 'Shauna'), k=1)
                        for index, items in enumerate(temp_cour_list):
                            print(str(index), '\t', str(items)) 
                
                    ord_user_input_cour = input(f'\nPlease, choose a courier by inputing the name from the available courier(s) above: ').title()
                    ord_status = 'PREPARING'
                    for char in ord_status:
                        print(char, end='')
                        sleep(0.01)
                    print()
                    for _ in range(6):
                        print('\6', end='')
                        sleep(0.01)
                    print()
                    mini_ord_dict = {}
                    mini_ord_dict['name'] = ord_user_input_name 
                    mini_ord_dict['address'] = ord_user_input_add 
                    mini_ord_dict['phone number'] = ord_user_input_ph
                    mini_ord_dict['courier'] = ord_user_input_cour 
                    mini_ord_dict['status'] = ord_status
                    mini_ord_dict['items'] = int_ord_user_input_item
                    ord_dict.append(mini_ord_dict)     
                    print(ord_dict)
                else:
                    print('\nDue to recent surge in demand we have no product in stock. We will refill in 2 hours and alert you')    
                    
            elif ord_user_input_2 == 3:
                if ord_dict:
                    print()
                    print('index \t order categories')
                    for index, items in enumerate(ord_dict):
                        print(str(index), '\t', str(items))
                    print()
                    try:
                        if len(ord_dict) > 1:
                            order_user_input_ind = int(input(f'you may change your order status\nInput a number between 0 to {len(ord_dict)-1} for the index representing your order: '))
                            print('Your order is: ', ord_dict[order_user_input_ind])
                        else:
                            order_user_input_ind = int(input(f'you may change your order status\nInput 0 for the index representing your order: '))
                            print('Your order is: ', ord_dict[order_user_input_ind])
                        order_user_input_item = input('What do you want to change the status of your order to: ')
                        ord_dict[order_user_input_ind]['status'] = order_user_input_item
                        print()
                        print(f'Your order status has been updated: ', ord_dict[order_user_input_ind])
                    except Exception as ex:
                        print(ex)
                else:
                    print('\nYou do not have any order')
                    
            elif ord_user_input_2 == 4:
                if ord_dict:
                    print()
                    print('index \t order categories')
                    for index, items in enumerate(ord_dict):
                        print(str(index), '\t', str(items))
                    print()
                    try:
                        if len(ord_dict) > 1:
                            ord_user_input_ind = int(input(f'You may change your existing order\nInput a number between 0 to {len(ord_dict)-1} for your order in the above list: '))
                        else:
                            ord_user_input_ind = int(input(f'You may change your existing order\nInput 0 for your order in the above list: '))
                            
                        print('\nYour order is: ', ord_dict[ord_user_input_ind])
                        print()
                        ord_user_input_item = input('Please, type in the order category you wish to change: ')
                        print()
                        new_ord_user_input_item = input('Please, type in the replacement: ')
                        if new_ord_user_input_item:
                            ord_dict[ord_user_input_ind][ord_user_input_item] = new_ord_user_input_item
                            print('\nYour updated order list is: ', ord_dict[ord_user_input_ind])
                        else:
                            pass
                    except Exception as e:
                        print(e)
                else:
                    print('\nYou have made no order')
                
            elif ord_user_input_2 == 5:   
                if ord_dict:
                    print()
                    print('index \t order categories')
                    for index, items in enumerate(ord_dict):
                        print(str(index), '\t', str(items)) 
                    if len(ord_dict) > 1:
                        get_del_ord_ind = f'Input a number between 0 and {len(ord_dict)-1} representing your order \nor -1 if your order is not here: '
                    else:
                        get_del_ord_ind = f'Input 0 representing your order \nor -1 if your order is not here: '
                    try:
                        print()
                        new_user_input_ind = int(input(get_del_ord_ind))
                    except IndexError as e:
                        print()
                        print(e)
                    except Exception:
                        ('\nPrint, please input an integer')
                    if 0 <= new_user_input_ind <= len(ord_dict)-1:
                        del ord_dict[new_user_input_ind]
                        print(f'\nYour order has been deleted')
                    elif new_user_input_ind == -1:
                        pass                   
                
            elif ord_user_input_2 == 6:
                os.system('cls || clear')
                
            elif not ord_user_input_2: # If the user input 0 above
                print()
                z = instructions3()
            else:
                print('\nPlease, type in a number between 0 and 6')     
                    
        elif not user_input: #After every operation, the app will allow users to input 0 to exit.
            if prod_list and cour_list and ord_dict:
                def save_csv_file(prod_list, cour_list, ord_dict):
                    with open(r'inventory-dict.csv', 'w', encoding='utf-8') as file4:
                        writer = csv.DictWriter(file4,  delimiter = ',', quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(item for item in prod_list)
                        
                    with open(r'courier-dict.csv', 'w', encoding='utf-8') as file5:
                        writer = csv.DictWriter(file5,  delimiter = ',', quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(item for item in cour_list)
                        
                    with open(r'order-dict.csv', 'w', encoding='utf-8') as file6:
                        writer = csv.DictWriter(file6,  delimiter = ',', quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(item for item in ord_dict)
                return save_csv_file(prod_list, cour_list, ord_dict)
            
            elif prod_list and cour_list and not ord_dict:
                def save_csv_file(prod_list, cour_list):
                    with open(r'inventory-dict.csv', 'w', encoding='utf-8') as file7:
                        writer = csv.DictWriter(file7,  delimiter = ',', quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(item for item in prod_list)
                        
                    with open(r'courier-dict.csv', 'w', encoding='utf-8') as file8:
                        writer = csv.DictWriter(file8,  delimiter = ',', quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(item for item in cour_list)
                return save_csv_file(prod_list, cour_list)
            
            elif prod_list and ord_dict and not cour_list:
                def save_csv_file(prod_list, ord_dict):
                    with open(r'inventory-dict.csv', 'w', encoding='utf-8') as file9:
                        writer = csv.DictWriter(file9,  delimiter = ',', quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(item for item in prod_list)
                        
                    with open(r'order-dict.csv', 'w', encoding='utf-8') as file10:
                        writer = csv.DictWriter(file10,  delimiter = ',', quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(item for item in ord_dict)
                return save_csv_file(prod_list, ord_dict)
            
            elif cour_list and ord_dict and not prod_list:
                def save_csv_file(cour_list, ord_dict):
                    with open(r'courier-dict.csv', 'w', encoding='utf-8') as file11:
                        writer = csv.DictWriter(file11,  delimiter = ',', quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(item for item in cour_list)
                        
                    with open(r'order-dict.csv', 'w', encoding='utf-8') as file12:
                        writer = csv.DictWriter(file12,  delimiter = ',', quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(item for item in ord_dict)
                return save_csv_file(cour_list, ord_dict)
            
            elif prod_list: #Did all these because python will write an empty string to my file if prod_list or cour_list is none
                def save_csv_file(prod_list): 
                    with open(r'inventory-dict.csv', 'w', encoding='utf-8') as file6: #The empty string will give a false result when I take, say, len [empty] (prod_list)
                        writer = csv.DictWriter(file6,  delimiter = ',', quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(item for item in prod_list)
                return save_csv_file(prod_list)
            
            elif cour_list:
                def save_csv_file(cour_list):
                    with open(r'courier-dict.csv', 'w', encoding='utf-8') as file7:
                        writer = csv.DictWriter(file7,  delimiter = ',', quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(item for item in cour_list)
                return save_csv_file(cour_list)
            
            elif ord_dict:
                def save_csv_file(ord_dict):
                    with open(r'order-dict.csv', 'w', encoding='utf-8') as file7:
                        writer = csv.DictWriter(file7,  delimiter = ',', quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(item for item in ord_dict)
                return save_csv_file(ord_dict)
            
            # if prod_list and cour_list:
            #     def save_csv_file(prod_list, cour_list):
            #         with open(r'inventory-list.csv', 'w', encoding='utf-8') as file4:
            #             writer = csv.writer(file4,  delimiter = ',', quoting=csv.QUOTE_MINIMAL)
            #             writer.writerow(item for item in prod_list)
                        
            #         with open(r'courier-list.csv', 'w', encoding='utf-8') as file5:
            #             writer = csv.writer(file5,  delimiter = ',', quoting=csv.QUOTE_MINIMAL)
            #             writer.writerow(item for item in cour_list)
            #     return save_csv_file(prod_list, cour_list)
            
            # elif prod_list: #Did all these because python will write an empty string to my file if prod_list or cour_list is none
            #     def save_csv_file(prod_list): 
            #         with open(r'inventory-list.csv', 'w', encoding='utf-8') as file6: #The empty string will give a false result when I take, say, len [empty] (prod_list)
            #             writer = csv.writer(file6,  delimiter = ',', quoting=csv.QUOTE_MINIMAL)
            #             writer.writerow(item for item in prod_list)
            #     return save_csv_file(prod_list)
            
            # elif cour_list:
            #     def save_csv_file(cour_list):
            #         with open(r'courier-list.csv', 'w', encoding='utf-8') as file7:
            #             writer = csv.writer(file7,  delimiter = ',', quoting=csv.QUOTE_MINIMAL)
            #             writer.writerow(item for item in cour_list)
            #     return save_csv_file(cour_list)
            
            #else:
            
            else:
                raise SystemExit
        else:
            print('Please input an integer between 0 and 3')        
    
if __name__ == '__main__':
    #instructions()
    #read_prod_csv() 
    print_prod_csv()
    # instructions2() 
    print_cour_csv()  
    instructions3()   
    main_func() 