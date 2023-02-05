import hashlib
import json
from datetime import datetime

class Blockchain:
    def __init__(self):
        self.blocks = [] #เก็บ block
        
        # Genesis block
        genesis = self.genesis_block = Block([236, 'Genesis Block', 500.69, 'โคราช', 'เมืองนครราชสีมา', 'โคกสูง', 30000, 5000000.00], prev_hash='0')
        self.blocks.append(genesis)
        
    #สร้าง block ขึ้นมาในระบบ blockchain
    def createt_block(self, transaction):
        prev_hash = self.blocks[-1].hash
        block = Block(transaction, prev_hash)
        
        self.blocks.append(block)
    
    # เพิ่มข้อมูล (transaction) ที่ดิน
    def add_tx(self):
        transaction = []
        print('======================================================')
        land_number = int(input('เลขที่ดิน: '))
        transaction.append(land_number)
        landowner = input('ชื่อเจ้าของที่ดิน: ')
        transaction.append(landowner)
        size = float(input('ขนาดพื้นที่ของที่ดิน (m^2): '))
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
        print('======================================================')
        blockchain.createt_block(transaction)
        
        
    def display(self):
        for index, block in enumerate(self.blocks):
            print('======================================================')
            print(f'บล็อคที่: {index}')

            print(f'เลขที่ดิน: {block.transaction[0]}')
            print(f'เจ้าของที่ดิน: {block.transaction[1]}')
            print(f'ขนาดพื้นที่ของที่ดิน (m^2): {block.transaction[2]}')
            print(f'จังหวัด: {block.transaction[3]}')
            print(f'อำเภอ: {block.transaction[4]}')
            print(f'ตำบล: {block.transaction[5]}')
            print(f'รหัสไปรษณีย์: {block.transaction[6]}')
            print(f'ราคาที่ดิน: {block.transaction[7]}')
            print(f'timestamp: {block.timestamp}')
            print(f'Hash: {block.hash}')
            print(f'Previous Hash: {block.prev_hash}\n')
            
    def display_by_idx(self, idx):
        for block in self.blocks:
            if self.blocks.index(block) == idx:
                print('======================================================')
                print(f'บล็อคที่: {idx}')

                print(f'เลขที่ดิน: {block.transaction[0]}')
                print(f'เจ้าของที่ดิน: {block.transaction[1]}')
                print(f'ขนาดพื้นที่ของที่ดิน (m^2): {block.transaction[2]}')
                print(f'จังหวัด: {block.transaction[3]}')
                print(f'อำเภอ: {block.transaction[4]}')
                print(f'ตำบล: {block.transaction[5]}')
                print(f'รหัสไปรษณีย์: {block.transaction[6]}')
                print(f'ราคาที่ดิน: {block.transaction[7]}')
                print(f'timestamp: {block.timestamp}')
                print(f'Hash: {block.hash}')
                print(f'Previous Hash: {block.prev_hash}\n')
                
    def edit_data(self, idx, new_landowner):
        for block in self.blocks:
            if self.blocks.index(block) == idx:
                block.transaction[1] = new_landowner
                block.hash = block.block_hash()
    
    #ตรวจสอบการแก้ไขข้อมูล
    def validate(self):
        for i in range(1, len(self.blocks)):
            current_block = self.blocks[i]
            previous_block = self.blocks[i - 1]
            if current_block.prev_hash != previous_block.hash:
                return "Transaction has been edited!!"
        return "Transaction No change."

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
    
blockchain = Blockchain()

while True:
    #แสดงฟังก์ชันต่างๆของระบบ
    print('======================================================')
    print('เลือกรูปแบบการทำงาน')
    print('1. เพิ่มข้อมูลที่ดิน')
    print('2. แสดงข้อมูลที่ดินแบบเลือก Block ที่ต้องการ')
    print('3. แสดงข้อมูลทุก Block')
    print('4. แก้ไขข้อมูล transaction')
    print('5. ตรวจว่ามีการแก้ไขข้อมูลหรือไม่')
    print('6. ออกจากการทำงาน')
    print('======================================================')

    choice = int(input('ใส่หมายเลขรูปแบบการทำงานที่ต้องการ: '))

    if choice == 1:
        blockchain.add_tx()
    elif choice == 2:
        block_index = int(input('ใส่หมายเลย Block ที่ต้องการแสดง : '))
        blockchain.display_by_idx(block_index)
        print("")
    elif choice == 3:
        blockchain.display()
    elif choice == 4:
        block_index = int(input('ใส่หมายเลข Block ที่ต้องการแก้ไข: '))
        new_landowner = input('ใส่ชื่อเจ้าของที่ดินคนใหม่: ')
        print("")
        blockchain.edit_data(block_index, new_landowner)
    elif choice == 5:
        valid = blockchain.validate()
        print(valid)
        
    elif choice == 6:
        break
    else:
        print('ไม่มีรูปแบบการทำการ กรุณาเลือกใหม่อีกครั้ง')