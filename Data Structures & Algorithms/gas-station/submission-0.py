class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_gas = sum(gas)

        sum_cost = sum(cost)

        if sum_gas < sum_cost:
            return -1

        current_tank = 0
        start_index = 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]

            current_tank += gain

            if current_tank < 0:
                start_index = i + 1
                current_tank = 0

        return start_index




