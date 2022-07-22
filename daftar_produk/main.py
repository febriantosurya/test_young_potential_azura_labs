import os, csv

class Product:
  def __init__(self):
    while True:
      os.system('clear')
      print('\t===PRODUCT LIST===')
      product_list = self.check_file()
      print('\n\n\t======OPTION======\n-> Input 1 to see Product detail\n-> Input 2 to add Product')
      print('-> Input 3 to edit Product\n-> Input 4 to delete Product\n-> Input 5 to exit program\n')
      try:
        option = int(input('=> '))
        if option == 1:
          self.product_detail(product_list)
        if option == 2:
          self.add_product(product_list)
        if option == 3:
          self.edit_product(product_list)
        if option == 4:
          self.delete_product(product_list)
        if option == 5:
          break
      except:
        continue

  def edit_product(self, products):
    edit_product = int(input('Input product number to edit = '))
    os.system('clear')
    product_name = products[edit_product - 1][0]
    print('Product {0} will be edited\n'.format(product_name))
    products[edit_product - 1][1] = input('Price = ')
    products[edit_product - 1][2] = input('Stock = ')
    with open('dump.txt', 'w+') as file:
      writer = csv.writer(file)
      writer.writerows(products)
    print('\n{0} is updated!'.format(product_name))
    input('\nPress enter to back')

  def delete_product(self, products):
    del_product = int(input('Input product number to delete = '))
    os.system('clear')
    del_product_name = products[del_product - 1][0]
    print('Are you sure to delete {0}? [Y/N]'.format(del_product_name))
    decision = input('=> ')
    if decision == 'y' or decision == 'Y':  
      products.pop(del_product - 1)
      with open('dump.txt', 'w+') as file:
        writer = csv.writer(file)
        writer.writerows(products)
      print('\n{0} is deleted!'.format(del_product_name))
      input('\nPress enter to back')
    elif decision == 'n' or decision == 'N':
      pass

  def add_product(self, products):
    os.system('clear')
    new_product = []
    new_product.append(input('Product Name\t= '))
    new_product.append(input('Price\t\t= '))
    new_product.append(input('Stock\t\t= '))
    products.append(new_product)
    with open('dump.txt', 'w+') as file:
      writer = csv.writer(file)
      writer.writerows(products)
    print('\nItem Added')
    input('\nPress enter to back')

  def product_detail(self, products):
    no_product = int(input('=> Input product number = '))
    os.system('clear')
    print('Product Name\t= {0}'.format(products[no_product - 1][0]))
    print('Price\t\t= {0}'.format(products[no_product - 1][1]))
    print('Stock\t\t= {0}'.format(products[no_product - 1][2]))
    input('\nPress enter to back')
      
  def check_file(self):
    arr_data = []
    data = open('dump.txt')
    data = csv.reader(data, delimiter=',')
    for item in data:
      arr_data.append(item)
    for i in range(len(arr_data)):
      print('{0}. '.format(i + 1) + arr_data[i][0])
    return arr_data

Product()