-- Backup do Banco de dados
create database appjunina;
use appjunina;

CREATE TABLE `estoque` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) DEFAULT NULL,
  `valor_unit` decimal(10,0) DEFAULT NULL,
  `quant_total` int DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `historico` (
  `id` int DEFAULT NULL,
  `nome` varchar(50) DEFAULT NULL,
  `valor_unit` decimal(10,0) DEFAULT NULL,
  `quant` int DEFAULT NULL,
  `valor_total` decimal(20,0) DEFAULT NULL,
  `horario` timestamp NULL DEFAULT NULL
);

CREATE TABLE `vendas` (
  `id` int DEFAULT NULL,
  `nome` varchar(50) DEFAULT NULL,
  `valor_unit` decimal(10,0) DEFAULT NULL,
  `quant` int DEFAULT NULL,
  `total` decimal(20,0) DEFAULT NULL
);

-- Valores aleatórios para as tabelas
INSERT INTO `estoque` (`nome`, `valor_unit`, `quant_total`) VALUES
('Pamonha', 5.00, 120),
('Curau', 4.50, 80),
('Canjica', 6.00, 100),
('Bolo de milho', 10.00, 50),
('Pé de moleque', 2.50, 200),
('Paçoca', 1.50, 300),
('Cuscuz', 7.00, 70),
('Quentão', 12.00, 30),
('Cocada', 3.00, 150),
('Milho assado', 5.50, 110);

INSERT INTO `historico` (`id`, `nome`, `valor_unit`, `quant`, `valor_total`, `horario`) VALUES
(1, 'Pamonha', 5.00, 3, 15.00, '2024-12-18 14:30:00'),
(2, 'Canjica', 6.00, 5, 30.00, '2024-12-18 15:45:00'),
(3, 'Pé de moleque', 2.50, 10, 25.00, '2024-12-18 16:10:00'),
(4, 'Quentão', 12.00, 2, 24.00, '2024-12-18 17:00:00'),
(5, 'Cocada', 3.00, 7, 21.00, '2024-12-18 18:20:00');

-- tabela de vendas precisa estar vazia, é preenchida apenas
-- quando se usa a tela de vendas
