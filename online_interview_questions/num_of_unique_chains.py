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
    # storing for unique ids
    seen_id = set()
    # dict for chain and number of stores of that chain
    chains = {}
    for buss in buss_obj:
        if location == buss.location:
            # eleminating the duplicated stores by checking ID
            if buss._id not in seen_id:
                seen_id.add(buss._id)
                # if we are seeing the store first time
                # the num is 1
                if buss.name not in chains:
                    chains[buss.name] = 1
                # each time we see the chain we increment
                # the number of stores
                else:
                    chains[buss.name] += 1

    # make a list of list from chains dictionary keys and values
    chains = list(map(list, chains.items()))

    # sorting the number of stores by descending,
    # and the names by alphabetical order
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
