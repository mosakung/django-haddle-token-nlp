from pythainlp.util import isthai
from pythainlp.spell import correct
from spellchecker import SpellChecker

spell = SpellChecker()


def spellCheckEnTh(word):
    fixCase = ['ฯ', 'ๆ']
    for case in fixCase:
        if(word == case):
            return word
    thai = isthai(word)
    if(thai):
        result = correct(word)
    else:
        result = spell.correction(word)
    # if(result != word):
    #     print("SPEEL CHECK DETECT <MODULE> >> " + word + " => " + result)
    return result


def spellcheck_specific_term(word, corpus):
    def minimun_edit_distance(word, compare):
        word_len = len(word)
        compare_len = len(compare)
        dp = [[0 for x in range(compare_len + 1)] for x in range(word_len + 1)]

        for i in range(word_len + 1):
            for j in range(compare_len + 1):

                if i == 0:
                    dp[i][j] = j

                elif j == 0:
                    dp[i][j] = i

                elif word[i-1] == compare[j-1]:
                    dp[i][j] = dp[i-1][j-1]

                else:
                    dp[i][j] = 1 + min(dp[i][j-1],
                                       dp[i-1][j],
                                       dp[i-1][j-1])
        return dp[word_len][compare_len]

    for row in corpus:
        med = minimun_edit_distance(word, row['term'])
        if(med <= int(row['threshold'])):
            # print("SPEEL CHECK DETECT <MY> >> " + word + " => " + row['term'])
            return row['term']

    return word
