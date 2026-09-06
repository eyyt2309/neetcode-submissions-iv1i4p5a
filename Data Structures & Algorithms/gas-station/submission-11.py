class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)
        m = len(gas)

        if total_cost > total_gas:
            return -1
        
        for i in range(len(gas)):
            curr_fuel = 0
            n = 0
            while True:
                if n == m - 1:
                    return i
                curr_fuel += gas[(i + n) % m] 
                if curr_fuel > cost[(i + n) % m]:
                    curr_fuel -= cost[(i + n) % m]
                    n += 1
                else:
                    break


            