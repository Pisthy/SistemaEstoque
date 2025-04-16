class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class Loja:
    def __init__(self):
        self.estoque = [
            Produto('Arroz', 25.99, 30),
            Produto('Feijão', 12.49, 30),
            Produto('Macarrão', 5.99, 30),
            Produto('Óleo', 15.50, 30),
            Produto('Café', 30.99, 30),
            Produto('Picanha', 89.90, 30),
            Produto('Frango', 16.00, 30),
            Produto('Tilápia', 15.00, 30),
            Produto('Extrato de Tomate', 8.99, 30),
            Produto('Cerveja Amstel', 33.99, 30)
        ]
        self.carrinho = []

    def menu(self):
        while True:
            print('\n🛍️ BEM-VINDO À NOSSA LOJA!')
            print('📋 MENU:')
            print('1. Ver produtos disponíveis')
            print('2. Adicionar produto ao carrinho')
            print('3. Ver carrinho')
            print('4. Finalizar compra')
            print('0. Sair da loja')
            
            escolha = input('\nDigite a opção desejada: ')
            if escolha == '1':
                self.listar_produtos()
            elif escolha == '2':
                self.adicionar_ao_carrinho()
            elif escolha == '3':
                self.Carrinho()
            elif escolha == '4':
                self.finalizar_compra()
            elif escolha == '0':
                print('\n👋 Obrigado por visitar nossa loja! Esperamos te ver novamente. 😊')
                break
            else:
                print('❌ Opção inválida. Tente novamente!')

    def listar_produtos(self):
        if not self.estoque:
            print('\n📦 Opa! Nosso estoque está vazio no momento.')
            return
        print('\n📦 PRODUTOS DISPONÍVEIS:')
        for i, produto in enumerate(self.estoque):
            print(f'{i} - {produto.nome} | R${produto.preco:.2f} | Quantidade disponível: {produto.quantidade}')

    def adicionar_ao_carrinho(self):
        self.listar_produtos()
        if not self.estoque:
            return
        try:
            indice = int(input('\nDigite o número do produto que deseja adicionar ao carrinho: '))
            quantidade = int(input('Quantidade desejada: '))
            produto = self.estoque[indice]
            if quantidade <= produto.quantidade:
                self.carrinho.append((produto.nome, produto.preco, quantidade))
                produto.quantidade -= quantidade
                print(f"\n✅ Adicionamos {quantidade}x '{produto.nome}' ao seu carrinho!")
            else:
                print('❌ Desculpe, não temos essa quantidade disponível em estoque.')
        except (IndexError, ValueError):
            print('⚠️ Entrada inválida. Tente novamente.')

    def Carrinho(self):
        if not self.carrinho:
            print('\n🛒 Seu carrinho está vazio no momento.')
            return
        print('\n🛒 SEU CARRINHO:')
        total = 0
        for nome, preco, quantidade in self.carrinho:
            subtotal = preco * quantidade
            print(f'{nome} x{quantidade} - R${subtotal:.2f}')
            total += subtotal
        print(f'\n🧾 Total parcial: R${total:.2f}')

    def finalizar_compra(self):
        if not self.carrinho:
            print('\n🛒 Seu carrinho está vazio. Adicione produtos antes de finalizar a compra.')
            return
        print('\n🎉 Estamos quase lá! Vamos finalizar sua compra.')
        total = 0
        for nome, preco, quantidade in self.carrinho:
            subtotal = preco * quantidade
            total += subtotal
        print(f'\n💰 Valor total da compra: R${total:.2f}')
        print('\n💳 Formas de pagamento:')
        print('1 - Cartão de Crédito')
        print('2 - Cartão de Débito')
        print('3 - PIX (10% de desconto!)')

        forma_pagamento = input('Escolha a forma de pagamento (1/2/3): ')
        if forma_pagamento == '3':
            desconto = total * 0.10
            total -= desconto
            print(f'\n🏷️ Você escolheu PIX! Recebeu R${desconto:.2f} de desconto.')
        elif forma_pagamento == '1':
            print('\n💳 Pagamento com cartão de crédito selecionado.')
        elif forma_pagamento == '2':
            print('\n🏦 Pagamento com cartão de débito selecionado.')
        else:
            print('❌ Forma de pagamento inválida. Compra cancelada.')
            return
        
        print(f'\n✅ Compra concluída com sucesso! Valor pago: R${total:.2f}')
        print('🧾 Agradecemos a preferência. Volte sempre!')
        self.carrinho.clear()
loja = Loja()
loja.menu()
