#Kyle Dahlin

#A disjoint set data structure. Support finding the set of a value, testing if 
#values are of hte same set, merging sets, and how may sets are in the entire
#structure.

class Disjoint:

    def __init__(self, value):
        self.sets = []
        self.create_set(value)

    def create_set(self, value):
        """
        Add a new grouping (set) that only contains this value
        """
        self.sets.append(set(value))

    def merge_sets(self, value1, value2):
        """
        Merge the sets containing the two values if they are not already in the same set
        """
        if not self.test_same_set(value1, value2):
            set1 = self.find_set(value1)
            set2 = self.find_set(value2)
            new_set = set1.union(set2);
            self.sets.remove(set2)
            self.sets.remove(set1)
            self.sets.append(new_set)

    def find_set(self, value):
        """
        Return the set that value belongs to
        """
        for s in self.sets:
            if value in s:
                return s

    def test_same_set(self, value1, value2):
        """
        Return a boolean stating whether or not the two values are in the same set
        """
        return self.find_set(value1) == self.find_set(value2)

    def size(self):
        """
        Return how many sets are in the structure
        """
        return len(self.sets)

if __name__ == '__main__':
    #Sanity test for myself when making this"""
    d = Disjoint('A')
    for char in ['B', 'C', 'D', 'E']:
        d.create_set(char)

    assert not d.test_same_set('A', 'B')
    assert not d.test_same_set('C', 'D')
    d.merge_sets('A', 'D')
    d.merge_sets('B', 'C')
    assert d.test_same_set('A', 'D')
    assert d.test_same_set('C', 'B')
    assert not d.test_same_set('A', 'C')
    d.merge_sets('B', 'D')
    assert d.test_same_set('A', 'C')
