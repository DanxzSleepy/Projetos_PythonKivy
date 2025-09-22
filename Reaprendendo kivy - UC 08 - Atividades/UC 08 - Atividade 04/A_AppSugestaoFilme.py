#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Movie Suggestion Application - Advanced UI with Genre Selection

This application demonstrates advanced Kivy concepts:
- Custom widget creation with visual styling (Card widget)
- Data management with structured movie database
- Toggle button groups for exclusive selection
- ScrollView for dynamic content history
- Input validation with age restrictions
- Professional popup dialogs for user feedback
- Image handling with error management
- Complex layout composition (FloatLayout + BoxLayout)

Features:
- Random movie suggestions based on genre selection
- Age-appropriate content filtering
- Visual movie history with images
- Comprehensive input validation
- Professional UI with retro styling

Purpose: Intermediate-Advanced Kivy application with real-world features
Complexity: Intermediate-Advanced
Concepts: Custom widgets, data structures, validation, image handling, scrollable content
"""

# Import Python standard library modules
import random  # For random movie selection
import os      # For file path operations

# Import Kivy framework components
from kivy.app import App                    # Base application class
from kivy.uix.boxlayout import BoxLayout    # Linear layout container
from kivy.uix.label import Label            # Text display widget
from kivy.uix.button import Button          # Interactive button widget
from kivy.uix.textinput import TextInput    # Text input field widget
from kivy.core.window import Window         # Window management
from kivy.uix.floatlayout import FloatLayout  # Free-positioning layout
from kivy.graphics import Color, RoundedRectangle  # Graphics primitives for custom styling
from kivy.uix.popup import Popup            # Modal dialog widget
from kivy.uix.scrollview import ScrollView  # Scrollable content container
from kivy.uix.image import Image            # Image display widget
from kivy.uix.gridlayout import GridLayout  # Grid-based layout (imported but not used)
from kivy.uix.togglebutton import ToggleButton  # Toggle button for exclusive selection


class Card(BoxLayout):
    """
    Custom Card Widget with Rounded Rectangle Background
    
    This custom widget demonstrates advanced Kivy graphics programming:
    - Custom background drawing using Canvas instructions
    - Automatic background updates when widget size/position changes
    - Professional visual styling with rounded corners
    
    The Card provides a modern, elevated appearance for containing
    other widgets, similar to Material Design card components.
    
    Technical Implementation:
        - Uses Canvas.before to draw background behind child widgets
        - Binds to size and position changes for dynamic updates
        - Creates rounded rectangle with customizable radius
    """
    
    def __init__(self, **kwargs):
        """
        Initialize the card with custom background graphics.
        
        Sets up the visual styling and event bindings for
        automatic background updates.
        """
        super().__init__(**kwargs)
        
        # Draw custom background using Canvas instructions
        with self.canvas.before:
            # Set background color to dark gray (RGB: 0.05, 0.05, 0.05)
            Color(0.05, 0.05, 0.05, 1)
            
            # Create rounded rectangle background
            # radius=[15] creates rounded corners with 15-pixel radius
            self.bg = RoundedRectangle(
                radius=[15],           # Corner radius in pixels
                pos=self.pos,          # Initial position
                size=self.size         # Initial size
            )
        
        # Bind size and position changes to update background
        # This ensures the background always matches the widget bounds
        self.bind(pos=self.update_bg, size=self.update_bg)

    def update_bg(self, *args):
        """
        Update background graphics when widget size or position changes.
        
        This callback method is automatically called whenever the widget's
        size or position properties change, ensuring the background graphics
        remain synchronized with the widget bounds.
        
        Args:
            *args: Variable arguments passed by Kivy's binding system
                  (instance, new_value) - not used but required by binding
        """
        self.bg.pos = self.pos      # Update background position
        self.bg.size = self.size    # Update background size


class FilmeSorteador:
    """
    Movie Database and Selection Logic Manager
    
    This class encapsulates all movie data and business logic for
    movie selection, demonstrating proper separation of concerns:
    - Data management (movie database)
    - Business logic (selection algorithms, age restrictions)
    - Configuration management (age limits per genre)
    
    The class maintains a structured database of movies organized by genre,
    with each movie containing title, year, and image filename information.
    
    Design Pattern: This follows the Repository pattern for data access
    and the Strategy pattern for selection logic.
    """
    
    def __init__(self):
        """
        Initialize the movie database and age restriction rules.
        
        Sets up the complete movie catalog with genre categorization
        and defines age-appropriate viewing restrictions for each genre.
        """
        # Movie database organized by genre
        # Each entry: (title, year, image_filename)
        self.filmes = {
            "Ação": [
                ("Mad Max: Estrada da Fúria", 2015, "mad_max.jpg"),
                ("John Wick", 2014, "john_wick.jpg"),
                ("Duro de Matar", 1988, "duro_de_matar.jpg"),
                ("Os Vingadores", 2012, "vingadores.jpg"),
                ("Gladiador", 2000, "gladiador.jpg"),
            ],
            "Comédia": [
                ("Superbad", 2007, "superbad.png"),
                ("A Morte Lhe Cai Bem", 1992, "morte_lhe_cai_bem.jpg"),
                ("Os Caça-Fantasmas", 1984, "caca_fantasmas.jpg"),
                ("O Diário de uma Princesa", 2001, "diario_princesa.webp"),
                ("As Branquelas", 2004, "branquelas.jpeg"),
            ],
            "Drama": [
                ("Forrest Gump", 1994, "forrest_gump.jpg"),
                ("O Poderoso Chefão", 1972, "poderoso_chefa.jpg"),
                ("A Lista de Schindler", 1993, "lista_schindler.jpg"),
                ("Clube da Luta", 1999, "clube_luta.jpg"),
                ("O Senhor dos Anéis: O Retorno do Rei", 2003, "senhor_aneis.jpg"),
            ],
            "Ficção Científica": [
                ("Interestelar", 2014, "interestelar.png"),
                ("Blade Runner 2049", 2017, "blade_runner.jpg"),
                ("A Origem", 2010, "origem.jpg"),
                ("Ex Machina", 2014, "ex_machina.webp"),
                ("Matrix", 1999, "matrix.png"),
            ],
            "Animação": [
                ("Toy Story", 1995, "toy_story.webp"),
                ("Procurando Nemo", 2003, "procurando_nemo.jpg"),
                ("O Rei Leão", 1994, "rei_leao.webp"),
                ("Shrek", 2001, "shrek.jpg"),
                ("Divertida Mente", 2015, "divertida_mente.webp"),
            ]
        }

        # Age restriction configuration for content filtering
        # Each genre: (minimum_age, maximum_age)
        self.idade_limite = {
            "Ação": (16, 100),           # Action movies: 16+ (violence content)
            "Comédia": (10, 100),        # Comedy movies: 10+ (mild content)
            "Drama": (12, 100),          # Drama movies: 12+ (mature themes)
            "Ficção Científica": (12, 100),  # Sci-fi movies: 12+ (complex themes)
            "Animação": (0, 100)         # Animation movies: All ages
        }

    def sortear_filme(self, genero):
        """
        Randomly select a movie from the specified genre.
        
        This method implements the core movie selection algorithm,
        providing random suggestions to keep the experience fresh
        and engaging for users.
        
        Args:
            genero (str): The movie genre to select from
                         (must be a key in self.filmes)
        
        Returns:
            tuple or None: Movie information as (title, year, image_filename)
                          Returns None if genre is invalid
        
        Algorithm:
            Uses Python's random.choice() for uniform random selection
            from the available movies in the specified genre.
        """
        if genero in self.filmes:
            return random.choice(self.filmes[genero])
        return None


class FilmeApp(App):
    """
    Advanced Movie Suggestion Application
    
    This application demonstrates professional-level Kivy development with:
    - Complex UI composition using multiple layout types
    - Dynamic content management with scrollable history
    - Advanced input validation with business rule enforcement
    - Image handling with graceful error management
    - Professional popup dialogs for user feedback
    - Toggle button groups for exclusive selection
    - Real-time UI updates based on user interactions
    
    Architecture:
        - Separation of concerns: UI logic, business logic, and data management
        - Event-driven programming with callback methods
        - Defensive programming with comprehensive error handling
        - User experience optimization with visual feedback
    
    Features:
        - Random movie suggestions based on selected genre
        - Age-appropriate content filtering
        - Visual history of suggestions with movie posters
        - Input validation with helpful error messages
        - Professional retro-themed UI design
    """
    
    def build(self):
        """
        Constructs the complete application interface.
        
        This method demonstrates advanced UI composition techniques:
        - Nested layouts for complex interfaces
        - Custom widget integration (Card component)
        - Multiple input types (TextInput, ToggleButton)
        - Dynamic content areas (ScrollView for history)
        - Professional styling with consistent theming
        
        Returns:
            FloatLayout: Root widget containing the entire interface
        """
        # Set global window background to dark theme
        Window.clearcolor = (0.1, 0.1, 0.1, 1)  # Dark gray background
        
        # Initialize movie selection engine
        self.sorteador = FilmeSorteador()

        # Create root layout for free positioning
        root = FloatLayout()

        # Create main card container with centered positioning
        self.card = Card(
            orientation="vertical",          # Stack widgets vertically
            padding=20,                     # 20px padding inside card
            spacing=15,                     # 15px spacing between widgets
            size_hint=(0.9, 0.75),          # 90% width, 75% height of parent
            pos_hint={"center_x": 0.5, "center_y": 0.5}  # Center in parent
        )

        # Application title with retro styling
        self.title_label = Label(
            text=" A.S.F.A. - App de Sugestão de Filmes Aleatórios ",
            font_size=24,                   # Large font for prominence
            bold=True,                      # Bold styling
            color=(0, 1, 0.6, 1),          # Neon green color
            size_hint=(1, 0.2)             # Full width, 20% of card height
        )
        self.card.add_widget(self.title_label)

        # Name input field with terminal styling
        self.name_input = TextInput(
            hint_text="Digite seu nome...",      # User guidance
            multiline=False,                   # Single line input
            size_hint=(1, 0.15),               # Full width, 15% height
            background_color=(0, 0, 0, 1),     # Black terminal background
            foreground_color=(0, 1, 0, 1),     # Green text color
            cursor_color=(1, 0, 1, 1),         # Magenta cursor
            font_size=18                       # Readable font size
        )
        self.card.add_widget(self.name_input)

        # Age input field with matching styling
        self.age_input = TextInput(
            hint_text="Digite sua idade...",     # User guidance
            multiline=False,                   # Single line input
            size_hint=(1, 0.15),               # Full width, 15% height
            background_color=(0, 0, 0, 1),     # Black terminal background
            foreground_color=(0, 1, 0, 1),     # Green text color
            cursor_color=(1, 0, 1, 1),         # Magenta cursor
            font_size=18                       # Readable font size
        )
        self.card.add_widget(self.age_input)

        # Genre selection button group
        # ToggleButton group ensures only one genre can be selected
        self.genre_buttons = BoxLayout(
            size_hint=(1, 0.15),    # Full width, 15% height
            spacing=10              # 10px spacing between buttons
        )
        
        # Define available movie genres
        self.genres = ["Ação", "Comédia", "Drama", "Ficção Científica", "Animação"]
        self.toggle_buttons = {}  # Store button references for state checking

        # Create toggle button for each genre
        for genre in self.genres:
            btn = ToggleButton(
                text=genre,         # Genre name as button text
                group='genres',     # Group name for exclusive selection
                size_hint=(1, 1)    # Equal size within container
            )
            self.toggle_buttons[genre] = btn  # Store reference
            self.genre_buttons.add_widget(btn)

        self.card.add_widget(self.genre_buttons)

        # Main action button for generating movie suggestions
        self.button = Button(
            text=" GERAR FILME ",              # Spaced text for retro feel
            size_hint=(1, 0.2),               # Full width, 20% height
            background_normal='',              # Remove default background
            background_color=(0, 0.8, 0.4, 1),  # Green action color
            font_size=20,                     # Large, readable font
            color=(0, 0, 0, 1)                # Black text for contrast
        )
        # Bind button click to movie suggestion logic
        self.button.bind(on_press=self.sugerir_filme)
        self.card.add_widget(self.button)

        # Clear button for resetting the interface
        self.clear_button = Button(
            text=" LIMPAR ",                  # Spaced text for retro feel
            size_hint=(1, 0.2),               # Full width, 20% height
            background_normal='',              # Remove default background
            background_color=(1, 0, 0, 1),    # Red warning color
            font_size=20,                     # Large, readable font
            color=(1, 1, 1, 1)                # White text for contrast
        )
        # Bind button click to clear functionality
        self.clear_button.bind(on_press=self.limpar_campos)
        self.card.add_widget(self.clear_button)

        # Dynamic message display area with markup support
        self.message_label = Label(
            text="",                    # Initially empty
            font_size=20,              # Readable font size
            halign="center",           # Center-align text horizontally
            valign="middle",           # Center-align text vertically
            size_hint=(1, 0.4),        # Full width, 40% height
            color=(1, 0, 1, 1),        # Magenta neon color
            markup=True                # Enable color/style markup
        )
        # Bind size changes to ensure proper text centering
        self.message_label.bind(size=self.ajustar_texto)
        self.card.add_widget(self.message_label)

        # Scrollable history area for displaying past suggestions
        # Initially hidden (height=0), expands when content is added
        self.history_scroll = ScrollView(
            size_hint=(1, None),    # Full width, fixed height
            height=0                # Initially hidden
        )
        
        # Container for history items with dynamic sizing
        self.history_box = BoxLayout(
            orientation='vertical',      # Stack history items vertically
            size_hint_y=None,           # Fixed height based on content
            spacing=10,                 # 10px spacing between items
            padding=5                   # 5px padding around content
        )
        # Bind minimum height to actual height for proper scrolling
        self.history_box.bind(minimum_height=self.history_box.setter('height'))
        self.history_scroll.add_widget(self.history_box)

        self.card.add_widget(self.history_scroll)

        # Add main card to root layout
        root.add_widget(self.card)
        return root

    def show_popup(self, message):
        """
        Display a modal popup dialog with user feedback message.
        
        This method provides professional user feedback through modal dialogs,
        ensuring important messages are noticed by users. The popup blocks
        interaction with the main interface until dismissed.
        
        Args:
            message (str): The message to display in the popup dialog
        
        Technical Implementation:
            - Creates a modal Popup widget with centered content
            - Uses Label widget for message display
            - Automatically sizes the popup relative to screen size
            - User must click outside or on a button to dismiss
        """
        popup = Popup(
            title='Mensagem',           # Popup window title
            content=Label(text=message),  # Message content as Label
            size_hint=(0.8, 0.4)       # 80% width, 40% height of screen
        )
        popup.open()  # Display the popup

    def ajustar_texto(self, instance, value):
        """
        Callback method to properly align text within labels.
        
        This essential method ensures that text alignment properties
        (halign, valign) work correctly in Kivy labels by setting
        the text rendering area to match the widget size.
        
        Args:
            instance (Label): The label widget whose size changed
            value (tuple): New size as (width, height)
        
        Technical Note:
            Without this binding, halign and valign properties don't
            function properly because Kivy needs explicit text boundaries.
        """
        instance.text_size = instance.size

    def validar_entrada(self, nome, idade_texto, genero):
        """
        Comprehensive input validation with business rule enforcement.
        
        This method implements robust validation logic that ensures:
        - Data integrity (valid name format, numeric age)
        - Business rule compliance (age restrictions per genre)
        - User experience optimization (clear error messages)
        - Security considerations (input sanitization)
        
        Args:
            nome (str): User's name input
            idade_texto (str): User's age input as string
            genero (str or None): Selected movie genre
        
        Returns:
            bool: True if all validation passes, False otherwise
        
        Validation Rules:
            1. Name: Non-empty, max 50 characters, alphanumeric only
            2. Age: Must be valid positive integer
            3. Genre: Must be selected (not None)
            4. Age Restriction: Must meet genre-specific age requirements
        """
        # Name validation: check for content, length, and character set
        if not nome or len(nome) > 50 or not nome.isalnum():
            self.show_popup(
                "ERRO: Digite um nome válido (máx. 50 caracteres, sem caracteres especiais)!"
            )
            return False
        
        # Age validation: check for numeric format and positive value
        if not idade_texto.isdigit() or int(idade_texto) < 0:
            self.show_popup("ERRO: Digite uma idade válida!")
            return False
        
        # Genre selection validation
        if genero is None:
            self.show_popup("ERRO: Selecione um gênero!")
            return False
        
        # Age restriction validation based on genre
        idade = int(idade_texto)
        min_idade, max_idade = self.sorteador.idade_limite[genero]
        
        if idade < min_idade or idade > max_idade:
            self.show_popup(
                f"ERRO: Idade deve estar entre {min_idade} e {max_idade} "
                f"para o gênero {genero}."
            )
            return False
        
        return True  # All validations passed

    def sugerir_filme(self, instance):
        """
        Main movie suggestion workflow with comprehensive features.
        
        This method orchestrates the complete movie suggestion process:
        1. Input extraction and validation
        2. Random movie selection
        3. Visual feedback generation
        4. History management with images
        5. UI updates and user experience enhancements
        
        Args:
            instance (Button): The button that triggered this method
        
        Process Flow:
            1. Extract user inputs (name, age, genre)
            2. Validate all inputs using comprehensive validation
            3. Generate random movie suggestion from selected genre
            4. Display personalized feedback message
            5. Add suggestion to visual history with movie poster
            6. Handle image loading with graceful error management
            7. Update scrollable history area
        """
        # Extract user inputs
        nome = self.name_input.text.strip()     # Remove whitespace from name
        idade_texto = self.age_input.text.strip()  # Remove whitespace from age
        
        # Determine selected genre from toggle button group
        # Uses generator expression to find the pressed button
        genero = next(
            (genre for genre, btn in self.toggle_buttons.items() if btn.state == 'down'), 
            None
        )

        # Validate all inputs before proceeding
        if not self.validar_entrada(nome, idade_texto, genero):
            return  # Exit if validation fails

        # Generate random movie suggestion
        filme_escolhido = self.sorteador.sortear_filme(genero)
        
        if filme_escolhido:
            # Display personalized suggestion message with rich text formatting
            self.message_label.text = (
                f"[b][color=00ff99]Olá, {nome}![/color][/b]\n"
                f"Sua sugestão de filme de {genero} é:\n"
                f"[color=ff00ff]{filme_escolhido[0]} ({filme_escolhido[1]})[/color]"
            )
        
            # Add suggestion to visual history with movie poster
            # Construct image path relative to script location
            img_path = os.path.join(os.path.dirname(__file__), filme_escolhido[2])
        
            # Image handling with graceful error management
            if not os.path.exists(img_path):
                # Debug output for missing images
                print(f"ERRO: Arquivo não encontrado: {img_path}")
                
                # Add text-only history entry when image is missing
                self.history_box.add_widget(Label(
                    text=f"{nome} sugeriu: {filme_escolhido[0]} ({filme_escolhido[1]}) - [Imagem não encontrada]",
                    color=(1, 1, 1, 1),      # White text
                    size_hint_y=None,        # Fixed height
                    height=30                # 30 pixels height
                ))
            else:
                # Debug output for successful image loading
                print(f"Imagem encontrada: {img_path}")
                
                # Create image widget with movie poster
                img = Image(
                    source=img_path,         # Movie poster image file
                    size_hint=(1, None),     # Full width, fixed height
                    height=200,              # 200 pixels height
                    allow_stretch=True       # Allow image stretching/scaling
                )
                
                # Create descriptive label for the suggestion
                label = Label(
                    text=f"{nome} sugeriu: {filme_escolhido[0]} ({filme_escolhido[1]})",
                    color=(1, 1, 1, 1),      # White text
                    size_hint_y=None,        # Fixed height
                    height=30                # 30 pixels height
                )
                
                # Add both label and image to history
                self.history_box.add_widget(label)
                self.history_box.add_widget(img)

            # Expand ScrollView to show history (max 300px height)
            self.history_scroll.height = min(300, self.history_box.height)
        
            # Auto-scroll to the latest entry (first child due to vertical layout)
            self.history_scroll.scroll_to(self.history_box.children[0])

    def limpar_campos(self, instance):
        """
        Reset all form fields and clear application state.
        
        This method provides a complete reset functionality that:
        - Clears all user input fields
        - Resets button states to default
        - Clears feedback messages
        - Removes suggestion history
        - Returns the interface to initial state
        
        Args:
            instance (Button): The clear button that triggered this method
        
        UI Reset Operations:
            1. Clear text input fields (name and age)
            2. Reset all toggle buttons to unpressed state
            3. Clear the main message display
            4. Remove all items from suggestion history
            5. Reset history scroll area height
        """
        # Clear text input fields
        self.name_input.text = ""
        self.age_input.text = ""
        
        # Reset all toggle buttons to normal (unpressed) state
        for btn in self.toggle_buttons.values():
            btn.state = 'normal'
        
        # Clear the main feedback message
        self.message_label.text = ""
        
        # Clear the suggestion history
        self.history_box.clear_widgets()
        
        # Reset history scroll area height to hidden
        self.history_scroll.height = 0


# Application Entry Point
if __name__ == "__main__":
    """
    Professional application entry point.
    
    This demonstrates a complete, production-ready Kivy application with:
    - Advanced UI composition and layout management
    - Professional input validation and error handling
    - Dynamic content management with scrollable history
    - Image handling with graceful error management
    - Professional user experience design
    - Clean code architecture with separation of concerns
    
    Key Features Demonstrated:
        - Custom widget creation (Card component)
        - Toggle button groups for exclusive selection
        - ScrollView for dynamic content
        - Professional popup dialogs
        - Rich text markup for styled messages
        - File system operations with error handling
        - Event-driven programming patterns
    """
    FilmeApp().run()
