#Sarah Fochs fochs007
import re

def main():
    infile=open("words.txt", "r")
    content=infile.read()
    infile.close()
    infile2=open("roots.rtf", "r")
    roots=infile2.read()
    infile2.close()
    prefixes = "out mal ante anti circum co de dis em en epi ex extra fore homo hyper il im in infra inter intra macro micro mid mis mono multi non omni over para past pre re semi sub super therm trans tri un uni"
    suffixes = "arian ian acy al ance ence dom er or ism ist ity ty ment ness ship sion tion ate en ify fy ise izeable ible al esque ful ic icalious ous ish ive less ly ward wards wise eer er ion ity ment ness or sion ship th able ible al ant ary ic ious ous ive less y ed en er ing ward wise atic ten"
    word = input("Enter a word: ")
    if re.search(r"\b" + re.escape(word) + r"\b", content):
        findPrefixes(word, prefixes, suffixes, content, roots)
    else:
        print("\n" + word + " is not a word\n")


def findPrefixes(word, prefixes, suffixes, content, roots):
    print("\n ❤️🧡💛💚💙💜 CHECKING FOR PREFIXES 💜💙💚💛🧡❤️")
    if len(word) < 4:
        print("\n" + word + " is a base or root\n")
        findSuffixes(word, suffixes, content, roots)
    if len(word) == 4:
        first2 = word[0:2]
        first1 = word[0:1]
        if re.search(r"\b" + re.escape(first2) + r"\b", prefixes):
            base = word[2:len(word)]
            verifyPrefix(word, base, first2, content, prefixes, suffixes, roots)
        elif re.search(r"\b" + re.escape(first1) + r"\b", prefixes):
            base = word[1:len(word)]
            verifyPrefix(word, base, first1, content, prefixes, suffixes, roots)
        else:
            print("\n" + word + " is a base or root\n")
            findSuffixes(word, suffixes, content, roots)
    if len(word) == 5:
        first3 = word[0:3]
        first2 = word[0:2]
        first1 = word[0:1]
        if re.search(r"\b" + re.escape(first3) + r"\b", prefixes):
            base = word[3:len(word)]
            verifyPrefix(word, base, first3, content, prefixes, suffixes, roots)
        elif re.search(r"\b" + re.escape(first2) + r"\b", prefixes):
            base = word[2:len(word)]
            verifyPrefix(word, base, first2, content, prefixes, suffixes, roots)
        elif re.search(r"\b" + re.escape(first1) + r"\b", prefixes):
            base = word[1:len(word)]
            verifyPrefix(word, base, first1, content, prefixes, suffixes, roots)
        else:
            print("\n" + word + " is a base or root\n")
            findSuffixes(word, suffixes, content, roots)
    if len(word) == 6:
        first4 = word[0:4]
        first3 = word[0:3]
        first2 = word[0:2]
        first1 = word[0:1]
        if re.search(r"\b" + re.escape(first4) + r"\b", prefixes):
            base = word[4:len(word)]
            verifyPrefix(word, base, first4, content, prefixes, suffixes, roots)
        elif re.search(r"\b" + re.escape(first3) + r"\b", prefixes):
            base = word[3:len(word)]
            verifyPrefix(word, base, first3, content, prefixes, suffixes, roots)
        elif re.search(r"\b" + re.escape(first2) + r"\b", prefixes):
            base = word[2:len(word)]
            verifyPrefix(word, base, first2, content, prefixes, suffixes, roots)
        elif re.search(r"\b" + re.escape(first1) + r"\b", prefixes):
            base = word[1:len(word)]
            verifyPrefix(word, base, first1, content, prefixes, suffixes, roots)
        else:
            print("\n" + word + " is a base or root\n")
            findSuffixes(word, suffixes, content, roots)
    if len(word) > 6:
        first5 = word[0:5]
        first4 = word[0:4]
        first3 = word[0:3]
        first2 = word[0:2]
        first1 = word[0:1]
        if re.search(r"\b" + re.escape(first5) + r"\b", prefixes):
            base = word[5:len(word)]
            verifyPrefix(word, base, first5, content, prefixes, suffixes, roots)
        elif re.search(r"\b" + re.escape(first4) + r"\b", prefixes):
            base = word[4:len(word)]
            verifyPrefix(word, base, first4, content, prefixes, suffixes, roots)
        elif re.search(r"\b" + re.escape(first3) + r"\b", prefixes):
            base = word[3:len(word)]
            verifyPrefix(word, base, first3, content, prefixes, suffixes, roots)
        elif re.search(r"\b" + re.escape(first2) + r"\b", prefixes):
            base = word[2:len(word)]
            verifyPrefix(word, base, first2, content, prefixes, suffixes, roots)
        elif re.search(r"\b" + re.escape(first1) + r"\b", prefixes):
            base = word[1:len(word)]
            verifyPrefix(word, base, first1, content, prefixes, suffixes, roots)
        else:
            print("\n" + word + " is a base or root\n")
            findSuffixes(word, suffixes, content, roots)


