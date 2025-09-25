
## **Código 3: Manutenção Evolutiva**

### **Código Antes da Evolução:**
```python
class GerenciadorContatos:
    def __init__(self):
        self.contatos = []
    
    def adicionar_contato(self, contato):
        self.contatos.append(contato)
        print(f"Contato '{contato.nome}' adicionado com sucesso.")
    
    def listar_contatos(self):
        print("\n--- Lista de Contatos ---")
        if not self.contatos:
            print("Nenhum contato cadastrado.")
        else:
            for contato in self.contatos:
                print(f"Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}")
        print("---\n")
```

### **Nova Funcionalidade Solicitada:** Pesquisar contatos por nome.

### **Código Após Evolução:**
```python
class GerenciadorContatos:
    def __init__(self):
        self.contatos = []
    
    def adicionar_contato(self, contato):
        self.contatos.append(contato)
        print(f"Contato '{contato.nome}' adicionado com sucesso.")
    
    def listar_contatos(self):
        print("\n--- Lista de Contatos ---")
        if not self.contatos:
            print("Nenhum contato cadastrado.")
        else:
            for contato in self.contatos:
                print(f"Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}")
        print("---\n")
    
    def pesquisar_por_nome(self, nome):
        resultados = [contato for contato in self.contatos if nome.lower() in contato.nome.lower()]
        if not resultados:
            print(f"Nenhum contato encontrado com o nome '{nome}'.")
        else:
            print(f"\n--- Resultados para '{nome}' ---")
            for contato in resultados:
                print(f"Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}")
            print("---\n")
        return resultados
```
