import pairsTrading
while True:
    y_n = input("Want to check 2 coins? (y/n) ").lower()
    if y_n == "y":
        cryptocurrency_1 = input("First cryptocurrency (expamle BTCUSDT): ").upper()
        cryptocurrency_2 = input("Second cryptocurrency (expamle ETHBTC): ").upper()
        interval = input("Interval to check co-integration on (1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M): ").lower()
        pairsTrading.PairsTradingChecker(cryptocurrency_1, cryptocurrency_2, interval)
    elif y_n == "n":
        break
