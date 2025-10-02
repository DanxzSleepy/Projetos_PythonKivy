class TaskManager {
    constructor() {
        this.tasks = [];
        this.loadFromLocalStorage();
        this.initializeEventListeners();
        this.renderTaskList();
    }

    initializeEventListeners() {
        const addBtn = document.getElementById('addBtn');
        const itemInput = document.getElementById('itemInput');

        addBtn.addEventListener('click', () => this.addTask());
        itemInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.addTask();
            }
        });
    }

    addTask() {
        const itemInput = document.getElementById('itemInput');
        const text = itemInput.value.trim();

        if (!text) {
            this.showMessage('Por favor, digite uma tarefa!', 'error');
            return;
        }

        // Check for duplicates
        if (this.tasks.some(task => task.text.toLowerCase() === text.toLowerCase())) {
            this.showMessage('Esta tarefa já existe!', 'error');
            return;
        }

        const newTask = {
            id: Date.now(),
            text: text,
            createdAt: new Date().toISOString()
        };

        this.tasks.push(newTask);
        this.saveToLocalStorage();
        this.renderTaskList();
        itemInput.value = '';
        this.showMessage('Tarefa adicionada com sucesso! ✅', 'success');
    }

    deleteTask(id) {
        this.tasks = this.tasks.filter(task => task.id !== id);
        this.saveToLocalStorage();
        this.renderTaskList();
        this.showMessage('Tarefa removida com sucesso! ❌', 'success');
    }

    editTask(id) {
        const task = this.tasks.find(task => task.id === id);
        if (!task) return;

        const itemElement = document.querySelector(`[data-id="${id}"]`);
        if (!itemElement) return;

        itemElement.classList.add('editing');
        itemElement.innerHTML = `
            <input type="text" class="edit-input" value="${task.text}">
            <button class="save-btn">Salvar</button>
            <button class="cancel-btn">Cancelar</button>
        `;

        const editInput = itemElement.querySelector('.edit-input');
        const saveBtn = itemElement.querySelector('.save-btn');
        const cancelBtn = itemElement.querySelector('.cancel-btn');

        editInput.focus();

        saveBtn.addEventListener('click', () => {
            const newText = editInput.value.trim();
            if (!newText) {
                this.showMessage('A tarefa não pode estar vazia!', 'error');
                return;
            }

            // Check for duplicates (excluding current task)
            if (this.tasks.some(t => t.id !== id && t.text.toLowerCase() === newText.toLowerCase())) {
                this.showMessage('Esta tarefa já existe!', 'error');
                return;
            }

            task.text = newText;
            this.saveToLocalStorage();
            this.renderTaskList();
            this.showMessage('Tarefa atualizada com sucesso! ✏️', 'success');
        });

        cancelBtn.addEventListener('click', () => {
            this.renderTaskList();
        });

        editInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                saveBtn.click();
            }
        });
    }

    renderTaskList() {
        const itemList = document.getElementById('itemList');
        itemList.innerHTML = '';

        if (this.tasks.length === 0) {
            itemList.innerHTML = '<p class="empty-list">Nenhuma tarefa encontrada. Adicione uma nova tarefa!</p>';
            return;
        }

        this.tasks.forEach(task => {
            const li = document.createElement('li');
            li.className = 'item';
            li.dataset.id = task.id;
            
            li.innerHTML = `
                <span class="item-text">${task.text}</span>
                <div class="item-buttons">
                    <button class="edit-btn" onclick="taskManager.editTask(${task.id})">Editar</button>
                    <button class="delete-btn" onclick="taskManager.deleteTask(${task.id})">Excluir</button>
                </div>
            `;
            
            itemList.appendChild(li);
        });
    }

    saveToLocalStorage() {
        localStorage.setItem('tasks', JSON.stringify(this.tasks));
    }

    loadFromLocalStorage() {
        const storedTasks = localStorage.getItem('tasks');
        if (storedTasks) {
            try {
                this.tasks = JSON.parse(storedTasks);
            } catch (e) {
                console.error('Error parsing tasks from localStorage:', e);
                this.tasks = [];
            }
        }
    }

    showMessage(text, type) {
        const messageDiv = document.getElementById('message');
        messageDiv.textContent = text;
        messageDiv.className = type;
        messageDiv.style.display = 'block';

        setTimeout(() => {
            messageDiv.style.display = 'none';
        }, 3000);
    }
}

// Initialize the app when the page loads
let taskManager;
document.addEventListener('DOMContentLoaded', () => {
    taskManager = new TaskManager();
});