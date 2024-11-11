import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Step 1: Load the data from CSV
df = pd.read_csv('route16.csv')

# Step 2: Convert 'Door Open Time' to datetime format
df['Door Open Time'] = pd.to_datetime(df['Door Open Time'])

# Step 3: Filter data for the specific days (16, 17, 18, 19)
df_filtered = df[df['Day'].isin([16, 17, 18, 19])]

# Step 4: Group by Door Open Time and Day, and sum the Max Load (total occupancy at that time)
df_grouped = df_filtered.groupby(['Day', 'Door Open Time'])['Max Load'].sum().reset_index()

# Step 5: Create the plot for the total Max Load (occupancy) on each day as a line graph
plt.figure(figsize=(10, 6))

# Step 6: Plot data for each day as a line
for day in [16, 17, 18, 19]:
    day_data = df_grouped[df_grouped['Day'] == day]
    
    # Plot the summed Max Load (occupancy) as a line (using Door Open Time)
    plt.plot(day_data['Door Open Time'], day_data['Max Load'], label=f'Day {day}', marker='o', linestyle='-', linewidth=2)

# Step 7: Format the plot for better readability
plt.title('Total Occupancy (Max Load) in the Vehicle at Any Time of the Day (Days 16, 17, 18, 19)', fontsize=14)
plt.xlabel('Time', fontsize=12)
plt.ylabel('Total Occupancy (Max Load)', fontsize=12)
plt.legend(title="Day")
plt.xticks(rotation=45)
plt.grid(True)

# Step 8: Adjust the x-axis format for time
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

# Step 9: Display the plot
plt.tight_layout()
plt.show()