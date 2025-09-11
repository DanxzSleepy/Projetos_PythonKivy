import os
import sqlite3
from datetime import datetime
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label

DB_FILENAME = "shop.db"

# ----------------- DATABASE HELPERS -----------------
def get_conn():
    return sqlite3.connect(DB_FILENAME)

def criar_banco():
    conn = get_conn()
    c = conn.cursor()
    # users: basic profile fields (add more as needed)
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            name TEXT,
            email TEXT,
            cpf TEXT,
            rg TEXT,
            cep TEXT,
            endereco TEXT,
            avatar TEXT
        )
    """)
    # products
    c.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            price REAL,
            stock INTEGER,
            image TEXT
        )
    """)
    # cart: stores items per user (simple design)
    c.execute("""
        CREATE TABLE IF NOT EXISTS cart (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            product_id INTEGER,
            qty INTEGER,
            added_at TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(product_id) REFERENCES products(id)
        )
    """)
    # orders (simple)
    c.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            total REAL,
            created_at TEXT
        )
    """)
    conn.commit()
    conn.close()

def seed_products():
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM products")
    if c.fetchone()[0] == 0:
        sample = [
            ("Camiseta Superman", "Camiseta oficial dos quadrinhos - algodão", 59.9, 10, "images/superman.jpg"),
            ("Caneca Zelda", "Caneca cerâmica 300ml - Link edition", 39.5, 15, "images/zelda.jpg"),
            ("Poster Neon City", "Poster 60x40cm - edição limitada", 79.0, 5, "images/poster.jpg"),
        ]
        c.executemany("INSERT INTO products (title,description,price,stock,image) VALUES (?,?,?,?,?)", sample)
    conn.commit()
    conn.close()

# ----------------- DB OPERATIONS -----------------
def create_user(username, password, name="", email="", cpf="", rg="", cep="", endereco="", avatar=None):
    try:
        conn = get_conn()
        c = conn.cursor()
        c.execute("INSERT INTO users (username,password,name,email,cpf,rg,cep,endereco,avatar) VALUES (?,?,?,?,?,?,?,?,?)",
                  (username, password, name, email, cpf, rg, cep, endereco, avatar))
        conn.commit()
        uid = c.lastrowid
        conn.close()
        return uid
    except sqlite3.IntegrityError:
        return None

def get_user_by_username(username):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    u = c.fetchone()
    conn.close()
    return u

def get_user_by_id(uid):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id=?", (uid,))
    u = c.fetchone()
    conn.close()
    return u

def update_user(uid, name, email, password, cpf, rg, cep, endereco, avatar):
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
        UPDATE users
        SET name=?, email=?, password=?, cpf=?, rg=?, cep=?, endereco=?, avatar=?
        WHERE id=?
    """, (name, email, password, cpf, rg, cep, endereco, avatar, uid))
    conn.commit()
    conn.close()

def list_products(order_by="id"):
    conn = get_conn()
    c = conn.cursor()
    query = f"SELECT * FROM products ORDER BY {order_by}"
    c.execute(query)
    rows = c.fetchall()
    conn.close()
    return rows

def get_product(pid):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE id=?", (pid,))
    p = c.fetchone()
    conn.close()
    return p

