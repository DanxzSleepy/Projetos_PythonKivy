from kivy.app import App
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kivy StringProperty Basic Example

This application demonstrates fundamental Kivy Properties concepts:
- StringProperty declaration and usage
- Reactive property binding with automatic UI updates
- Property inheritance and widget integration
- KV file integration for declarative UI design

Kivy Properties are special attributes that:
- Automatically trigger events when values change
- Enable data binding between widgets and application logic
- Provide type safety and validation
- Support reactive programming patterns

Purpose: Introduction to Kivy's property system
Complexity: Beginner
Concepts: StringProperty, reactive programming, data binding
"""

# Import Kivy framework components
from kivy.app import App                    # Base application class
from kivy.uix.boxlayout import BoxLayout    # Linear layout container
from kivy.properties import StringProperty   # Reactive string property


class MyWidget(BoxLayout):
    """
    Custom Widget Demonstrating StringProperty Usage
    
    This widget showcases the fundamental concept of Kivy Properties:
    - Reactive data binding that automatically updates the UI
    - Type-safe property declaration with default values
    - Integration with KV files for declarative UI design
    
    The StringProperty automatically notifies any bound widgets
    when its value changes, enabling reactive user interfaces
    without manual UI update code.
    
    Technical Details:
        - StringProperty creates a descriptor that manages the string value
        - Changes to the property automatically trigger 'on_property_name' events
        - KV files can bind to this property using standard Kivy syntax
        - The property supports validation and type conversion
    """
    
    # StringProperty Declaration with Default Value
    saudacao = StringProperty("Olá, Kivy!")  # Reactive string property
    
    # Technical Note:
    # This property can be accessed and modified like a normal attribute,
    # but changes automatically trigger UI updates and event callbacks.
    # Example usage:
    #   widget.saudacao = "New greeting"  # Automatically updates bound UI


class StringPropApp(App):
    """
    Basic StringProperty Demonstration Application
    
    This app shows how StringProperty integrates with Kivy's
    application architecture and KV file system.
    
    The corresponding KV file (stringpropapp.kv) will automatically
    bind to the 'saudacao' property and display its value.
    """
    
    def build(self):
        """
        Build the application interface.
        
        Returns the custom widget that contains the StringProperty.
        The KV file will handle the actual UI layout and property binding.
        
        Returns:
            MyWidget: Custom widget with StringProperty for demonstration
        """
        return MyWidget()


# Application Entry Point
if __name__ == '__main__':
    """
    Entry point demonstrating basic Kivy Properties usage.
    
    This example shows the foundation of reactive programming in Kivy:
    - Properties that automatically update the UI
    - Clean separation between data and presentation
    - Type-safe property management
    - Integration with Kivy's event system
    """
    StringPropApp().run()
