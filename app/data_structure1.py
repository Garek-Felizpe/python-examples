zelda_characters = ["Link", "Zelda", "Ganon", "Sheik", "Midna", "Darunia", "Navi", "Impa", "Tingle", "Ruto", "Malon", "Saria","Majora"]
zelda_characters.append("Kafei")
zelda_characters.insert(13, "Anju")
zelda_characters.remove("Tingle")
zelda_characters_triforce = zelda_characters.pop(4) # Removes "Midna", but if you want to remove more dynamically, you can use index -1 to remove the last item, or search for the index of a specific item.
print(zelda_characters)
print("Removed character:", zelda_characters_triforce)
zelda_characters.sort()
print("Sorted characters:", zelda_characters)
zelda_characters.reverse()
print("Reversed characters:", zelda_characters)