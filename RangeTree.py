import operator

'''
    RangeTree.py created by Vikram Sai Arsid 07/19/2015 08:36 PM PST
'''


class RangeTree:
    # Parsing intervals for events on calendar
    def __init__(self, intervals):
        self.root_node = self.interval_division(intervals)

    # Building interval tree for time intervals of events on the calendar
    def interval_division(self, intervals):

        if not intervals:
            return None

        tree_center = self.center(intervals)

        node_center = []
        node_left = []
        node_right = []

        for k in intervals:
            if k.get_end() < tree_center:
                node_left.append(k)
            elif k.get_begin() > tree_center:
                node_right.append(k)
            else:
                node_center.append(k)

        return Node(tree_center, node_center, self.interval_division(node_left), self.interval_division(node_right))

    # Function to get center of the tree
    def center(self, intervals):
        fs = sort_by_begin(intervals)
        length = len(fs)

        return fs[int(length / 2)].get_begin()

    # Search function to process the query
    def search(self, begin, end=None):

        """
            Returns a set of all intervals overlapping the given range. Or,
            returns the set of all intervals fully
            contained in the range [begin, end].

            Completes in O(m + k*log n) time, where:
              * n = size of the tree
              * m = number of matches
              * k = size of the search range (this is 1 for a point search)
            :rtype: interval data
        """
        if end:
            result = []

            for j in xrange(begin, end + 1):
                for k in self.search(j):
                    result.append(k.data)
                result = list(set(result))
            return sort_by_begin(result)
        else:
            return self._search(self.root_node, begin, [])

    def _search(self, node, point, result):

        for k in node.node_center:
            if k.get_begin() <= point <= k.get_end():
                result.append(k.data)
        if point < node.tree_center and node.left_node:
            for k in self._search(node.left_node, point, []):
                result.append(k)
        if point > node.tree_center and node.right_node:
            for k in self._search(node.right_node, point, []):
                result.append(k)

        return list(set(result))


# Class for interval
class Interval:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def get_begin(self):
        return self.begin

    def get_end(self):
        return self.end


# Class representing the node
class Node:
    def __init__(self, tree_center, node_center, left_node, right_node):
        self.tree_center = tree_center
        self.node_center = sort_by_begin(node_center)
        self.left_node = left_node
        self.right_node = right_node


# Class to schedule a event with data , start time and end time
class ScheduleEvent:
    def __init__(self, data, start_time, end_time):
        self.data = data
        self.start_time = start_time
        self.end_time = end_time
        self.time = [start_time, end_time]

    def get_begin(self):
        return int(self.start_time)

    def get_end(self):
        return int(self.end_time)

    def __getitem__(self, item):
        return int(self.time[item])

    def __repr__(self):
        return ''.join([str((self.data, self.start_time, self.end_time))])


def sort_by_begin(intervals):
    return sorted(intervals, key=operator.itemgetter(0))
