key learnings:
- traversals are easily done by recursion
- spending some more time thinking about the problem before attempting it, leads to more avenues on solution
- going from destination to source instead of source to destination is useful, i.e. think backwards
  - the case that broke 3.py was [1,1] --> [1,10000] which led to the involvement of 'k' to subtract all the times when tx > ty or vice versa
- for chessboard problem, way more thought was required to define what a chessboard is, and to check the two things
  - is valid board
  - minimum number of moves [this one was more tricky based on just selecting the min moves for row 1 and col 1]