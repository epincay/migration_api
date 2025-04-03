SELECT 
    d.name AS departamento,
    j.title AS puesto,
    COUNT(CASE WHEN EXTRACT(QUARTER FROM e.date) = 1 THEN 1 END) AS q1,
    COUNT(CASE WHEN EXTRACT(QUARTER FROM e.date) = 2 THEN 1 END) AS q2,
    COUNT(CASE WHEN EXTRACT(QUARTER FROM e.date) = 3 THEN 1 END) AS q3,
    COUNT(CASE WHEN EXTRACT(QUARTER FROM e.date) = 4 THEN 1 END) AS q4,
    COUNT(*) AS total_2021
FROM 
    employees e
JOIN departments d ON e.department_id = d.id
JOIN 
    jobs j ON e.job_id = j.id
WHERE 
    EXTRACT(YEAR FROM e.date) = 2021
GROUP BY 
    d.name, j.title
ORDER BY 
    d.name ASC, j.title ASC;