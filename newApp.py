#Guided by: https://www.linode.com/docs/guides/create-restful-api-using-python-and-flask/


from flask import Flask, request

app = Flask(__name__)



in_memory_datastore = {
   "COBOL": {"name": "COBOL", "publication_year": 1960, "contribution": "record data"},
   "ALGOL": {"name": "ALGOL", "publication_year": 1958, "contribution": "scoping and nested functions"},
   "APL": {"name": "APL", "publication_year": 1962, "contribution": "array processing"},
   "BASIC": {"name": "BASIC", "publication_year": 1964, "contribution": "runtime interpretation, office tooling"},
   "PL": {"name": "PL", "publication_year": 1966, "contribution": "constants, function overloading, pointers"},
   "SIMULA67": {"name": "SIMULA67", "publication_year": 1967,
                "contribution": "class/object split, subclassing, protected attributes"},
   "Pascal": {"name": "Pascal", "publication_year": 1970,
              "contribution": "modern unary, binary, and assignment operator syntax expectations"},
   "CLU": {"name": "CLU", "publication_year": 1975,
           "contribution": "iterators, abstract data types, generics, checked exceptions"},
}

    

# @app.route('/programmingLang', methods=['GET', 'POST'])

# def programmingLangRoute():
#     if request.method == 'GET':
#         return listProgramLang()
#     elif request.method == 'POST':
#         return createProgramLang(request.get_json(force=True))
    
@app.route('/programmingLang/<programLangName>', methods=['GET', 'PUT', 'DELETE'])

def programmingLangRoute(programLangName):
      if request.method == 'GET':
         return getProgramLang(programLangName)
      elif request.method == 'PUT':
         return updateProgramLang(programLangName, request.get_json(force=True))
      elif request.method == 'DELETE':
         return deleteProgramLang(programLangName)


def listProgramLang():
    beforeYear = request.args.get('beforeYear') or '30000'
    afterYear = request.args.get('afterYear') or '0'
    qualifyingData = list(
        filter(
            lambda pl: int(beforeYear) > pl['publication_year'] > int(afterYear),
            in_memory_datastore.values()
        )
    )
    return {"programmingLang": qualifyingData}


def createProgramLang(newLang):
   langName = newLang['name']
   in_memory_datastore[langName] = newLang
   return newLang

# def updateProgramLang(tName, newLang):
#    updateLang = in_memory_datastore[tName]
#    updateLang.update(newLang)
#    return updateLang

def updateProgramLang(name, newLang):
    if name in in_memory_datastore:
        updateLang = in_memory_datastore[name]
        updateLang.update(newLang)
        return updateLang
    else:
        return {"error": f"Programming language '{name}' not found."}
    
def deleteProgramLang(name):
    deleteLang = in_memory_datastore[name]
    del in_memory_datastore[name]
    return deleteLang


@app.route('/programmingLang/<name>')

def getProgramLang(name):
   return in_memory_datastore[name]
    


if __name__ == '__main__':
   app.run(debug=True)
