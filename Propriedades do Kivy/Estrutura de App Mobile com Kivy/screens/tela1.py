#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tela1 - Feature Screen Example for Mobile App Architecture

This module demonstrates professional screen development patterns:
- Individual screen module organization
- Screen class inheritance from Kivy's Screen
- Professional UI construction within screens
- Navigation integration with ScreenManager
- StringProperty usage for dynamic content

Screen Development Patterns:
- Each screen is a separate module for clean organization
- Screen classes inherit from kivy.uix.screenmanager.Screen
- UI construction happens in __init__ method
- Navigation is handled through self.manager.current
- Properties enable reactive content updates

Purpose: Professional screen development example
Complexity: Intermediate
Concepts: Screen inheritance, modular design, navigation, Properties
"""

# Import Kivy framework components
from kivy.uix.screenmanager import Screen    # Base class for app screens
from kivy.uix.button import Button           # Interactive button widget
from kivy.properties import StringProperty   # Reactive string property
from kivy.uix.label import Label            # Text display widget
from kivy.uix.boxlayout import BoxLayout     # Linear layout container


class Tela1(Screen):
    """
    Feature Screen 1 - Professional Screen Development Example
    
    This screen demonstrates professional mobile app screen development:
    - Clean inheritance from Screen base class
    - StringProperty for dynamic, reactive content
    - Professional UI construction with proper layouts
    - Navigation integration with the parent ScreenManager
    - Modular design enabling independent development and testing
    
    The screen showcases:
    - Property-driven content management
    - Professional UI layout with BoxLayout
    - Navigation back to home screen
    - Extensible structure for adding features
    
    Technical Implementation:
        - Inherits from Screen for ScreenManager integration
        - Uses StringProperty for reactive title and description
        - Constructs UI programmatically in __init__
        - Implements navigation through manager.current
    
    Attributes:
        title (StringProperty): Screen title for dynamic updates
        description (StringProperty): Screen description content
    """
    
    # StringProperty for Dynamic Content Management
    title = StringProperty('Tela 1')  # Screen title
    description = StringProperty('Esta é a Tela 1 do aplicativo.')  # Description
    
    # Technical Note:
    # StringProperty enables reactive content updates throughout the app.
    # Changes to these properties automatically update any bound UI elements.
    
    def __init__(self, **kwargs):
        """
        Initialize the screen with professional UI construction.
        
        This method demonstrates proper screen initialization:
        - Call to parent Screen.__init__
        - Professional UI layout construction
        - Widget configuration and styling
        - Event binding for navigation
        
        Args:
            **kwargs: Additional arguments passed to parent Screen class
        """
        # Initialize parent Screen class
        super().__init__(**kwargs)
        
        # Create main layout container
        # BoxLayout provides clean, responsive layout management
        layout = BoxLayout(
            orientation='vertical',  # Stack widgets vertically
            padding=20,             # 20px padding around layout
            spacing=10              # 10px spacing between widgets
        )
        
        # Screen title label with property binding
        # Uses self.title StringProperty for dynamic content
        title_label = Label(
            text=self.title,        # Bound to StringProperty
            font_size=30,           # Large font for visual hierarchy
            size_hint_y=0.2         # 20% of container height
        )
        
        # Navigation button for returning to home screen
        # Demonstrates proper navigation pattern in mobile apps
        back_btn = Button(
            text='Voltar',          # Back button label in Portuguese
            size_hint_y=0.1         # 10% of container height
        )
        # Bind button press to navigation method
        back_btn.bind(on_press=self.go_back)
        
        # Description label with property binding
        # Uses self.description StringProperty for dynamic content
        desc_label = Label(
            text=self.description,  # Bound to StringProperty
            font_size=18,           # Readable font size
            text_size=(None, None), # Allow text wrapping
            halign="left",          # Left-align text
            valign="middle"         # Vertically center text
        )
        # Bind label size to enable proper text alignment
        desc_label.bind(texture_size=desc_label.setter('size'))
        
        # Add all widgets to the layout
        layout.add_widget(title_label)
        layout.add_widget(back_btn)
        layout.add_widget(desc_label)
        
        # Add the complete layout to this screen
        self.add_widget(layout)
    
    def go_back(self, instance):
        """
        Navigate back to the home screen.
        
        This method demonstrates proper navigation patterns in mobile apps:
        - Clean navigation through ScreenManager
        - Consistent back navigation behavior
        - Professional mobile app user experience
        
        Args:
            instance (Button): The button that triggered navigation
                              (required by Kivy's event binding system)
        
        Navigation Technical Details:
            - self.manager refers to the parent ScreenManager
            - Setting manager.current triggers screen transition
            - ScreenManager handles transition animations automatically
            - Previous screen state is preserved for smooth user experience
        """
        # Navigate to home screen using ScreenManager
        # The name 'home' corresponds to the registration in app.py
        self.manager.current = 'home'
        
        # Alternative navigation methods:
        # self.manager.transition.direction = 'right'  # Set transition direction
        # self.manager.current = 'home'                # Then navigate
        # 
        # For programmatic navigation with history:
        # self.manager.push('home')  # Push to history stack
        # self.manager.pop()         # Go back in history