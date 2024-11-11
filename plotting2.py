import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data from CSV
df = pd.read_csv('route16.csv')

# Step 2: Group by Route and Day, and sum the On's (boarding passengers)
df_grouped = df.groupby(['Route', 'Day'])['On\'s'].sum().reset_index()

# Step 3: Filter the data to only include days 16, 17, 18, and 19
valid_days = [16, 17, 18, 19]
df_filtered_days = df_grouped[df_grouped['Day'].isin(valid_days)]

# Step 4: Calculate the total On's per route
df_route_totals = df_filtered_days.groupby('Route')['On\'s'].sum().reset_index()

# Step 5: Get the top 5 routes based on total On's
top_5_routes = df_route_totals.sort_values(by='On\'s', ascending=False).head(5)

# Step 6: Filter the data to include only these top 5 routes
df_filtered = df_filtered_days[df_filtered_days['Route'].isin(top_5_routes['Route'])]

# Step 7: Define a color palette for the routes
colors = ['b', 'g', 'r', 'c', 'm']  # Blue, Green, Red, Cyan, Magenta for 5 routes

# Step 8: Create the plot
plt.figure(figsize=(12, 8))

# Step 9: Plot the data for each route and day with different colors
for i, route in enumerate(top_5_routes['Route']):
    route_data = df_filtered[df_filtered['Route'] == route]
    
    # Plot On's for each day for this route
    plt.scatter(route_data['Day'], route_data['On\'s'], label=f'Route {route}', 
                color=colors[i], s=100, edgecolor='black', alpha=0.7)

# Step 10: Format the plot for better readability
plt.title('Total Number of Passengers Boarding (On\'s) for Top 5 Routes Over Different Days', fontsize=14)
plt.xlabel('Day', fontsize=12)
plt.ylabel('Total Number of Passengers Boarding (On\'s)', fontsize=12)
plt.legend(title="Route", loc='upper left')

# Step 11: Set x-ticks to the days (16, 17, 18, 19) and rotate for readability
plt.xticks([16, 17, 18, 19], rotation=45)

# Adding grid for better readability
plt.grid(True)

# Step 12: Display the plot
plt.tight_layout()
plt.show()