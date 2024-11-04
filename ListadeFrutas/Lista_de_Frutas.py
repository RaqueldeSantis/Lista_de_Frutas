# Classe Fruta
class Fruta:
    def __init__(self, nome, quantidade, preco, disponibilidade):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.disponibilidade = disponibilidade

    def atualizar_disponibilidade(self):
        if self.quantidade > 0:
            self.disponibilidade = "Disponível"
        else:
            self.disponibilidade = "Não disponível"

    def __str__(self):
        return f"Nome: {self.nome}, Quantidade: {self.quantidade}, Preço: {self.preco}, Disponibilidade: {self.disponibilidade}"


# Lista de frutas
frutas = []


# Função para adicionar uma fruta
def adicionar_fruta(nome, quantidade, preco):
    nova_fruta = Fruta(nome, quantidade, preco, "Disponível" if quantidade > 0 else "Não disponível")
    frutas.append(nova_fruta)
    print(f"Fruta {nome} adicionada com sucesso.")


# Função para buscar frutas
def buscar_frutas(criterio):
    criterio = criterio.lower()
    for fruta in frutas:
        if fruta.nome.lower() == criterio or str(fruta.quantidade) == criterio or str(
                fruta.preco) == criterio or fruta.disponibilidade.lower() == criterio:
            return fruta
    return None


# Função para gerenciar a lista
def gerenciar_lista():
    while True:
        acao = input(
            "Digite 'adicionar' para adicionar uma fruta, 'buscar' para buscar uma fruta ou 'sair' para sair: ").strip().lower()

        if acao == 'sair':
            print("Ação finalizada.")
            break
        elif acao == 'adicionar':
            nome = input("Digite o nome da fruta: ").strip()
            if not nome.istitle():
                print("Opção inválida, inicie com letra maiúscula.")
                continue
            quantidade = int(input("Digite a quantidade: "))
            preco = float(input("Digite o preço: "))
            adicionar_fruta(nome, quantidade, preco)
        elif acao == 'buscar':
            criterio = input("Digite o nome, quantidade, preço ou disponibilidade para buscar: ").strip()
            fruta = buscar_frutas(criterio)
            if fruta:
                print(f"{criterio} já está cadastrada.")
                print(fruta)
                editar = input("Deseja modificar os dados desta fruta? (sim/não): ").strip().lower()
                if editar == 'sim':
                    fruta.preco = float(input("Digite o novo preço: "))
                    fruta.quantidade = int(input("Digite a nova quantidade: "))
                    fruta.atualizar_disponibilidade()
                    print(f"Dados da fruta {fruta.nome} atualizados com sucesso.")
            else:
                print("Fruta não cadastrada.")
                adicionar_novo = input("Adicionar nova fruta? (sim/não): ").strip().lower()
                if adicionar_novo == 'sim':
                    nome = input("Digite o nome: ").strip()
                    if not nome.istitle():
                        print("Opção inválida, inicie com letra maiúscula.")
                        continue
                    quantidade = int(input("Digite a quantidade: "))
                    preco = float(input("Digite o preço: "))
                    adicionar_fruta(nome, quantidade, preco)
        else:
            print("Opção inválida.")


# Executar a função principal
gerenciar_lista()

