from PyQt5 import uic,QtWidgets
import mysql.connector
import sys

numero_id = 0

#criando tabela
#cursor = banco.cursor()
#comando_mysql = ("""create table novos(
#                id int not null auto_increment,
#                nome varchar(50) not null,
#                idade int(3),
#                sexo enum('M','F','NB','NI'),
#                telefone bigint(15),
#                email varchar(30),
#                primary key(id)
#)""")
#cursor.execute(comando_mysql)
#banco.commit()

banco = mysql.connector.connect(
    host='localhost',
    user='AlexAffs',
    passwd='AlexAffs@1995',
    database = 'desafio'
)
#tela inicial1
def funcao_principal():
    formulario.show()
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    linha4 = formulario.lineEdit_4.text()
    linha5 = formulario.lineEdit_5.text()

    

  #inserindo dados:  
    cursor = banco.cursor()
    comando_sql = 'INSERT INTO novos (nome, idade, sexo, telefone, email) VALUES (%s, %s, %s, %s, %s)'
    dados = (str(linha1), str(linha2), str(linha3), str(linha4), str(linha5))
    cursor.execute(comando_sql, dados)
    banco.commit()
    formulario.lineEdit.setText('')
    formulario.lineEdit_2.setText('')
    formulario.lineEdit_3.setText('')
    formulario.lineEdit_4.setText('')
    formulario.lineEdit_5.setText('')

def cadastrados_lista():
    segunda_tela.show()
#dados_lidos
    cursor = banco.cursor()
    comando_sql = 'SELECT * FROM novos'
    cursor.execute(comando_sql)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(6)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 6):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
#excluindo dados
def excluir_dados():
    linha = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute('SELECT id FROM novos')
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute('DELETE FROM novos WHERE id='+ str(valor_id))
    banco.commit()

#criando a tabela2
#    cursor = banco.cursor()
#    comando_mysql = ("""create table unidades(
#        id INT NOT NULL AUTO_INCREMENT,
#        identificação varchar(255),
#        propriedade varchar(255),
#        condominio varchar(255),
#        endereço varchar(255),
#        PRIMARY KEY(id)
#        )""")
#    cursor.execute(comando_mysql)
#    banco.commit()

def funcao_principal2():
        unidades.show()
        linha6 = unidades.lineEdit.text()
        linha7 = unidades.lineEdit_2.text()
        linha8 = unidades.lineEdit_3.text()
        linha9 = unidades.lineEdit_4.text()

        cursor = banco.cursor()
        comando_sql = 'INSERT INTO unidades (identificação, propriedade, condominio, endereço) VALUES (%s, %s, %s, %s)'
        dados = (str(linha6), str(linha7), str(linha8), str(linha9))
        cursor.execute(comando_sql, dados)
        banco.commit()
        unidades.lineEdit.setText('')
        unidades.lineEdit_2.setText('')
        unidades.lineEdit_3.setText('')
        unidades.lineEdit_4.setText('')
    

def unidades_cadastradas():
    caduni.show()

    cursor = banco.cursor()
    comando_sql = 'SELECT * FROM unidades'
    cursor.execute(comando_sql)
    dados_lidos = cursor.fetchall()

    caduni.tableWidget.setRowCount(len(dados_lidos))
    caduni.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            caduni.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
def excluir_dados2():
    linha = caduni.tableWidget.currentRow()
    caduni.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute('SELECT id FROM unidades')
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute('DELETE FROM unidades WHERE id='+ str(valor_id))
    banco.commit()
#criando tabela3
#cursor = banco.cursor()
#comando_mysql = ("""create table despesas(
 #   id int not null auto_increment,
 #   descrição varchar(255),
 #   tipo_despesa varchar(255),
 #   valor double,
 #   vencimento_fatura date,
 #   status_pagamento varchar(25),
 #   primary key(id)
#)""")
#cursor.execute(comando_mysql)
#banco.commit()

