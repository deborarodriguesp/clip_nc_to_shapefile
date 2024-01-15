import xarray as xr
import geopandas as gpd
from shapely.geometry import mapping

def clip_nc_to_shapefile(nc_path, shapefile_path, output_path):
    # Carregue o NetCDF
    ds = xr.open_dataset(nc_path, decode_times=False)

    # Carregue o shapefile da bacia hidrográfica
    gdf = gpd.read_file(shapefile_path)

    # Obtenha o envelope da bacia hidrográfica
    envelope = gdf.geometry.envelope
    minx, miny, maxx, maxy = envelope.total_bounds

    # Selecione apenas as células dentro do envelope
    ds_subset = ds.sel(lon=slice(minx, maxx), lat=slice(miny, maxy))

    # Converta o xarray.Dataset para um array numpy
    subset_data = ds_subset['gveg'].values

    # Salve a nova versão do NetCDF (se necessário)
    ds_subset.to_netcdf(output_path)

    # Feche os datasets
    ds.close()
    ds_subset.close()
    
 # Netcdf Path
nc_path  = 'your/path/file.nc'

# Watershed shapefile:
shapefile_path = 'your/path/file.shp'

# Output Path for the Clipped NetCDF
output_path = 'your/path/output_file.nc'

clip_nc_to_shapefile(nc_path, shapefile_path, output_path)
