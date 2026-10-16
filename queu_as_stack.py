class Queue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
        #stackout is gonna be stackin but reversed so i can take the bottom item of stackin as the top item of stackout

    def enqueue(self, value):
        self.stack_in.append(value)

    def dequeue(self):
        if len(self.stack_out) == 0:
            # make oldest item at the top so basically flip the box upsidedown
            while len(self.stack_in) > 0:
                top = self.stack_in.pop()
                self.stack_out.append(top)
        # returns the top item? or removes it and returns it 
        return self.stack_out.pop()
    def peek(self):
        if self.is_empty():
            #so it doesnt crash if theres no item to look at
            return None
        if len(self.stack_out) == 0:
            while len(self.stack_in) > 0:
                top_item = self.stack_in.pop()
                self.stack_out.append(top_item)
        # returns -1 because the stack is upside down so the top item is at the end  
        return self.stack_out[-1]

    def is_empty(self):
        #look if there is anything in the in stack
        if len(self.stack_in) != 0:
            return False  # If it has items, the queue is NOT empty
            
        # look if there is anything in the out stack
        if len(self.stack_out) != 0:
            return False  # If it has items, the queue is NOT empty
            
        #If both checks passed with zero items, it is truly empty
        return True
    def size(self):
        #Gemini said this is better than making variables then adding them
        return len(self.stack_in) + len(self.stack_out)


if __name__ == "__main__":
    my_queue = Queue()
    my_queue.enqueue(2)
    my_queue.enqueue(1)
    my_queue.enqueue(3)
    print(my_queue.peek())
    print(my_queue.size())
    print(my_queue.dequeue())
    print(my_queue.dequeue())   
    print(my_queue.is_empty())
