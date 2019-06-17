def reversePrint(head):
    if head is None:
        return
    reversePrint(head.next)
    print(head.data)
