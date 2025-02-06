# Write your MySQL query statement below
SELECT S1.student_id, S1.student_name, S2.subject_name,
COUNT(E.subject_name) AS attended_exams
FROM Students AS S1
CROSS JOIN Subjects AS S2
LEFT JOIN Examinations AS E
ON S1.student_id = E.student_id
AND S2.subject_name = E.subject_name
GROUP BY S1.student_id, S1.student_name, S2.subject_name
ORDER BY S1.student_id, S2.subject_name;