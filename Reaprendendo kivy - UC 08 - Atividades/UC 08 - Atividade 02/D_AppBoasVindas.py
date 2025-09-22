#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Welcome Application - Professional Architecture Version

This is an enhanced version of the welcome app demonstrating:
- Professional code organization with private methods
- Separation of concerns (UI creation vs logic)
- Comprehensive documentation
- Modular design patterns
- Error handling best practices

Purpose: Educational example of clean code architecture
Complexity: Intermediate
Concepts: Private methods, modular design, code organization
"""

# Import Kivy framework components
from kivy.app import App                # Base application class
from kivy.uix.boxlayout import BoxLayout  # Linear layout container
from kivy.uix.label import Label        # Text display widget
from kivy.uix.button import Button      # Interactive button widget
from kivy.uix.textinput import TextInput  # Text input field widget


class WelcomeApp(App):
    """
    Professional Welcome Application with Clean Architecture
    
    This application demonstrates professional coding practices:
    - Modular method design
    - Clear separation of UI setup and business logic
    - Comprehensive documentation
    - Private method usage for internal operations
    
    The app receives a user's name and displays a personalized welcome message
    using a well-structured, maintainable codebase.
    
    Attributes:
        layout (BoxLayout): Main container for all UI elements
        title_label (Label): Application title display
        name_input (TextInput): User name input field
        submit_button (Button): Action button for form submission
        message_label (Label): Dynamic message display area
    """
    
    def build(self):
        """
        Main build method that orchestrates the UI construction.
        
        This method follows the single responsibility principle by
        delegating specific tasks to private helper methods.
        
        Returns:
            BoxLayout: The complete user interface layout
        """
        # Use private methods to organize UI construction
        self._setup_layout()           # Initialize main layout
        self._create_title_label()     # Add application title
        self._create_name_input()      # Add name input field
        self._create_submit_button()   # Add submit button
        self._create_message_label()   # Add message display area
        
        return self.layout
    
    def _setup_layout(self):
        """
        Private method to configure the main application layout.
        
        Creates a vertical BoxLayout with appropriate spacing and padding.
        The underscore prefix indicates this is an internal method not
        intended for external use.
        """
        self.layout = BoxLayout(
            orientation="vertical",  # Arrange widgets vertically
            padding=20,             # 20px padding on all sides
            spacing=10              # 10px spacing between widgets
        )
    
    def _create_title_label(self):
        """
        Private method to create and add the application title.
        
        Creates a prominent title label with custom styling and
        adds it to the main layout.
        """
        self.title_label = Label(
            text="App de Boas-Vindas",  # Application title in Portuguese
            font_size=28,              # Large font for visual hierarchy
            bold=True,                 # Bold styling for emphasis
            size_hint=(1, 0.2)         # Full width, 20% of container height
        )
        self.layout.add_widget(self.title_label)
    
    def _create_name_input(self):
        """
        Private method to create and add the name input field.
        
        Creates a single-line text input with placeholder text
        to guide user interaction.
        """
        self.name_input = TextInput(
            hint_text="Digite seu nome",  # Placeholder text for guidance
            multiline=False,             # Restrict to single line input
            size_hint=(1, 0.2)           # Full width, 20% height
        )
        self.layout.add_widget(self.name_input)
    
    def _create_submit_button(self):
        """
        Private method to create and add the submit button.
        
        Creates a styled button with event binding for user interaction.
        The button uses custom colors and responds to press events.
        """
        self.submit_button = Button(
            text="Enviar",                    # Button label text
            size_hint=(1, 0.2),             # Full width, 20% height
            background_color=(0.2, 0.6, 1, 1),  # Custom blue color (RGBA)
            font_size=20                     # Medium font size
        )
        # Bind button press event to the submission handler
        # Note: Using private method for event handling maintains encapsulation
        self.submit_button.bind(on_press=self._handle_submission)
        self.layout.add_widget(self.submit_button)
    
    def _create_message_label(self):
        """
        Private method to create and add the message display area.
        
        Creates a label for displaying dynamic messages to the user.
        Initially empty, it will show welcome messages or error prompts.
        """
        self.message_label = Label(
            text="",                # Initially empty text
            font_size=20,          # Medium font size for readability
            halign="center",       # Center-align text horizontally
            valign="middle",       # Center-align text vertically
            size_hint=(1, 0.4)     # Full width, 40% height (main display area)
        )
        self.layout.add_widget(self.message_label)
    
    def _handle_submission(self, instance):
        """
        Private method to process form submission and display appropriate message.
        
        This method implements the business logic for validating user input
        and providing feedback. It demonstrates input validation and
        conditional message display.
        
        Args:
            instance (Button): The button widget that triggered this event
                             (automatically provided by Kivy's event system)
        
        Process:
            1. Extract and sanitize user input
            2. Validate input is not empty
            3. Display personalized welcome or error message
        """
        # Extract user input and remove leading/trailing whitespace
        name = self.name_input.text.strip()
        
        # Conditional logic for user feedback
        if name:  # If name contains actual content
            # Display personalized welcome message
            self.message_label.text = f"Bem-vindo(a), {name}!"
        else:  # If name is empty or only whitespace
            # Display helpful error message
            self.message_label.text = "Por favor, digite seu nome."


# Application Entry Point
if __name__ == "__main__":
    """
    Main execution block - demonstrates professional application startup.
    
    This pattern ensures the app only runs when the script is executed directly,
    not when imported as a module, which is important for code reusability.
    """
    WelcomeApp().run()  # Instantiate and run the application
