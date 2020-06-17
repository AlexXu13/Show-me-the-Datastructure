import hashlib
import datetime
class Block:
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
    def calc_hash(self):
        newsha = hashlib.sha256()
        newhash = self.data.encode('utf-8')+self.timestamp.encode('utf-8')
        newsha.update(newhash)
        return newsha.hexdigest()

class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None
    def append(self,timestamp, data):
        if not self.head:
            self.head = Block(timestamp, data, 0)
            self.next = self.head
        else:
            sub = self.next
            self.next = Block(timestamp, data, sub)
            self.next.previous_hash = sub

if __name__ == '__main__':
    def nowtime():
        return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    block0 = Block(nowtime(), "I'm block0", 0)
    block1 = Block(nowtime(), "I'm block1", block0)
    block2 = Block(nowtime(), "I'm block2", block1)
    block3 = Block(nowtime(), "I'm block3", block2)
    block4 = Block(nowtime(), "I'm block4", block3)
    newlist = LinkedList()
    
    
    #test block0
    print(str(block0.data) + " " + str(block0.hash) )
    #test block1
    print(str(block1.data) + " " + str(block1.hash) )
    #test block2
    print(str(block2.data) + " " + str(block2.hash) )
    #test block3
    print(str(block3.data) + " " + str(block3.hash) )
    #test append once
    newlist.append(nowtime(),"I'm block5")
    #test append twice
    newlist.append(nowtime(), "I'm block6")
    print(str(newlist.head.data) + " " + str(newlist.head.hash))
    print(str(newlist.next.data) + " " + str(newlist.next.hash))
    
