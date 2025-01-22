def main():
  char_dict = {}
  char_list = []
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    word_count = len(file_contents.split())
    characters = list(file_contents.lower())
    for ch in characters:
      if ch in char_dict:
        char_dict[ch] += 1
      else:
        char_dict[ch] = 1
    
    for ch in char_dict:
      if ch.isalpha():
        char_list.append({ch: char_dict[ch]})
        
    sorted_dict = sorted(char_list, key=lambda x: list(x.values())[0], reverse=True)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for dict in sorted_dict:
      for key, value in dict.items():
        print(f"The '{key}' was found {value} times")
    print("--- End report ---")

main()