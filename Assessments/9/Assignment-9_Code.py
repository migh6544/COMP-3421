import pymongo
from pymongo import MongoClient
import pprint

# Connect to the MongoDB client and select the database and collection
client = MongoClient()
db = client.db_people
peeps = db.thePeople

# Q1: Complete info about people who have 7 children
print("\nQ1 Results:")
for person in peeps.find({"numChildren": 7}):
    pprint.pprint(person)

# Q2: pid, state, and name of the children for people who have 7 children
print("\nQ2 Results:")
for person in peeps.find({"numChildren": 7}, {"pid": 1, "state": 1, "children": 1, "_id": 0}):
    pprint.pprint(person)

# Q3: Complete info of people who live in CA and have 6 children
print("\nQ3 Results:")
for person in peeps.find({"state": "CA", "numChildren": 6}):
    pprint.pprint(person)

# Q4: Complete info of people who live in CA and have 6 or 7 children
print("\nQ4 Results:")
for person in peeps.find({"state": "CA", "numChildren": {"$in": [6, 7]}}):
    pprint.pprint(person)

# Q5: List the pid and children names for all people who have a child whose name contains 'Bob A'
print("\nQ5 Results:")
for person in peeps.find({"children": {"$regex": "Bob A"}}):
    pprint.pprint({"pid": person["pid"], "children": person["children"]})

# Q6: Number of people who have 0, 1, ... 8 children
print("\nQ6 Results:")
pipeline_q6 = [
    {"$group": {
        "_id": "$numChildren",
        "numInGroup": {"$sum": 1}
    }}
]
for result in peeps.aggregate(pipeline_q6):
    pprint.pprint(result)

# Q7: Average salary for each state
print("\nQ7 Results:")
pipeline_q7 = [
    {"$group": {
        "_id": "$state",
        "avgSalary": {"$avg": "$salary"},
        "numInGroup": {"$sum": 1}
    }}
]
for result in peeps.aggregate(pipeline_q7):
    pprint.pprint(result)

# Q8: Average salary and how many people in the grouping for those living in WI state
print("\nQ8 Results:")
pipeline_q8 = [
    {"$match": {"state": "WI"}},
    {"$group": {
        "_id": "$state",
        "avgSalary": {"$avg": "$salary"},
        "numInGroup": {"$sum": 1}
    }}
]
for result in peeps.aggregate(pipeline_q8):
    pprint.pprint(result)

# Q9: Average, min, and max salary for people in Midwest states
midwest_states = ["ND", "SD", "NE", "KS", "MN", "IA", "MS", "WI", "IL", "IN", "MI", "OH"]
print("\nQ9 Results:")
pipeline_q9 = [
    {"$match": {"state": {"$in": midwest_states}}},
    {"$group": {
        "_id": "$state",
        "avgSalary": {"$avg": "$salary"},
        "minSalary": {"$min": "$salary"},
        "maxSalary": {"$max": "$salary"}
    }}
]
for result in peeps.aggregate(pipeline_q9):
    pprint.pprint(result)

# Q10: Average salary in states where the average salary within that state is >= $82,000
print("\nQ10 Results:")
pipeline_q10 = [
    {"$group": {
        "_id": "$state",
        "avgSalary": {"$avg": "$salary"}
    }},
    {"$match": {"avgSalary": {"$gte": 82000}}}
]
for result in peeps.aggregate(pipeline_q10):
    pprint.pprint(result)

# Q11: For Midwest states, average/min/max salary where the average salary > $82,000
print("\nQ11 Results:")
pipeline_q11 = [
    {"$match": {"state": {"$in": midwest_states}}},
    {"$group": {
        "_id": "$state",
        "avgSalary": {"$avg": "$salary"},
        "minSalary": {"$min": "$salary"},
        "maxSalary": {"$max": "$salary"},
        "numInGroup": {"$sum": 1}
    }},
    {"$match": {"avgSalary": {"$gt": 82000}}}
]
for result in peeps.aggregate(pipeline_q11):
    pprint.pprint(result)

# Part 2: Examples of updates and deletes

# Update example (single document)
print("\nUpdate single document example:")
person_before_update = peeps.find_one({"pid": 0})
print("Before update:")
pprint.pprint(person_before_update)
peeps.update_one({"pid": 0}, {"$set": {"age": 25}})
person_after_update = peeps.find_one({"pid": 0})
print("After update:")
pprint.pprint(person_after_update)

# Update example (multiple documents)
print("\nUpdate multiple documents example:")
people_before_update = list(peeps.find({"state": "CA"}).limit(2))
print("Before update:")
pprint.pprint(people_before_update)
peeps.update_many({"state": "CA"}, {"$set": {"salary": 90000}})
people_after_update = list(peeps.find({"state": "CA"}).limit(2))
print("After update:")
pprint.pprint(people_after_update)

# Delete example (more than one document)
print("\nDelete multiple documents example:")
people_before_delete = list(peeps.find({"age": {"$lt": 25}}).limit(2))
print("Before delete:")
pprint.pprint(people_before_delete)
delete_result = peeps.delete_many({"age": {"$lt": 25}})
people_after_delete = list(peeps.find({"age": {"$lt": 25}}).limit(2))
print("After delete:")
pprint.pprint(people_after_delete)
print(f"Documents deleted: {delete_result.deleted_count}")