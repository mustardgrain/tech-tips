Suggested General Configuration
===============================

1. Close the "Welcome" tab
2. Close the "Task List" tab
3. Drag the "Outline" tab to the bottom-left corner
4. Select "Window" -> "Show View" -> "Navigator"
5. Open "Preferences" -> "General" -> "Startup and Shutdown"
5.1. Check "Refresh workspace on startup"
5.2. Uncheck "Confirm exit when closing last window"


  5. Open the Preferences
    1. Open "General"
      1. Open "Appearance" -> "Colors and Fonts" and change the font to your liking (mine is Monospace 8)
      2. Open "Editors" -> "Text Editors"
        1. Check "Insert spaces for tabs"
        2. Check "Show line numbers"
        3. Uncheck "Enable drag and drop of text"


    2. Open "Java"
      1. Open "Code Style" -> "Formatter"
        1. Click the "Edit..." button
          1. Rename "Java Conventions [built-in]" to "Java Conventions [built-in], using Spaces"
          2. Click the "Indentation" tab
            1. Select the "Spaces only" "Tab policy"
            2. Change "Tab size" to 4
          3. Click the "Blank Lines" tab
            1. Change "Before first declaration" to 1
          4. Click the "Line Wrapping" tab
            1. Change "Maximum Line Width" to 140
            2. For parameters, function calls, constructor calls, etc.
              1. Change the "Line wrapping policy" to "Wrap all elements, except first element if not necessary"
              2. Change the "Identation policy" to "Indent on column"
      2. Open "Editor" -> "Folding" and uncheck "Enable Folding"
      3. Open "Installed JREs"
        1. Remove any OpenJDK-based JDKs and add one on your system
    3. Open "Maven" -> "User Interface"
      1. Check the "Open XML page in the POM editor by default"
    4. Open "XML" -> "XML Files" -> "Editor"
      1. Click "Indent using spaces"
      2. Change "Indentation size" to 2
