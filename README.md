# Futures Contract Profit/Loss Calculator

This project is a Python script designed to calculate potential profit or loss at different selling prices for a futures contract, factoring in leverage and USD value. It also estimates the liquidation price (the price at which a position will be closed by the broker) and plots this along with other relevant data.

## What it does

- **Profit/Loss Calculation**: The script calculates the potential profit or loss at different selling prices based on your initial buy price, leverage, and purchase USD value.
- **Liquidation Price**: The liquidation price is estimated based on your leverage and buy price. This is the price at which your position will be closed automatically by the exchange.
- **Interactive Graph**: The script generates an interactive Plotly graph that shows the profit or loss at different selling prices, including the liquidation price and break-even point.
- **Inputs**: You enter the buy price, leverage, and USD value of your purchase. These inputs are used to generate various potential outcomes, which are displayed visually.

## Input Prompts

When running the script, the following input prompts will appear:

1. **Enter the price you wish to buy at**  
   - This is the price at which you are entering the futures position (e.g., the price of a cryptocurrency, stock, or commodity).

2. **Enter your leverage**  
   - This is the leverage ratio you are using for the position. For example, leverage of 10 means you control 10 times the value of your investment.

3. **Enter the USD value of your purchase**  
   - This is the total USD value of your position. It is the amount you are investing (taking leverage into account).

## How the inputs are used:

- **Buy Price**: The price at which the asset is bought. It’s used as the starting point to calculate potential profits or losses at different selling prices.
- **Leverage**: Determines how much larger your position is relative to the amount of USD you’ve invested. Leverage amplifies both potential profit and loss.
- **USD Value**: This is the amount you are investing in USD, which is then used to calculate how much profit or loss you would incur at each different selling price.

## Requirements

To run the script, you need to install the following Python packages:

- `plotly` for generating interactive plots.
- `numpy` for numerical operations.

You can install them using pip:

```bash
pip install plotly numpy

