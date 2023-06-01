"""
Description:
 Uses a complex data structure to store information about me.

Usage:
 python about_me.py
"""
def main():
    # Step 2: Create a complex data structure that holds information about me
    about_me = {
        # TODO: Put full name into data structure
        # TODO: Put student ID into data structure
        # TODO: Put list of 3 pizza toppings into data structure

        'name' : 'Nadirsha kareem',
        'studentid': '123456789',
        'pizza_topping' : [
            'pineapple',
            'sausage',
            'pepperoni'
        ],
        'movies': [
            # TODO: Change this to a movie you like
            {
                'title': 'The Dark Knight',
                'genre': 'Action'
            },
            {
                'title': 'Ice Age',
                'genre' : 'Animation'
            }
            # TODO: Add one more movie
        ]
    }

    # Step 3: Print student name and ID
    print_student_name_and_id(about_me)

    # Step 4: Print a bullet list of pizza toppings
    print_pizza_toppings(about_me)

    # Step 5: Add pizza toppings to the data structure
    # TODO: Change to pizza toppings you like
    add_pizza_toppings(about_me, ['soylent green', 'racht'])
    print_pizza_toppings(about_me)

    # Step 6: Add another movie to the data structure
    # TODO: Change to a movie you like
    add_movie(about_me, 'The Dictator', 'Comedy')

    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(about_me)

    # Step 8: Print a comma-separated list of movie titles
    print_movie_titles(about_me['movies'])

def print_student_name_and_id(my_info):
    """Prints sentences containing student name and ID

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 3
    # Print sentence containing name
    # Print sentence containing student ID
    fullname = my_info['name']
    firstname = fullname.split()[0]
    print(f"My name is {my_info ['name']}, but you can call me Mr.{firstname}.")
    print(f"My student ID is {my_info['studentid']}.")

def print_pizza_toppings(my_info):
    """Prints a bullet list of favourite pizza toppings

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 4
    # Print header "My favourite pizza toppings are:"
    # Print bullet list of favourite pizza toppings
    print(f"\n my favourite pizza toppings are:")
    for toppings in my_info['pizza_topping'] :
        print(f"- {toppings}")


def add_pizza_toppings(my_info, toppings):
    """Adds some pizza toppings to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        toppings (list): List of pizza toppings
    """
    # TODO: Complete function body per Step 5
    # Append new pizza toppings to end of list 
    # Convert all pizza toppings to lowercase
    # Sort toppings list alphabetically

    my_info['pizza_topping'].extend(toppings)
    for i, toppings in enumerate(my_info['pizza_topping']) :
        my_info ['pizza_topping'][i] = toppings.lower()

    my_info['pizza_topping'].sort()

    return

def add_movie(my_info, title, genre):
    """Adds a movie to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        title (str): Movie title
        genre (str): Movie genre
    """
    # TODO: Complete function body per Step 6
    # Create dictionary for new movie and add to movie list

    new_movie = {
        'title' : title,
        'genre' : genre
    }
    
    my_info['movies'].append(new_movie)

    
    #print (f" {my_info['movies']}")

    return

def print_movie_genres(my_info):
    """Prints a sentence listing all favourite movie genres

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 7

    genrenames = [new_movie['genre'] for new_movie in my_info['movies']]
    allgenre = ', '.join(genrenames)

    print(f"\n I like to watch {allgenre} movies")

def print_movie_titles(movie_list):
    """Prints a sentence listing all favourite movie titles

    Args:
        movie_list (list): List of favourite movies
    """
    # TODO: Complete function body per Step 8
    title_names = [new_movie['title'] for new_movie in movie_list ]
    all_movies = ', '.join(title_names)

    print(f"\n Some of my favourite movies are {all_movies}!")

if __name__ == '__main__':
    main()