## **Código 2: Manutenção Adaptativa**

### **Código Antes da Adaptação:**
```javascript
const Formatter = require('old-date-formatter');

function formatar_data(data) {
    let data_formatada = new Formatter(data).toFormat('DD/MM/YYYY');
    return '$(data_formatada) - Timestamp: $(data.getTime())';
}
```

### **Problemas Identificados:**
1. **Biblioteca desatualizada:** Uso de `old-date-formatter`.
2. **Template string incorreta:** Uso de `$()` em vez de `${}`.
3. **Método inválido:** `data.getTime()` dentro da string estático.

### **Código Após Adaptação (usando Day.js moderno):**
```javascript
const dayjs = require('dayjs');

function formatar_data(data) {
    const data_formatada = dayjs(data).format('DD/MM/YYYY');
    const timestamp = dayjs(data).valueOf();
    return `${data_formatada} - Timestamp: ${timestamp}`;
}
```
