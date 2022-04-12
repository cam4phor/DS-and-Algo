class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next


def mergeTwoSortedList(firstList: ListNode, secondList: ListNode):
  fN = firstList
  sN = secondList
  finalList = ListNode()
  t = finalList
  while(fN.next and sN.next):
    if(fN.data < sN.data):
      finalList.data = fN.data
      fN = fN.next
    else:
      finalList.data = sN.data
      sN = sN.next
    finalList.next = ListNode()
    finalList = finalList.next
  
  while(fN.next):
    finalList.data = fN.data
    fN = fN.next
    finalList.next = ListNode()
    finalList = finalList.next
  
  while(sN.next):
    finalList.data = sN.data
    sN = sN.next
    finalList.next = ListNode()
    finalList = finalList.next

  del finalList
  while(t):
    print(t.data)
    t = t.next

A = [2, 3, 3]
B = [1, 4, 5]

def populateList(A):
  firstList = ListNode()
  k = firstList
  for i in range(len(A)):
    firstList.data = A[i]
    firstList.next = ListNode()
    firstList = firstList.next

  return k

listOne = populateList(A)
listTwo = populateList(B)

mergeTwoSortedList(listOne, listTwo)


    
    
    

    
