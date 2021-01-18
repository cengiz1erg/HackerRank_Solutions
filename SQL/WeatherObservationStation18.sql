/*
In a plane with p1 at (x1, y1) and p2 at (x2, y2), Manhattan Distance = |x1 - x2| + |y1 - y2|.
*/

select round(abs(max(LAT_N)-min(LAT_N))+abs(max(LONG_W)-min(LONG_W)),4)
from station
