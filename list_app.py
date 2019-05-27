#THIS IS AN SIMPLE LIST OPERATION APPLICATION

print('------------List Application------------')
print('          1. Add Element')
print('          2. Change Element')
print('          3. Delete Element')
print('          4. Show List')
print('          5. Show Indexed Data')
print('          0. Exit')
print('------------List Application------------')

storage = []  #DECLARE LIST

while True:
    operation = int(input('Please Enter Operation: '))
    #EXIT OPERATION
    if operation == 0:
        confirm = input('Are you sure to exit! Enter \'yes\': ')
        if confirm == 'yes':
            break
    #ADD ELEMENT OPERATION
    if operation == 1:
        item = input('Enter an item: ').split()
        storage.extend(item)
        print('{} is added in list!'.format(item))
    #CHANGE ELEMENT OPERATION
    if operation == 2:
        if len(storage) < 1:
            print('List is Empty!')
        else:

            index = int(input('Enter item\'s index 0 to {}: '.format(len(storage)-1)))
            if index < len(storage)-1:
                print('Old item is {}'.format(storage[index]))
                new_item = input('Enter an new item: ')
                storage[index] = new_item
                print('Data: ', storage)
            else:
                print('Index out of Range!')
        #print('{} as new item add on {} position!'.format(new_item, index))
    #DELETE ELEMENT OPERATION
    if operation == 3:
        index = int(input('Enter item\'s index: '))
        confirm = input('Enter yes for confirm: ')
        if (index <= len(storage)-1):
            print('{} is deleted from {} position!'.format(storage[index], index))
            if confirm == 'yes':
                del storage[index]
                print('Data delete successfully!')
            else:
                print('Data: ', storage, 'Length: ', len(storage))
                print('Data not deleted!')
        else:
            print('Index out of bound!')
    #SHOW LIST OPERATION
    if operation == 4:
        print('Data: ', storage)
        print('Length: ', len(storage))
    #SHOW INDEXED DATA OPERATION
    if operation == 5:
        for data in storage:
            print(data)
        print('Length: ', len(storage))
