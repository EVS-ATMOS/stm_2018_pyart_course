radar = pyart.io.read('../inf_tutorial_data/sgpxsaprcmacsurI5.c1.20170801.044013.nc')
radar.fields.keys()
reproc_phase, kdp = pyart.correct.phase_proc_lp(radar, 0, refl_field='reflectivity', 
                                                )
radar.add_field('corrected_differential_phase', reproc_phase, replace_existing=True)
radar.add_field('specific_differential_phase', kdp, replace_existing=True)
display = pyart.graph.RadarMapDisplayCartopy(radar)
fig = plt.figure(figsize=(15,5))
ax1 = plt.subplot(1,2,1, projection=ccrs.PlateCarree())
display.plot_ppi_map('corrected_differential_phase', cmap='pyart_LangRainbow12', vmin=0, vmax=360,
                     resolution='10m')
ax2 = plt.subplot(1,2,2, projection=ccrs.PlateCarree())
display.plot_ppi_map('specific_differential_phase', cmap='pyart_LangRainbow12', vmin=0, vmax=1,
                     resolution='10m')
