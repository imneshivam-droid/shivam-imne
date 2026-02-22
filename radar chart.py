import plotly.express as px
import pandas as pd

# Sample data
data = {
    'Category': ['Food Quality', 'Food Variety', 'Service Quality', 'Ambiance', 'Affordability'],
    'Value': [4, 5, 4, 3, 5]
}
df = pd.DataFrame(data)

# Create the radar chart
fig = px.line_polar(df, r='Value', theta='Category', line_close=True)

# Customize and display the chart
fig.update_traces(fill='toself') # Fills the area within the plot
fig.show()
