
SELECT 
    f.nome AS nome_funcionario,
    d.nome AS nome_departamento
FROM funcionarios f
RIGHT JOIN departamentos d 
    ON f.departamento_id = d.id;