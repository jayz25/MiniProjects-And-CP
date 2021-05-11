def detectLoop(head):
    s = set()
    temp = head
    while(temp):
        if temp in set:
            return True #Loop found
        s.add(temp)
        temp = temp.next
    return False #No Loop Found
    