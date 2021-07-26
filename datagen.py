import os, csv, random
from time import sleep
from copy import deepcopy

#class mini_project:     

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
    
def instructions():
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
    

def main_function():
    
    use_prod_list = read_prod_csv()
    use_cour_list = read_cour_csv()
    use_ord_dict = read_ord_csv()
    prod_dict = {}
    cour_dict = {}
    
    while True: # The app keeps running until users input 0 in the main menu or encounter uncaught error
        try:
            user_input = int(input('Input 0 to exit the app and save your progess \n1 to progress to product menu \n2 to courier menu \n3 to order menu: '))
        except Exception:
            print('\nPlease, input an integer\n')
            continue
        
        if user_input == 1: #progress to product menu
                        
            def user_input_1():
                
                print()
                try:
                    user_input_2 = int(input('Input: \n0 to return to main menu \n1 to print product menu \
                                        \n2 to add a new product and display stock \n3 to print index and items in stock, and update items \
                                        \n4 to remove an item from stock \n5 to clear the screen \
                                        \n6 to clear stock: '))
                except Exception:
                    os.system('cls || clear')
                    print('\nYou input string(s) instead of a number, clearing the screen and returning to main menu\n')
                else:    
                    return user_input_2
            
            input_result_prod = user_input_1()
            
            if input_result_prod == 1: #print product list
                print()
                if use_prod_list:
                    print(f'You have {use_prod_list} in stock\n')
                else:
                    print(f'You have no product in stock\n')
            
            elif input_result_prod == 2: #get new item
                
                def if_user_input_is_2():
                    print()
                    user_input_3 = input('Type in the name of the item you wish to add: ').lower()
                    user_input_3_price = input('Type in the price of the item you wish to add: ')
                    prod_dict.clear()
                    prod_dict['item_name'] = user_input_3
                    prod_dict['price'] = float(user_input_3_price) if '.' in user_input_3_price else int(user_input_3_price)
                    copy_product_dict = deepcopy(prod_dict)
                    use_prod_list.append(copy_product_dict)
                    
                    print(f'\nYou now have {use_prod_list} in stock\n')
                
                if_user_input_is_2()
                
            elif input_result_prod == 3: #update product list
                
                def if_user_input_is_3():
                    
                    if use_prod_list:
                        print()
                        print('index \t item')
                        for index, items in enumerate(use_prod_list):
                            print(str(index), '\t', str(items))
                        print()
                        try:
                            if len(use_prod_list) > 1:
                                user_input_ind = int(input(f'you may update your items \nInput a number between 0 to {len(use_prod_list)-1} for the item you wish to update: '))
                            else:
                                user_input_ind = int(input(f'Please, input 0 to change/update the item: '))
                            user_input_item = input('\nPlease, type in the replacement: ')
                            user_input_item_price = input('\nPlease, type in the item price: ')
                            
                            if user_input_item:
                                prod_dict.clear()
                                prod_dict['item_name'] = user_input_item
                                prod_dict['price'] = float(user_input_item_price) if '.' in user_input_item_price else int(user_input_item_price)
                                copy_product_dict2 = deepcopy(prod_dict)
                                use_prod_list[user_input_ind] = copy_product_dict2
                                print()
                                print(f'You now have {use_prod_list} in stock\n')
                            else:
                                print('\nItem name missing; thus, item not added. Returning to main menu\n')
                        except Exception as ex:
                            print(f'\n {ex} \n')      
                            print('Returning to main menu\n')
                
                    else:
                        print('\nNo product in stock yet\n')
                        
                if_user_input_is_3()    
                
            elif input_result_prod == 4: #delete product
                
                def if_user_input_is_4():
                    if use_prod_list:
                        print()
                        print('index \t item')
                        for index, items in enumerate(use_prod_list):
                            print(str(index), '\t', str(items))
                        print()
                        if len(use_prod_list) == 1: 
                            get_info = f'Please, input 0 to remove your product: '
                        else:    
                            get_info = f'Please, input a number between 0 and {len(use_prod_list)-1} representing the product you wish to remove: '
                        
                        try:
                            new_user_input_ind = int(input(get_info))
                            del use_prod_list[new_user_input_ind]
                            if use_prod_list:
                                print(f'\nYou now have {use_prod_list} in stock\n')
                            else:
                                print(f'\nYou now have no product in stock\n')  
                        except IndexError as e: 
                            print(f'\n {e} \n')
                            print('Returning to main menu\n')
                        except ValueError:
                            print('\nPlease, input an integer\n')
                            print('Returning to main menu\n')
       
                    else:
                        print('\nYou cannot delete any product as your stock is empty\n')
                        
                if_user_input_is_4()
                    
            elif input_result_prod == 5:
                os.system('cls || clear')
                
            elif input_result_prod == 6:
                use_prod_list.clear()
                print(f'\nYour stock is now empty\n')
                
            elif not input_result_prod: # If the user input 0 above
                print()
                print_product_menu = instructions()
            else:
                print('\nPlease, you should type in a number between 0 and 6\n')
                
        elif user_input == 2:
            
            def user_input_2():
                print()
                try:
                    sub_user_input = int(input('Input: \n0 to return to main menu \n1 to print courier list \
                                            \n2 to add a new courier and print list \n3 to print index and names in your courier and update courier \
                                            \n4 to remove a courier \n5 to clear the screen \
                                            \n6 to clear courier list: '))
                except Exception:
                    os.system('cls || clear')
                    print('\nYou input string(s) instead of a number, clearing the screen and returning to main menu\n')
                else:    
                    return sub_user_input
            
            input_result_cour = user_input_2()
            
            if input_result_cour == 1:
                if use_cour_list:
                    if len(use_cour_list) == 1:
                        print(f'\nYou have {use_cour_list} courier at your service\n')
                    else:
                        print(f'\nYou have {use_cour_list} couriers at your service\n')
                else:
                    print(f'\nYou have no courier service\n')
                
            elif input_result_cour == 2:
                
                def if_user_input_2_is_2():
                    
                    sub_user_input_3 = input('\nPlease, type in a courier name to add to your service: ').title()
                    sub_user_input_3_ph = input('Please, type in the courier phone number: ')
                    cour_dict.clear()
                    cour_dict['name'] = sub_user_input_3
                    cour_dict['phone'] = sub_user_input_3_ph
                    copy_courier_dict1 = deepcopy(cour_dict)
                    use_cour_list.append(copy_courier_dict1)
                
                    if len(use_cour_list) == 1:
                        print(f'You now have {use_cour_list} courier at your service\n')
                    else:
                        print(f'\nYou now have {use_cour_list} couriers at your service\n') 
                
                if_user_input_2_is_2()
                
            elif input_result_cour == 3:
                
                def if_user_input_2_is_3():
                    
                    if use_cour_list:
                        print()
                        print('index \t courier')
                        for index, items in enumerate(use_cour_list):
                            print(str(index), '\t', str(items))
                        print()   
                     
                        try:
                            if len(use_cour_list) > 1:
                                sub_user_input_ind = int(input(f'you may update your courier service \nInput a number between 0 to {len(use_cour_list)-1} for the courier you wish to update: '))
                            else:
                                sub_user_input_ind = int(input(f'Please, input 0 to change/update the courier: '))
                            sub_user_input_name= input('\nPlease, type in the replacement: ')
                            sub_user_input_ph = input('\nPlease, type in the courier phone number: ')
                            
                            if sub_user_input_name:
                                cour_dict.clear()
                                cour_dict['name'] = sub_user_input_name
                                cour_dict['phone'] = sub_user_input_ph
                                copy_courier_dict2 = deepcopy(cour_dict)
                                use_cour_list[sub_user_input_ind] =  copy_courier_dict2
                                print()
                                print(f'You now have {use_cour_list} at your courier service\n')
                            else:
                                print('\nCourier name missing; thus, courier not added. Returning to main menu\n')
                                
                        except Exception as ex:
                            print(f'\n {ex} \n')
                            print('Returning to main menu\n')
                    else:
                        print('\nNo courier in service yet\n')
                                                    
                if_user_input_2_is_3()
                                                            
            elif input_result_cour == 4:   
                
                def if_user_input_2_is_4():
                    if use_cour_list:
                        print()
                        print('index \t courier')
                        for index, items in enumerate(use_cour_list):
                            print(str(index), '\t', str(items))
                        print()
                        if len(use_cour_list) == 1: 
                            get_info_cour = f'Input 0 to remove your courier: '
                        else:    
                            get_info_cour = f'Input a number between 0 and {len(use_cour_list)-1} representing the courier you wish to remove: '
                        
                        try:
                            new_user_cour_ind = int(input(get_info_cour))
                            del use_cour_list[new_user_cour_ind]
                            if use_cour_list:
                                print(f'\nYou now have {use_cour_list} at your courier service\n')
                            else:
                                print(f'\nYou now have no courier service\n')
                        except IndexError as e:
                            print(f'\n {e} \n')
                        except ValueError:
                            print('\nPlease, input an integer\n')
                            print('Returning to main menu\n')
                            
                    else:
                        print('\nYou cannot delete any courier as you have none\n')
                        
                if_user_input_2_is_4()
                    
            elif input_result_cour == 5:
                os.system('cls || clear')
            
            elif input_result_cour == 6:
                use_cour_list.clear()
                print(f'\nYou now have no courier service\n')
          
            elif not input_result_cour:
                print_courier_menu = instructions()
            else:
                print('\nPlease, type in a number between 0 and 6')   
                
        elif user_input == 3:
            
            def user_input_3():
                print()
                try:
                    ord_user_input = int(input('Input: \n0 to return to main menu \n1 to print list of available orders \
                                        \n2 to add your order \n3 to print index, available orders, and change your order status \
                                        \n4 to change your order \n5 to delete your order \
                                        \n6 to clear the screen: '))
                except Exception:
                    os.system('cls || clear')
                    print('\nYou input string(s) instead of a number, clearing the screen and returning to main menu\n')
                else:    
                    return ord_user_input
             
            input_result_ord = user_input_3() 
                
            if input_result_ord == 1:
                if use_ord_dict:
                    if len(use_ord_dict) == 1:
                        print(f'\nYou have this order: {use_ord_dict}\n')
                    else:
                        print(f'\nYou have the following orders: {use_ord_dict}\n')
                else:
                    print(f'\nThere is no order\n')

            elif input_result_ord == 2: #add order
                
                def if_user_input_3_is_2():
                    print()
                    ord_user_input_name = input('Please, type in your full name: ').title()
                    ord_user_input_add = input('Please, type in your address: ').capitalize()
                    ord_user_input_ph = input('Please, type in your phone number: ')
                    
                    if use_prod_list:
                        print('\nindex \t product category')
                        for index, items in enumerate(use_prod_list):
                            print(str(index), '\t', str(items))
                        print()
                        
                        if len(use_prod_list) > 1:
                            ord_user_input_item = input(f'Please, choose your order item by inputting the index number between 0 and {len(use_prod_list)-1} separated by commas from the categories above: ')
                        else:
                            ord_user_input_item = input('Please, input 0 to choose your order item: ')
                        try:
                            int_ord_user_input_item = [int(i) for i in ord_user_input_item.split(',')]
                        except Exception as e:
                            print(f'\n {e} \n')
                            
                    if use_prod_list:
                        print('\nindex \t couriers')
                        if use_cour_list:
                            for index, courier in enumerate(use_cour_list):
                                print(str(index), '\t', str(courier))
                        else:
                            print()
                            temp_cour_list = random.sample(('Micheal', 'Matthew', 'Cypher', 'Linda', 'Ahmed', 'Ela', 'Shauna'), k=1)
                            for index, items in enumerate(temp_cour_list):
                                print(str(index), '\t', str(items)) 
                    
                        ord_user_input_cour = input(f'\nPlease, choose a courier by inputing the name from the available courier(s) above: ').title()
                        print()
                        ord_status = 'PREPARING'
                        for char in ord_status:
                            print(char, end='')
                            sleep(0.03)
                        print()
                        
                        for _ in range(6):
                            print('\6', end='')
                            sleep(0.03)
                        print()
                        
                        mini_ord_dict = {}
                        mini_ord_dict['name'] = ord_user_input_name 
                        mini_ord_dict['address'] = ord_user_input_add 
                        mini_ord_dict['phone'] = ord_user_input_ph
                        mini_ord_dict['courier'] = ord_user_input_cour 
                        mini_ord_dict['status'] = ord_status
                        mini_ord_dict['items'] = int_ord_user_input_item
                        use_ord_dict.append(mini_ord_dict)     
                        print(use_ord_dict, '\n')
                        
                    else:
                        print('\nDue to recent surge in demand we have no product in stock. We will refill in 2 hours and alert you\n')   
                    
                if_user_input_3_is_2() 
                        
            elif input_result_ord == 3: #change order status
                
                def if_user_input_3_is_3():
                    if use_ord_dict:
                        print()
                        print('index \t order categories')
                        for index, items in enumerate(use_ord_dict):
                            print(str(index), '\t', str(items))
                        print()
                        try:
                            if len(use_ord_dict) > 1:
                                order_user_input_ind = int(input(f'you may change your order status\nInput a number between 0 to {len(use_ord_dict)-1} for the index representing your order: '))
                                print('Your order is: ', use_ord_dict[order_user_input_ind])
                            else:
                                order_user_input_ind = int(input(f'you may change your order status\nInput 0 for the index representing your order: '))
                                print('Your order is: ', use_ord_dict[order_user_input_ind])
                                
                            order_user_input_item = input('What do you want to change the status of your order to: ')
                            use_ord_dict[order_user_input_ind]['status'] = order_user_input_item
                            print()
                            print(f'Your order status has been updated: ', use_ord_dict[order_user_input_ind])
                        except Exception as ex:
                            print(ex)
                    else:
                        print('\nThere is no order yet\n')
                        
                if_user_input_3_is_3()
                        
            elif input_result_ord == 4: #update order
                
                def if_user_input_3_is_4():
                    if use_ord_dict:
                        print()
                        print('index \t order categories')
                        for index, items in enumerate(use_ord_dict):
                            print(str(index), '\t', str(items))
                        print()
                        try:
                            if len(use_ord_dict) > 1:
                                ord_user_input_ind = int(input(f'You may change your existing order\nInput a number between 0 to {len(use_ord_dict)-1} for your order in the above list: '))
                            else:
                                ord_user_input_ind = int(input(f'You may change your existing order\nInput 0 for your order in the above list: '))
                                
                            print('\nYour order is: ', use_ord_dict[ord_user_input_ind])
                            ord_user_input_item = input('\nPlease, type in the order category you wish to change: ')
                            new_ord_user_input_item = input('\nPlease, type in the replacement: ')
                            
                            if new_ord_user_input_item:
                                use_ord_dict[ord_user_input_ind][ord_user_input_item] = new_ord_user_input_item
                                print('\nYour updated order is: ', use_ord_dict[ord_user_input_ind])
                                print()
                            else:
                                print('\nOrder category missing; thus, order not updated. Returning to main menu')
                                
                        except Exception as e:
                            print(f'\n {e} \n')
                    else:
                        print('\nThere is no order yet')

                if_user_input_3_is_4()
                
            elif input_result_ord == 5: #delete order
                
                def if_user_input_3_is_5():
                    
                    if use_ord_dict:
                        print()
                        print('index \t order categories')
                        for index, items in enumerate(use_ord_dict):
                            print(str(index), '\t', str(items)) 
                            
                        if len(use_ord_dict) == 1:
                            get_del_ord_ind = f'Please, input 0 to remove your order \nor -1 if your order is not here: ' 
                        else:
                            get_del_ord_ind = f'Please, input a number between 0 and {len(use_ord_dict)-1} representing your order \nor -1 if your order is not here: '
                        try:
                            print()
                            new_user_input_ind = int(input(get_del_ord_ind))
                            if 0 <= new_user_input_ind <= len(use_ord_dict)-1:
                                del use_ord_dict[new_user_input_ind]
                                print(f'\nYour order has been deleted\n')
                            
                            elif new_user_input_ind == -1:
                                pass 
                        except IndexError as e:
                            print(f'\n {e} \n')
                            print('Returning to main menu\n')
                        except ValueError:
                            ('\nPrint, please input an integer\n')
                            print('Returning to main menu\n')
                            
                    else:
                        print('\nThere is no order yet\n')
                             
                if_user_input_3_is_5()    
                    
            elif input_result_ord == 6:
                os.system('cls || clear')
                
            elif not input_result_ord: # If the user input 0 above
                print()
                print_courier_menu = instructions()
            else:
                print('\nPlease, type in a number between 0 and 6\n')     
                        
        elif not user_input: #After every operation, the app will allow users to input 0 to save menu and exit
            
            def inventory_writer():
                with open(r'inventory-dict.csv', 'w', newline='', encoding='utf-8') as file4:
                    fieldname = ['item_name', 'price']
                    writer = csv.DictWriter(file4, fieldnames=fieldname, delimiter = ',', quoting=csv.QUOTE_MINIMAL)
                    writer.writeheader()
                    writer.writerows(item for item in use_prod_list)


            def courier_writer():
                with open(r'courier-dict.csv', 'w', newline='', encoding='utf-8') as file5:
                    fieldname = ['name', 'phone']
                    writer = csv.DictWriter(file5, fieldnames=fieldname, delimiter = ',', quoting=csv.QUOTE_MINIMAL)
                    writer.writeheader()
                    writer.writerows(item for item in use_cour_list)
                    
            def order_writer():
                with open(r'order-dict.csv', 'w', newline='', encoding='utf-8') as file6:
                    fieldname = ['name', 'address', 'phone', 'courier', 'status', 'items']
                    writer = csv.DictWriter(file6, fieldnames=fieldname, delimiter = ',', quoting=csv.QUOTE_MINIMAL)
                    writer.writeheader()
                    writer.writerows(item for item in use_ord_dict)
                    
            inv_writer = inventory_writer
            cou_writer = courier_writer
            ord_writer = order_writer
            
            if use_prod_list and use_cour_list and use_ord_dict: #Did all these because python will write invisible empty strings to file if any of the categories is empty
                                                                 #That will make the initial length of any (empty) categories equal length of the invisible string
                return inv_writer(), cou_writer(), ord_writer()  #The empty string will give a false result when I take, say, len(prod_list) if prod_list is empty
            
            elif use_prod_list and use_cour_list and not use_ord_dict:
                
                return inv_writer(), cou_writer()
                
            elif use_prod_list and use_ord_dict and not use_cour_list:
            
                return inv_writer(), ord_writer()
            
            elif use_cour_list and use_ord_dict and not use_prod_list:
               
                return cou_writer(), ord_writer()
            
            elif use_prod_list:
            
                return inv_writer()
            
            elif use_cour_list:
            
                return cou_writer()
            
            elif use_ord_dict:
            
                return ord_writer()
                        
            else:
                raise SystemExit
        else:
            print('\nPlease input an integer between 0 and 3\n')        
    
if __name__ == '__main__':
    print_prod_csv() 
    print_cour_csv()  
    instructions()   
    main_function()  