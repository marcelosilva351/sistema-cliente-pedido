
import mysql.connector
import os
import time

banco = mysql.connector.connect(
    host="localhost",
    user = "root",
    passwd="1234",
    database="aluminex"
)
cursor = banco.cursor()



while True:

   
    
       
    def apagarTela():
        os.system('cls')
    def clientes():
            print("Cadastrar clientes [1]")
            print("listar clintes     [2]")
            print("voltar para o menu [3]")
            decisao_cliente = int(input())
            if decisao_cliente == 1:
                cadastrar_cliente()
            elif decisao_cliente == 2:
                listar_cliente()
            elif decisao_cliente == 3:
                pass
    
    def listar_cliente():
        comando = 'select c.cpf,c.nome,c.email,t.tipo,t.numero,e.cidade,e.cep,e.quadra,e.numero,e.referencia from cliente c inner join telefone t on c.cpf = t.cpf_cliente inner join endereco e on c.cpf = e.cpf_cliente'
        cursor.execute(comando)
        clientes_lista = cursor.fetchall()
        tamanholista = len(clientes_lista)
        
        for k,i in enumerate(clientes_lista):
            if k == 1:
                break
            for k,j in enumerate(clientes_lista):
                print(k,j)
               
                
                
                
            
             

        print("[1] para remover algum cliente")
        print("[2] Editar cliente")
        print("[3] ver pedidos do cliente")
        print("[4] voltar para tela de clientes") 
        
        decisaoListar = int(input())
        if decisaoListar == 1:
            print("digite o cpf do cliente que deseja excluir")
            cpf_excluir = input()
            cpf_naoexiste = True
            
            for i in clientes_lista:
                for k,v in enumerate(clientes_lista):
                    for v in v:
                        if cpf_excluir == v:
                            cpf_naoexiste = False

          
                   
        
            if not cpf_naoexiste:
                comando_puxarnome = f"select cpf, nome from cliente where cpf = '{cpf_excluir}'"
                cursor.execute(comando_puxarnome)
                cliente_excluir = cursor.fetchall()
                apagarTela()
                    
                print(f"cpf: {cliente_excluir[0][0]}")
                print(f"nome: {cliente_excluir[0][1]}")
                    
                decisao_excluir = input("Quer excluir esse cliente? [s][n]")
                if decisao_excluir.lower() == 's':
                    remever_cliente(cpf_excluir)
                elif decisao_excluir.lower() == 'n':
                    print("cliente não excluido")
                    clientes()
            else:
                print("cpf não existe no banco de dados")
                input()


        elif decisaoListar == 2:

            print("digite o cpf do cliente que deseja editar")
            cpf_editar = input()
            cpf_naoexiste = True
            
            for i in clientes_lista:
                for k,v in enumerate(clientes_lista):
                    for v in v:
                        if cpf_editar == v:
                            cpf_naoexiste = False

          
                   
        
            if not cpf_naoexiste:
                comando_puxarnome = f"select c.cpf,c.nome,c.email,t.tipo,t.numero,e.cidade,e.cep,e.quadra,e.numero,e.referencia from cliente c inner join telefone t on c.cpf = t.cpf_cliente inner join endereco e on c.cpf = e.cpf_cliente where cpf = {cpf_editar}"
                cursor.execute(comando_puxarnome)
                cliente_editar = cursor.fetchall()
          
                    
                print(f"cpf: {cliente_editar[0][0]}")
                print(f"nome: {cliente_editar[0][1]}")
                print(f"email: {cliente_editar[0][2]}")
                print(f"tipo: {cliente_editar[0][3]}")
                print(f"numero: {cliente_editar[0][4]}")
                print(f"cidade: {cliente_editar[0][5]}")
                print(f"cep: {cliente_editar[0][6]}")
                print(f"quadra: {cliente_editar[0][7]}")
                print(f"numero: {cliente_editar[0][8]}")
                print(f"referencia: {cliente_editar[0][9]}")

  
                decisao_editar = input("Quer editar esse cliente? [s][n]")
                if decisao_editar.lower() == 's':
                    print("Qual campo deseja alterar?")
                    campo = input()
                   
                    print("Deseja alterar para qual valor?")
                    valor = input()
                    update_cliente(campo,cpf_editar,valor)
            else:
                print("cpf não existe no banco")
                input()



        elif decisaoListar == 3:
            print("digite o cpf que deseja pesquisar")
            cpf = input()
            pegar_pedidos_cliente(cpf)
            
        elif decisaoListar == 4:
            apagarTela()
            clientes()

    def pegar_pedidos_cliente(cpf):
        comando = f"select p.descricao,p.valor,c.nome from pedido p inner join cliente c on p.cpf_cliente = C.CPF where c.cpf = '{cpf}'"
        cursor.execute(comando)
        pedidos = cursor.fetchall()
        print(' DESCRIÇÃO   VALOR   NOME CLIENTE ')
        for i,v in enumerate(pedidos):
            print(i,v)
        
        input()

        
        

           
            
        
    def update_cliente(campo,cpf,valor):
        if campo == "cpf" or campo == "nome" or campo == "email":
            comando = f"update cliente set {campo} = '{valor}' where cpf = '{cpf}'"
            cursor.execute(comando)
            print(f"campo {campo} atualizado com sucesso")
            time.sleep(1)
            apagarTela()
            clientes()


    def remever_cliente(cpf):
        
        comando_delete_endereco = f"delete from endereco where cpf_cliente = '{cpf}'"
        comando_delete_telefone = f"delete from telefone where cpf_cliente = '{cpf}'"
        comando_delete_cliente = f"delete from cliente where cpf = '{cpf}'"

        cursor.execute(comando_delete_telefone)
        cursor.execute(comando_delete_endereco)
        cursor.execute(comando_delete_cliente)
        banco.commit()
        print("cliente Excluido com sucesso")
        time.sleep(1)
        clientes()







    def cadastrar_cliente():
        print("Digite o Cpf do cliente:")
        cpf = input()
        print("digite o nome do cliente:")
        nome = input()
        print("digite o email do cliente")
        email = input()
        print("Ok! vamos cadastra o telefone:")
        print("Digite o tipo de telefone do cliente")
        tipoTel = input()
        print("digite o numero")
        numero = input()
        print("Ok! vamo cadastrar o endereço")
        print("digite a cidade")
        cidade = input()
        print("digite o cep")
        cep = input()
        print("digite a quadra")
        quadra = input()
        print("digite o numero do endereço")
        numeroEndereco = input()
        print("digite uma referencia")
        referencia = input()
   
        insert_cliente(cpf,nome,email)
        insert_telefone(tipoTel,numero,cpf)
        insert_endereco(cidade,cep,quadra,numeroEndereco,referencia,cpf)
    
    def insert_cliente(cpf, nome, email):
        comando = f"insert into cliente values('{cpf}', '{nome}', '{email}')"
        cursor.execute(comando)
        banco.commit()

       
    def insert_telefone(tipo, numero, cpf):
        comando = f"insert into telefone values('{tipo}', '{numero}', '{cpf}')"
        cursor.execute(comando)
        banco.commit()

    def insert_endereco(cidade, cep,quadra,numeroEndereco,referencia,cpf):
        comando = f"insert into endereco values('{cidade}', '{cep}','{quadra}','{numeroEndereco}','{referencia}','{cpf}')"
        cursor.execute(comando)
        banco.commit()
        print("cliente adicionado com sucesso!")
        time.sleep(1)
        os.system('cls')
        clientes()
   
   

    def sair():
        print("Deseja realmente sai do programa? [s][n]")
        condicaoSair = False
        sair = input()
        if sair.lower() == 's':
            condicaoSair = True
        return condicaoSair


    def telapedidos():
        print("Pedidos")
        print("[1] cadastrar")
        print("[2] listar")
        print("[3] excluir pedido")

        decisaopedido = input()
        if decisaopedido == '1':
            cadastrarpedido()
        if decisaopedido == '2':
            listarpedidos()
        if decisaopedido == '3':
            listarpedidos()
            print("digite o id do pedido  para excluir pedido")
            idpedido = input()
            deletarpedido(idpedido)

    
    def listarclientepedido():
        comando = 'select c.cpf,c.nome,c.email,t.tipo,t.numero,e.cidade,e.cep,e.quadra,e.numero,e.referencia from cliente c inner join telefone t on c.cpf = t.cpf_cliente inner join endereco e on c.cpf = e.cpf_cliente'
        cursor.execute(comando)
        clientes_lista = cursor.fetchall()
        for k,i in enumerate(clientes_lista):
            if k == 1:
                break
            for k,j in enumerate(clientes_lista):
                print(k,j)

    def listarpedidos():
        comando = "select p.id, p.descricao,p.valor,c.nome, c.cpf from pedido p inner join cliente c on p.cpf_cliente = C.CPF"
        cursor.execute(comando)
        pedidos = cursor.fetchall()
        for i,v in enumerate(pedidos):
            print(i,v)
        
        input()

    
    def deletarpedido(idpedido):
        comando = f"delete from pedido where id = {idpedido}"
        cursor.execute(comando)
        banco.commit()
        print("pedido excluido com sucesso")
        time.sleep(1)
        input()
    
    def cadastrarpedido():
        print('digite a descrição do pedido')
        descricao = input()
        print('digite o valor')
        valor = float(input())
        apagarTela()
        listarclientepedido()
        print("cpf do cliente")
        cpf_cliente = input()
        comando_adicionar_pedido = f"insert into pedido values(NULL,'{descricao}',{valor},'{cpf_cliente}')"
        cursor.execute(comando_adicionar_pedido)
        banco.commit()
        print("pedido adicionado com sucesso!")
        time.sleep(1)
        apagarTela()
        telapedidos()

    def apagarTela():
        os.system('cls')

    apagarTela()
    print("------- ALUMINEX -------")
    print("Clientes [1]")
    print("Pedidos  [2]")
    print("Sair     [3]")

    decisao = int(input())
    if decisao == 1:
        apagarTela()
        clientes()
    if decisao == 2:
        telapedidos()
    if decisao == 3:
        sair = sair()
        if sair:
            break


    