#tela inicial
def funcao_principal3():
        despesas.show()
        descrição = despesas.lineEdit.text()
        tipo = despesas.lineEdit_2.text()
        valor = despesas.lineEdit_3.text()
        vencimento = despesas.lineEdit_4.text()
        status = despesas.lineEdit_5.text()

  #inserindo dados:  
        cursor = banco.cursor()
        comando_SQL = 'INSERT INTO despesas (descrição, tipo_despesa, valor, vencimento_fatura, status_pagamento) VALUES (%s, %s, %s, %s, %s)'
        dados = (str(descrição), str(tipo), str(valor), str(vencimento), str(status))
        cursor.execute(comando_SQL, dados)
        banco.commit()
        despesas.lineEdit.setText('')
        despesas.lineEdit_2.setText('')
        despesas.lineEdit_3.setText('')
        despesas.lineEdit_4.setText('')
        despesas.lineEdit_5.setText('')

def despesas_lista():
    segunda_tela3.show()

#dados_lidos
    cursor = banco.cursor()
    comando_sql = 'SELECT * FROM despesas'
    cursor.execute(comando_sql)
    dados_lidos = cursor.fetchall()

    segunda_tela3.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela3.tableWidget.setColumnCount(6)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 6):
            segunda_tela3.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def editar_dados():
    global numero_id
    
    linha = segunda_tela3.tableWidget.currentRow()
    
    cursor = banco.cursor()
    cursor.execute('SELECT id FROM despesas')
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute('SELECT * FROM despesas WHERE id='+ str(valor_id))
    despesas_cad = cursor.fetchall()
    menu_editar.show()

    menu_editar.lineEdit.setText(str(despesas_cad[0][0]))
    menu_editar.lineEdit_2.setText(str(despesas_cad[0][1]))
    menu_editar.lineEdit_3.setText(str(despesas_cad[0][2]))
    menu_editar.lineEdit_4.setText(str(despesas_cad[0][3]))
    menu_editar.lineEdit_5.setText(str(despesas_cad[0][4]))
    menu_editar.lineEdit_6.setText(str(despesas_cad[0][5]))
    numero_id = valor_id
    
def salvar_dados_editados():
  #pega o número do id
    global numero_id
 #valor digitado no lineEdit
    id = menu_editar.lineEdit.text()
    descricao = menu_editar.lineEdit_2.text()
    tipo_despesa = menu_editar.lineEdit_3.text()
    valor = menu_editar.lineEdit_4.text()
    vencimento_fatura = menu_editar.lineEdit_5.text()
    status_pagamento = menu_editar.lineEdit_6.text()
 #atualizar os dados do banco:
    cursor = banco.cursor()
    cursor.execute('UPDATE despesas SET descrição = "{}", tipo_despesa = "{}", valor = "{}", vencimento_fatura = "{}", status_pagamento = "{}" WHERE id ={}'.format(descricao, tipo_despesa, valor, vencimento_fatura, status_pagamento, numero_id))
    banco.commit()
    #atualizar as janelas
    menu_editar.close()
    

#excluindo dados
def excluir_dados3():
    linha = segunda_tela3.tableWidget.currentRow()
    segunda_tela3.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute('SELECT id FROM despesas')
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute('DELETE FROM despesas WHERE id='+ str(valor_id))
    banco.commit()

app=QtWidgets.QApplication([])
principal=uic.loadUi('INICIAL.ui')
principal.show()
principal.pushButton.clicked.connect(funcao_principal)
principal.pushButton_2.clicked.connect(funcao_principal2)
principal.pushButton_3.clicked.connect(funcao_principal3)
despesas=uic.loadUi('DESPESAS.ui')
segunda_tela3=uic.loadUi('DESPESASCAD.ui')
menu_editar =uic.loadUi('EDITAR.ui')
despesas.pushButton.clicked.connect(funcao_principal3)
despesas.pushButton_2.clicked.connect(despesas_lista)
segunda_tela3.pushButton.clicked.connect(editar_dados)
segunda_tela3.pushButton_2.clicked.connect(excluir_dados3)
menu_editar.pushButton.clicked.connect(salvar_dados_editados)
unidades=uic.loadUi('UNIDADES.ui')
caduni=uic.loadUi('CADUNI.ui')
unidades.pushButton.clicked.connect(funcao_principal2)
unidades.pushButton_2.clicked.connect(unidades_cadastradas)
formulario=uic.loadUi('FORMULARIO.ui')
segunda_tela=uic.loadUi('CADASTRADOS.ui')
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(cadastrados_lista)
segunda_tela.pushButton_2.clicked.connect(excluir_dados)
caduni.pushButton.clicked.connect(excluir_dados2)
app.exec()