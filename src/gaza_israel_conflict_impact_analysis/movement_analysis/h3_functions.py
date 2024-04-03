import geopandas
import h3
import pandas as pd
from shapely.geometry import Polygon


def geometry_to_h3_indexes(geometry, resolution=9):
    """Convert a geometry to H3 indexes at the specified resolution."""
    # Prepare the polygon coordinates for h3.polyfill
    if geometry.geom_type == "Polygon":
        exterior_coords = [(x, y) for x, y in zip(*geometry.exterior.xy)]
        geojson_polygon = {"type": "Polygon", "coordinates": [exterior_coords]}

    # Use h3.polyfill to get H3 indexes
    h3_indexes = h3.polyfill(
        geojson=geojson_polygon, res=resolution, geo_json_conformant=True
    )
    return list(h3_indexes)


def h3_to_polygon(h3_index):
    """Convert an H3 index to a Shapely Polygon representing its hexagonal grid."""
    boundary = h3.h3_to_geo_boundary(
        h3_index, geo_json=True
    )  # Get the hexagon boundary coordinates
    return Polygon(boundary)


from shapely.geometry import Point


def map_movement_data_to_h3(oct_23, gaza_h3):
    quad_bounds = oct_23[["geography", "bounds", "xlat", "xlon"]].drop_duplicates()

    geometry = [Point(xy) for xy in zip(quad_bounds.xlon, quad_bounds.xlat)]
    gdf = geopandas.GeoDataFrame(quad_bounds, geometry=geometry, crs="EPSG:4326")

    h3_quad_mapping = gaza_h3.sjoin(gdf)[["h3_index", "geography"]].drop_duplicates()

    h3_quad_mapping = h3_quad_mapping.set_index("geography").to_dict()["h3_index"]

    oct_23["h3_index"] = oct_23["geography"].map(h3_quad_mapping)

    # filter the dataset for only Gaza points and remove West Bank related points
    oct_23 = oct_23[~(oct_23["h3_index"].isnull())]

    return oct_23


def map_movement_data_to_adm(oct_23, gaza_adm):
    quad_bounds = oct_23[["geography", "bounds", "xlat", "xlon"]].drop_duplicates()

    geometry = [Point(xy) for xy in zip(quad_bounds.xlon, quad_bounds.xlat)]
    gdf = geopandas.GeoDataFrame(quad_bounds, geometry=geometry, crs="EPSG:4326")

    adm_quad_mapping = gaza_adm.sjoin(gdf)[["ADM2_EN", "geography"]].drop_duplicates()

    adm_quad_mapping = adm_quad_mapping.set_index("geography").to_dict()["ADM2_EN"]

    oct_23["ADM2_EN"] = oct_23["geography"].map(adm_quad_mapping)

    # filter the dataset for only Gaza points and remove West Bank related points
    oct_23 = oct_23[~(oct_23["ADM2_EN"].isnull())]

    return oct_23


def aggregate_movement_to_temporal_aggregation(oct_23, agg_type, temp_agg_type="W-MON"):
    oct_23_agg = (
        oct_23.groupby([agg_type, "agg_day_period"])
        .sum("activity_index_total")[["activity_index_total"]]
        .reset_index()
        .sort_values(by="agg_day_period")
    )
    oct_23_agg["agg_day_period"] = oct_23_agg["agg_day_period"].apply(
        lambda x: pd.to_datetime(x)
    )
    oct_23_agg = (
        oct_23_agg.groupby(
            [agg_type, pd.Grouper(key="agg_day_period", freq=temp_agg_type)]
        )
        .sum()
        .reset_index()
        .sort_values(by=[agg_type, "agg_day_period"])
    )

    return oct_23_agg


def process_movement_data(df, gaza_agg, agg_type="h3_index", temp_agg_type="W-MON"):
    if agg_type == "h3_index":
        df = map_movement_data_to_h3(df, gaza_agg)
    elif agg_type == "ADM2_EN":
        df = map_movement_data_to_adm(df, gaza_agg)

    # agg = aggregate_movement_to_temporal_aggregation(df, agg_type, temp_agg_type)

    return df
