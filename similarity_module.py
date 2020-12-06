#import the required library
from load_dataset_module import retrieve_artist_features, retrieve_music_features
import numpy as np
import sys



def euclidean_similarity(feature_dict, id1, id2):
    #get the required data using the specified ids
    x= feature_dict[id1]
    y= feature_dict[id2]

    #if release_date is in the dict, make sure it is an integer with only the year
    if 'release_date' in x.keys(): x['release_date'] = int(x['release_date'][:4])
    if 'release_date' in y.keys(): y['release_date'] = int(y['release_date'][:4])
    
    #put all the details that are either integer or float into a list
    x_1 = [i for i in x.values() if type(i) == int or type(i) == float]
    y_1 = [i for i in y.values() if type(i) == int or type(i) == float]
    
    #calculate the euclidean distance and return it
    return np.sqrt(sum(np.power(a-b,2) for a, b in zip(x_1, y_1)))



def manhattan_similarity(feature_dict, id1, id2):
    #get the required data using the specified ids
    x= feature_dict[id1]
    y= feature_dict[id2]

    #if release_date is in the dict, make sure it is an integer with only the year
    if 'release_date' in x.keys(): x['release_date'] = int(x['release_date'][:4])
    if 'release_date' in y.keys(): y['release_date'] = int(y['release_date'][:4])

    #put all the details that are either integer or float into a list
    x_1 = [i for i in x.values() if type(i) == int or type(i) == float]
    y_1 = [i for i in y.values() if type(i) == int or type(i) == float]
    
    #calculate the manhattan distance and return it
    return sum(np.abs(a-b) for a,b in zip(x_1,y_1))



def jaccard_similarity(feature_dict, id1, id2):
    #get the required data using the specified ids
    x= feature_dict[id1]
    y= feature_dict[id2]

    #if release_date is in the dict, make sure it is an integer with only the year
    if 'release_date' in x.keys(): x['release_date'] = int(x['release_date'][:4])
    if 'release_date' in y.keys(): y['release_date'] = int(y['release_date'][:4])

    #put all the details that are either integer or float into a list
    x_1 = [i for i in x.values() if type(i) == int or type(i) == float]
    y_1 = [i for i in y.values() if type(i) == int or type(i) == float]

    #get the intersection cardinality and union cardinality of the two lists
    intersection_cardinality = len(set.intersection(*[set(x_1), set(y_1)]))
    union_cardinality = len(set.union(*[set(x_1), set(y_1)]))

    #calculate the jaccard similarity and return it
    return intersection_cardinality/float(union_cardinality)



def cosine_similarity(feature_dict, id1, id2):
    #get the required data using the specified ids
    x= feature_dict[id1]
    y= feature_dict[id2]

    #if release_date is in the dict, make sure it is an integer with only the year
    if 'release_date' in x.keys(): x['release_date'] = int(x['release_date'][:4])
    if 'release_date' in y.keys(): y['release_date'] = int(y['release_date'][:4])

    #put all the details that are either integer or float into a list
    x_1 = [i for i in x.values() if type(i) == int or type(i) == float]
    y_1 = [i for i in y.values() if type(i) == int or type(i) == float]
    
    #get the dot product of the two lists, then the l2 norm of each list
    dot = np.dot(x_1, y_1)
    norma = np.linalg.norm(x_1)
    normb = np.linalg.norm(y_1)
    
    #calculate the cosine similarity and return it
    return dot / (norma * normb)



def pearson_similarity(feature_dict, id1, id2):
    #get the required data using the specified ids
    x= feature_dict[id1]
    y= feature_dict[id2]

    #if release_date is in the dict, make sure it is an integer with only the year
    if 'release_date' in x.keys(): x['release_date'] = int(x['release_date'][:4])
    if 'release_date' in y.keys(): y['release_date'] = int(y['release_date'][:4])

    #put all the details that are either integer or float into a list
    x_1 = [i for i in x.values() if type(i) == int or type(i) == float]
    y_1 = [i for i in y.values() if type(i) == int or type(i) == float]

    #subtract the mean from each element in the list
    x_meaned = x_1 - np.mean(x_1)
    y_meaned = y_1- np.mean(y_1)
    
    #sum the product of the lists after subtracting the mean value
    numerator = sum(x_meaned*y_meaned)
    
    #square the elements in the meaned list, sum each list, multiply them and get the square root
    denominator = np.sqrt(sum(x_meaned**2) * sum(y_meaned**2))
    
    #use the calculated value to compute the pearson similarity and return it
    return numerator / denominator




