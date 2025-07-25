# ----------------------------- Input Helpers -----------------------------

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")

# ----------------------------- Pattern Recognition -----------------------------

def get_price_action_data():
    print("Enter at least 3 price action data points.")
    data = []
    while True:
        print(f"\nData Point #{len(data)+1}")
        open_price = get_float_input("  Open: ")
        close_price = get_float_input("  Close: ")
        high_price = get_float_input("  High: ")
        low_price = get_float_input("  Low: ")
        data.append({'open': open_price, 'close': close_price, 'high': high_price, 'low': low_price})
        if len(data) >= 3:
            done = input("Add another? (y/n): ").lower()
            if done != 'y':
                break
    return data

def analyze_price_patterns(data):
    if len(data) < 3:
        return "Not enough data for advanced pattern recognition."

    patterns = []
    closes = [d['close'] for d in data]

    if closes[-1] > closes[-2] > closes[-3]:
        patterns.append("Short-term Uptrend Potential")
    elif closes[-1] < closes[-2] < closes[-3]:
        patterns.append("Short-term Downtrend Potential")

    c1, c2 = data[-1], data[-2]
    real_body_c1 = abs(c1['close'] - c1['open'])
    real_body_c2 = abs(c2['close'] - c2['open'])

    if c1['open'] < c2['close'] and c1['close'] > c2['open'] and real_body_c1 > real_body_c2 \
       and c1['close'] > c1['open'] and c2['close'] < c2['open']:
        patterns.append("Bullish Engulfing Pattern Potential")
    elif c1['open'] > c2['close'] and c1['close'] < c2['open'] and real_body_c1 > real_body_c2 \
         and c1['close'] < c1['open'] and c2['close'] > c2['open']:
        patterns.append("Bearish Engulfing Pattern Potential")

    current = data[-1]
    body_size = abs(current['close'] - current['open'])
    range_size = current['high'] - current['low']
    if range_size > 0 and body_size <= 0.1 * range_size:
        patterns.append("Doji Pattern Detected (Indecision)")

    return "Potential Price Action Patterns Detected:\n  - " + "\n  - ".join(patterns) if patterns else \
           "No significant advanced price action patterns detected."

def run_pattern_recognition():
    price_data = get_price_action_data()
    analysis = analyze_price_patterns(price_data)
    print("\nAdvanced Pattern Recognition Analysis:")
    print(analysis)

# ----------------------------- AI Features -----------------------------

def sentiment_analysis():
    sentiment = input("Enter news headline or sentiment description: ").lower()
    if any(word in sentiment for word in ["beat", "surge", "gain", "rise", "positive"]):
        print("Positive sentiment detected: May indicate bullish movement.")
    elif any(word in sentiment for word in ["miss", "drop", "fall", "loss", "negative"]):
        print("Negative sentiment detected: May indicate bearish movement.")
    else:
        print("Neutral sentiment.")

def volatility_checker():
    high = get_float_input("High price: ")
    low = get_float_input("Low price: ")
    volatility = ((high - low) / low) * 100
    print(f"Volatility: {volatility:.2f}%")

def moving_average_signal():
    prices = []
    print("Enter closing prices (at least 5). Type 'done' when finished.")
    while True:
        entry = input("Price: ")
        if entry.lower() == 'done':
            break
        try:
            prices.append(float(entry))
        except ValueError:
            print("Invalid input.")
    if len(prices) < 5:
        print("Not enough data for analysis.")
        return
    short_ma = sum(prices[-3:]) / 3
    long_ma = sum(prices) / len(prices)
    print(f"Short MA: {short_ma:.2f}, Long MA: {long_ma:.2f}")
    print("Bullish crossover signal." if short_ma > long_ma else "Bearish or neutral trend.")

def stop_loss_suggester():
    entry = get_float_input("Entry price: ")
    volatility = get_float_input("Expected volatility %: ")
    stop = entry - (entry * (volatility / 100))
    print(f"Suggested Stop Loss: ${stop:.2f}")

def take_profit_suggester():
    entry = get_float_input("Entry price: ")
    target_gain = get_float_input("Target gain %: ")
    target = entry + (entry * (target_gain / 100))
    print(f"Suggested Take Profit: ${target:.2f}")

def confidence_index():
    recent_results = []
    print("Enter last 5 trades as 'win' or 'loss'.")
    while len(recent_results) < 5:
        result = input(f"Trade {len(recent_results)+1}: ").strip().lower()
        if result in ["win", "loss"]:
            recent_results.append(result)
        else:
            print("Invalid. Use 'win' or 'loss'.")
    confidence = (recent_results.count("win") / 5) * 100
    print(f"Trader Confidence Index: {confidence:.0f}%")

def time_of_day_effect():
    time = input("Enter time of day (e.g., morning, midday, close): ").lower()
    print({
        "morning": "Morning volatility is typically higher. Trade cautiously.",
        "midday": "Midday often experiences lower volume.",
        "close": "Power hour may bring sharp moves."
    }.get(time, "Unknown time frame. Cannot analyze."))

def emotion_check():
    mood = input("How do you feel? (e.g., confident, anxious, greedy): ").lower()
    if mood in ["anxious", "greedy"]:
        print("Warning: Emotions may be influencing decisions.")
    else:
        print("Stay calm and trade with a plan.")

