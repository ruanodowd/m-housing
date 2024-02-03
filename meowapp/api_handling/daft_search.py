import pandas as pd
from daftlistings import Daft, Location, SearchType, PropertyType, SortType
import map_visualisation_iframe as mvi


def test():
    # location = [Location.LIMERICK_CITY, Location.CASTLETROY_LIMERICK, Location.ANNACOTTY_LIMERICK]
    # living_type = SearchType.SHARING
    # max_price = 1500
    # sort_type = SortType.PRICE_ASC
    # daft_search(location, max_price, living_type, sort_type)
    listings_to_map(52.673772, -8.5778347)


def daft_search(location, max_price, living_type, sort_type):
    daft = Daft()
    daft.set_location(location)
    daft.set_search_type(living_type)
    daft.set_sort_type(sort_type)
    daft.set_max_price(max_price)

    listings = daft.search()
    # cache the listings in the local file
    with open("result.txt", "w") as fp:
        fp.writelines("%s\n" % listing.as_dict_for_mapping() for listing in listings)
    # read from the local file
    return "wow"


def listings_to_map(work_lat, work_lon):
    with open("result.txt") as fp:
        lines = fp.readlines()
    properties = []
    for line in lines:
        properties.append(eval(line))
    df = pd.DataFrame(properties)
    print(df)
    limerick_map = mvi.MapVisualization(df)
    limerick_map.add_markers()
    limerick_map.add_colorbar()
    limerick_map.add_work_marker(work_lat, work_lon)
    iframe = limerick_map.to_iframe("500", "100%")
    website = """
            <!DOCTYPE html>
            <html>
                <head></head>
                <body>
                    <h1>Using an iframe</h1>
                    """ + iframe + """
                </body>
            </html>
        """
    with open("ireland_rent.html", "w") as f:
        f.write(website)
    return "wow"


# def getCycleTime(locations, targetX, targetY):
#     # get the public transport time from the dataframe of locations to the target


if __name__ == "__main__":
    test()
    print("Done, please checkout the html file")
