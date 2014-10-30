import os.path, math

def clean_up(s):
    ''' Return a version of string str in which all letters have been
    converted to lowercase and punctuation characters have been stripped 
    from both ends. Inner punctuation is left untouched. '''
    
    punctuation = '''!"',;:.-?)([]<>*#\n\t\r'''
    result = s.lower().strip(punctuation)
    return result

# Test data --AD
t1 = [
        "James Fennimore Cooper\n",
        "Peter, Paul, and Mary\n",
        "James Gosling\n"
    ]
def average_word_length(text):
    ''' Return the average length of all words in text. Do not
    include surrounding punctuation in words. 
    text is a non-empty list of strings each ending in \n.
    At least one line in text contains a word.'''
    
    # Approach:
    # Get a list of all the words present in 'text'
    # Call it 'words'
    # Use clean_up() on each word to remove punctuation
    # Using 'words' calculate required average as:-
    #   length(each_word in words) / length(words)

    words = [clean_up(each_word) for each_sentence in text
     for each_word in each_sentence.split()]

    # Replace each word with its length
    words = [len(each_word) for each_word in words]
    
    average = sum(words) / float(len(words))
    return average
    

def type_token_ratio(text):
    ''' Return the type token ratio (TTR) for this text.
    TTR is the number of different words divided by the total number of words.
    text is a non-empty list of strings each ending in \n.
    At least one line in text contains a word. '''

    # Approach:
    # Get a list of words present in text
    # Call it 'words'. Use set() to get a list of unique words
    # Divide lengths of 'set(words)' by that of 'words'
    # Return the result
    
    words = [clean_up(each_word) for each_sentence in text
             for each_word in each_sentence.split()]
    TTR = len(set(words)) / float(len(words))
    return TTR
    
                
def hapax_legomana_ratio(text):
    ''' Return the hapax_legomana ratio for this text.
    This ratio is the number of words that occur exactly once divided
    by the total number of words.
    text is a list of strings each ending in \n.
    At least one line in text contains a word.'''
    words = [clean_up(each_word) for each_sentence in text
             for each_word in each_sentence.split()]
    seen_once = []
    seen_twice = []

    for index, word in enumerate(words):
        #print "in HLR for block", index, len(words)
        seen_once.append(word)
        words[index] = None
        if word in words:
            seen_twice.append(word)
            #print "in HLR if  block", index, len(words)

    exactly_once = [word for word in seen_once if word not in seen_twice]
    HLR = len(exactly_once) / float(len(words))
    return HLR

# Test data
##org = "Hooray! Finally, we're done."
##o = "Hooray! Finally, we're done."
##sep = '!,'
##res = ['Hooray', ' Finally', " we're done."]
def split_on_separators(original, separators):
    ''' Return a list of non-empty, non-blank strings from the original string
    determined by splitting the string on any of the separators.
    separators is a string of single-character separators.'''
    
    # To do: Complete this function's body to meet its specification.
    # You are not required to keep the two lines below but you may find
    # them helpful. (Hint)

    original__ = str(original)
    split_marker = 'MY_SPLIT_MARKER'
    for each in original__:
        if each in separators:
            original__ = original__.replace(each, split_marker)
    result = original__.split(split_marker)
    
    ## TO DO: Need to find better Impl. Consider using below method
    ## result = [original]
    ## // Code Here
    ## return result

    return result            
t2 = ["The time has come, the Walrus said\n",
            "To talk of many things: of shoes - and ships - and sealing wax,\n",
            "Of cabbages; and kings.\n"
            "And why the sea is boiling hot;\n"
            "and whether pigs have wings.\n"]    
def average_sentence_length(text):
    ''' Return the average number of words per sentence in text.
    text is guaranteed to have at least one sentence.
    Terminating punctuation defined as !?.
    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation
    or beginning or end of file. '''

    terminators = '?!.'

    # Get alllines from text as a huge string. # Need to find better Impl
    all_lines = ''.join(each_line.replace('\n', ' ') for each_line in text)
    sentences = split_on_separators(all_lines, terminators) # Get sentences

    while ' ' in sentences: sentences.remove(' ') # Remove empty sentences

    # Get a list of the words in each sentence
    # Now 'sentences' is a list containing a list (inner_list).
    # Each inner_list is a list of words in that particular sentence
    sentences = [each_sentence.split() for each_sentence in sentences]

    total_words = len([clean_up(each_word) for each_sent in sentences
                             for each_word in each_sent
                             if clean_up(each_word) != ''])
    total_sentences = len(sentences)    
    return float(total_words) / float(total_sentences)

