Range Query Program

------------------------------------------------------------------------------------------------
1.Instructions for compiling and running the program
------------------------------------------------------------------------------------------------
The program is written in Python 2.7.8 and needs python to be installed prior to the execution of the program.

-Place the inut.txt within the same folder as in the python file.

-usage: python range_query.py <inputfile> <outputfile>

------------------------------------------------------------------------------------------------
2. Runtime and space analysis for each operation
------------------------------------------------------------------------------------------------
To implement range query program I have built a data structure based on interval tree concept.


ADD      -  O(n log n)

QUERY    -  O(m + k*log n) where,
          * n = size of the tree
          * m = number of matches
          * k = size of the search range (this is 1 for a point search)

CLEAR    - O(1)

------------------------------------------------------------------------------------------------
Justification for the performance requirements
------------------------------------------------------------------------------------------------
Queries require O(m + 1*log n) time, with n being the total number of intervals and m being the number of reported results.
Construction requires O(n log n) time, and storage requires O(n) space. 'n' being the number of events.

The program starts by taking the entire range of all the intervals and dividing it in half at tree_center (to keep the tree relatively balanced).
This gives three sets of intervals,
those completely to the left of tree_center which we'll call node_left,
those completely to the right of tree_center which we'll call node_right, and
those overlapping x_center which we'll call node_center.

The intervals in node_left and node_right are recursively divided in the same manner until there are no intervals left.
The intervals in node_center that overlap the center point are stored in a separate data structure linked to the node in the interval tree.
This data structure consists of two lists, one containing all the intervals sorted by their beginning points, and another containing all the intervals sorted by their ending points.

The result is a interval tree with each node storing:
A center point
A pointer to another node containing all intervals completely to the left of the center point
A pointer to another node containing all intervals completely to the right of the center point
All intervals overlapping the center point sorted by their beginning point
All intervals overlapping the center point sorted by their ending point

I believe this is the best optimized approach to address the rquirements of calendar events.