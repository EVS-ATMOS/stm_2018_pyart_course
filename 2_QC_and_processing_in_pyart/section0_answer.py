gatefilter = pyart.filters.GateFilter(radar)
gatefilter.exclude_below('reflectivity', 0)
display = pyart.graph.RadarMapDisplayCartopy(radar)
display.plot_ppi_map('reflectivity', sweep=2, resolution='50m',
                     vmin=-8, vmax=64, min_lon=-98.25, max_lon=-96.75,
                     min_lat=35.75, max_lat=37.25,
                     projection=ccrs.PlateCarree(), cmap='pyart_LangRainbow12',
                     gatefilter=gatefilter)
plt.show()