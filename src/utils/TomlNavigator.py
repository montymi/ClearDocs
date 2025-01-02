from pprint import pprint
import toml

class TomlNavigator:
    def __init__(self, toml_file):
        self.toml_file = toml_file
        self.data = self.load_toml()
        self.current_path = []

    def load_toml(self):
        try:
            with open(self.toml_file, 'r') as file:
                return toml.load(file)
        except Exception as e:
            raise Exception(f'An error occurred while loading the TOML file: {e}')

    def save_toml(self):
        try:
            with open(self.toml_file, 'w') as file:
                toml.dump(self.data, file)
        except Exception as e:
            raise Exception(f'An error occurred while saving the TOML file: {e}')

    def get_current_element(self):
        element = self.data
        for key in self.current_path:
            element = element[key]
        return element

    def navigate_to(self, key):
        current_element = self.get_current_element()
        if key == '..':
            self.navigate_back()
        elif key == '/':
            self.current_path = []
        elif key == '.':
            self.display_current_key()
        elif key in ['show', 'display', 'ls', 'list']:
            self.display_next_options()
        elif isinstance(current_element, dict) and key in current_element:
            self.current_path.append(key)
        else:
            raise KeyError(f'Key "{key}" not found in the current element.')

    def navigate_back(self):
        if self.current_path:
            self.current_path.pop()
        else:
            raise IndexError('Already at the root element.')

    def edit_element(self, key, value):
        current_element = self.get_current_element()
        if isinstance(current_element, dict):
            current_element[key] = value
            self.save_toml()
        else:
            raise TypeError('Current element is not a dictionary.')

    def display_current_element(self):
        current_element = self.get_current_element()
        pprint(toml.dumps(current_element))
    
    def display_next_options(self):
        current_element = self.get_current_element()
        if isinstance(current_element, dict):
            options = list(current_element.keys())
            pprint(options)
        else:
            raise TypeError('Current element is not a dictionary.')
    
    def display_current_key(self):
        pprint(self.current_path)

# Example usage
if __name__ == '__main__':
    try: 
        navigator = TomlNavigator('docconfig.toml')

        while True:
            try:
                command = input("Enter command (navigate/edit/display/exit): ").strip().lower()
                if command == 'exit':
                    raise KeyboardInterrupt
                elif command == 'navigate':
                    key = input("Enter key to navigate to (or '..' to go back, '/' for root): ").strip()
                    navigator.navigate_to(key)
                elif command == 'edit':
                    key = input("Enter key to edit: ").strip()
                    value = input("Enter new value: ").strip()
                    navigator.edit_element(key, value)
                elif command == 'display':
                    navigator.display_current_element()
                else:
                    print("Unknown command. Please try again.")
            except Exception as e:
                print(f"Error: {e}")
    except KeyboardInterrupt as e:
        print("Exiting...")