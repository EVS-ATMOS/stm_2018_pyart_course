radar = pyart.io.read('../inf_tutorial_data/cfrad.20060120_005000.000_to_20060120_005810.000_CPOL_PPI_level1a.nc')
display = pyart.graph.RadarMapDisplayCartopy(radar)
display.plot_ppi_map('Refl', sweep=0, vmin=-10, vmax=60,
                     cmap='pyart_LangRainbow12', resolution='10m')