Grid_better = pyart.map.grid_from_radars([radar], grid_shape=(21, 101, 101), 
                                  grid_limits=((0.,20000,), (-100000., 100000.), (-100000, 100000.)),
                                  roi_func='dist_beam', min_radius=2000.0)
gdisplay = pyart.graph.GridMapDisplay(Grid_better)
gdisplay.plot_latitude_slice('reflectivity', lat=36.75, cmap='pyart_LangRainbow12', vmin=0, vmax=60)
plt.xlim([-50,50])