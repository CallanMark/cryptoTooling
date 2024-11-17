import plotly.graph_objects as go
import numpy as np

usdEurRate = 0.95  # Adjust as needed #TODO: Implement USD/EUR option for chart 


print("Enter the price you wish to buy at ")
buyPrice = float(input())  # Changed to float for decimal input
print("Enter your leverage ") 
leverage = float(input())  # Changed to float for decimal input

openingFee = buyPrice * 0.005

print("Enter the USD value of your purchase ")
usdVal = float(input())

upperRange= buyPrice*1.2
lowerRange= buyPrice*0.8
intervals= buyPrice * 0.0025
liqPrice=buyPrice*(1-1/leverage)
# Generate a range of potential selling prices for the plot
sellPrices = np.arange(lowerRange, upperRange, intervals)  # Start at 85,000, end at 95,000, step size of 500

# List to store formatted returns for each selling price
plReturns = []
usdTotal = []
returnPct = []

for sellPrice in sellPrices:
    sellFee = sellPrice * 0.005
    percentReturn = (sellPrice - sellFee) / (buyPrice - openingFee)
    
    # Calculate USD gain and USD return
    usdGain = usdVal * ((percentReturn - 1) * leverage)
    usdReturn = usdVal + usdGain
    usdTotal.append(usdReturn)
    # Append the USD return
    plReturns.append(usdGain)
    
    # Calculate and append the percentage gain
    percentageGain = ((percentReturn - 1) * leverage) * 100
    returnPct.append(percentageGain)

returnPct = [float(val) for val in returnPct]
usdTotal = [float(val) for val in usdTotal]
'''
# Calculate the USD return for each selling price
for sellPrice in sellPrices:
    sellFee = sellPrice * 0.005
    percentReturn = (sellPrice - sellFee) / (buyPrice - openingFee)
    usdGain = usdVal  * ((percentReturn-1) * leverage)
    plReturns.append(usdGain)

for sellPrice in sellPrices :
    sellFee = sellPrice * 0.005
    percentReturn = (sellPrice - sellFee) / (buyPrice - openingFee)
    usdGain = usdVal  * ((percentReturn-1) * leverage)
    usdReturn = usdVal + usdGain
    if usdGain > 0 :
       usdReturn = usdVal + usdGain
       usdVal.append(usdReturn)
    else: 
        usdReturn = usdVal - usdGain
        usdVal.append(usdReturn)

for sellPrice in sellPrices:
    percentReturn = (sellPrice - sellFee) / (buyPrice - openingFee)
    percentageGain = ((percentReturn - 1 ) * leverage) * 100
    returnPct.append(percentageGain)

'''



# Create an interactive Plotly graph
fig = go.Figure(data=go.Scatter(
    mode='markers',
    marker=dict(size=12),
    customdata=list(zip(returnPct, usdTotal)),  # Combine data for hover
    hovertemplate=(
        'Selling Price: %{x}<br>'  # Display the x-axis value
        'Profit/Loss (USD): %{y}<br>'  # Display the y-axis value
        'Return PCT: %{customdata[0]:.2f}%<br>'  # Display percentage return
        'USD Total: %{customdata[1]:.2f}<extra></extra>'  # Display USD total
    )
))

fig.add_trace(go.Scatter(
    x=sellPrices,
    y=plReturns,
    mode='lines',
    name='Profit/Loss',
    line=dict(color='blue')
))

# Add a break-even line
fig.add_trace(go.Scatter(
    x=[min(sellPrices), max(sellPrices)],
    y=[0, 0],
    mode='lines',
    name='Break-even',
    line=dict(color='red', dash='dash')
))
''' 
# TODO: Add the liq line in the chart 
fig.add_trace(go.Scatter(
    x = [usdVal * -1 , liqPrice],
    y = [0,0],
    mode='lines',
    name='Liquadation',
    line=dict(color='black', dash='dash')
))
'''
# Customize the layout
fig.update_layout(
    title='USD Profit/Loss at Different Selling Prices',
    xaxis_title='Selling Price (USD)',
    yaxis_title='Profit/Loss (USD)',
    xaxis=dict(showgrid=True),
    yaxis=dict(showgrid=True),
    template='plotly_white'
)

fig.show()


