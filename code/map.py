import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.lines import Line2D

# =========================
# 1. Color Styling
# =========================
milton_color = "#e46b6b"
ian_color = "#3a9ad9"
land_color = "#f3efe6"
ocean_color = "#d7e4ef"
coast_color = "#b8b8b8"
state_color = "#cdcdcd"
grid_color = "#cfcfcf"

# =========================
# 2. Create Figure & Axes
# =========================
fig = plt.figure(figsize=(7, 7), facecolor="white")
ax = plt.axes(projection=ccrs.PlateCarree())

# Focus on the Florida region
ax.set_extent([-88.8, -79.3, 24.0, 31.8], crs=ccrs.PlateCarree())

# =========================
# 3. Basemap Features
# =========================
ax.add_feature(cfeature.LAND, facecolor=land_color, zorder=0)
ax.add_feature(cfeature.OCEAN, facecolor=ocean_color, zorder=0)
ax.add_feature(cfeature.COASTLINE, linewidth=0.8, edgecolor=coast_color, zorder=1)
ax.add_feature(cfeature.STATES, linewidth=0.6, edgecolor=state_color, zorder=1)

# Add gridlines
ax.gridlines(
    draw_labels=False,
    linewidth=0.4,
    color=grid_color,
    alpha=0.45,
    linestyle="--"
)

# =========================
# 4. Hurricane Locations (Approximate)
# =========================
# Milton: Near Florida's west coast
milton_lon, milton_lat = -82.55, 27.30

# Ian: Near Cayo Costa / Punta Gorda
ian_lon, ian_lat = -82.20, 26.70

# Plot Hurricane Milton
ax.plot(
    milton_lon, milton_lat,
    marker='*', color=milton_color, markersize=14,
    markeredgecolor='white', markeredgewidth=0.8,
    transform=ccrs.PlateCarree(), zorder=4
)

# Plot Hurricane Ian
ax.plot(
    ian_lon, ian_lat,
    marker='*', color=ian_color, markersize=14,
    markeredgecolor='white', markeredgewidth=0.8,
    transform=ccrs.PlateCarree(), zorder=4
)

# Hurricane Labels
ax.text(
    milton_lon + 0.18, milton_lat + 0.14, "Milton",
    fontsize=11.5, color=milton_color, weight="bold",
    transform=ccrs.PlateCarree(), zorder=5
)

ax.text(
    ian_lon + 0.16, ian_lat - 0.38, "Ian",
    fontsize=11.5, color=ian_color, weight="bold",
    transform=ccrs.PlateCarree(), zorder=5
)

# State Label
ax.text(
    -84.9, 28.25, "Florida, USA",
    fontsize=17, color="dimgray", weight="bold", alpha=0.8,
    transform=ccrs.PlateCarree(), zorder=3
)

# =========================
# 5. Legend
# =========================
legend_elements = [
    Line2D([0], [0], marker='*', color='w', label='Hurricane Milton',
           markerfacecolor=milton_color, markeredgecolor='white',
           markeredgewidth=0.8, markersize=11),
    Line2D([0], [0], marker='*', color='w', label='Hurricane Ian',
           markerfacecolor=ian_color, markeredgecolor='white',
           markeredgewidth=0.8, markersize=11)
]

legend = ax.legend(
    handles=legend_elements,
    title="Storm Events",
    loc="lower left",
    frameon=True,
    framealpha=0.9,
    fontsize=11,
    title_fontsize=12,
    borderpad=0.8
)
legend.get_frame().set_facecolor("white")

plt.show()
