#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Age Access Verification Application - Retro Neon Style

This application demonstrates:
- Advanced input validation and error handling
- Custom color theming with retro neon aesthetics
- Age-based categorization logic
- Visual feedback with icons and colored messages
- Professional UI styling with consistent design patterns

Purpose: Age verification with enhanced user experience
Complexity: Intermediate
Concepts: Input validation, theming, conditional logic, visual feedback
"""

# Import Kivy framework components
from kivy.app import App                # Base application class
from kivy.uix.boxlayout import BoxLayout  # Linear layout container
from kivy.uix.label import Label        # Text display widget
from kivy.uix.button import Button      # Interactive button widget
from kivy.uix.textinput import TextInput  # Text input field widget
from kivy.core.window import Window     # Window management for global styling
from kivy.uix.image import Image        # Image display widget for feedback icons


class Colors:
    """
    Retro Neon Color Palette Configuration
    
    This class defines a consistent color scheme inspired by 80s neon aesthetics.
    Using a centralized color palette ensures visual consistency and makes
    theme changes easier to implement across the entire application.
    
    Each color is defined as an RGBA tuple (Red, Green, Blue, Alpha)
    where values range from 0.0 to 1.0.
    """
    BACKGROUND = (0, 0, 0, 1)      # Terminal-style black background
    TITLE_COLOR = (0, 1, 0.6, 1)   # Bright neon green for titles
    BUTTON_COLOR = (1, 0.2, 0.8, 1)  # Hot pink neon for interactive elements
    ERROR_COLOR = (1, 0, 0, 1)     # Classic red for errors
    WARNING_COLOR = (1, 1, 0, 1)   # Bright yellow for warnings
    INFO_COLOR = (0.3, 0.8, 1, 1)  # Electric blue for information
    SUCCESS_COLOR = (0, 1, 0, 1)   # Bright green for success states


class AgeForm(BoxLayout):
    """
    Custom Age Verification Form Widget
    
    This widget encapsulates all the age verification functionality
    in a reusable component with retro neon styling. It demonstrates
    advanced form validation, visual feedback, and user experience design.
    
    Attributes:
        title_label (Label): Application title with neon styling
        name_input (TextInput): User name input field
        age_input (TextInput): Age input field with integer filtering
        button (Button): Verification trigger button
        message_label (Label): Dynamic feedback message display
        feedback_icon (Image): Visual feedback icon
    """
    
    def __init__(self, **kwargs):
        """
        Initialize the age verification form with retro neon styling.
        
        Creates a vertical layout with terminal-inspired aesthetics
        and comprehensive input validation.
        """
        # Initialize parent BoxLayout with vertical orientation
        super().__init__(
            orientation="vertical",  # Stack widgets vertically
            padding=20,             # 20px padding around the form
            spacing=15,             # 15px spacing between elements
            **kwargs                # Pass through any additional arguments
        )

        # Application title with retro terminal styling
        self.title_label = Label(
            text=" IDADE - Verificador de Faixa Etária ",  # Spaced title for retro feel
            font_size=28,              # Large, prominent font
            bold=True,                 # Bold for emphasis
            color=Colors.TITLE_COLOR,  # Neon green color
            size_hint=(1, 0.2)         # Full width, 20% height
        )
        self.add_widget(self.title_label)

        # Name input field with terminal aesthetics
        self.name_input = TextInput(
            hint_text="Digite seu nome...",        # User guidance placeholder
            multiline=False,                     # Single line input
            size_hint=(1, 0.15),                 # Full width, 15% height
            background_color=(0, 0, 0, 1),       # Black terminal background
            foreground_color=Colors.SUCCESS_COLOR,  # Green text color
            cursor_color=Colors.BUTTON_COLOR,     # Pink cursor for visibility
            font_size=18                         # Readable font size
        )
        self.add_widget(self.name_input)

        # Age input field with integer filtering and validation
        self.age_input = TextInput(
            hint_text="Digite sua idade...",       # User guidance placeholder
            multiline=False,                     # Single line input
            input_filter="int",                  # Only allow integer input
            size_hint=(1, 0.15),                 # Full width, 15% height
            background_color=(0, 0, 0, 1),       # Black terminal background
            foreground_color=Colors.SUCCESS_COLOR,  # Green text color
            cursor_color=Colors.BUTTON_COLOR,     # Pink cursor for visibility
            font_size=18                         # Readable font size
        )
        # Bind Enter key to trigger validation
        self.age_input.bind(on_text_validate=self.validate_input)
        self.add_widget(self.age_input)

        # Verification button with neon styling
        self.button = Button(
            text=" VERIFICAR ",           # Spaced text for retro feel
            size_hint=(1, 0.2),         # Full width, 20% height
            background_normal='',        # Remove default button background
            background_color=Colors.BUTTON_COLOR,  # Hot pink neon color
            font_size=20,               # Large, readable font
            color=(0, 0, 0, 1)          # Black text for contrast against pink
        )
        # Bind button click to verification method
        self.button.bind(on_press=self.verify_age)
        self.add_widget(self.button)

        # Dynamic message display with markup support
        self.message_label = Label(
            text="",                    # Initially empty
            font_size=20,              # Readable font size
            halign="center",           # Center-align text horizontally
            valign="middle",           # Center-align text vertically
            size_hint=(1, 0.3),        # Full width, 30% height
            color=Colors.SUCCESS_COLOR,  # Default to success color
            markup=True                # Enable color markup in text
        )
        # Bind size changes to text alignment adjustment
        self.message_label.bind(size=self.adjust_text)
        self.add_widget(self.message_label)

        # Feedback icon for visual status indication
        self.feedback_icon = Image(
            size_hint=(None, None),    # Fixed size, not relative
            size=(50, 50)              # 50x50 pixel icon
        )
        self.add_widget(self.feedback_icon)

    def adjust_text(self, instance, value):
        """
        Callback method to properly center text within the label.
        
        This method is automatically called when the label's size changes.
        It ensures that halign and valign properties work correctly by
        setting the text_size to match the widget size.
        
        Args:
            instance (Label): The label widget whose size changed
            value (tuple): The new size as (width, height)
        
        Note:
            Without this binding, halign and valign don't work properly
            because Kivy needs to know the text rendering area boundaries.
        """
        instance.text_size = instance.size

    def validate_input(self, instance):
        """
        Real-time input validation triggered by Enter key or programmatically.
        
        This method provides immediate feedback to users about input validity
        without requiring them to click the verification button first.
        
        Args:
            instance (TextInput): The input widget that triggered validation
        
        Validation Rules:
            1. Name field must not be empty or only whitespace
            2. Age field must not be empty
            3. Age field must contain valid integer (handled by input_filter)
        """
        # Check if name field is empty or contains only whitespace
        if not self.name_input.text.strip():
            self.update_message(
                "[color=ff0000]ERRO: Nome vazio![/color]", 
                Colors.ERROR_COLOR, 
                "error.png"
            )
        # Check if age field is empty
        elif not self.age_input.text.strip():
            self.update_message(
                "[color=ff0000]ERRO: Idade vazia![/color]", 
                Colors.ERROR_COLOR, 
                "error.png"
            )
        else:
            # Clear any previous error messages if validation passes
            self.update_message("", (0, 0, 0, 1), "")

    def update_message(self, message, color, icon_path):
        """
        Centralized method for updating user feedback display.
        
        This helper method ensures consistent message formatting and
        visual feedback across all validation and verification scenarios.
        
        Args:
            message (str): The text to display (supports markup)
            color (tuple): RGBA color tuple for the message text
            icon_path (str): Path to feedback icon image file
        
        Features:
            - Supports markup for colored text within messages
            - Updates both text and visual icon feedback
            - Handles icon visibility based on whether path is provided
        """
        self.message_label.text = message
        self.message_label.color = color
        self.feedback_icon.source = icon_path
        # Show icon only if path is provided, hide otherwise
        self.feedback_icon.opacity = 1 if icon_path else 0

    def verify_age(self, instance):
        """
        Main age verification logic with comprehensive validation and categorization.
        
        This method implements the core business logic for age verification,
        including input validation, error handling, and age-based categorization
        with appropriate visual feedback.
        
        Args:
            instance (Button): The button widget that triggered verification
        
        Process Flow:
            1. Extract and sanitize user inputs
            2. Validate that all required fields are filled
            3. Validate that age is a valid integer
            4. Categorize user based on age ranges
            5. Display appropriate feedback with themed colors
        
        Age Categories:
            - Children: < 13 years
            - Adolescents: 13-17 years
            - Young Adults: 18-29 years
            - Adults: 30-59 years
            - Seniors: 60+ years
        """
        # Extract and sanitize user inputs
        nome = self.name_input.text.strip()      # Remove whitespace from name
        idade_texto = self.age_input.text.strip()  # Remove whitespace from age

        # Comprehensive input validation
        if not nome or not idade_texto:
            self.update_message(
                "[color=ff0000]Por favor, preencha todos os campos.[/color]", 
                Colors.ERROR_COLOR, 
                "error.png"
            )
            return  # Exit early if validation fails

        # Age parsing with error handling
        try:
            idade = int(idade_texto)
        except ValueError:
            # This shouldn't happen due to input_filter="int", but better safe than sorry
            self.update_message(
                "[color=ff0000]Digite apenas números.[/color]", 
                Colors.ERROR_COLOR, 
                "error.png"
            )
            return

        # Age-based categorization with retro-styled messages
        if idade < 13:
            # Children category - yellow warning style
            self.update_message(
                f"[color=ffff00]Olá, {nome}! Você é uma CRIANÇA.[/color]", 
                Colors.WARNING_COLOR, 
                "warning.png"
            )
        elif idade < 18:
            # Adolescent category - magenta warning style
            self.update_message(
                f"[color=ff00ff]Olá, {nome}! Você é um ADOLESCENTE.[/color]", 
                Colors.WARNING_COLOR, 
                "warning.png"
            )
        elif idade < 30:
            # Young adult category - green success style
            self.update_message(
                f"[color=00ff00]Olá, {nome}! Você é um JOVEM ADULTO.[/color]", 
                Colors.SUCCESS_COLOR, 
                "success.png"
            )
        elif idade < 60:
            # Adult category - cyan success style
            self.update_message(
                f"[color=00ffff]Olá, {nome}! Você é um ADULTO.[/color]", 
                Colors.SUCCESS_COLOR, 
                "success.png"
            )
        else:
            # Senior category - blue info style with friendly emoji
            self.update_message(
                f"[color=00aaff]Olá, {nome}! Você é um IDOSO :D[/color]", 
                Colors.INFO_COLOR, 
                "info.png"
            )


class IdadeApp(App):
    """
    Main Age Verification Application
    
    This app demonstrates advanced Kivy concepts including:
    - Custom theming with consistent color palettes
    - Input validation and error handling
    - Visual feedback with icons and colored messages
    - Professional UI design with retro aesthetics
    
    The application verifies user age and categorizes them into
    appropriate age groups with styled feedback messages.
    """
    
    def build(self):
        """
        Build the application with retro neon theming.
        
        Sets the window background color to match the retro terminal
        aesthetic and returns the main form widget.
        
        Returns:
            AgeForm: The main application widget with all functionality
        """
        # Set global window background to terminal black
        Window.clearcolor = Colors.BACKGROUND
        
        # Return the main form widget
        return AgeForm()


# Application Entry Point
if __name__ == "__main__":
    """
    Main execution block for the Age Verification application.
    
    This demonstrates a complete Kivy application with:
    - Professional error handling
    - Consistent theming
    - User experience best practices
    - Comprehensive input validation
    """
    IdadeApp().run()

