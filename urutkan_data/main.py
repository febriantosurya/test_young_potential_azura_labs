import pandas as pd

def conv_excel_to_csv():
  read_file = pd.read_excel('data/all_data.xlsx', sheet_name='Sheet1')
  read_file.to_csv('data/data_input.csv', index = None, header=True)

def conv_to_arr():
  scsv = open('data/data_input.csv')
  text = scsv.readlines()
  text = [s.strip('\n') for s in text]
  arr2 = []
  for item in text[1:]:
    arr1 = item.split(',')
    arr2.append(arr1)
  return arr2

def sorting(arr):
  temp = []
  for i in range(len(arr) - 1):
    for j in range(i, len(arr)):
      if int(arr[i][1]) > int(arr[j][1]):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
      elif i == 0:
        pass
      else:
        if int(arr[i - 1][1]) == int(arr[i][1]) and float(arr[i - 1][2]) < float(arr[i][2]):
          temp = arr[i]
          arr[i] = arr[i - 1]
          arr[i - 1] = temp
        elif int(arr[i - 1][1]) == int(arr[i][1]) and float(arr[i - 1][2]) == float(arr[i][2]) and int(arr[i - 1][3]) < int(arr[i][3]):
          temp = arr[i]
          arr[i] = arr[i - 1]
          arr[i - 1] = temp
  return arr

def main():
  conv_excel_to_csv()
  res = sorting(conv_to_arr())
  for item in res:
    print(item)
  # conv_to_arr()
  return 0

if __name__ == '__main__':
  main()