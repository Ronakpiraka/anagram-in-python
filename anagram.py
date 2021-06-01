def anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)


n = int(input("Enter number of queries: "))
for a in range(0, n):
    ele1 = input("Enter first word: ")
    ele2 = input("Enter Second word: ")
    print(anagram(ele1,ele2))
#sample input 1 :("cinema", "iceman"))
#sample input 2 :("cool", "loco"))
#sample input 3 :("men", "women"))
