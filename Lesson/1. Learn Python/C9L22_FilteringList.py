def filter_messages(messages):
    clean_log = []
    filter_words_count = []

    for setence in messages:
        counter=0
        good_words=[]
        words = setence.split()
        
        for word in words:
            if word == 'dang':
                counter +=1
            else: good_words.append(word)

        clean_sentence = " ".join(good_words)
        clean_log.append(clean_sentence)
        filter_words_count.append(counter)
        
    return clean_log, filter_words_count


def main():
    pass

main()