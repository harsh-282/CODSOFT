# Movies Dataset
movies = {
    'Vikram': ['action', 'thriller', 'popular'],
    'Master': ['action', 'drama', 'popular'],
    'Jailer': ['action', 'comedy', 'recent'],
    'Love Today': ['romance', 'comedy', 'recent'],
    'Soorarai Pottru': ['drama', 'inspiring', 'popular'],
    'Ponniyin Selvan': ['adventure', 'historical', 'recent'],
    'Kaithi': ['thriller', 'action', 'intense'],
    '96': ['romance', 'drama', 'emotional'],
    'Asuran': ['drama', 'action', 'popular'],
    'Theri': ['action', 'family', 'popular'],
    'Karnan': ['drama', 'inspiring', 'recent'],
    'Bigil': ['sports', 'action', 'inspiring'],
    'Varisu': ['family', 'drama', 'recent'],
    'Doctor': ['comedy', 'thriller', 'recent'],
    'Beast': ['action', 'comedy', 'recent'],
    'Naduvula Konjam Pakkatha Kaanom': ['comedy', 'quirky'],
    'Mersal': ['thriller', 'action', 'popular'],
    'Thunivu': ['thriller', 'heist', 'recent'],
    'Etharkkum Thunindhavan': ['action', 'family', 'recent'],
    'Vedalam': ['family', 'action', 'popular'],
    'Viswasam': ['family', 'emotional', 'drama'],
    'Soodhu Kavvum': ['comedy', 'crime', 'quirky'],
    'Pariyerum Perumal': ['social', 'inspiring', 'drama'],
    'I': ['romance', 'thriller', 'action'],
    'Anniyan': ['thriller', 'psychological', 'popular'],
    'Petta': ['action', 'family', 'popular'],
    'Kabali': ['drama', 'gangster', 'action'],
    'Aayirathil Oruvan': ['adventure', 'historical', 'thriller'],
    'Raatchasan': ['thriller', 'crime', 'psychological'],
    'Pizza': ['thriller', 'horror', 'unique'],
    'Eeram': ['horror', 'thriller', 'emotional'],
}

# Songs Dataset
songs = {
    'Naatu Naatu': ['dance', 'upbeat', 'popular'],
    'Vaathi Coming': ['energetic', 'dance', 'popular'],
    'Pathala Pathala': ['folk', 'fun', 'recent'],
    'Two Two Two': ['romantic', 'peppy', 'recent'],
    'Rowdy Baby': ['dance', 'romantic', 'popular'],
    'Enjoy Enjaami': ['folk', 'unique', 'recent'],
    'Why This Kolaveri': ['fun', 'quirky', 'popular'],
    'Aalaporan Tamizhan': ['patriotic', 'inspiring'],
    'Arabic Kuthu': ['dance', 'trendy', 'recent'],
    'Vaaathi': ['melody', 'inspiring', 'popular'],
    'Thunivu Theme': ['intense', 'action', 'recent'],
    'Marana Mass': ['energetic', 'powerful', 'popular'],
    'Jolly O Gymkhana': ['fun', 'upbeat', 'recent'],
    'Kanave Kanave': ['melody', 'emotional'],
    'Pachai Nirame': ['melody', 'romantic', 'classic'],
    'Aga Naga': ['melody', 'soothing', 'recent'],
    'Kanne Kalaimaane': ['emotional', 'classic', 'melody'],
    'Unakkaga': ['romantic', 'recent', 'emotional'],
    'Verithanam': ['energetic', 'trendy', 'sports'],
    'Maari Thara Local': ['folk', 'fun', 'dance'],
    'Otha Sollala': ['folk', 'quirky', 'popular'],
    'Chinna Chinna Aasai': ['classic', 'inspiring', 'melody'],
    'Uyire Uyire': ['melody', 'romantic', 'classic'],
    'Munbe Vaa': ['melody', 'romantic', 'popular'],
    'Kadhal Sadugudu': ['romantic', 'melody', 'classic'],
    'Naanae Varugiren': ['melody', 'emotional'],
    'Satham Illatha': ['melody', 'inspiring'],
}

# Function to calculate overlap
def calculate_overlap(user_input, features):
    return len(set(features) & set(user_input.split()))

# Recommendation function
def recommend_item(user_input, dataset):
    best_match = None
    max_overlap = 0

    for item, features in dataset.items():
        overlap = calculate_overlap(user_input, features)
        if overlap > max_overlap:
            max_overlap = overlap
            best_match = item

    return best_match

# Main Function
if __name__ == "__main__":
    print("Welcome to the Recommendation System!")
    while True:
        choice = input("\nDo you want a recommendation for 'movie' or 'song'? (type 'exit' to quit): ").lower()
        
        if choice == 'exit':
            print("Thank you for using the recommendation system!")
            break
        
        user_input = input("Enter your preferred genres or keywords (e.g., action, romance, recent): ").lower()
        
        if choice == 'movie':
            recommended_movie = recommend_item(user_input, movies)
            if recommended_movie:
                print(f"Recommended movie for you: {recommended_movie}")
            else:
                print("Sorry, no movie recommendations found for your input.")

        elif choice == 'song':
            recommended_song = recommend_item(user_input, songs)
            if recommended_song:
                print(f"Recommended song for you: {recommended_song}")
            else:
                print("Sorry, no song recommendations found for your input.")

        else:
            print("Invalid choice! Please type 'movie' or 'song'.")