# Magic Dictionary Game

magic_dict = {
    "dream": "мрія",
    "python": "друг, що завжди поруч",
    "coffee": "еліксир ранку"
}

print("🔮 Welcome to the Magic Dictionary Game!")
print("Type an English word to discover its magical meaning.")
print("Type 'exit' to quit the game.")

while True:
    word = input("🔍 Enter a word: ").lower().strip()
    
    if word == "exit":
        print("👋 Thanks for playing! See you again!")
        break

    meaning = magic_dict.get(word, "🙈 Oops! This word is not in the magic dictionary.")
    print(f"✨ {word} → {meaning}")
