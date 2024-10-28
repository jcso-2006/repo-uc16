SELECT 
    f1.nome AS funcionario1,
    f2.nome AS funcionario2,
    f1.salario AS salario_comum
FROM funcionarios f1
INNER JOIN funcionarios f2 
    ON f1.salario = f2.salario
    AND f1.id < f2.id;