def add_to_cart(user_id, product_id, qty=1):
    conn = get_conn()
    c = conn.cursor()
    # If exists, increase qty
    c.execute("SELECT id, qty FROM cart WHERE user_id=? AND product_id=?", (user_id, product_id))
    r = c.fetchone()
    if r:
        c.execute("UPDATE cart SET qty=? WHERE id=?", (r[1]+qty, r[0]))
    else:
        c.execute("INSERT INTO cart (user_id,product_id,qty,added_at) VALUES (?,?,?,?)",
                  (user_id, product_id, qty, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()

def get_cart(user_id):
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
        SELECT cart.id, products.id, products.title, products.price, cart.qty, products.image
        FROM cart JOIN products ON cart.product_id=products.id
        WHERE cart.user_id=?
    """, (user_id,))
    rows = c.fetchall()
    conn.close()
    return rows

def remove_cart_item(cart_id):
    conn = get_conn()
    c = conn.cursor()
    c.execute("DELETE FROM cart WHERE id=?", (cart_id,))
    conn.commit()
    conn.close()

def clear_cart(user_id):
    conn = get_conn()
    c = conn.cursor()
    c.execute("DELETE FROM cart WHERE user_id=?", (user_id,))
    conn.commit()
    conn.close()

def create_order(user_id, total):
    conn = get_conn()
    c = conn.cursor()
    c.execute("INSERT INTO orders (user_id,total,created_at) VALUES (?,?,?)",
              (user_id, total, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()

# ----------------- UI SCREENS -----------------
class LoginScreen(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def do_login(self):
        usr = self.username.text.strip()
        pwd = self.password.text.strip()
        if not usr or not pwd:
            Popup(title="Erro", content=Label(text="Preencha usuário e senha"), size_hint=(0.6,0.4)).open()
            return
        user = get_user_by_username(usr)
        if user and user[2] == pwd:
            app = App.get_running_app()
            app.current_user = user[0]  # user id
            app.root.current = "home"
            self.username.text = ""
            self.password.text = ""
        else:
            Popup(title="Erro", content=Label(text="Usuário ou senha incorretos"), size_hint=(0.6,0.4)).open()

class RegisterScreen(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def do_register(self):
        uname = self.ids.username_input.text.strip()
        pwd = self.ids.password_input.text.strip()
        name = self.ids.name_input.text.strip()
        email = self.ids.email_input.text.strip()

        if not uname or not pwd:
            Popup(
                title="Erro",
                content=Label(text="Usuário e senha obrigatórios"),
                size_hint=(0.6, 0.4)
            ).open()
            return

        res = create_user(uname, pwd, name=name, email=email)

        if res:
            Popup(
                title="Sucesso",
                content=Label(text="Conta criada! Faça login."),
                size_hint=(0.6, 0.4)
            ).open()

            # Limpa os campos
            self.ids.username_input.text = ""
            self.ids.password_input.text = ""
            self.ids.name_input.text = ""
            self.ids.email_input.text = ""

        # Vai para a tela de login
            self.manager.current = "login"
        else:
            Popup(
                title="Erro",
                content=Label(text="Usuário já existe"),
                size_hint=(0.6, 0.4)
            ).open()

class HomeScreen(Screen):
    products_list = ObjectProperty(None)
    search_input = ObjectProperty(None)

    def on_pre_enter(self):
        self.load_products()

    def load_products(self, order_by="id", query=None):
        self.products_list.clear_widgets()
        rows = list_products(order_by=order_by)
        if query:
            q = query.lower()
            rows = [r for r in rows if q in r[1].lower() or q in (r[2] or "").lower()]
        for p in rows:
            item = ProductItem(pid=p[0], title=p[1], price=p[3], image=p[5])
            self.products_list.add_widget(item)

    def do_search(self):
        q = self.search_input.text.strip()
        self.load_products(query=q)

class ProductItem(BoxLayout):
    pid = NumericProperty()
    title = StringProperty()
    price = NumericProperty()
    image = StringProperty()

    def view_detail(self):
        app = App.get_running_app()
        app.root.get_screen("detail").load_product(self.pid)
        app.root.current = "detail"

class DetailScreen(Screen):
    title = ObjectProperty(None)
    desc = ObjectProperty(None)
    price = ObjectProperty(None)
    image = ObjectProperty(None)
    qty = ObjectProperty(None)
    current_pid = None

    def load_product(self, pid):
        p = get_product(pid)
        if not p:
            return
        self.current_pid = p[0]
        self.title.text = p[1]
        self.desc.text = p[2] or ""
        self.price.text = f"R$ {p[3]:.2f}"
        self.image.source = p[5] if p[5] else ""
        self.qty.text = "1"

    def add_to_cart(self):
        app = App.get_running_app()
        if not app.current_user:
            Popup(title="Erro", content=Label(text="Faça login para adicionar ao carrinho"), size_hint=(0.6,0.4)).open()
            return
        q = int(self.qty.text) if self.qty.text.isdigit() else 1
        add_to_cart(app.current_user, self.current_pid, q)
        Popup(title="Sucesso", content=Label(text="Adicionado ao carrinho"), size_hint=(0.6,0.4)).open()

    def buy_now(self):
        app = App.get_running_app()
        if not app.current_user:
            Popup(title="Erro", content=Label(text="Faça login para comprar"), size_hint=(0.6,0.4)).open()
            return
        # create order for this single product (simple)
        p = get_product(self.current_pid)
        total = p[3] * (int(self.qty.text) if self.qty.text.isdigit() else 1)
        create_order(app.current_user, total)
        Popup(title="Sucesso", content=Label(text=f"Compra finalizada. Total R$ {total:.2f}"), size_hint=(0.6,0.4)).open()

class CartScreen(Screen):
    cart_list = ObjectProperty(None)
    total_label = ObjectProperty(None)

    def on_pre_enter(self):
        self.load_cart()

    def load_cart(self):
        self.cart_list.clear_widgets()
        app = App.get_running_app()
        if not app.current_user:
            return
        rows = get_cart(app.current_user)
        total = 0
        for r in rows:
            # r: cart.id, prod.id, prod.title, prod.price, qty, image
            cart_id, prod_id, title, price, qty, image = r
            item = CartItem(cart_id=cart_id, title=title, price=price, qty=qty, image=image)
            self.cart_list.add_widget(item)
            total += price * qty
        self.total_label.text = f"Total: R$ {total:.2f}"

    def finalize(self):
        app = App.get_running_app()
        if not app.current_user:
            Popup(title="Erro", content=Label(text="Faça login para finalizar compra"), size_hint=(0.6,0.4)).open()
            return
        rows = get_cart(app.current_user)
        if not rows:
            Popup(title="Carrinho", content=Label(text="Carrinho vazio"), size_hint=(0.6,0.4)).open()
            return
        total = sum(r[3]*r[4] for r in rows)
        create_order(app.current_user, total)
        clear_cart(app.current_user)
        Popup(title="Parabéns", content=Label(text=f"Compra finalizada! Total R$ {total:.2f}"), size_hint=(0.6,0.4)).open()
        self.load_cart()

class CartItem(BoxLayout):
    cart_id = NumericProperty()
    title = StringProperty()
    price = NumericProperty()
    qty = NumericProperty()
    image = StringProperty()

    def remove(self):
        remove_cart_item(self.cart_id)
        App.get_running_app().root.get_screen("cart").load_cart()

class ProfileScreen(Screen):
    name = ObjectProperty(None)
    email = ObjectProperty(None)
    cpf = ObjectProperty(None)
    rg = ObjectProperty(None)
    cep = ObjectProperty(None)
    endereco = ObjectProperty(None)
    avatar = ObjectProperty(None)
    password = ObjectProperty(None)
    username_label = ObjectProperty(None)
    uid = None

    def on_pre_enter(self):
        app = App.get_running_app()
        uid = app.current_user
        if not uid:
            app.root.current = "login"
            return
        self.uid = uid
        user = get_user_by_id(uid)
        # user tuple: (id,username,password,name,email,cpf,rg,cep,endereco,avatar)
        self.username_label.text = user[1]
        self.name.text = user[3] or ""
        self.email.text = user[4] or ""
        self.cpf.text = user[5] or ""
        self.rg.text = user[6] or ""
        self.cep.text = user[7] or ""
        self.endereco.text = user[8] or ""
        self.avatar.source = user[9] or ""

    def save_profile(self):
        update_user(
            self.uid,
            self.name.text,
            self.email.text,
            self.password.text or get_user_by_id(self.uid)[2],  # keep old pwd if empty
            self.cpf.text,
            self.rg.text,
            self.cep.text,
            self.endereco.text,
            self.avatar.source or None
        )
        Popup(title="Sucesso", content=Label(text="Perfil atualizado"), size_hint=(0.6,0.4)).open()

class LogoutScreen(Screen):
    def on_enter(self):
        App.get_running_app().current_user = None
        App.get_running_app().root.current = "login"

# ----------------- APP -----------------
class ShopApp(App):
    current_user = None

    def build(self):
        criar_banco()
        seed_products()
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(DetailScreen(name="detail"))
        sm.add_widget(CartScreen(name="cart"))
        sm.add_widget(ProfileScreen(name="profile"))
        sm.add_widget(LogoutScreen(name="logout"))
        return sm

if __name__ == "__main__":
    ShopApp().run()

# tens uns bugs no avatar, mas tá ok
# falta melhorar o visual
# falta melhorar a usabilidade
# falta melhorar a segurança (senha em texto puro, etc)
# falta melhorar a lógica (ex: não checa estoque, etc)
# falta melhorar o código (ex: repetição, etc)
# mas tá ok para fins didáticos
