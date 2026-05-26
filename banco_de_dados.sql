-- ============================================================
--  Script de criação do banco de dados
--  Compatível com: novomain.py
--  Banco: BD240226189
-- ============================================================

CREATE DATABASE IF NOT EXISTS BD240226189
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE BD240226189;

-- ------------------------------------------------------------
-- Tabela: cadastro_solicitantes
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS cadastro_solicitantes (
    codigo   INT          NOT NULL AUTO_INCREMENT,
    nome     VARCHAR(100) NOT NULL,
    email    VARCHAR(150)          DEFAULT NULL,
    telefone VARCHAR(20)           DEFAULT NULL,
    PRIMARY KEY (codigo),
    UNIQUE KEY uq_email    (email),
    UNIQUE KEY uq_telefone (telefone)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ------------------------------------------------------------
-- Tabela: categorias
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS categorias (
    id        INT         NOT NULL AUTO_INCREMENT,
    categoria VARCHAR(80) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Categorias iniciais (ajuste conforme necessário)
INSERT INTO categorias (categoria) VALUES
    ('Suporte Técnico'),
    ('Financeiro'),
    ('Recursos Humanos'),
    ('Infraestrutura'),
    ('Outros');

-- ------------------------------------------------------------
-- Tabela: solicitacoes
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS solicitacoes (
    id                  INT          NOT NULL AUTO_INCREMENT,
    codigo_solicitante  INT          NOT NULL,
    id_categoria        INT          NOT NULL,
    descricao           TEXT         NOT NULL,
    data_abertura       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status              VARCHAR(20)  NOT NULL DEFAULT 'Aberta',
    prioridade          VARCHAR(10)  NOT NULL DEFAULT 'Baixa',
    PRIMARY KEY (id),
    CONSTRAINT fk_solicitante FOREIGN KEY (codigo_solicitante)
        REFERENCES cadastro_solicitantes (codigo)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_categoria FOREIGN KEY (id_categoria)
        REFERENCES categorias (id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    CONSTRAINT chk_status     CHECK (status     IN ('Aberta', 'Em andamento', 'Fechada')),
    CONSTRAINT chk_prioridade CHECK (prioridade IN ('Baixa', 'Média', 'Alta'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
