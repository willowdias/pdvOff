
import sqlite3
class sqlite_db:
    def __init__(self,banco=None):
        self.conn =None
        self.curso = None
        
        if banco:
            self.open(banco)
        self.create()
    def open(self,banco):
        try:
            self.conn = sqlite3.connect(banco)
            self.cursor = self.conn.cursor() 
        except:
           print("banco Off")     

    def insert(self,query):#acicionar item
        cur = self.cursor
        cur.execute(query)
        return self.conn.commit()
    def update(self,query):#upadte
        cur = self.cursor
        cur.execute(query)
        self.conn.commit()   
    def select(self,query): #selecionar item
        
        cur = self.cursor
        cur.execute(query)
        return cur.fetchall()  
    def create(self):
        cur = self.cursor
        cur.execute(''' CREATE TABLE IF NOT EXISTS tb_estoque(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo_barra varchar(200),
            descricao varchar(200),
            quant varchar(200),
            codmarca int,
            marca varchar(200),
            codgrupo int,
            grupo varchar(200),
            custo NUMERIC (18,4),
            venda NUMERIC (18,4)
        );''')
        cur.execute(''' CREATE TABLE IF NOT EXISTS clientes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome varchar(200),
            sobrenome char(200),
            cpf_cnpj INT,
            rg_inscricao INT,
            celular INT,
            telefone INT ,
            email char(200),
            obs char(500),
            cod_ibge INT,
            cep INT,          
            cidade char(200),
            estado char(2),
            endereco char(500),
            bairro char(120),
            numeroresidencia INT,
            data_emissao varchar(255),
            data_aniversario varchar(255),
            data_ultimaCompra VARCHAR (255),
            pai               VARCHAR (255),
            mae               VARCHAR (255),
            estado_civil      VARCHAR (255),
            situacao          CHAR (1),
            sexo              CHAR (1),
            tipo_cliente      CHAR (1) 


        );''')
db=sqlite_db("database/pdv.db")