#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hello World Application - Documented Version

This is an improved version of the basic Hello World app with:
- Comprehensive documentation
- Professional code structure
- Clear explanation of Kivy concepts
- Best practices for beginners

Purpose: Educational example showing proper documentation
Complexity: Beginner with professional documentation
Concepts: App class, Label widget, documentation standards
"""

# Import necessary Kivy modules
from kivy.app import App        # Base application class
from kivy.uix.label import Label  # Text display widget


class HelloWorldApp(App):
    """
    Hello World Application Class
    
    This class demonstrates the minimal structure required for a Kivy application.
    Every Kivy app must inherit from the App class and implement the build() method.
    
    Attributes:
        None (inherits from App class)
        
    Methods:
        build(): Creates and returns the root widget for the application
    """
    
    def build(self):
        """
        Constructs and returns the root widget for the application.
        
        This method is the heart of every Kivy application. It's called automatically
        when the app starts and must return a widget that will serve as the root
        of the widget tree.
        
        Returns:
            Label: A text widget displaying "Hello, World!" with custom styling
            
        Note:
            The Label widget automatically centers itself in the available space.
            The halign and valign properties control text alignment within the label,
            not the label's position on screen.
        """
        return Label(
            text="Hello, World!",      # Text content to display
            font_size=40,             # Font size in device-independent pixels
            halign="center",          # Horizontal text alignment (left/center/right)
            valign="middle"           # Vertical text alignment (top/middle/bottom)
        )


# Application Entry Point
if __name__ == "__main__":
    """
    Main execution block - runs only when script is executed directly.
    
    This prevents the app from running if this file is imported as a module.
    Creates an instance of HelloWorldApp and starts the Kivy main loop.
    """
    HelloWorldApp().run()  # Instantiate and run the application