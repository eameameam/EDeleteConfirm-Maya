# EDeleteConfirm: Maya Deletion Confirmation Tool

The EDeleteConfirm script adds a confirmation dialog to Autodesk Maya, similar to Blender's deletion confirmation. It prompts with a simple "Yes/No" popup window to confirm their intent before proceeding with the deletion.

![EDeleteConfirm Window](/EDeleteConfirm.png)

## Installation

1. Place the `EDeleteConfirm.py` file in the `scripts` folder of your Maya directory.
2. Assign a hotkey in Maya's Hotkey Editor:
   
```python
import EDeleteConfirm; 
EDeleteConfirm.create_popup_window()
```

## Usage

Whenever you need to delete keyframes or objects in Maya, press the assigned hotkey.

The EDeleteConfirm dialog will appear, asking for confirmation before deletion:

1. Click "Yes" to proceed with the deletion.
2. Click "No" to cancel and keep the keyframes or objects intact.
