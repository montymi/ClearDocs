import toml
import mistune

class MarkdownConverter:
    def __init__(self, toml_file):
        self.toml_file = toml_file
        self.data = self.load_toml()
        self.renderer = mistune.create_markdown()

    def load_toml(self):
        try:
            with open(self.toml_file, 'r') as file:
                data = toml.load(file)
                return data.get('readme', {})
        except Exception as e:
            raise Exception(f'An error occurred while loading the TOML file: {e}')

    def convert_to_markdown(self):
        markdown = []
        try:
            self.convert_section(self.data, markdown)
            return '\n'.join(markdown)
        except KeyError as e:
            raise KeyError(f'Key "{e.args[0]}" not found in {self.data}.')

    def convert_section(self, section, markdown, level=1):
        if isinstance(section, dict):
            for key, value in section.items():
                if key == 'list' and isinstance(value, list):
                    for item in value:
                        self.convert_section(item, markdown, level)
                elif key == 'subtitle':
                    markdown.append(f"{'#' * (level + 1)} {value}\n")
                else:
                    markdown.append(f"{'#' * level} {key.replace('_', ' ').title()}\n")
                    self.convert_section(value, markdown, level + 1)
        elif isinstance(section, list):
            for item in section:
                self.convert_section(item, markdown, level)
        else:
            markdown.append(f"{section}\n")

    def save_markdown(self, output_file):
        markdown_content = self.convert_to_markdown()
        mdx_content = self.renderer(markdown_content)
        with open(output_file, 'w') as file:
            file.write(mdx_content)

# Example usage
if __name__ == '__main__':
    converter = MarkdownConverter('docconfig.toml')
    converter.save_markdown('README.mdx')
