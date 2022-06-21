from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(self, pdes="", name=None, diameter=0.0, pha=False, **info):
        """Create a new `NearEarthObject`.

        :param pdes: Primary designation of the asteroid or comet.
        :param name: The International Astronomical Union (IAU) name of the NEO.
        :param diameter: the NEO's diameter (from an equivalent sphere) in kilometers.
        :param pha: Whether the NEO is a "Potentially Hazardous Asteroid".
        :param info: A dict of excess keyword arguments supplied to the constructor.
        """
        self.designation = pdes
        self.name = name
        self.diameter = float(diameter)
        self.hazardous = pha

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        des = self.designation
        name = self.name if self.name else ""
        return " ".join([des, name])

    def __str__(self):
        """Return `str(self)`."""
        pha = "is" if self.hazardous else "is not"

        return (
            f"NEO {self.fullname} has a diameter of {self.diameter:.3f} km "
            f"and {pha} potentially hazardous."
        )

    def __repr__(self):
        """Return `repr(self)`,
        a computer-readable string representation of this object.
        """
        return (
            f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
            f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"
        )


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    # TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, des="", dist=0.0, v_rel=0.0, cd=None, **info):
        """Create a new `CloseApproach`.

        :param des: Primary designation of the asteroid or comet
        :param dist: Nominal approach distance (au)
        :param v_rel: Velocity relative to the approach body at close approach (km/s)
        :param cd: Time of close-approach (formatted calendar date/time, in UTC)
        :param info: A dict of excess keyword arguments supplied to the constructor.
        """
        # The `cd_to_datetime` function will be useful.
        self._designation = des
        self.time = cd_to_datetime(cd)
        self.distance = float(dist)
        self.velocity = float(v_rel)

        # Create an attribute for the referenced NEO, originally None.
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        # TODO: Use this object's `.time` attribute and the `datetime_to_str` function to
        # build a formatted representation of the approach time.
        # TODO: Use self.designation and self.name to build a fullname for this object.
        return ""

    def __str__(self):
        """Return `str(self)`."""
        # TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        return f"A CloseApproach ..."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (
            f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
            f"velocity={self.velocity:.2f}, neo={self.neo!r})"
        )
