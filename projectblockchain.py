import hashlib
import json
from datetime import datetime

class Blockchain:
    def __init__(self):
        self.blocks = [] #เก็บ block
        
        # Genesis block
        genesis = self.genesis_block = Block([236, 'Genesis Block', 640.50, 'โคราช', 'เมืองนครราชสีมา', 'โคกสูง', 30000, 5000000.00, '13/02/1999'], prev_hash='0')
        self.blocks.append(genesis)
        
        # เพิ่ม 10 block
        info1 = ([101, 'tle', 200.00, 'โคราช', 'เมื่องนครราชสีมา', 'สุรนารี', 30000, 1500000.00, '15/04/2002'])
        info2 = ([231, 'pud', 423.00, 'บึงกาฬ', 'เซกา', 'เซกา', 38150, 1200000.00, '22/05/2004'])
        info3 = ([254, 'nine', 500.00, 'บึงกาฬ', 'เซกา', 'บึงโขงหลง', 12354, 2342000.00, '15/04/2005'])
        info4 = ([6452, 'opp', 500.00, 'หนองคาบ', 'เมืองหนองคาย', 'จากยา', 56215, 2120000.00, '15/04/2005'])
        info5 = ([7865, 'uma', 400.00, 'บุรีรัมย์', 'เมื่องบุรีรัมย์', 'นางรอง', 54621, 2342000.00, '15/04/2005'])
        info6 = ([2134, 'tods', 450.00, 'นราธิวาส', 'เมื่องนราธิวาส', 'เม๊ก', 7864, 1234200.00, '15/04/2006'])
        info7 = ([45621, 'henlies', 900.00, 'สกลนคร', 'เมืองสกลนคร', 'สว่างแดนดิน', 56123, 4523000.00, '15/04/2007'])
        info8 = ([1237, 'you', 502.00, 'อุดรธานี', 'เมื่องอุดรธานี', 'สามหมอ', 31500, 2001200.00, '15/04/2005'])
        info9 = ([12354, 'tle', 645.00, 'กรุงเทพมหานคร', 'เมื่องกรุงเทพมหานคร', 'ปากมด', 54640, 1400000.00, '15/04/2004'])
        info10 = ([1324, 'kurve', 754.00, 'อยุธยา', 'เมื่องอยุธยา', 'เสนา', 12354, 2000000.00, '15/04/2019'])
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
        
    #สร้าง block ขึ้นมาในระบบ blockchain
    def create_block(self, transaction):
        prev_hash = self.blocks[-1].hash
        block = Block(transaction, prev_hash)
        
        self.blocks.append(block)
    
    # เพิ่มข้อมูล (transaction) ที่ดิน
    def add_tx(self):
        transaction = []
        land_number = int(input('\nเลขที่ดิน: '))
        transaction.append(land_number)
        landowner = input('ชื่อเจ้าของที่ดิน: ')
        transaction.append(landowner)
        size = float(input('ขนาดพื้นที่ของที่ดิน(ตารางเมตร): '))
        transaction.append(size)
        province = input('จังหวัด: ')
        transaction.append(province)
        district = input('อำเภอ: ')
        transaction.append(district)
        parish = input('ตำบล: ')
        transaction.append(parish)
        zip_code = int(input('รหัสไปรษณีย์: '))
        transaction.append(zip_code)
        price = float(input('ราคาที่ดิน: '))
        transaction.append(price)
        time = input('เวลาที่ออกที่ดิน: ')
        transaction.append(time)
        blockchain.create_block(transaction)
        print(f'\n>> เพิ่มข้อมูลเสร็จสิ้น <<')
        
        
    def display(self):
        for index, block in enumerate(self.blocks):
            print(f'\nบล็อคที่: {index}')

            print(f'เลขที่ดิน: {block.transaction[0]}')
            print(f'เจ้าของที่ดิน: {block.transaction[1]}')
            print(f'ขนาดพื้นที่ของที่ดิน(ตารางเมตร): {block.transaction[2]}')
            print(f'จังหวัด: {block.transaction[3]}')
            print(f'อำเภอ: {block.transaction[4]}')
            print(f'ตำบล: {block.transaction[5]}')
            print(f'รหัสไปรษณีย์: {block.transaction[6]}')
            print(f'ราคาที่ดิน: {block.transaction[7]}')
            print(f'เวลาที่ออกที่ดิน: {block.transaction[8]}')
            print(f'timestamp: {block.timestamp}')
            print(f'Hash: {block.hash}')
            print(f'Previous Hash: {block.prev_hash}')
            
    def display_by_name(self, name):
        for index, block in enumerate(self.blocks):
            if block.transaction[1] == name:
                print(f'\nบล็อคที่: {index}')

                print(f'เลขที่ดิน: {block.transaction[0]}')
                print(f'เจ้าของที่ดิน: {block.transaction[1]}')
                print(f'ขนาดพื้นที่ของที่ดิน(ตารางเมตร): {block.transaction[2]}')
                print(f'จังหวัด: {block.transaction[3]}')
                print(f'อำเภอ: {block.transaction[4]}')
                print(f'ตำบล: {block.transaction[5]}')
                print(f'รหัสไปรษณีย์: {block.transaction[6]}')
                print(f'ราคาที่ดิน: {block.transaction[7]}')
                print(f'เวลาที่ออกที่ดิน: {block.transaction[8]}')
                print(f'timestamp: {block.timestamp}')
                print(f'Hash: {block.hash}')
                print(f'Previous Hash: {block.prev_hash}')

    def check_name(self, name):
        data = []
        for block in self.blocks:
            if block.transaction[1] == name:
                data.append(block)
        if data != []:
            self.display_by_name(name)
        else:
            print(f'\n>> ชื่อ {name} ไม่มีข้อมูลที่ดิน <<')
            
    def display_by_index(self, index):
        for block in self.blocks:
            if self.blocks.index(block) == index:
                print(f'\nบล็อคที่: {index}')

                print(f'เลขที่ดิน: {block.transaction[0]}')
                print(f'เจ้าของที่ดิน: {block.transaction[1]}')
                print(f'ขนาดพื้นที่ของที่ดิน(ตารางเมตร): {block.transaction[2]}')
                print(f'จังหวัด: {block.transaction[3]}')
                print(f'อำเภอ: {block.transaction[4]}')
                print(f'ตำบล: {block.transaction[5]}')
                print(f'รหัสไปรษณีย์: {block.transaction[6]}')
                print(f'ราคาที่ดิน: {block.transaction[7]}')
                print(f'เวลาที่ออกที่ดิน: {block.transaction[8]}')
                print(f'timestamp: {block.timestamp}')
                print(f'Hash: {block.hash}')
                print(f'Previous Hash: {block.prev_hash}')
    
    def check_index(self, index):
        data = []
        for block in self.blocks:
            if self.blocks.index(block) == index:
                data.append(block)
        if data != []:
            self.display_by_index(index)
        else:
            print(f'\n>> ไม่มีข้อมูลที่ดิน <<')
            
    def edit_data(self, index):
        for block in self.blocks:
            if self.blocks.index(block) == index:
                block = self.blocks[index]

                # แสดงฟังก์ชันในการแก้ไข
                while True:
                    print('\nเลือกสิ่งที่คุณต้องการเปลี่ยน')
                    print('1. แก้ไขเลขที่ดิน')
                    print('2. แก้ไขเจ้าของที่ดิน')
                    print('3. แก้ไขขนาดพื้นที่ของที่ดิน')
                    print('4. แก้ไขจังหวัด')
                    print('5. แก้ไขอำเภอ')
                    print('6. แก้ไขตำบล')
                    print('7. แก้ไขรหัสไปรษณี')
                    print('8. แก้ไขราคาที่ดิน')
                    print('9. แก้ไขเวลาที่ออกที่ดิน')
                    print('10. แก้ไขเสร็จสิ้น')

                    choice = int(input('ใส่หมายเลขรูปแบบที่ต้องการแก้ไข: '))
                    if (choice == 1):
                        new_land_number = int(input('เลขที่ดิน: '))
                        block.transaction[0] = new_land_number
                    elif (choice == 2):
                        new_landowner = input('ชื่อเจ้าของที่ดิน: ')
                        block.transaction[1] = new_landowner
                    elif (choice == 3):
                        new_size = float(input('ขนาดพื้นที่ของที่ดิน(ตารางเมตร): '))
                        block.transaction[2] = new_size
                    elif (choice == 4):
                        new_province = input('จังหวัด: ')
                        block.transaction[3] = new_province
                    elif (choice == 5):
                        new_district = input('อำเภอ: ')
                        block.transaction[4] = new_district
                    elif (choice == 6):
                        new_parish = input('ตำบล: ')
                        block.transaction[5] = new_parish
                    elif (choice == 7):
                        new_zip_code = int(input('รหัสไปรษณีย์: '))
                        block.transaction[6] = new_zip_code
                    elif (choice == 8):
                        new_price = float(input('ราคาที่ดิน: '))
                        block.transaction[7] = new_price
                    elif (choice == 9):
                        new_time = float(input('ราคาที่ดิน: '))
                        block.transaction[8] = new_time
                    elif (choice == 10):
                        print(f'\n>> แก้ไขเสร็จสิ้น <<')
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
            print(f'\n>>ไม่มีข้อมูลที่ดิน<<')
            
    #ตรวจสอบการแก้ไขข้อมูล
    def validate(self):
        index = []
        for i in range(1, len(self.blocks)):
            current_block = self.blocks[i]
            previous_block = self.blocks[i - 1]
            if current_block.prev_hash != previous_block.hash:
                index.append(i)
        if index != []:
            print(f'\n>> ข้อมูลถูกแก้ไข ที่ตำแหน่ง {index} <<')
        else:
            print(f'\n>> ข้อมูลไม่ถูกแก้ไข <<')

