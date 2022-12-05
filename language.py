import random
import textwrap
import tidy_text

"""Code outline created by Professor Chase Hartemink for CS260. This was modified from it's original purpose
as a markov model based on letters to a markov model based on words.
"""


def run_language():
    """Call `generate_mm_text` with the provided parameters."""
    file_name = "tidy.Marston_mega"
    file_name = "tidy.Jonson_Volpone.txt"
    #file_name = "tidy.Marston_AntonioandMellida.txt"
    order = 2
    M = 250 #num of words to produce
    generated_text = generate_mm_text(file_name, order, M)
    print(generated_text)


def generate_mm_text(file_name, order, M):
    """Create a Markov model for a given text file and output artificially
    generated text from the model.

    Args:
        file_name (str): path of the text to process
        order (int): order of the Markov model
        M (int): the length of the number of characters in the returned generated
        string

    Returns:
        A string of randomly generated text using a Markov model
    """
    # Read the contents of the file
    f = open(file_name, "r")

    if f is None:
        print("Can't open " + file_name)
    else:
        contents = f.read()
        f.close()
        contents = contents.replace("\n", "")
        contents = contents.replace("\r", "")

    # Collect the counts necessary to estimate transition probabilities
    # This dictionary will store all the data needed to estimate the Markov model:
    txt_dict = collect_counts(contents, order)
    display_dict(txt_dict)
    display_dict(txt_dict)
    contents = contents.split(" ")
    # Generate artificial text from the trained model
    seed = "volp: true" #starting word: make sure it is valid and has the same number of words as the Order M
    text = seed.split(" ")

    for _ in range(M): #loops through M words
        next_word = generate_next_character(seed, txt_dict) #generates next word
        text.append(next_word) #adds the word to the text array
        seed = " ".join(text[-order:]) #creates the next seed

    i = 0
    while i < len(text): #this is just used to format lines for plays
        word = text[i]
        if word != "" and (word[-2:] == "._" or word[-1:] == ":"):
            text[i] = "\n" + word
        i +=1

    text = " ".join(text) #turn text array into a string

    # Return the generated text
    return text


def display_dict(txt_dict):
    """Print the text dictionary as a table of keys to counts.
    Currently accepts a dictionary specified by the return documentation in the
    `build_dict` function.

    You will need to modify this function to accept the dictionary returned by
    the `collect_counts` function.

    Arguments:
        txt_dict (dict) - Mapping keys (as strings) to counts (as ints). After
        modification for `collect_counts`, the txt_dict will map keys (as strings)
        to dictionaries of counts and followers described in the return method
        of `collect_counts`.
    """
    print("key\tcount\tfollower counts")
    for key in txt_dict.keys():
        print("%s\t%d\t%s" % ([key], txt_dict[key]["count"], txt_dict[key]["followers"]))


def build_dict(contents, k):
    """Builds a dictionary of k-word (k-word) substring counts. Store the
    dictionary mapping from the k-word to an integer count.

    Args:
        contents (str): the string contents of to count
        k (int): number of characters in the substring

    Returns:
        a text dictionary mapping k-word to an integer
        Example return value with k=2:
        { 
            "hello volpone": 1,
            "lusty greed": 2,
            ... 
        }
    """
    results = {} #results dict
    contents = contents.split(" ")
    length = len(contents) #length of the string with the counting contents
    i = 0 #index to loop through
    while i < length - k: #loops through all word-grams while excluding the last one
        substring = " ".join(contents[i:i+k]) #finds the word-gram for that correpsonding index
        if substring not in results.keys(): #adds word-gram to results dict if its not in there
            results[substring] = 1
        else:
            results[substring] += 1 #if the word-gram is in there, increment by 1
        i += 1 #increment 1

    return results


def collect_counts(contents, k):
    """Build a word-gram dictionary mapping from k-word-gram to a dictionary
    of counts and dictionary of follower counts.
    
    Args:
        contents (str): the string contents to count
        k (int): number of characters in the substring

    Returns:
        a dictionary mapping k-word-gram to a dictionary of counts and dictionary
        of follower counts. Example return value with k=2:
        {
            "ac": {
                "count": 1,
                "followers": {"hello": 1, "celia": 2}
            },
            ...
        }

    Note: This function will similar to `build_dict`. We separated the 
    k-character and follower counting to explain each as distinct concepts. You
    should use the k-character counting code you wrote in `build_dict` as a 
    starting point.

    While the Markov model only needs to use `collect_counts` to generate text,
    our auto-grader will test the behavior of `build_dict` so that function 
    does need to work properly.
    """
    counts = build_dict(contents, k) #gets the counts for the k-word-grams in contents
    results = {} #results dict
    for key in counts.keys(): #adds the results from the counts dict into the results dict
        results[key] = {"count": counts[key], "followers": {}}
    contents = contents.split(" ")
    length = len(contents)
    i = 0
    while i < length - k: #loops through the content (excluding last word gram)
        substring = " ".join(contents[i:i+k]) #k-word-gram
        char = contents[i+k] #char after that word-gram
        if char not in results[substring]["followers"].keys(): #if the char isnt in the followers dict for the word-gram, add it
            results[substring]["followers"][char] = 1
        else: #if the char is in the followers dict for the k-word-gram, increment it by 1
            results[substring]["followers"][char] += 1
        i += 1 #increment the index

    return results


def generate_next_character(seed, txt_dict):
    """Randomly select the next character of a k-wordgram using the follower
    counts to determine the probability.

    Args:
        seed (str): k-wordgram to follow from
        txt_dict (dict): k-wordgram count follower dictionary

    Returns:
        (str) of the next character
    """
    #if seed not in txt_dict.keys():
    #    return "."
    counts = txt_dict[seed]["count"] #number of times the k-word-gram occured (also the denominator for probs)
    followers = [] #this array will hold the chars that follow the word-gram
    probs = []#this will hold the corresponding probabiities for each char
    for follower in txt_dict[seed]["followers"].keys(): #loop through all the follower keys
        followers.append(follower) #add each char to the follower array
        probs.append(txt_dict[seed]["followers"][follower]/counts) #add the corresponding prob to the prob array at the same index

    result = random.choices(followers, weights=probs, k=1) #chooses 1 val from followers given the probs

    return result[0]


if __name__ == "__main__":
    """Main method call, do not modify"""
    run_language()

