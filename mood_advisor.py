print("📚 Mood-Based Study Time Advisor")

mood = input("How are you feeling today? (happy / tired / sad / angry): ").lower()

if mood == "happy":
    print("\nYou are feeling happy 😊")
    print("📖 Study for 90 minutes")
    print("☕ Take a 10 minute break after that")

elif mood == "tired":
    print("\nYou are feeling tired 😴")
    print("📖 Study for 30 minutes")
    print("💧 Take rest and drink water")

elif mood == "sad":
    print("\nYou are feeling sad 😔")
    print("📖 Study for 20 minutes")
    print("🎵 Listen to calm music after studying")

elif mood == "angry":
    print("\nYou are feeling angry 😠")
    print("🌬️ Do deep breathing for 5 minutes")
    print("📖 Then study for 25 minutes")

else:
    print("\nMood not recognized 🤔")
    print("📖 Do light study for 15 minutes")
