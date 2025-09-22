
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Age Verification Application - Professional Refactored Version

This is an enhanced version demonstrating professional software development practices:
- Clean code architecture with single responsibility principle
- Comprehensive method decomposition for maintainability
- Professional naming conventions and documentation
- Separation of UI creation, validation, and business logic
- Enhanced error handling and user experience

Improvements over the basic version:
- Modular method structure for better code organization
- Clear separation between UI setup and business logic
- Enhanced validation with better user feedback
- Professional documentation and code comments

Purpose: Educational example of clean code and professional development
Complexity: Intermediate-Advanced
Concepts: Clean architecture, method decomposition, professional practices
"""

# Import Kivy framework components
from kivy.app import App                # Base application class
from kivy.uix.boxlayout import BoxLayout  # Linear layout container
from kivy.uix.label import Label        # Text display widget
from kivy.uix.button import Button      # Interactive button widget
from kivy.uix.textinput import TextInput  # Text input field widget
from kivy.core.window import Window     # Window management for theming
from kivy.uix.image import Image        # Image display widget


class Colors:
    """
    Centralized Color Palette for Retro Neon Theme
    
    This class provides a consistent color scheme across the entire application.
    Using a centralized palette makes theme changes easier and ensures visual
    consistency throughout the user interface.
    
    Color Values:
        All colors are defined as RGBA tuples with values from 0.0 to 1.0
        Following the retro neon aesthetic with high contrast and vibrant colors
    """
    BACKGROUND = (0, 0, 0, 1)          # Terminal-style black background
    TITLE_COLOR = (0, 1, 0.6, 1)       # Bright neon green for titles
    BUTTON_COLOR = (1, 0.2, 0.8, 1)    # Hot pink neon for buttons
    ERROR_COLOR = (1, 0, 0, 1)         # Classic red for error states
    WARNING_COLOR = (1, 1, 0, 1)       # Bright yellow for warnings
    INFO_COLOR = (0.3, 0.8, 1, 1)      # Electric blue for information
    SUCCESS_COLOR = (0, 1, 0, 1)       # Bright green for success states


class AgeVerificationForm(BoxLayout):
    """
    Professional Age Verification Form Component
    
    This class demonstrates advanced software engineering principles:
    - Single Responsibility Principle: Each method has one clear purpose
    - Encapsulation: UI setup is broken into logical, manageable pieces
    - Maintainability: Code is organized for easy modification and extension
    - Readability: Clear method names that describe their purpose
    
    The form provides comprehensive age verification with:
    - Real-time input validation
    - Visual feedback with icons and colors
    - Age-based categorization
    - Professional error handling
    
    Attributes:
        All UI components are created and managed through private methods
        following the principle of controlled access and encapsulation.
    """
    
    def __init__(self, **kwargs):
        """
        Initialize the age verification form with professional structure.
        
        Uses the Template Method pattern where the main structure is defined
        here and specific implementations are delegated to specialized methods.
        """
        # Initialize parent BoxLayout with vertical arrangement
        super().__init__(
            orientation="vertical",  # Stack components vertically
            padding=20,             # 20px padding around the form
            spacing=15,             # 15px spacing between elements
            **kwargs                # Pass through additional arguments
        )
        
        # Delegate UI setup to organized helper methods
        self._setup_ui_components()
    
    def _setup_ui_components(self):
        """
        Master method for orchestrating UI component creation.
        
        This method follows the Template Method pattern, defining the
        overall structure while delegating specific implementations
        to specialized private methods.
        
        Benefits:
        - Clear overview of the complete UI structure
        - Easy to modify the order or add new components
        - Each component creation is isolated and testable
        """
        self._create_title_label()     # Application title
        self._create_name_input()      # User name input field
        self._create_age_input()       # Age input with validation
        self._create_verify_button()   # Verification action button
        self._create_message_label()   # Dynamic feedback display
        self._create_feedback_icon()   # Visual status indicator
    
    def _create_title_label(self):
        """
        Creates the application title with retro styling.
        
        Demonstrates proper widget configuration with:
        - Appropriate sizing for visual hierarchy
        - Theme-consistent coloring
        - Professional text formatting
        """
        self.title_label = Label(
            text="IDADE - Verificador de Faixa Etária",  # Clear, descriptive title
            font_size=28,              # Large font for visual prominence
            bold=True,                 # Bold styling for emphasis
            color=Colors.TITLE_COLOR,  # Neon green theme color
            size_hint=(1, 0.2)         # Full width, 20% of container height
        )
        self.add_widget(self.title_label)
    
    def _create_name_input(self):
        """
        Creates the name input field with terminal aesthetics.
        
        Features:
        - Placeholder text for user guidance
        - Terminal-style black background
        - Neon green text for visibility
        - Hot pink cursor for visual appeal
        """
        self.name_input = TextInput(
            hint_text="Digite seu nome...",        # User guidance placeholder
            multiline=False,                     # Single line input only
            size_hint=(1, 0.15),                 # Full width, 15% height
            background_color=(0, 0, 0, 1),       # Terminal black background
            foreground_color=Colors.SUCCESS_COLOR,  # Neon green text
            cursor_color=Colors.BUTTON_COLOR,     # Hot pink cursor
            font_size=18                         # Readable font size
        )
        self.add_widget(self.name_input)
    
    def _create_age_input(self):
        """
        Creates the age input field with built-in validation.
        
        Advanced features:
        - Integer-only input filtering (prevents non-numeric input)
        - Real-time validation on Enter key press
        - Consistent terminal styling
        - Event binding for immediate feedback
        """
        self.age_input = TextInput(
            hint_text="Digite sua idade...",       # User guidance placeholder
            multiline=False,                     # Single line input only
            input_filter="int",                  # Only allow integer input
            size_hint=(1, 0.15),                 # Full width, 15% height
            background_color=(0, 0, 0, 1),       # Terminal black background
            foreground_color=Colors.SUCCESS_COLOR,  # Neon green text
            cursor_color=Colors.BUTTON_COLOR,     # Hot pink cursor
            font_size=18                         # Readable font size
        )
        # Bind Enter key to trigger real-time validation
        self.age_input.bind(on_text_validate=self._validate_input)
        self.add_widget(self.age_input)
    
    def _create_verify_button(self):
        """
        Creates the verification button with neon styling.
        
        Professional button configuration:
        - Removes default button background for custom styling
        - Uses theme-consistent hot pink color
        - High contrast black text for readability
        - Event binding for age verification logic
        """
        self.verify_button = Button(
            text="VERIFICAR",              # Clear action label
            size_hint=(1, 0.2),          # Full width, 20% height
            background_normal='',         # Remove default background
            background_color=Colors.BUTTON_COLOR,  # Hot pink neon color
            font_size=20,                # Large, readable font
            color=(0, 0, 0, 1)           # Black text for contrast
        )
        # Bind button press to verification logic
        self.verify_button.bind(on_press=self._verify_age)
        self.add_widget(self.verify_button)
    
    def _create_message_label(self):
        """
        Creates the dynamic message display area.
        
        Advanced label configuration:
        - Markup support for colored text within messages
        - Proper text centering with size binding
        - Large display area for comprehensive feedback
        - Initially empty, populated by validation/verification
        """
        self.message_label = Label(
            text="",                    # Initially empty text
            font_size=20,              # Readable font size
            halign="center",           # Center-align text horizontally
            valign="middle",           # Center-align text vertically
            size_hint=(1, 0.3),        # Full width, 30% height
            color=Colors.SUCCESS_COLOR,  # Default to success color
            markup=True                # Enable color markup in text
        )
        # Bind size changes to ensure proper text centering
        self.message_label.bind(size=self._adjust_text_wrapping)
        self.add_widget(self.message_label)
    
    def _create_feedback_icon(self):
        """
        Creates the visual feedback icon for status indication.
        
        Features:
        - Fixed size for consistent appearance
        - Initially invisible (opacity controlled by validation)
        - Supports different icon types (error, warning, success, info)
        """
        self.feedback_icon = Image(
            size_hint=(None, None),    # Fixed size, not relative
            size=(50, 50)              # 50x50 pixel icon
        )
        self.add_widget(self.feedback_icon)
    
    def _adjust_text_wrapping(self, instance, value):
        """
        Callback method to ensure proper text centering in labels.
        
        This method is crucial for proper text alignment in Kivy labels.
        Without setting text_size, the halign and valign properties
        don't work as expected.
        
        Args:
            instance (Label): The label widget whose size changed
            value (tuple): The new size as (width, height)
        
        Technical Note:
            Kivy needs to know the text rendering boundaries to properly
            apply horizontal and vertical alignment. This binding ensures
            the text area matches the widget size.
        """
        instance.text_size = instance.size
    
    def _validate_input(self, instance):
        """
        Performs real-time validation of user input fields.
        
        This method provides immediate feedback to users without requiring
        them to click the verify button first. It demonstrates proactive
        user experience design.
        
        Args:
            instance (TextInput): The input widget that triggered validation
                                 (typically through Enter key press)
        
        Validation Process:
            1. Check if name field contains actual content
            2. Check if age field contains actual content
            3. Provide immediate visual feedback for any issues
            4. Clear feedback if all validations pass
        """
        # Validate name field - check for empty or whitespace-only input
        if not self.name_input.text.strip():
            self._update_message_display(
                "[color=ff0000]ERRO: Nome vazio![/color]", 
                Colors.ERROR_COLOR, 
                "error.png"
            )
        # Validate age field - check for empty input
        elif not self.age_input.text.strip():
            self._update_message_display(
                "[color=ff0000]ERRO: Idade vazia![/color]", 
                Colors.ERROR_COLOR, 
                "error.png"
            )
        else:
            # Clear any previous error messages if validation passes
            self._update_message_display("", (0, 0, 0, 1), "")
    
    def _update_message_display(self, message, color, icon_path):
        """
        Centralized method for updating all user feedback elements.
        
        This method ensures consistent feedback presentation across
        all validation and verification scenarios. It demonstrates
        the DRY (Don't Repeat Yourself) principle.
        
        Args:
            message (str): The text to display (supports Kivy markup)
            color (tuple): RGBA color tuple for the message text
            icon_path (str): File path to the feedback icon image
        
        Features:
            - Supports markup for rich text formatting
            - Coordinates text and icon feedback
            - Handles icon visibility automatically
            - Maintains consistent styling across all messages
        """
        # Update message text with markup support
        self.message_label.text = message
        
        # Update message color for theme consistency
        self.message_label.color = color
        
        # Update feedback icon source
        self.feedback_icon.source = icon_path
        
        # Show icon only if path is provided, hide otherwise
        # This provides clean UI when no icon feedback is needed
        self.feedback_icon.opacity = 1 if icon_path else 0
    
    def _verify_age(self, instance):
        """
        Main age verification workflow with comprehensive validation.
        
        This method orchestrates the complete age verification process:
        1. Input extraction and sanitization
        2. Comprehensive validation
        3. Age parsing with error handling
        4. Age categorization and feedback
        
        Args:
            instance (Button): The button widget that triggered verification
        
        Process Flow:
            1. Extract user inputs and remove whitespace
            2. Validate all required fields are filled
            3. Parse age as integer with error handling
            4. Delegate to age categorization logic
        """
        # Extract and sanitize user inputs
        name = self.name_input.text.strip()      # Remove leading/trailing whitespace
        age_text = self.age_input.text.strip()   # Remove leading/trailing whitespace
        
        # Comprehensive input validation
        if not name or not age_text:
            self._update_message_display(
                "[color=ff0000]Por favor, preencha todos os campos.[/color]", 
                Colors.ERROR_COLOR, 
                "error.png"
            )
            return  # Exit early if validation fails
        
        # Age parsing with robust error handling
        try:
            age = int(age_text)
        except ValueError:
            # This should rarely happen due to input_filter="int",
            # but we handle it for completeness and robustness
            self._update_message_display(
                "[color=ff0000]Digite apenas números.[/color]", 
                Colors.ERROR_COLOR, 
                "error.png"
            )
            return
        
        # Delegate to age categorization logic
        self._determine_age_category(name, age)
    
    def _determine_age_category(self, name, age):
        """
        Determines age category and displays themed feedback message.
        
        This method implements the business logic for age categorization
        with professionally styled feedback messages. Each category has
        its own color theme and icon for enhanced user experience.
        
        Args:
            name (str): The user's name for personalized messages
            age (int): The user's age for category determination
        
        Age Categories:
            - Children (< 13): Yellow warning style
            - Adolescents (13-17): Magenta warning style
            - Young Adults (18-29): Green success style
            - Adults (30-59): Cyan success style
            - Seniors (60+): Blue info style with friendly emoji
        
        Design Notes:
            - Each category uses thematically appropriate colors
            - Messages are personalized with the user's name
            - Icons provide additional visual feedback
            - Friendly tone maintains positive user experience
        """
        if age < 13:
            # Children category - yellow warning theme
            self._update_message_display(
                f"[color=ffff00]Olá, {name}! Você é uma CRIANÇA.[/color]", 
                Colors.WARNING_COLOR, 
                "warning.png"
            )
        elif age < 18:
            # Adolescent category - magenta warning theme
            self._update_message_display(
                f"[color=ff00ff]Olá, {name}! Você é um ADOLESCENTE.[/color]", 
                Colors.WARNING_COLOR, 
                "warning.png"
            )
        elif age < 30:
            # Young adult category - green success theme
            self._update_message_display(
                f"[color=00ff00]Olá, {name}! Você é um JOVEM ADULTO.[/color]", 
                Colors.SUCCESS_COLOR, 
                "success.png"
            )
        elif age < 60:
            # Adult category - cyan success theme
            self._update_message_display(
                f"[color=00ffff]Olá, {name}! Você é um ADULTO.[/color]", 
                Colors.SUCCESS_COLOR, 
                "success.png"
            )
        else:
            # Senior category - blue info theme with friendly touch
            self._update_message_display(
                f"[color=00aaff]Olá, {name}! Você é um IDOSO :D[/color]", 
                Colors.INFO_COLOR, 
                "info.png"
            )


class AgeVerificationApp(App):
    """
    Professional Age Verification Application
    
    This application demonstrates advanced Kivy development practices:
    - Clean code architecture with proper separation of concerns
    - Professional documentation and code organization
    - Comprehensive user experience design
    - Robust error handling and validation
    - Consistent theming and visual design
    
    The app serves as an educational example of how to structure
    larger Kivy applications with maintainable, professional code.
    """
    
    def build(self):
        """
        Builds the application with professional theming and structure.
        
        This method demonstrates proper application initialization:
        - Sets global window theming
        - Returns the main application widget
        - Maintains clean separation between app and UI logic
        
        Returns:
            AgeVerificationForm: The main application widget containing
                               all functionality and user interface
        """
        # Set global window background to match retro terminal theme
        Window.clearcolor = Colors.BACKGROUND
        
        # Return the main form widget with all functionality
        return AgeVerificationForm()


# Application Entry Point
if __name__ == "__main__":
    """
    Professional application entry point.
    
    This demonstrates proper Python application structure with:
    - Conditional execution (only when run directly)
    - Clear application instantiation and startup
    - Professional documentation
    
    The application showcases:
    - Advanced input validation techniques
    - Professional code organization patterns
    - Comprehensive user experience design
    - Robust error handling strategies
    - Clean architecture principles
    """
    AgeVerificationApp().run()
