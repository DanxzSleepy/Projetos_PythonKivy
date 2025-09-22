#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hello World Application - Basic Kivy Example

This is the simplest possible Kivy application that demonstrates:
- Basic App class structure
- Label widget usage
- Text positioning and styling
- Application lifecycle (build method)

Purpose: Introduction to Kivy framework fundamentals
Complexity: Beginner
Concepts: App class, Label widget, basic properties
"""

# Import necessary Kivy modules
from kivy.app import App        # Base class for all Kivy applications
from kivy.uix.label import Label  # Widget for displaying text


class HelloWorldApp(App):
    """
    Main application class that inherits from Kivy's App class.
    
    The App class is the foundation of every Kivy application.
    It manages the application lifecycle and provides the main entry point.
    """
    
    def build(self):
        """
        Build method - REQUIRED for every Kivy App.
        
        This method is automatically called by Kivy when the app starts.
        It must return the root widget that will be displayed on screen.
        
        Returns:
            Label: A text widget that serves as the root widget
        """
        # Create and return a Label widget with customized properties
        return Label(
            text="Hello, World!",      # The text to display
            font_size=40,             # Font size in pixels
            halign="center",          # Horizontal alignment within the label
            valign="middle"           # Vertical alignment within the label
        )
        # Note: halign and valign control text alignment within the widget,
        # not the widget position on screen


# Application entry point
if __name__ == "__main__":
    """
    Entry point when script is run directly (not imported).
    Creates an instance of HelloWorldApp and starts the application.
    """
    HelloWorldApp().run()  # Create app instance and start the main loop