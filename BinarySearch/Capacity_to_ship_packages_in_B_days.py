def daysForShipWithCapacity(self, A, capacity):
        n_days = 0
        totalWeight = 0
        for i in A:
            if(totalWeight + i > capacity):
                totalWeight = 0
                n_days += 1
            totalWeight += i
        return n_days

def solve(self, A, B):
    # given the capacity
    # we have one ship
    # And B days
    # we can allot different capacities to the ship 
    # and check whether the ship can carry the load 
    # in B days

    low = max(A)
    high = sum(A)
    mid = 0
    while (low <= high):
        mid = low + (high-low)//2
        if(self.daysForShipWithCapacity(A, mid) >= B):
            # try increasing the capacity
            low = mid + 1
        else:
            high = mid - 1
    return low