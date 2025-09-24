import json

file_path = 'animals_data.json'




def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as fobj:
    return json.load(fobj)

animals_data = load_data('animals_data.json')
# print(animals_data)

def print_data(anim_dic):
    for animal in animals_data:
        print(f"Name: {animal['name']}\n"
              f"Diet: {animal['characteristics'].get('diet', 'N/A')}\n"
              f"Location: {animal['locations']}\n"
              f"Type: {animal['characteristics'].get('type', 'N/A')}"
              f"\n"
              )

print_data(animals_data)




def main():
    pass

if __name__ == "__main__":
    main()