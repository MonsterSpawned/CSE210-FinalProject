from platform import system, version, release

# OS utils:
class OSUtils():
    
    # Print system information.
    def __init__(self):
        print(f"You are running {system} {release} v{version}...")
    
    # Get the current OS:
    def get_current_os(self):
        return system
    
    # Get the current OS version:
    def get_current_os_version(self):
        return version
    
    # Get the current OS release:
    def get_current_os_release(self):
        return release