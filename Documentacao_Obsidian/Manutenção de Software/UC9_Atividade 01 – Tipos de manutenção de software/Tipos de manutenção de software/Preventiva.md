## **Código 4: Manutenção Preventiva**

### **Código Antes da Otimização:**
```python
def processador_pedidos():
    lista_pedidos = []
    
    for i in range(1000):
        lista_pedidos.append(Pedido(f"Produto {i}", i + 10.0, 2))
    
    for i in range(len(lista_pedidos)):
        total_geral = 0
        for j in range(len(lista_pedidos)):
            total_geral += lista_pedidos[j].get_subtotal()
        print(f"Processando o pedido {i}. Total geral atual: {total_geral}")
```

### **Problemas Identificados:**
1. **Complexidade O(n²):** Laço aninhado desnecessário recalcula o total geral para cada pedido.
2. **Ineficiência:** O total geral é o mesmo em todas as iterações.

### **Código Após Otimização Preventiva:**
```python
def processador_pedidos():
    lista_pedidos = []
    
    for i in range(1000):
        lista_pedidos.append(Pedido(f"Produto {i}", i + 10.0, 2))
    
    # Calcula o total geral UMA VEZ
    total_geral = sum(pedido.get_subtotal() for pedido in lista_pedidos)
    
    for i, pedido in enumerate(lista_pedidos):
        print(f"Processando o pedido {i}. Total geral: {total_geral}")
```