def findSuffixes(word, suffixes, content, roots):
    print("\n ❤️🧡💛💚💙💜 CHECKING FOR SUFFIXES 💜💙💚💛🧡❤️")
    if len(word) < 4:
        print("\n" + word + " is a base or root\n")
    if len(word) == 4:
        last2 = word[len(word)-2:len(word)]
        last1 = word[len(word)-1:len(word)]
        if re.search(r"\b" + re.escape(last2) + r"\b", suffixes):
            base = word[0:(len(word)-2)]
            verifySuffix(word, base, last2, content, suffixes, roots)
            print(2)
        elif re.search(r"\b" + re.escape(last1) + r"\b", suffixes):
            base = word[0:(len(word)-1)]
            verifySuffix(word, base, last1, content, suffixes, roots)
            print(1)
        else:
            print("\n" + word + " is a base or root\n")
    if len(word) == 5:
        last3 = word[len(word)-3:len(word)]
        last2 = word[len(word)-2:len(word)]
        last1 = word[len(word)-1:len(word)]
        if re.search(r"\b" + re.escape(last2) + r"\b", suffixes):
            base = word[0:(len(word)-2)]
            verifySuffix(word, base, last2, content, suffixes, roots)
            print(2)
        elif re.search(r"\b" + re.escape(last3) + r"\b", suffixes):
            base = word[0:(len(word)-3)]
            verifySuffix(word, base, last3, content, suffixes, roots)
            print(3)
        elif re.search(r"\b" + re.escape(last1) + r"\b", suffixes):
            base = word[0:(len(word)-1)]
            verifySuffix(word, base, last1, content, suffixes, roots)
            print(1)
        else:
            print("\n" + word + " is a base or root\n")
    if len(word) > 5:
        last4 = word[len(word)-4:len(word)]
        last3 = word[len(word)-3:len(word)]
        last2 = word[len(word)-2:len(word)]
        last1 = word[len(word)-1:len(word)]
        if re.search(r"\b" + re.escape(last3) + r"\b", suffixes):
            base = word[0:(len(word)-3)]
            print(3)
            verifySuffix(word, base, last3, content, suffixes, roots)
        elif re.search(r"\b" + re.escape(last4) + r"\b", suffixes):
            base = word[0:(len(word)-4)]
            print(4)
            verifySuffix(word, base, last4, content, suffixes, roots)
        elif re.search(r"\b" + re.escape(last2) + r"\b", suffixes):
            base = word[0:(len(word)-2)]
            print(2)
            verifySuffix(word, base, last2, content, suffixes, roots)
        elif re.search(r"\b" + re.escape(last1) + r"\b", suffixes):
            base = word[0:(len(word)-1)]
            print(1)
            verifySuffix(word, base, last1, content, suffixes, roots)
        else:
            print("\n" + word + " is a base or root\n")
    if len(word) > 8:
        last5 = word[len(word)-5:len(word)]
        last4 = word[len(word)-4:len(word)]
        last3 = word[len(word)-3:len(word)]
        last2 = word[len(word)-2:len(word)]
        last1 = word[len(word)-1:len(word)]
        if re.search(r"\b" + re.escape(last3) + r"\b", suffixes):
            base = word[0:(len(word)-3)]
            print(3)
            verifySuffix(word, base, last3, content, suffixes, roots)
        elif re.search(r"\b" + re.escape(last4) + r"\b", suffixes):
            base = word[0:(len(word)-4)]
            print(4)
            verifySuffix(word, base, last4, content, suffixes, roots)
        elif re.search(r"\b" + re.escape(last5) + r"\b", suffixes):
            base = word[0:(len(word)-5)]
            print(5)
            verifySuffix(word, base, last5, content, suffixes, roots)
        elif re.search(r"\b" + re.escape(last2) + r"\b", suffixes):
            base = word[0:(len(word)-2)]
            print(2)
            verifySuffix(word, base, last2, content, suffixes, roots)
        elif re.search(r"\b" + re.escape(last1) + r"\b", suffixes):
            base = word[0:(len(word)-1)]
            print(1)
            verifySuffix(word, base, last1, content, suffixes, roots)
        else:
            print("\n" + word + " is a base or root\n")


def verifyPrefix(word, base, prefix, content, prefixes, suffixes, roots):
    print("Checking: " + prefix + " - " + base)
    if re.search(r"\b" + re.escape(base) + r"\b", content) or re.search(r"\b" + re.escape(base) + r"\b", roots):
        print("\n" + word + " has the prefix '" + prefix + "'\n")
        findPrefixes(base, prefixes, suffixes, content, roots)
    else:
        print("\n" + word + " does not have the prefix '" + prefix + "'\n")
        findSuffixes(word, suffixes, content, roots)


def verifySuffix(word, base, suffix, content, suffixes, roots):
    print("Checking: " + base + " - " + suffix)
    if re.search(r"\b" + re.escape(base) + r"\b", content) or re.search(r"\b" + re.escape(base) + r"\b", roots):
        print("\n" + word + " has a suffix '" + suffix + "'\n")
        findSuffixes(base, suffixes, content, roots)
    else:
        print("\n" + word + " may not have the suffix '" + suffix + "'\n")
        print("\n" + word + " is a base or root\n")


if __name__ == '__main__':
    main()
