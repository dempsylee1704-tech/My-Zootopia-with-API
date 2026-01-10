import json
import data_fetcher as data



def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def read_data(file_path):
    with open(file_path, "r", encoding="utf-8") as fileobj:
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
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(content)

def main():
    animal_name = input("Enter a name of an animal: ").strip()
    if animal_name == "":
        print("Please enter animal name")
        return

    animals = data.fetch_data(animal_name)

    if not animals:
        animals_html = f'<h2>The animal "{animal_name}" does not exist.</h2>'
    else:
        animals_html = serialize_animals(animals)

    template_html = read_data("animals_template.html")


    final_html = template_html.replace(
        "__REPLACE_ANIMALS_INFO__", animals_html
    )

    write_html("animals.html", final_html)
    print("Website was successfully generated to the file animals.html.")

if __name__ == "__main__":
    main()