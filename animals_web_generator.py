import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def read_data(file_path):
    with open(file_path, "r") as fileobj:
         return fileobj.read()

def serialize_animal(animal):
    """Serialize a single animal object into HTML."""
    output = '<li class="cards__item">\n'

    if "name" in animal:
        output += f'  <div class="card__title">{animal["name"]}</div>\n'

    output += '  <p class="card__text">\n'

    if "characteristics" in animal and "diet" in animal["characteristics"]:
        output += (
            f'    <strong>Diet:</strong> '
            f'{animal["characteristics"]["diet"]}<br/>\n'
        )

    if "locations" in animal and animal["locations"]:
        output += (
            f'    <strong>Location:</strong> '
            f'{animal["locations"][0]}<br/>\n'
        )

    if "type" in animal:
        output += f'    <strong>Type:</strong> {animal["type"]}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'

    return output

def serialize_animals(animals):
    """Serialize a list of animals into HTML."""
    output = ""
    for animal in animals:
        output += serialize_animal(animal)
    return output


def write_html(file_path, content):
    """Write HTML content to a file."""
    with open(file_path, "w") as handle:
        handle.write(content)

def main():
    animals = load_data("animals_data.json")
    template_html = read_data("animals_template.html")

    animals_html = serialize_animals(animals)
    final_html = template_html.replace(
        "__REPLACE_ANIMALS_INFO__", animals_html
    )

    write_html("animals.html", final_html)


if __name__ == "__main__":
    main()