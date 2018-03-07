
sandy_datetime = datetime(2012,10,29,10,0)

#grab the key for Sandy
my_key = find_my_key('KDOX', sandy_datetime)
print(my_key)

#create a temporary named file
localfile = tempfile.NamedTemporaryFile()

#fetch the data from AWS S3
aws_radar.download_file(my_key, localfile.name)

#read that file into Py-ART!
radar = pyart.io.read(localfile.name)

#Sweep we want to plot
sweep = 0

#Get the date at the start of collection
index_at_start = radar.sweep_start_ray_index['data'][sweep]
time_at_start_of_radar = pyart.io.cfradial.netCDF4.num2date(radar.time['data'][index_at_start],
                                  radar.time['units'])

#make a nice time stamp
pacific = pytz.timezone('US/Eastern')
local_time = pacific.fromutc(time_at_start_of_radar)
fancy_date_string = local_time.strftime('%A %B %d at %I:%M %p %Z')
print(fancy_date_string)

#Set up our figure
fig = plt.figure(figsize = [10,8])

#create a Cartopy Py-ART display object
display = pyart.graph.RadarMapDisplayCartopy(radar)

#get center of the display for the projection
lat_0 = display.loc[0]
lon_0 = display.loc[1]

# Main difference from Basemap!
#Cartopy forces you to select a projection first!
projection = cartopy.crs.Mercator(
                central_longitude=lon_0,
                min_latitude=35, max_latitude=45)

title = 'KDOX \n' + fancy_date_string

#plot a PPI! add coastline at 10m resolution
display.plot_ppi_map(
    'reflectivity', sweep, colorbar_flag=True,
    title=title,
    projection=projection, resolution='10m',
    cmap=pyart.graph.cm.LangRainbow12, vmin=-12, vmax=64,
    min_lon=-78, max_lon=-73.5, min_lat=37, max_lat=40)

# Mark the radar
display.plot_point(lon_0, lat_0, label_text='KDOX')

# Plot some lat and lon lines
gl = display.ax.gridlines(draw_labels=True,
                          linewidth=2, color='gray', alpha=0.5, linestyle='--')
gl.xlabels_top = False
gl.ylabels_right = False
