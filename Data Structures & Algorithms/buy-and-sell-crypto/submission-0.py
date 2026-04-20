class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_value = 101     # min
        sell_value = -1     # max value or more than buy value.
        sell_value_day = -1
        buy_value_day = -2  # Must be buy_day < sell_day
        for i in range(len(prices)):
            if (sell_value_day <= buy_value_day and buy_value_day + 1 <= len(prices)):
                sell_value_day = buy_value_day + 1
                sell_value = -1

            if (prices[i] < buy_value):
                print(f'{prices[i]}<{buy_value}')
                buy_value = prices[i]
                buy_value_day = i
            if (prices[i] > sell_value):
                print(f'{prices[i]}>{sell_value}')
                sell_value = prices[i]
                sell_value_day = i
            print(f'Min: {buy_value}, Max: {sell_value}, ', end="")
            print("Difference", sell_value - buy_value)

        return sell_value - buy_value if sell_value_day > buy_value_day else 0
