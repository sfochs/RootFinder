#Sarah Fochs fochs007
import re

def getStartNum(word):
    if len(word) < 4:
        return 0
    if len(word) == 4:
        return 2
    if len(word) == 5:
        return 3
    if len(word) > 5 and len(word) < 8:
        return 4
    if len(word) >= 8:
        return 5

def getEndNum(word):
    if len(word) < 4:
        return 0
    if len(word) == 4:
        return 2
    if len(word) == 5:
        return 3
    if len(word) > 5 and len(word) < 8:
        return 4
    if len(word) >= 8:
        return 5

def userVerify(word):
    response = input("→ Does '" + word + "' have meaning? Enter Y for yes and N for no:\n")
    response = response.lower()
    if (response == "y"):
        return True
    elif (response != "n"):
        print("Enter Y for yes or N for no")
    else:
        return False

def main():
    run = 1
    infile=open("words.txt", "r")
    content=infile.read()
    infile.close()
    infile2=open("roots.rtf", "r")
    roots=infile2.read()
    infile2.close()
    prefixes = "out mal ante anti circum co de dis em en epi ex extra fore homo hyper il im in infra inter intra intro macro micro mid mis mono multi non omni over para past pre re semi sub super therm trans tri un uni"
    suffixes = "arian ian ial rial acy al ance ence dom er or ism ist ity ty ment ness ship sion tion ate en ify fy ise izeable ible al esque ful ic icalious ous ish ive less ly ward wards wise eer er ion ity ment ness or sion ship th able ible al ant ary ic ious ous ive less y ed en er ing ward wise atic ten s "
    print("\n🦷 🦷 🦷 🦷 🦷 🦷 🦷 🦷 🦷  Welcome to RootCanal 🦷 🦷 🦷 🦷 🦷 🦷 🦷 🦷 🦷")
    print("Use this program to find the roots, affixes, and suffixes of English words! \n")
    while run == 1:
        word = input("Enter a word or press Q to quit program: ")
        word = word.lower()
        startNum = getStartNum(word)
        if (word != 'q'):
            if re.search(r"\b" + re.escape(word) + r"\b", content):
                print("\n--------Checking for Prefixes--------")
                findPrefixes(word, prefixes, suffixes, content, roots, startNum)
            else:
                print("\n" + word + " is not a word\n")
        else:
            run = 0

def findPrefixes(word, prefixes, suffixes, content, roots, startNum):
    if startNum == 5:
        first5 = word[0:5]
        if re.search(r"\b" + re.escape(first5) + r"\b", prefixes):
            base = word[5:len(word)]
            verifyPrefix(word, base, first5, content, prefixes, suffixes, roots, startNum)
        else:
            findPrefixes(word, prefixes, suffixes, content, roots, startNum-1)
    elif startNum == 4:
        first4 = word[0:4]
        if re.search(r"\b" + re.escape(first4) + r"\b", prefixes):
            base = word[4:len(word)]
            verifyPrefix(word, base, first4, content, prefixes, suffixes, roots, startNum)
        else:
            findPrefixes(word, prefixes, suffixes, content, roots, startNum-1)
    elif startNum == 3:
        first3 = word[0:3]
        if re.search(r"\b" + re.escape(first3) + r"\b", prefixes):
            base = word[3:len(word)]
            verifyPrefix(word, base, first3, content, prefixes, suffixes, roots, startNum)
        else:
            findPrefixes(word, prefixes, suffixes, content, roots, startNum-1)
    elif startNum == 2:
        first2 = word[0:2]
        if re.search(r"\b" + re.escape(first2) + r"\b", prefixes):
            base = word[2:len(word)]
            verifyPrefix(word, base, first2, content, prefixes, suffixes, roots, startNum)
        else:
            findPrefixes(word, prefixes, suffixes, content, roots, startNum-1)
    elif startNum == 1:
        first1 = word[0:1]
        if re.search(r"\b" + re.escape(first1) + r"\b", prefixes):
            base = word[1:len(word)]
            verifyPrefix(word, base, first1, content, prefixes, suffixes, roots, startNum)
        else:
            findPrefixes(word, prefixes, suffixes, content, roots, startNum-1)
    else:
        print("\n--------Checking for Prefixes--------")
        endNum = getEndNum(word)
        findSuffixes(word, suffixes, content, roots, endNum)


def findSuffixes(word, suffixes, content, roots, endNum):
    if endNum == 5:
        last5 = word[len(word)-5:len(word)]
        if re.search(r"\b" + re.escape(last5) + r"\b", suffixes):
            base = word[0:(len(word)-5)]
            verifySuffix(word, base, last5, content, suffixes, roots, endNum)
        else:
            findSuffixes(word, suffixes, content, roots, endNum-1)
    elif endNum == 4:
        last4 = word[len(word)-4:len(word)]
        if re.search(r"\b" + re.escape(last4) + r"\b", suffixes):
            base = word[0:(len(word)-4)]
            verifySuffix(word, base, last4, content, suffixes, roots, endNum)
        else:
            findSuffixes(word, suffixes, content, roots, endNum-1)
    elif endNum == 3:
        last3 = word[len(word)-3:len(word)]
        if re.search(r"\b" + re.escape(last3) + r"\b", suffixes):
            base = word[0:(len(word)-3)]
            verifySuffix(word, base, last3, content, suffixes, roots, endNum)
        else:
            findSuffixes(word, suffixes, content, roots, endNum-1)
    elif endNum == 2:
        last2 = word[len(word)-2:len(word)]
        if re.search(r"\b" + re.escape(last2) + r"\b", suffixes):
            base = word[0:(len(word)-2)]
            verifySuffix(word, base, last2, content, suffixes, roots, endNum)
        else:
            findSuffixes(word, suffixes, content, roots, endNum-1)
    elif endNum == 1:
        last1 = word[len(word)-1:len(word)]
        if re.search(r"\b" + re.escape(last1) + r"\b", suffixes):
            base = word[0:(len(word)-1)]
            verifySuffix(word, base, last1, content, suffixes, roots, endNum)
        else:
            findSuffixes(word, suffixes, content, roots, endNum-1)
    else:
        print("\n🌳 " + word + " is a root\n")


def verifyPrefix(word, base, prefix, content, prefixes, suffixes, roots, startNum):
    print("Checking: " + prefix + " - " + base)
    if (re.search(r"\b" + re.escape(base) + r"\b", content) or re.search(r"\b" + re.escape(base) + r"\b", roots)) or (userVerify(base) == True):
        print("\n⭐️ " + word + " has the prefix '" + prefix + "'\n")
        startNum = getStartNum(base)
        findPrefixes(base, prefixes, suffixes, content, roots, startNum)
    else:
        findPrefixes(word, prefixes, suffixes, content, roots, startNum-1)


def verifySuffix(word, base, suffix, content, suffixes, roots, endNum):
    print("Checking: " + base + " - " + suffix)
    if (re.search(r"\b" + re.escape(base) + r"\b", content)) or (re.search(r"\b" + re.escape(base) + r"\b", roots)) or (userVerify(base) == True):
        print("\n⭐️ " + word + " has the suffix '" + suffix + "'\n")
        endNum = getEndNum(base)
        findSuffixes(base, suffixes, content, roots, endNum)
    else:
        findSuffixes(word, suffixes, content, roots, endNum-1)


if __name__ == '__main__':
    main()

