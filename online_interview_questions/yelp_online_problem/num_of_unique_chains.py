class Business():
    def __init__(self, name, location, _id):
        """Inititlize the obeject with name, location, and
        _id attributes
        """
        self.name = name
        self.location = location
        self._id = _id

    def __repr__(self):
        """String representation of the object"""
        return (f"name: {self.name}, location: {self.location}, id: {self._id}")


def unique_chains(buss_obj, location):
    """Counts the unique number of chains in the given location"""
    seen_id = set()
    chains = {}
    for buss in buss_obj:
        if location == buss.location:
            if buss._id not in seen_id:
                seen_id.add(buss._id)
                if buss.name not in chains:
                    chains[buss.name] = 1
                else:
                    chains[buss.name] += 1
    chains = list(map(list, chains.items()))
    return sorted(chains, key=lambda x: (-x[1], x[0]))


businesses = [
            Business("Sturbucks", "SF", 100),
            Business("Sturbucks", "SF", 100),
            Business("Whole Foods", "SF", 101),
            Business("Whole Foods", "SF", 102),
            Business("Amazon", "SF", 103),
            Business("Amazon", "SF", 110),
            Business("McDonalds", "SF", 104),
            Business("McDonalds", "SF", 105),
            Business("McDonalds", "NYC", 106)
            ]


result = unique_chains(businesses, "SF")
print(result)
