Suggested General Configuration
===============================

* Close the "Welcome" tab
* Close the "Task List" tab
* Drag the "Outline" tab to the bottom-left corner
* Select "Window" -> "Show View" -> "Navigator"
* Open "Preferences" -> "General" -> "Startup and Shutdown"
  * Check "Refresh workspace on startup"
  * Uncheck "Confirm exit when closing last window"

Editor Configuration
====================

* Open the Preferences
  * Open "General"
    * Open "Appearance" -> "Colors and Fonts" and change the font to your liking (mine is Monospace 8)
    * Open "Editors" -> "Text Editors"
      * Check "Insert spaces for tabs"
      * Check "Show line numbers"
      * Uncheck "Enable drag and drop of text"

Java Configuration
==================

* Open "Preferencs -> "Java"
  * Open "Code Style" -> "Formatter"
    * Click the "Edit..." button
      * Rename  to "Java Conventions [built-in], using Spaces"
      * Click the "Indentation" tab
        * Select the "Spaces only" "Tab policy"
        * Change "Tab size" to 4
      * Click the "Blank Lines" tab
        * Change "Before first declaration" to 1
      * Click the "Line Wrapping" tab
        * Change "Maximum Line Width" to 140
        * For parameters, function calls, constructor calls, etc.
          * Change the "Line wrapping policy" to "Wrap all elements, except first element if not necessary"
          * Change the "Identation policy" to "Indent on column"
  * Open "Editor" -> "Folding" and uncheck "Enable Folding"
  * Open "Installed JREs"
    * Remove any OpenJDK-based JDKs and add one on your system

Maven Configuration
===================

* Open "Preferencs -> "Maven"
  * Open "User Interface"
    * Check the "Open XML page in the POM editor by default"

XML Configuration
=================

* Open "Preferencs -> "XML"
  * Open "XML Files" -> "Editor"
    * Click "Indent using spaces"
    * Change "Indentation size" to 2
