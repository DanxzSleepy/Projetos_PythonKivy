#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Welcome Application - Interactive User Input Example

This application demonstrates:
- Interactive user input with TextInput widget
- Button events and callback functions
- Dynamic text updates based on user interaction
- Layout management with BoxLayout
- Widget styling and sizing

Purpose: Introduction to user interaction and event handling
Complexity: Beginner-Intermediate
Concepts: TextInput, Button, BoxLayout, event binding, dynamic content
"""

# Import Kivy framework components
from kivy.app import App                # Base application class
from kivy.uix.boxlayout import BoxLayout  # Linear layout container
from kivy.uix.label import Label        # Text display widget
from kivy.uix.button import Button      # Interactive button widget
from kivy.uix.textinput import TextInput  # Text input field widget


class WelcomeApp(App):
    """
    Interactive Welcome Application
    
    This app creates a simple interface where users can enter their name
    and receive a personalized welcome message. It demonstrates basic
    user interaction patterns in Kivy.
    
    Attributes:
        layout (BoxLayout): Main container for all widgets
        title_label (Label): Application title display
        name_input (TextInput): User name input field
        button (Button): Submit button for user interaction
        message_label (Label): Dynamic message display area
    """
    
    def build(self):
        """
        Builds the application interface with interactive components.
        
        Creates a vertical layout containing:
        1. Title label
        2. Text input field for name entry
        3. Submit button
        4. Message display area
        
        Returns:
            BoxLayout: The main layout containing all UI elements
        """
        # Create main vertical layout container
        # BoxLayout arranges children either vertically or horizontally
        self.layout = BoxLayout(
            orientation="vertical",  # Stack widgets vertically
            padding=20,             # 20 pixels padding around the layout
            spacing=10              # 10 pixels space between widgets
        )

        # Application title - fixed at the top
        self.title_label = Label(
            text="App de Boas-Vindas",  # Title text in Portuguese
            font_size=28,              # Large font for prominence
            bold=True,                 # Bold text for emphasis
            size_hint=(1, 0.2)         # Full width, 20% of available height
        )
        self.layout.add_widget(self.title_label)

        # Text input field for user name
        self.name_input = TextInput(
            hint_text="Digite seu nome",  # Placeholder text
            multiline=False,             # Single line input only
            size_hint=(1, 0.2)           # Full width, 20% height
        )
        # Note: hint_text appears when the field is empty to guide the user
        self.layout.add_widget(self.name_input)

        # Submit button with custom styling
        self.button = Button(
            text="Enviar",                    # Button label
            size_hint=(1, 0.2),             # Full width, 20% height
            background_color=(0.2, 0.6, 1, 1),  # Blue color (R, G, B, Alpha)
            font_size=20                     # Medium font size
        )
        # Bind button click event to the enviar method
        # When button is pressed, self.enviar will be called
        self.button.bind(on_press=self.enviar)
        self.layout.add_widget(self.button)

        # Message display area - initially empty
        self.message_label = Label(
            text="",                # Start with empty text
            font_size=20,          # Medium font size
            halign="center",       # Center-align text horizontally
            valign="middle",       # Center-align text vertically
            size_hint=(1, 0.4)     # Full width, 40% height (largest area)
        )
        self.layout.add_widget(self.message_label)

        # Return the complete layout as the root widget
        return self.layout

    def enviar(self, instance):
        """
        Event handler for the submit button.
        
        This method is called when the user clicks the "Enviar" button.
        It validates the input and updates the message display accordingly.
        
        Args:
            instance (Button): The button widget that triggered this event
                             (automatically passed by Kivy's event system)
        
        Process:
            1. Get text from input field and remove whitespace
            2. Check if name is not empty
            3. Display personalized welcome message or error message
        """
        # Get the user input and remove leading/trailing whitespace
        nome = self.name_input.text.strip()
        
        # Validate input and provide appropriate response
        if nome:  # If name is not empty
            # Create personalized welcome message
            self.message_label.text = f"Bem-vindo(a), {nome}!"
        else:  # If name is empty or only whitespace
            # Display error message prompting user to enter name
            self.message_label.text = "Por favor, digite seu nome."


# Application Entry Point
if __name__ == "__main__":
    """
    Main execution block for running the application.
    
    This code runs only when the script is executed directly,
    not when it's imported as a module.
    """
    WelcomeApp().run()  # Create and run the application
