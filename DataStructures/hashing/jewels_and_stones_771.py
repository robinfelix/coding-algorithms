
def numJewelsInStones(J, S):
    setJ = set(J)
    print (setJ)
    return sum(s in setJ for s in S)

jewels = "aA"
stones = "aAAbbbb"
J = jewels
S = stones
print (numJewelsInStones(J,S))