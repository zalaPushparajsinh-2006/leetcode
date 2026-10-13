class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        money -= children
        eighters = (money//7) 
        remainder = money%7
        if children >= eighters and remainder == 0:
            return eighters
        if children < eighters:
            return children-1
        if remainder > 0:
            if children == eighters:
                return eighters - 1
            elif children > eighters:
                if remainder == 3 and (children - eighters) == 1:
                    return eighters - 1
                else:
                    return eighters