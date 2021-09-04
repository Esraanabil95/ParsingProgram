# ParsingProgram
Transforming all  formats to unified format with well defined structures.

## Table of Contents:
* xml parsing feature.
* csv parsing feature.
* how to run a local mongo database.
* API to enrich vehicle data by its VIN number.

## Credits:
* Converting XML : https://www.hellocodeclub.com/how-to-convert-xml-to-json-in-python-ultimate-guide/
* Converting CSV : https://www.geeksforgeeks.org/convert-csv-to-json-using-python/
* MongoDB Documentation : https://www.mongodb.com/
* Creating MongoDB : https://medium.com/mongoaudit/how-to-enable-authentication-on-mongodb-b9e8a924efac
* Dealing with ReadMe file : https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/

## How to run a local mongo DB:
1. open bin/mongo.exe
2. create a local DB with name trufla: use trufla
3. create user : db.createUser(
    {
        user: "trufla_admin",
        pwd: "P@ssw0rd",
        roles: [{role: "readWrite", db: "trufla"}]
    }
)
4. to create collections : db.createCollection("xml")  db.createCollection("csv")
