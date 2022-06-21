import csv
import json
import pathlib

from models import NearEarthObject, CloseApproach

neo_csv_path = pathlib.Path("./data/neos.csv")
cad_json_path = pathlib.Path("./data/cad.json")


def load_neos(neo_csv_path=neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    collection = []

    with open(neo_csv_path, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if not row["diameter"]:
                del row["diameter"]

            collection.append(
                NearEarthObject(
                    pdes=row.get("pdes", ""),
                    name=row["name"] or None,
                    diameter=row.get("diameter", float("nan")),
                    pha=True if row["pha"] == "Y" else False,
                )
            )

    return collection


def load_approaches(cad_json_path=cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    collection = []

    with open(cad_json_path, "r") as cads:
        contents = json.load(cads)
        data = contents.get("data", list())
        fields = contents.get("fields", list())

        for d in data:
            current_cad = dict()

            for i in range(len(fields)):
                key = fields[i]
                value = d[i]

                current_cad[key] = value

            collection.append(
                CloseApproach(
                    des=current_cad["des"],
                    dist=current_cad["dist"],
                    v_rel=current_cad["v_rel"],
                    cd=current_cad["cd"],
                )
            )

    return collection


if __name__ == "__main__":
    load_neos()
