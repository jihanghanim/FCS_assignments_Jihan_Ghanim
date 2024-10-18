#Exercise 3
# dic of available items with prices
#dic_items={barcode: ['item name', quantiy, price]}
dic_items={'11003': ['item1', 12, 6],'11004': ['item2', 14, 2]}
#dic of purchased items
dic_purchase= {}

#function to enter purchased items
def item(dic_purchase, dic_items):

    barcode= input('Please enter the item barcode: ')
    if not barcode in dic_items :
        print('The barcode does not exist')
        #exist system
        return
    try:
        q_item= int(input('Please enter the quantity of the purchased item: '))
    except:
        print('Quantity is invalid')
        #exist system
        return 
    
    if q_item <0:
        print('Quantity is invalid')
        #exist system
        return

    if barcode in dic_purchase:
        dic_purchase[barcode]+= q_item
    else:
        dic_purchase[barcode]= q_item

    dic_items[barcode][1] -= q_item


    ans2= input('Do you want to add another item? y/n ')
    if ans2== 'y':
        #enter purchased items
        item(dic_purchase, dic_items)

    # even if the user by mistake did not enter "n" it would still print the receipt
    else:

            #print receipt
            print("Item", "Quantity", "Price")
            t_q=0
            t_p=0
            for bc in dic_purchase:
                print(dic_items[bc][0], '   ',dic_purchase[bc], '   ',dic_purchase[bc] *dic_items[bc][2],'$\n' )
                t_q+= dic_purchase[bc]
                t_p+= dic_purchase[bc] *dic_items[bc][2]
            
            print('Total Amount','Total Price')
            print('     ',t_q, '        ',t_p, '$')

            #ask to start a new recipe
            dic_purchase={}
            pos(dic_purchase, dic_items)
    


#POS system
def pos(dic_purchase, dic_items):   
    ans= input('Do you want to start a new recipe? y/n ')
    if ans== 'y':
        # call function to enter purchased items
        item(dic_purchase, dic_items)
    elif ans== 'n':
        #exist sysem
        return
    else:
        print('Please answer by y/n.')
        #exist sysem
        return

pos(dic_purchase, dic_items)