def smart_position_size():
    balance = get_float_input("Account balance: ")
    risk_pct = get_float_input("% of account to risk: ")
    entry = get_float_input("Entry price: ")
    stop = get_float_input("Stop-loss price: ")
    risk = entry - stop
    if risk <= 0:
        print("Invalid stop-loss below entry.")
        return
    amount_risk = (risk_pct / 100) * balance
    shares = int(amount_risk / risk)
    print(f"Suggested position size: {shares} shares")

def pattern_memory():
    print("Saved patterns from previous sessions not yet implemented.")

# ----------------------------- Portfolio -----------------------------

portfolio_balance = 10000.00
trade_log = []

def add_to_portfolio():
    global portfolio_balance
    trade_type = input("Was this a 'buy' or 'sell' trade? ").lower()
    amount = get_float_input("How much was gained or lost in this trade? ")

    if trade_type in ("buy", "sell"):
        portfolio_balance += amount
        trade_log.append((trade_type, amount))
        print(f"Updated portfolio balance: ${portfolio_balance:.2f}")
    else:
        print("Invalid trade type. Please enter 'buy' or 'sell'.")

def view_portfolio():
    print(f"\nCurrent Balance: ${portfolio_balance:.2f}")
    if trade_log:
        print("Trade History:")
        for i, trade in enumerate(trade_log):
            print(f"{i+1}. {trade[0].capitalize()} | ${trade[1]:.2f}")
    else:
        print("No trades recorded yet.")

# ----------------------------- Strategy & Risk Tools -----------------------------

def buy_sell_hold_advice():
    price = get_float_input("Current stock price: ")
    ma = get_float_input("Moving average: ")
    if price > ma:
        print("Advice: Consider BUY or HOLD – price is above average.")
    elif price < ma:
        print("Advice: Consider SELL or HOLD – price is below average.")
    else:
        print("Advice: HOLD – price is near the average.")

def calculate_profit_loss():
    buy = get_float_input("Buy price: ")
    sell = get_float_input("Sell price: ")
    shares = get_int_input("Number of shares: ")
    profit = (sell - buy) * shares
    print(f"Profit/Loss: ${profit:.2f}")

def calculate_trade_risk():
    entry = get_float_input("Entry price: ")
    stop = get_float_input("Stop-loss price: ")
    shares = get_int_input("Shares to trade: ")
    risk = (entry - stop) * shares
    print(f"Total risk on trade: ${risk:.2f}")

def list_brokers():
    print("\nPopular Online Brokers:")
    print("  - Interactive Brokers")
    print("  - TD Ameritrade")
    print("  - E*TRADE")
    print("  - Robinhood")
    print("  - Charles Schwab")

def strategy_suggestions():
    print("\nTrading Strategy Suggestions:")
    print("  - Trend Following: Use MAs and trade in the direction of trend.")
    print("  - Breakout: Enter when price breaks resistance/support.")
    print("  - Swing Trading: Capture short-term moves between support/resistance.")
    print("  - News-Based: Trade based on sentiment/news analysis.")
    print("  - Mean Reversion: Look for price to return to average after spike.")

# ----------------------------- Utility -----------------------------

def display_help():
    print("\nAvailable Commands:")
    print("  bsh         - Buy/Sell/Hold advice")
    print("  profit      - Calculate and log profit/loss")
    print("  risk        - Calculate trade risk")
    print("  brokers     - List brokers")
    print("  pattern     - Pattern recognition")
    print("  strategy    - Strategy guide")
    print("  add         - Update portfolio")
    print("  view        - Portfolio status")
    print("  senti       - Sentiment analysis")
    print("  ma          - Moving average signal")
    print("  stoploss    - Suggest stop-loss")
    print("  takeprofit  - Suggest take-profit")
    print("  conf        - Confidence index")
    print("  time        - Time-of-day effect")
    print("  emotion     - Emotion check")
    print("  posize      - Position size calculator")
    print("  vol         - Volatility check")
    print("  help        - Show help")
    print("  exit        - Quit tool")

def print_banner():
    print("=" * 60)
    print("          Simple AI Trading Assistant by Anderson")
    print("=" * 60)

# ----------------------------- Main Loop -----------------------------

def main():
    print_banner()
    while True:
        print("\n(Enter 'help' for a list of commands)")
        action = input("What would you like to do? ").lower().strip()

        if action == "bsh":
            buy_sell_hold_advice()
        elif action == "profit":
            calculate_profit_loss()
        elif action == "risk":
            calculate_trade_risk()
        elif action == "brokers":
            list_brokers()
        elif action == "pattern":
            run_pattern_recognition()
        elif action == "strategy":
            strategy_suggestions()
        elif action == "add":
            add_to_portfolio()
        elif action == "view":
            view_portfolio()
        elif action == "senti":
            sentiment_analysis()
        elif action == "ma":
            moving_average_signal()
        elif action == "stoploss":
            stop_loss_suggester()
        elif action == "takeprofit":
            take_profit_suggester()
        elif action == "conf":
            confidence_index()
        elif action == "time":
            time_of_day_effect()
        elif action == "emotion":
            emotion_check()
        elif action == "posize":
            smart_position_size()
        elif action == "vol":
            volatility_checker()
        elif action == "help":
            display_help()
        elif action == "exit":
            print("Exiting the trading tool. Goodbye!")
            break
        else:
            print("ERROR: Invalid command. Type 'help' to see valid options.")

if __name__ == "__main__":
    main()
