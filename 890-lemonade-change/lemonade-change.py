class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                ten += 1
        
            change = bill - 5
            if change == 5:
                if five > 0:
                    five -= 1
                else:
                    return False
            # we don't need to add change == 10, because we only have either a 5, 10 or 20
            # so the change is either 0, 5 or 15
            elif change == 15:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
