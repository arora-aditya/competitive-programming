/* Write your T-SQL query statement below */
-- https://leetcode.com/problems/activity-participants/
with cte as
(
select activity, count(id) as num
from Friends
group by activity
)
select activity as ACTIVITY
from cte
where num not in (select max(num) from cte)
and num not in (select min(num) from cte)