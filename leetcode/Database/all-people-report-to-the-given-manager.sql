-- https://leetcode.com/problems/all-people-report-to-the-given-manager/submissions/s
SELECT e.employee_id FROM employees e
JOIN employees x ON e.manager_id = x.employee_id
JOIN employees y ON x.manager_id = y.employee_id
JOIN employees z ON y.manager_id = z.employee_id
WHERE (x.manager_id = 1 OR y.manager_id = 1 OR z.manager_id = 1) AND e.employee_id != 1