def main():
    artist_dict = retrieve_artist_features()
    music_dict = retrieve_music_features()

    print("\nWelcome to the app.")

    #make it an infinite loop unless the user qants to quit
    while True:
        #get the user option and make it lower case
        option = input("\nWhat would you like to do: (compare artists, compare musics, quit): ").lower()

        if 'artists' in option:
            # if the user wants to compare artists, get the similarity function to use
            similarity = input("\nWhat similarity function would you like to use? (cosine, jaccard, euclidean, manhattan pearson): ").lower()

            #get the first ID and check if it is valid
            id1 = input("Enter the ID of the first artist you want to compare: ")
            if id1 not in artist_dict.keys():
                print("Invalid ID. Try again")
                continue
        
            #get the second ID and check if it is valid
            id2 = input("Enter the ID of the second artist you want to compare: ")
            if id2 not in artist_dict.keys():
                print("Invalid ID. Try again")
                continue

            #check the similarity function that the user entered, get the return value from the function and print it out
            if  similarity == 'cosine':
                score = cosine_similarity(artist_dict, id1, id2)
                print(f"The cosine similarity between the two artists is {score}.")
            elif  similarity == 'jaccard':
                score = jaccard_similarity(artist_dict, id1, id2)
                print(f"The jaccard similarity between the two artists is {score}.")
            elif  similarity == 'euclidean':
                score = euclidean_similarity(artist_dict, id1, id2)
                print(f"The euclidean similarity between the two artists is {score}.")
            elif  similarity == 'manhattan':
                score = manhattan_similarity(artist_dict, id1, id2)
                print(f"The manhattan similarity between the two artists is {score}.")
            elif  similarity == 'pearson':
                score = pearson_similarity(artist_dict, id1, id2)
                print(f"The pearson similarity between the two artists is {score}.")
            else:
                #if the user entered an invalid similarity function, notify them
                print("Invalid similarity function. Try again.")

        elif 'musics' in option:

            #if the user wants to compare musics, get the similarity function to use
            similarity = input("\nWhat similarity function would you like to use? (cosine, jaccard, euclidean, manhattan pearson): ").lower()
            
            #get the first if and check if it is valid
            id1 = input("Enter the ID of the first music you want to compare: ")
            if id1 not in music_dict.keys():
                print("Invalid ID. Try again")
                continue

            #get the second id and check if it is valid
            id2 = input("Enter the ID of the second music you want to compare: ")
            if id2 not in music_dict.keys():
                print("Invalid ID. Try again")
                continue
            
            #check the similarity function that the user entered, get the return value from the function and print it out
            if  similarity == 'cosine':
                score = cosine_similarity(music_dict, id1, id2)
                print(f"The cosine similarity between the two musics is {score}.")
            elif  similarity == 'jaccard':
                score = jaccard_similarity(music_dict, id1, id2)
                print(f"The jaccard similarity between the two musics is {score}.")
            elif  similarity == 'euclidean':
                score = euclidean_similarity(music_dict, id1, id2)
                print(f"The euclidean similarity between the two musics is {score}.")
            elif  similarity == 'manhattan':
                score = manhattan_similarity(music_dict, id1, id2)
                print(f"The manhattan similarity between the two musics is {score}.")
            elif  similarity == 'pearson':
                score = pearson_similarity(music_dict, id1, id2)
                print(f"The pearson similarity between the two musics is {score}.")
            else:
                #if the user entered an invalid similarity function, notify them
                print("Invalid similarity function. Try again.")
        elif option == 'quit':
            #use sys.exit() to stop the code execution if the user wants to quit
            print("Goodbye.")
            sys.exit()
        else:
            #if the user entered an invalid operation, notify them
            print("Invalid operation. Try again.")



main()