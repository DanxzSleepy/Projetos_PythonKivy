## **Código 1: Manutenção Corretiva**

### **Código Antes da Correção:**
```python
def calcular_frete(distancia_km, peso_kg, tipo_entrega):
    tabela_precos = [10.00, 15.50, 20.00]
    
    if not 0 <= tipo_entrega <= 2:
        return "Erro: Tipo de entrega inválido."
    
    custo_base = distancia_km * tabela_precos[tipo_entrega]
    
    if peso_kg > 50:
        custo_peso = peso_kg * 0.20
    elif 10 < peso_kg <= 50:
        custo_peso = peso_kg * 0.10
    elif peso_kg > 0:
        custo_peso = 0.05
    
    custo_total = custo_base + custo_peso
    
    if distancia_km > 100 and tipo_entrega == 1:
        return tabela_precos[3]
    
    return custo_total
```

### **Problemas Identificados:**
1. **Erro de índice:** `tabela_precos[3]` não existe (índice inválido).
2. **Variável não inicializada:** Se `peso_kg <= 0`, `custo_peso` fica indefinido.
3. **Lógica inconsistente:** Retorna um valor da tabela em vez de calcular o custo total.

### **Código Após Correção:**
```python
def calcular_frete(distancia_km, peso_kg, tipo_entrega):
    tabela_precos = [10.00, 15.50, 20.00]
    
    if not 0 <= tipo_entrega <= 2:
        return "Erro: Tipo de entrega inválido."
    
    if peso_kg <= 0:
        return "Erro: Peso deve ser maior que zero."
    
    custo_base = distancia_km * tabela_precos[tipo_entrega]
    
    if peso_kg > 50:
        custo_peso = peso_kg * 0.20
    elif peso_kg > 10:
        custo_peso = peso_kg * 0.10
    else:
        custo_peso = peso_kg * 0.05
    
    custo_total = custo_base + custo_peso
    
    if distancia_km > 100 and tipo_entrega == 1:
        custo_total *= 1.10  # Acréscimo de 10% para entrega expressa acima de 100km
    
    return round(custo_total, 2)
```

