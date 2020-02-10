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


def get_unique_business_id(buss_list):
    """
    Returns only businesses with unique id
    """
    seen_id = set()
    for i, buss in buss_list:
        if buss._id not in seen_id:
            seen_id.add(buss._id)
        else:
            buss_list.pop(i)

    return buss_list


def get_chains_at_location(businesses, location):
    """
    Return number of chains at given location
    """
    pass


def unique_chains(buss_obj, location):
    """Counts the unique number of chains in the given location"""
    seen_id = set()
    chains = {}
    for buss in buss_obj:
        # first filter by location
        if location == buss.location:
            # filter by unique business id
            if buss._id not in seen_id:
                seen_id.add(buss._id)
                # count the chains
                if buss.name not in chains:
                    chains[buss.name] = 1
                else:
                    chains[buss.name] += 1
    chains = list(map(list, chains.items()))
    # sort the chains by number of stores and alphabetically
    return sorted(chains, key=lambda x: (-x[1], x[0]))

def count_unique_id(businesses, location)
businesses = [
            Business("Sturbucks", "SF", 100),
            Business("Sturbucks", "SF", 100),
            Business("Whole Foods", "SF", 101),
            Business("Whole Foods", "SF", 102),
            Business("Amazon", "SF", 103),
            Business("Amazon", "SF", 110),
            Business("McDonalds", "SF", 104),
            Business("McDonalds", "SF", 104),
            Business("McDonalds", "NYC", 106),
            Business("McDonalds", "NYC", 105)
            ]

# obj = Business()

result = unique_chains(businesses, "NYC")
print(result)
