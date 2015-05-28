from sys import exit

content = None
with open("mongo.md", "r") as mongo_file:
    content = mongo_file.read()

if content != "# Just use Postgres.":
    print "WRONG WRONG WRONG WHY WHY :("
    exit(1)
print "passes!"
