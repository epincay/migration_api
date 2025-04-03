WITH hires_by_dept AS (
    SELECT 
        d.id,
        d.name AS department_name,
        COUNT(e.id) AS employees_hired
    FROM 
        departments d
    JOIN 
        employees e ON d.id = e.department_id
    WHERE 
        EXTRACT(YEAR FROM e.date) = 2021
    GROUP BY 
        d.id, d.name
),
avg_hires AS (
    SELECT AVG(employees_hired) AS avg_value
    FROM hires_by_dept
)
SELECT 
    h.id,
    h.department_name,
    h.employees_hired
FROM 
    hires_by_dept h
CROSS JOIN 
    avg_hires a
WHERE 
    h.employees_hired > a.avg_value
ORDER BY 
    h.employees_hired DESC;