def avg_sentence_complexity(text):
    '''Return the average number of phrases per sentence.
    Terminating punctuation defined as !?.
    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation
    or beginning or end of file.
    Phrases are substrings of a sentences separated by
    one or more of the following delimiters ,;: '''

    sentence_terminators = '?!.'
    phrase_terminators = ',:;'
    # Get alllines from text as a huge string. # Need to find better Impl
    all_lines = ''.join(each_line.replace('\n', ' ') for each_line in text)
    sentences = split_on_separators(all_lines,
                                    sentence_terminators) # Get sentences
    while ' ' in sentences: sentences.remove(' ') # Remove empty sentences

    phrases = [split_on_separators(each_sentence, phrase_terminators)
               for each_sentence in sentences]
    phrase_lengths = [len(each) for each in phrases]
    
    return sum(phrase_lengths) / float(len(phrase_lengths))
    
    
def get_valid_filename(prompt):
    '''Use prompt (a string) to ask the user to type the name of a file. If
    the file does not exist, keep asking until they give a valid filename.
    Return the name of that file.'''
    
    # To do: Complete this function's body to meet its specification.
    filename = raw_input(prompt)
    while not os.path.exists(filename):
        print "That file does not exist."
        filename = raw_input(prompt)
    return filename
    
    # Uncomment and use this statement as many times as needed for input:
    # filename = raw_input(prompt)
    # Uncomment and use this statement as many times as needed for output:
    # print "That file does not exist."
    # Do not use any other input or output statements in this function.

    
def read_directory_name(prompt):
    '''Use prompt (a string) to ask the user to type the name of a directory. If
    the directory does not exist, keep asking until they give a valid directory.
    '''
    
    # To do: Complete this function's body to meet its specification.
    dirname = raw_input(prompt)
    while not os.path.isdir(dirname):
        print "That directory does not exist."
        dirname = raw_input(prompt)
    return dirname

    # Uncomment and use this statement as many times as needed for input:
    # dirname = raw_input(prompt)
    # Uncomment and use this statement as many times as needed for output:
    # print "That directory does not exist."
    # Do not use any other input or output statements in this function.
    
#test compare_signatures(sig1, sig2, weight):
sig1 = ["a_string" , 4.4, 0.1, 0.05, 10.0, 2.0]
sig2 = ["a_string2", 4.3, 0.1, 0.04, 16.0, 4.0]
weight = [0, 11, 33, 50, 0.4, 4]

def compare_signatures(sig1, sig2, weight):
    '''Return a non-negative real number indicating the similarity of two 
    linguistic signatures. The smaller the number the more similar the 
    signatures. Zero indicates identical signatures.
    sig1 and sig2 are 6 element lists with the following elements
    0  : author name (a string)
    1  : average word length (float)
    2  : TTR (float)
    3  : Hapax Legomana Ratio (float)
    4  : average sentence length (float)
    5  : average sentence complexity (float)
    weight is a list of multiplicative weights to apply to each
    linguistic feature. weight[0] is ignored.
    '''

    similarity = []
    sig1_ = sig1[1:]
    sig2_ = sig2[1:]
    weight_ = weight[1:]
    
    for idx, val in enumerate(sig1_):
            similarity.append(abs(sig1_[idx] - sig2_[idx]) * weight_[idx])
    return  sum(similarity)
    

def read_signature(filename):
    '''Read a linguistic signature from filename and return it as 
    list of features. '''
    
    file = open(filename, 'r')
    # the first feature is a string so it doesn't need casting to float
    result = [file.readline()]
    # all remaining features are real numbers
    for line in file:
        result.append(float(line.strip()))
    return result
        

if __name__ == '__main__':
    
    prompt = 'enter the name of the file with unknown author:'
    mystery_filename = get_valid_filename(prompt)

    print "\nReading File...\n"
    # readlines gives us a list of strings one for each line of the file
    text = open(mystery_filename, 'r').readlines()
    print "Calculating Signature...\n"
    
    # calculate the signature for the mystery file
    mystery_signature = [mystery_filename]
    print "Calculating average_word_length..."
    mystery_signature.append(average_word_length(text))

    print "Calculating type_token_ratio..."
    mystery_signature.append(type_token_ratio(text))

    print "Calculating hapax_legomana_ratio..."
    mystery_signature.append(hapax_legomana_ratio(text))

    print "Calculating average_sentence_length..."
    mystery_signature.append(average_sentence_length(text))

    print "Calculating average_sentence_complexity...\n"
    mystery_signature.append(avg_sentence_complexity(text))
    
    weights = [0, 11, 33, 50, 0.4, 4]
    
    prompt = 'enter the path to the directory of signature files: '
    dir = read_directory_name(prompt)
    # every file in this directory must be a linguistic signature
    files = os.listdir(dir)

    # we will assume that there is at least one signature in that directory
    this_file = files[0]
    signature = read_signature('%s/%s'%(dir,this_file))
    best_score = compare_signatures(mystery_signature, signature, weights)
    print signature[0], signature, mystery_signature
    best_author = signature[0]
    for this_file in files[1:]:
        signature = read_signature('%s/%s'%(dir, this_file))
        score = compare_signatures(mystery_signature, signature, weights)
        if score < best_score:
            best_score = score
            best_author = signature[0]
    print "best author match: %s with score %s"%(best_author, best_score)    
    
