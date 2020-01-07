import sys

print(sys.argv[1])

x = len(sys.argv)

if x > 2:
    print("Proram usage error.\nSee /? to understand how to work wish program.")

if sys.argv[1] == '/?':
    print("Usage: python(3 for MacOS) [text file] [length of text]")

