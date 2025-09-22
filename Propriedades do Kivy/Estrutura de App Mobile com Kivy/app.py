#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mobile Application Structure with Multi-Screen Navigation

This application demonstrates professional mobile app architecture:
- ScreenManager for multi-screen navigation
- Modular screen organization with separate files
- Scalable application structure for complex mobile apps
- Professional import organization and dependency management
- Clean separation of concerns between screens

Architecture Patterns:
- Screen-based navigation (common in mobile apps)
- Modular design with each screen in separate files
- Centralized screen management and registration
- Extensible structure for adding new screens

Purpose: Professional mobile app structure demonstration
Complexity: Intermediate-Advanced
Concepts: ScreenManager, modular architecture, navigation patterns
"""

# Import Kivy framework components
from kivy.app import App                      # Base application class
from kivy.uix.screenmanager import ScreenManager  # Multi-screen navigation manager

# Import individual screen modules
# This modular approach enables:
# - Clean code organization
# - Independent screen development
# - Easy maintenance and testing
# - Team collaboration on different screens
from screens.homescreen import HomeScreen     # Main/landing screen
from screens.tela1 import Tela1              # Feature screen 1
from screens.tela2 import Tela2              # Feature screen 2
from screens.tela3 import Tela3              # Feature screen 3
from screens.tela4 import Tela4              # Feature screen 4
from screens.tela5 import Tela5              # Feature screen 5


class MyApp(App):
    """
    Main Mobile Application with Multi-Screen Architecture
    
    This application demonstrates professional mobile app development:
    - ScreenManager for smooth screen transitions
    - Modular screen organization for maintainability
    - Scalable architecture supporting unlimited screens
    - Professional navigation patterns used in real mobile apps
    
    The app uses ScreenManager to handle:
    - Screen transitions with built-in animations
    - Screen history and back navigation
    - Memory management for inactive screens
    - Consistent navigation experience across platforms
    
    Architecture Benefits:
        - Each screen is independently developed and tested
        - Easy to add new screens without modifying existing code
        - Clear separation of concerns between different app features
        - Professional mobile app structure used in production apps
    """
    
    def build(self):
        """
        Build the multi-screen mobile application.
        
        This method demonstrates professional app initialization:
        - ScreenManager configuration for navigation
        - Screen registration with unique identifiers
        - Proper screen instantiation and setup
        - Extensible architecture for future screens
        
        Returns:
            ScreenManager: Root widget managing all application screens
        
        Screen Management:
            Each screen is registered with a unique name that can be used
            for navigation throughout the app. The ScreenManager handles
            all the complex navigation logic, transitions, and memory management.
        """
        # Create the main screen manager
        # ScreenManager handles all navigation logic and screen transitions
        sm = ScreenManager()
        
        # Register all application screens with the manager
        # Each screen gets a unique name for navigation purposes
        # The order of registration doesn't affect navigation behavior
        
        # Home screen - typically the app's main/landing page
        sm.add_widget(HomeScreen(name='home'))
        
        # Feature screens - each represents a different app functionality
        sm.add_widget(Tela1(name='tela1'))    # Feature area 1
        sm.add_widget(Tela2(name='tela2'))    # Feature area 2
        sm.add_widget(Tela3(name='tela3'))    # Feature area 3
        sm.add_widget(Tela4(name='tela4'))    # Feature area 4
        sm.add_widget(Tela5(name='tela5'))    # Feature area 5
        
        # Navigation Usage:
        # From any screen, you can navigate using:
        # self.manager.current = 'screen_name'
        # 
        # Example: self.manager.current = 'home'  # Go to home screen
        #          self.manager.current = 'tela1' # Go to feature screen 1
        
        return sm


# Application Entry Point
if __name__ == '__main__':
    """
    Professional mobile application entry point.
    
    This demonstrates a complete mobile app structure with:
    - Professional multi-screen navigation architecture
    - Modular design enabling team development
    - Scalable structure for complex mobile applications
    - Clean separation of concerns between different app areas
    - Industry-standard mobile app development patterns
    
    Key Architectural Benefits:
        - Each screen can be developed and tested independently
        - Easy to add new features without affecting existing screens
        - Professional navigation patterns familiar to mobile users
        - Memory-efficient screen management
        - Smooth animations and transitions between screens
        - Extensible structure supporting unlimited app growth
    
    Real-World Applications:
        This structure is suitable for:
        - E-commerce apps with product catalogs, cart, checkout
        - Social media apps with feed, profile, settings, messaging
        - Business apps with dashboard, reports, settings, help
        - Educational apps with lessons, exercises, progress, profile
        - Any multi-feature mobile application requiring navigation
    """
    MyApp().run()