import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Replace 'file_path.csv' with your actual file path
file_path = 'Bicycle_Thefts_Open_Data.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the data
# print(data.dtypes)
average_cost_per_year = data.groupby('OCC_YEAR')['BIKE_COST'].mean()
#print(average_cost_per_year)


entries_per_year = data.groupby('OCC_YEAR').size()

# Display the result
#print(entries_per_year)

thefts_per_hour = data.groupby('OCC_HOUR').size()

#print(thefts_per_hour)

month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
data['OCC_MONTH'] = pd.Categorical(
    data['OCC_MONTH'], categories=month_order, ordered=True)
data_filtered = data[(data['OCC_YEAR'] >= 2014) & (data['OCC_YEAR'] <= 2023)]


heatmap_data = data_filtered.groupby(
    ['OCC_YEAR', 'OCC_MONTH']).size().unstack(fill_value=0)

plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlGnBu',
            cbar_kws={'label': 'Number of Thefts'})

# Customize the plot
plt.title('Number of Thefts per Year and Month')
plt.xlabel('Month')
plt.ylabel('Year')

# Show the plot
plt.show()
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
data['OCC_DOW'] = pd.Categorical(data['OCC_DOW'], categories=days_order, ordered=True)
##data['OCC_HOUR'] = pd.to_datetime(data['OCC_DATE']).dt.hour
hour_day_pivot = data.pivot_table(index='OCC_DOW', columns='OCC_HOUR', aggfunc='size', fill_value=0)

# Heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(hour_day_pivot, cmap='viridis', annot=False, linewidths=0.5)
plt.title("Theft Activity by Hour and Day")
plt.xlabel("Hour of the Day")
plt.ylabel("Day of the Week")
plt.show()

# Create a risk score (e.g., normalized theft count per neighborhood)
neighborhood_risk = data.groupby('NEIGHBOURHOOD_140').size().reset_index(name='Theft_Count')
neighborhood_risk['Risk_Score'] = neighborhood_risk['Theft_Count'] / neighborhood_risk['Theft_Count'].max()

# Bar chart for risk scores
plt.figure(figsize=(12, 6))
neighborhood_risk.sort_values('Risk_Score', ascending=False).head(10).plot(
    kind='barh', x='NEIGHBOURHOOD_140', y='Risk_Score', color='red', legend=False)
plt.title("Neighborhood Risk Profile")
plt.xlabel("Risk Score")
plt.ylabel("Neighborhood")
plt.show()

# Determine top 10 neighborhoods based on theft count
top_neighborhoods = data['NEIGHBOURHOOD_140'].value_counts().head(10).index

# Filter data to include only top 10 neighborhoods
filtered_data = data[data['NEIGHBOURHOOD_140'].isin(top_neighborhoods)]

# Prepare data for the Sankey diagram
sources = filtered_data['BIKE_TYPE'].astype(str)  # Bike type
targets = filtered_data['NEIGHBOURHOOD_140']  # Neighborhood
values = filtered_data.groupby(['BIKE_TYPE', 'NEIGHBOURHOOD_140']).size()  # Count thefts

# Create Sankey diagram
fig = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=list(sources.unique()) + list(targets.unique())
    ),
    link=dict(
        source=sources.map({v: i for i, v in enumerate(sources.unique())}).values,
        target=targets.map({v: i + len(sources.unique()) for i, v in enumerate(targets.unique())}).values,
        value=values.values
    )
))

fig.update_layout(title_text="Bike Theft Flow by Type and Top 10 Neighborhoods", font_size=10)
fig.show()

# Calculate distance from city center (approximate)
