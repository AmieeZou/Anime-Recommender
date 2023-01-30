'''
from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("sound.wav")
play(song)

'''
import pandas as pd
import time


def print_instructions():
    """
    Prints out instructions for users of how to user the anime recommender.
    """
    print("Welcome to the anime recommender!")
    time.sleep(2)
    print("You will need to answer several questions to figure out what is your potential favorite anime! ")
    time.sleep(2)
    print("Try to answer as much of the questions as you could, so that you can get the most accurate results.")
    time.sleep(2)
    print("Lets get started!")


def anime_search():
    """
    Display questions regarding anime to the users
    User will make choices based on their preferences

    """
    desired_anime = []
    # Dictionary for Genre
    genre_dict = {"A": "Action", "B": 'Adventure', "C": "Comedy", "D": "Drama", "F": "Fantasy", "S": "Sci-Fi",
                  "T": "School", "R": "Romance", "null": "null"}
    # Dictionary for Rating
    rating_dict = {"G": "All Ages", "PG": "Children", "PG-13": "Teens 13 or older", "R": "17+ (violence & profanity)",
                   "R+": "Mild Nudity", "null": "null"}
    # Dictionary for Source
    source_dict = {"O": "Original", "M": "Manga", "null": "null"}
    # Dictionary for Score
    score_dict = {"7": "7", "5": "5", "null": "null"}
    # Dictionary for Year
    year_dict = {"1": (2010, 2023), "2": (2000, 2010), "3": (1990, 2001), "4": (1980, 1991), "null": "null"}
    # Game Start

    # Question1 :Score
    while True:
        q1 = input("Do you have a score preference for the anime? \n"
                   "Put in '7' for choosing all anime that has a rating higher than or equals to 7; \n"
                   "'5' for choosing all anime that has a rating higher than or equals to 5; \n"
                   "and 'null' for not filtering any anime based on their scores. \n")
        if q1 == "null":
            break
        else:
            #score_value = float(score_dict.get(q1))
            score_value = score_dict.get(q1)
            if score_value is None:
                print("Sorry, you have an invalid answer. Please try again.")
            elif score_value is not None:
                score_value = float(score_value)
                desired_anime.append(score_value)
                break


    # Question2: Genre preferences
    while True:
        q2 = input("What kind of anime genre do you prefer?\n"
                   "Please choose the following options: \n"
                   "A: Action, B: Adventure, C: Comedy, D: Drama, F: Fantasy, S: Sci-Fi, T: School, R: Romance \n"
                   "and 'null' for not filtering any anime based on their genres. \n")
        # add the filtered genre value to empty lists
        genre_value = genre_dict.get(q2)
        if genre_value is None:
            print("Sorry, you have an invalid answer. Please try again.")
        elif genre_value is not None:
            break
    desired_anime.append(genre_value)
    # Question3: Rating
    while True:
        q3 = input("What type of anime do you prefer? Please type in the answer: \n"
                   "G: All Ages \n"
                   "PG: Children \n"
                   "PG-13: Teens 13 or older \n"
                   "R : 17+ (violence & profanity) \n"
                   "R+ : Mild Nudity \n"
                   "and 'null' for not filtering any anime based on their type. \n")
        rating_value = rating_dict.get(q3)
        if rating_value is None:
            print("Sorry, you have an invalid answer. Please try again.")
        elif rating_value is not None:
            break
    desired_anime.append(rating_value)

    # Question4: Source
    while True:
        q4 = input("Do you prefer original anime or anime based on manga?\n"
                   "Please answer 'O' for original, or 'M' for Manga to this question. \n"
                   "and 'null' for not filtering any anime based on their scores.\n")
        source_value = source_dict.get(q4)
        if source_value is None:
            print("Sorry, you have an invalid answer. Please try again.")
        elif source_value is not None:
            break
    desired_anime.append(source_value)

    # Question5: Time period preferences
    while True:
        q5 = input("Of which time period of anime are you looking for? Please select: \n"
                   "1: Year 2010-2022 \n"
                   "2: Year 2000-2010 \n"
                   "3: Year 1990-2000 \n"
                   "4: Year 1980-1990 \n"
                   "and 'null' for not filtering any anime based on their premiered year. \n")
        year_value = year_dict.get(q5)
        if year_value is None:
            print("Sorry, you have an invalid answer. Please try again.")
        elif year_value is not None:
            break
    desired_anime.append(year_value)

    return desired_anime


def filter_data(df, wishlist):
    # Put score as the 1st item in the list
    score = wishlist[0]
    print(wishlist[0])
    # Filter the selected score out
    if score == "null":
        pass
    elif score != "null":
        filtered_data = df[df["Score"] >= float(score)]
    print(filtered_data)
    # Put Genre as the 2nd item in the list
    genre = wishlist[1]
    # Filter the selected genre out
    if score == "null":
        pass
    elif genre != "null":
        filtered_data = filtered_data[filtered_data["Genres"].str.contains(genre)]
        print(filtered_data)
    print(filtered_data)
    # Put rating as the 3rd item in the list
    rating = wishlist[2]
    # Filter the selected type out
    if rating == "null":
        pass
    elif rating != "null":
        filtered_data = filtered_data[filtered_data["Rating"].str.contains(rating)]
    print(filtered_data)
    # Put source as the 4th item in the list
    source = wishlist[3]
    # Filter source as the third selected item out
    if source == "null":
        pass
    elif source != "null":
        filtered_data = filtered_data[filtered_data["Source"].str.contains(source)]
    print(filtered_data)
    # Put Year as the 5th item in the list
    year = wishlist[4]
    start_year = year[0]
    end_year = year[1]
    if year == "null":
        pass
    elif year != "null":
        filtered_data = filtered_data[(filtered_data["Year"] >= start_year) & (filtered_data["Year"] < end_year)]
    print(filtered_data)
    print("This is the end of filtered_data function!")
    return filtered_data


def main():
    """
    Main Function.
    Reads the data from anime csv file, and
    filter out a desired anime recommendation list for users.
   """
    # read the UPDATED anime data
    anime = pd.read_csv("anime_updated.csv")
    # get and set user's name
    username = input("Hello! What is your name? \n")
    # Greet the user
    print("Hello " + str(username) + "!")
    # print the anime user interface instructions
    time.sleep(1)
    print_instructions()
    time.sleep(1)
    while True:
        # start the anime_search engine
        desired_anime = anime_search()
        filtered_data = filter_data(anime, desired_anime)
        # print(filtered_data.columns)
        # Convert the dataframe into a list
        print("Based on your answers, here is your recommended list:")
        final_list = filtered_data["Name"].tolist()
        # Check if the list is empty
        if len(final_list) == 0:
            print("Unfortunately, no anime is found based on your input. Please try again.")
        else:
            for i in final_list:
                print(i, end="\n")
        # Ask the user if they want to use the recommender again
        time.sleep(1)
        userinput = input("Would you like to user the recommender again? \n"
                          "Please answer 'Y' for yes, 'N' for No.")
        userinput = userinput.upper().strip()
        # if the user wants to leave
        if userinput == 'N':
            print("Thank you for using the anime recommender! Goodbye and have a great day!")
            break


if __name__ == '__main__':
    main()
