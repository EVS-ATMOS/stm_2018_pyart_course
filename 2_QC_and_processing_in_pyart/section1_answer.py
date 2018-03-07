file_path = '../inf_tutorial_data/cfrad.20060120_005000.000_to_20060120_005810.000_CPOL_PPI_level1a.nc'
radar = pyart.io.read(file_path)
vel_texture = pyart.retrieve.calculate_velocity_texture(radar, vel_field='VEL', wind_size=3, nyq=13.1)
radar.add_field('texture', vel_texture, replace_existing=True)
gatefilter = pyart.filters.GateFilter(radar)
gatefilter.exclude_above('texture', 3)
nyq = 13.8
velocity_dealiased = pyart.correct.dealias_region_based(radar, vel_field='VEL', nyquist_vel=nyq,
                                                        centered=True, gatefilter=gatefilter)
radar.add_field('corrected_velocity', velocity_dealiased, replace_existing=True)
fig = plt.figure(figsize=[8,16])
ax = plt.subplot(2,1,1,projection=ccrs.PlateCarree())
display = pyart.graph.RadarMapDisplayCartopy(radar)
display.plot_ppi_map('VEL', sweep=2, resolution='50m',
                     vmin=-14, vmax=14, 
                     projection=ccrs.PlateCarree(), cmap='pyart_LangRainbow12',
                     gatefilter=gatefilter)

ax2 = plt.subplot(2,1,2,projection=ccrs.PlateCarree())
display = pyart.graph.RadarMapDisplayCartopy(radar)
display.plot_ppi_map('corrected_velocity', sweep=2, resolution='50m',
                     vmin=-30, vmax=30, 
                     projection=ccrs.PlateCarree(), cmap='pyart_LangRainbow12',
                     gatefilter=gatefilter)
plt.show()