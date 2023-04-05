import csv
from pprint import pprint 

class Melon():
    def __init__(
        self,
        melon_id,
        common_name,
        price,
        image_url,
        color,
        seedless
    ):
        self.melon_id = melon_id
        self.common_name = common_name
        self.price = price
        self.image_url = image_url
        self.color = color
        self.seedless = seedless

def __repr__(self):
    """Convenience method to show information about melon in console."""

    return(
        f"<Melon: {self.melon_id}, {self.common_name}>"
    )

def price_str(self):
    """Return price formatted as string $x.xx"""

    return f"${self.price:.2f}"

def get_by_id(melon_id):
    """Return a melon, given its ID."""

    return melon_dict[melon_id]

def get_all():
    """Return list of melons."""

    return list(melon_dict.values())

with open("melons.csv") as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        print(row)

melon_dict = {}

with open("melons.csv") as csvfile:
    rows = csv.DictReader(csvfile)

    for row in rows:
        melon_id = row['melon_id']
        melon = Melon(
            melon_id,
            row['common_name'],
            float(row['price']),
            row['image_url'],
            row['color'],
            eval(row['seedless']))

        melon_dict[melon_id] = melon

@app.route("/melons")
def all_melons():
    """Return a page listing all the melons avaiable for purchase."""

    melon_list = melons.get_all()
    return render_template("all_melons.html", melon_list=melon_list)

@app.route("/melon/<melon_id>")
def melon_details(melon_id):
    """Return a page showing all info about a melon. Also, provide a button to buy that melon."""
    melon = melon.get_by_id(melon_id)
    return render_template("melon_details.html", melon=melon)