class Block:
    #โครงสร้าง block
    def __init__(self, transaction, prev_hash):
        self.timestamp = str(datetime.now())
        self.transaction = transaction
        self.prev_hash = prev_hash
        self.hash = self.block_hash()

    def block_hash(self):
        tx = json.dumps(self.transaction)
        block_contents = (str(tx) + str(self.prev_hash)).encode()
        return hashlib.sha256(block_contents).hexdigest()


# Main

blockchain = Blockchain()

while True:
    #แสดงฟังก์ชันต่างๆของระบบ
    print('\nเลือกรูปแบบการทำงาน')
    print('1. เพิ่มข้อมูลที่ดิน')
    print('2. แสดงข้อมูลที่ดินแบบเลือก Block ที่ต้องการ')
    print('3. แสดงข้อมูลทุก Block')
    print('4. แสดงข้อมูลจากชื่อ')
    print('5. แก้ไขข้อมูล transaction')
    print('6. ตรวจว่ามีการแก้ไขข้อมูลหรือไม่')
    print('7. ออกจากการทำงาน\n')
    choice = int(input('ใส่หมายเลขรูปแบบการทำงานที่ต้องการ: '))

    if (choice == 1):
        blockchain.add_tx()
    elif (choice == 2):
        index = int(input('ใส่หมายเลย Block ที่ต้องการแสดง : '))
        blockchain.check_index(index)
    elif (choice == 3):
        blockchain.display()
    elif (choice == 4):
        name = input('ใส่ชื่อที่ต้องการแสดง : ')
        blockchain.check_name(name)
    elif (choice == 5):
        index = int(input('ใส่หมายเลข Block ที่ต้องการแก้ไข: '))
        blockchain.check_index_e(index)
    elif (choice == 6):
        blockchain.validate()
    elif (choice == 7):
        break
    else:
        print('>> ไม่มีรูปแบบการทำงาน กรุณาเลือกใหม่อีกครั้ง <<')
        