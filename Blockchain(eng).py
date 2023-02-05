import hashlib
import json
from datetime import datetime

class Blockchain:
    def __init__(self):
        self.blocks = []
        
        genesis = self.genesis_block = Block([236, 'Genesis Block', 640.50, 'korat', 'mueng', 'Kocsnug', 30000, 5000000.00, '13/02/1999'], prev_hash='0')
        self.blocks.append(genesis)
        
        info1 = ([101, 'tle', 200.00, 'korat', 'mueng', 'suranaree', 30000, 1500000.00, '15/04/2002'])
        info2 = ([231, 'pud', 423.00, 'buengkan', 'seka', 'seka', 38150, 1200000.00, '22/05/2004'])
        info3 = ([254, 'nine', 500.00, 'buengkan', 'seka', 'muengkonglong', 12354, 2342000.00, '15/04/2005'])
        info4 = ([6452, 'opp', 500.00, 'nongkai', 'mueng', 'jakya', 56215, 2120000.00, '15/04/2005'])
        info5 = ([7865, 'uma', 400.00, 'burirum', 'mueng', 'nangrong', 54621, 2342000.00, '15/04/2005'])
        info6 = ([2134, 'tods', 450.00, 'naratiwat', 'mueng', 'mek', 7864, 1234200.00, '15/04/2006'])
        info7 = ([45621, 'henlies', 900.00, 'sakonnakhon', 'mueng', 'swangdandin', 56123, 4523000.00, '15/04/2007'])
        info8 = ([1237, 'you', 502.00, 'udontani', 'mueng', 'sammho', 31500, 2001200.00, '15/04/2005'])
        info9 = ([12354, 'tle', 645.00, 'bangkok', 'mueng', 'pakmod', 54640, 1400000.00, '15/04/2004'])
        info10 = ([1324, 'kurve', 754.00, 'ayutthaya', 'mueng', 'sena', 12354, 2000000.00, '15/04/2019'])
        self.create_block(info1)
        self.create_block(info2)
        self.create_block(info3)
        self.create_block(info4)
        self.create_block(info5)
        self.create_block(info6)
        self.create_block(info7)
        self.create_block(info8)
        self.create_block(info9)
        self.create_block(info10)
        
    def create_block(self, transaction):
        prev_hash = self.blocks[-1].hash
        block = Block(transaction, prev_hash)
        
        self.blocks.append(block)
    
    def add_tx(self):
        transaction = []
        land_number = int(input('\nnumber: '))
        transaction.append(land_number)
        landowner = input('name: ')
        transaction.append(landowner)
        size = float(input('size(m*m): '))
        transaction.append(size)
        province = input('province: ')
        transaction.append(province)
        district = input('district: ')
        transaction.append(district)
        parish = input('parish: ')
        transaction.append(parish)
        zip_code = int(input('zip code: '))
        transaction.append(zip_code)
        price = float(input('price: '))
        transaction.append(price)
        time = input('time of landing: ')
        transaction.append(time)
        blockchain.create_block(transaction)
        print(f'\n>> add success <<')
        
        
    def display(self):
        for index, block in enumerate(self.blocks):
            print(f'\nchain: {index}')

            print(f'number: {block.transaction[0]}')
            print(f'name: {block.transaction[1]}')
            print(f'size(m*m): {block.transaction[2]}')
            print(f'province: {block.transaction[3]}')
            print(f'district: {block.transaction[4]}')
            print(f'parish: {block.transaction[5]}')
            print(f'zip code: {block.transaction[6]}')
            print(f'price: {block.transaction[7]}')
            print(f'time of landing: {block.transaction[8]}')
            print(f'timestamp: {block.timestamp}')
            print(f'hash: {block.hash}')
            print(f'previous Hash: {block.prev_hash}')
            
    def display_by_name(self, name):
        for index, block in enumerate(self.blocks):
            if block.transaction[1] == name:
                print(f'\nchain: {index}')

                print(f'number: {block.transaction[0]}')
                print(f'name: {block.transaction[1]}')
                print(f'size(m*m): {block.transaction[2]}')
                print(f'province: {block.transaction[3]}')
                print(f'district: {block.transaction[4]}')
                print(f'parish: {block.transaction[5]}')
                print(f'zip code: {block.transaction[6]}')
                print(f'price: {block.transaction[7]}')
                print(f'time of landing: {block.transaction[8]}')
                print(f'timestamp: {block.timestamp}')
                print(f'hash: {block.hash}')
                print(f'previous Hash: {block.prev_hash}')

    def check_name(self, name):
        data = []
        for block in self.blocks:
            if block.transaction[1] == name:
                data.append(block)
        if data != []:
            self.display_by_name(name)
        else:
            print(f'\n>>{name} not have data <<')
            
    def display_by_index(self, index):
        for block in self.blocks:
            if self.blocks.index(block) == index:
                print(f'\nchain: {index}')

                print(f'number: {block.transaction[0]}')
                print(f'name: {block.transaction[1]}')
                print(f'size(m*m): {block.transaction[2]}')
                print(f'province: {block.transaction[3]}')
                print(f'district: {block.transaction[4]}')
                print(f'parish: {block.transaction[5]}')
                print(f'zip code: {block.transaction[6]}')
                print(f'price: {block.transaction[7]}')
                print(f'time of landing: {block.transaction[8]}')
                print(f'timestamp: {block.timestamp}')
                print(f'hash: {block.hash}')
                print(f'previous Hash: {block.prev_hash}')
    
    def check_index(self, index):
        data = []
        for block in self.blocks:
            if self.blocks.index(block) == index:
                data.append(block)
        if data != []:
            self.display_by_index(index)
        else:
            print(f'\n>> not have data <<')
            
    def edit_data(self, index):
        for block in self.blocks:
            if self.blocks.index(block) == index:
                block = self.blocks[index]

                # แสดงฟังก์ชันในการแก้ไข
                while True:
                    print('\nchoose fix')
                    print('1. fix number')
                    print('2. fix name')
                    print('3. fix size')
                    print('4. fix Province')
                    print('5. fix district')
                    print('6. fix parish')
                    print('7. fix zip code')
                    print('8. fix Price')
                    print('9. fix time of landing')
                    print('10. fix success')

                    choice = int(input('Choose fix: '))
                    if (choice == 1):
                        new_land_number = int(input('number: '))
                        block.transaction[0] = new_land_number
                    elif (choice == 2):
                        new_landowner = input('name: ')
                        block.transaction[1] = new_landowner
                    elif (choice == 3):
                        new_size = float(input('size(m*m): '))
                        block.transaction[2] = new_size
                    elif (choice == 4):
                        new_province = input('province: ')
                        block.transaction[3] = new_province
                    elif (choice == 5):
                        new_district = input('district: ')
                        block.transaction[4] = new_district
                    elif (choice == 6):
                        new_parish = input('parish: ')
                        block.transaction[5] = new_parish
                    elif (choice == 7):
                        new_zip_code = int(input('zip code: '))
                        block.transaction[6] = new_zip_code
                    elif (choice == 8):
                        new_price = float(input('price: '))
                        block.transaction[7] = new_price
                    elif (choice == 9):
                        new_time = float(input('time of landing: '))
                        block.transaction[8] = new_time
                    elif (choice == 10):
                        print(f'\n>> fix success <<')
                        break
                block.hash = block.block_hash()

    def check_index_e(self, index):
        data = []
        for block in self.blocks:
            if self.blocks.index(block) == index:
                data.append(block)
        if data != []:
            self.edit_data(index)
        else:
            print(f'\n>>not have data<<')
            
    def validate(self):
        index = []
        for i in range(1, len(self.blocks)):
            current_block = self.blocks[i]
            previous_block = self.blocks[i - 1]
            if current_block.prev_hash != previous_block.hash:
                index.append(i)
        if index != []:
            print(f'\n>> data change on {index} <<')
        else:
            print(f'\n>> data not change <<')

class Block:
    def __init__(self, transaction, prev_hash):
        self.timestamp = str(datetime.now())
        self.transaction = transaction
        self.prev_hash = prev_hash
        self.hash = self.block_hash()

    def block_hash(self):
        tx = json.dumps(self.transaction)
        block_contents = (str(tx) + str(self.prev_hash)).encode()
        return hashlib.sha256(block_contents).hexdigest()

blockchain = Blockchain()

while True:
    print('\nchoose functions')
    print('1. add data')
    print('2. type block and show data')
    print('3. show all data')
    print('4. type name and show data')
    print('5. fix data')
    print('6. check data ')
    print('7. out of program\n')
    choice = int(input('type number call functions: '))

    if (choice == 1):
        blockchain.add_tx()
    elif (choice == 2):
        index = int(input('type block to show: '))
        blockchain.check_index(index)
    elif (choice == 3):
        blockchain.display()
    elif (choice == 4):
        name = input('type name to show: ')
        blockchain.check_name(name)
    elif (choice == 5):
        index = int(input('type block to fix: '))
        blockchain.check_index_e(index)
    elif (choice == 6):
        blockchain.validate()
    elif (choice == 7):
        break
    else:
        print('>> fail, please choose again <<')
        