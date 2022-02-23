from gui.functionalities import *

# Main Menu
MANAGER_MENU = "m_m"
# Clean Action
CLEAN = "c"


STATES = {
    MANAGER_MENU: manager_menu,
    CLEAN: clean,
}

NEXT_STATES = {
    MANAGER_MENU: MANAGER_MENU,
    CLEAN: MANAGER_MENU,
}

# text message receives in these states for search
# view is dynamic here
CUSTOM_REQUIRED_STATED = [
]