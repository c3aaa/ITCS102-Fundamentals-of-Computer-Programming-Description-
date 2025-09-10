name = input("Enter your username: ").upper()
print("Welcome to Chinese Fantasy Recommendation", name, "!")
print("To find your cup of tea; please answer a few questions.")

genre = input("What genre of drama do you like", name, "!", (Wuxia / Xianxia / Romance))
name = input("Enter your username: ").upper()
print("Welcome to Chinese Fantasy Recommendation", name, "!")
print("To find your cup of tea; please answer a few questions.")

genre = input("What genre of drama do you like? (Wuxia / Xianxia / Romance): ")\
hlong = input("How long should the drama be? (Short / Medium / Long  ): ")
year = input("How long should the drama be? (2000s / 2010s / 2020s): ")


if genre == "wuxia":
    if hlong == "short":
        if year == "2000":
            print("Recommended drama: Hidden")
        elif year == "2010":
            print("Recommended drama: Story")
            pass
        elif year == "2020":
            print("Recommended drama: Joy of Life")
            pass

    elif hlong == "medium":
        if year == "2000":
            print("Recommended drama: Ancient Love Poetry")
            pass
        elif year == "2010":
            print("Recommended drama: Nirvana ")
            pass
        elif year == "2020":
            print("Recommended drama: Enternal Love of Dream")
            pass
        
        pass

    elif hlong == "long":
        if year == "2000":
            print("Recommended drama: Princess Agent")
            pass
        elif year == "2010":
            print("Recommended drama: Evernight ")
            pass
        elif year == "2020":
            print("Recommended drama: Legend of Fei")
            pass

elif genre == "xianxia":
    if hlong == "short":
        if year == "2000":
            print("Recommended drama: Princess Agents")
        elif year == "2010":
            print("Recommended drama: The Untamed")
            pass
        elif year == "2020":
            print("Recommended drama: Love and Redemption ")
            pass

    elif hlong == "medium":
        if year == "2000":
            print("Recommended drama: The Legends")
            pass
        elif year == "2010":
            print("Recommended drama: Douluo Continent")
            pass
        elif year == "2020":
            print("Recommended drama: Ever Night")
            pass
        
        pass

    elif hlong == "long":
        if year == "2000":
            print("Recommended drama: Starry Love ")
            pass
        elif year == "2010":
            print("Recommended drama: Immortal Samsara")
            pass
        elif year == "2020":
            print("Recommended drama: Bloody")
            pass
    pass

elif genre == "romance":
    if hlong == "short":
        if year == "2000":
            print("Recommended drama: The Romance of Tiger and Rose Season 2")
        elif year == "2010":
            print("Recommended drama: I Am Sorry, I Love You ")
            pass
        elif year == "2020":
            print("Recommended drama: First Romance")
            pass

    elif hlong == "medium":
        if year == "2000":
            print("Recommended drama: Mr. Right")
            pass
        elif year == "2010":
            print("Recommended drama: Suddenly Seventeen ")
            pass
        elif year == "2020":
            print("Recommended drama: She and Her Perfect Husband  ")
            pass
        
        pass

    elif hlong == "long":
        if year == "2000":
            print("Recommended drama: Stay with Me ")
            pass
        elif year == "2010":
            print("Recommended drama: I Cannot Hug You")
            pass
        elif year == "2020":
            print("Recommended drama: My Dear Lady")
            pass
    pass    
else:
    print("Genre not found")

print("The end")