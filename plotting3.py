import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
bus_trips = pd.read_csv("bus_trips_3.csv")

# Count trips by route
route_counts = bus_trips["route_id"].value_counts().reset_index()
route_counts.columns = ["route_id", "trip_count"]

# Set Seaborn style and color palette
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# Create a bar chart with Seaborn
bar_plot = sns.barplot(
    x="route_id", 
    y="trip_count", 
    data=route_counts, 
    palette="viridis"
)

# Customize plot aesthetics
bar_plot.set_xlabel("Route ID", fontsize=12)
bar_plot.set_ylabel("Trip Count", fontsize=12)
bar_plot.set_title("Frequency of Bus Trips by Route", fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()

# Show plot
plt.show()
