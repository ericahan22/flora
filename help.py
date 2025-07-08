import pandas as pd
import geopandas as gpd
import math

# Load the CSV data
df = pd.read_csv('flora_observations.csv')

# Display the first few rows
print(df.head())

# Convert to a GeoDataFrame
gdf = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df.longitude, df.latitude),
    crs='EPSG:4326'  # WGS 84
)
import folium

# Calculate the mean latitude and longitude for map centering
mean_lat = gdf.geometry.y.mean()
mean_lon = gdf.geometry.x.mean()

# Initialize the map
m = folium.Map(location=[mean_lat, mean_lon], zoom_start=6)

# Add observation markers
for _, row in gdf.iterrows():
    if not math.isnan(row.geometry.y):
        folium.Marker(
            location=[row.geometry.y, row.geometry.x],
            popup=f"{row['scientific name']} ({row['name']})",
            icon=folium.Icon(color='green', icon='leaf')
        ).add_to(m)

# Save the map to an HTML file
m.save('flora_map.html')
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for seaborn
sns.set_theme(style="whitegrid")

# Count of observations per species
species_counts = df['scientific name'].value_counts().head(10)
species_counts_df = species_counts.reset_index()
species_counts_df.columns = ['species', 'count']

# Plot the top 10 observed species
plt.figure(figsize=(10, 6))
sns.barplot(
    data=species_counts_df,
    x='count',
    y='species',
    hue='species',
    palette='viridis',
    legend=False
)
plt.xlabel('Number of Observations')
plt.ylabel('Species')
plt.title('Top 10 Observed Plant Species')
plt.tight_layout()
plt.show()
