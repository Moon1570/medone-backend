from flask import Flask
from flask import Flask, request

app = Flask(__name__)


...
in_memory_datastore = {
   "Sourav": {"name": "Sourav", "birth_year": 1960, "phone": "0123456789"},
   "Afridi": {"name": "Afridi", "birth_year": 1958, "phone": "0123456789"},
   "Moon": {"name": "Moon", "birth_year": 1962, "phone": "01784463101"},
   "Zahid": {"name": "Zahid", "birth_year": 1964, "phone": "0123456789"},
   "Rashed": {"name": "Rashed", "birth_year": 1966, "phone": "0123456789"},
   "Sohag": {"name": "Sohag", "birth_year": 1967, "phone": "0123456789"},
   "Amir": {"name": "Amir", "birth_year": 1970, "phone": "0123456789"},
   "Irfan": {"name": "Irfan", "birth_year": 1975, "phone": "0123456789"},
}
...


#@app.route('/patient/<patient_name>')
#def get_programming_language(patient_name):
#   return in_memory_datastore[patient_name]
    
@app.route('/patient', methods=['GET', 'POST'])
def patient_route():
   if request.method == 'GET':
        return list_patient()
   elif request.method == "POST":
        print(request.get_json(force=True))
        return create_patient(request.get_json(force=True))


def create_patient(new_patient):
   patient_name = new_patient['name']
   in_memory_datastore[patient_name] = new_patient
   return new_patient


...
@app.route('/patient/<patient_name>', methods=['GET', 'PUT'])
def patient_update_route(patient_name):
   if request.method == 'GET':
       return get_patient(patient_name)
   elif request.method == "PUT":
        print(request.get_json(force=True))
        return update_patient(patient_name, request.get_json(force=True))
    
...
def update_patient(name, new_patient_attributes):
   patient_getting_update = in_memory_datastore[name]
   patient_getting_update.update(new_patient_attributes)
   return patient_getting_update
    
...

...
@app.route('/patient/<patient_name>', methods=['GET', 'PUT', 'DELETE'])
def patient_delete_route(patient_name):
   if request.method == 'GET':
       return get_patient(patient_name)
   elif request.method == "PUT":
       return update_patient(patient_name, request.get_json(force=True))
   elif request.method == "DELETE":
       return delete_patient(patient_name)
    
...

...
def delete_patient(patient_name):
   deleting_patient = in_memory_datastore[patient_name]
   del in_memory_datastore[patient_name]
   return deleting_patient
    
...


    

@app.get('/patient')
def list_patient():
   before_year = request.args.get('before_year') or '30000'
   print(before_year)
   after_year = request.args.get('after_year') or '0'
   qualifying_data = list(
       filter(
           lambda pl: int(before_year) > pl['birth_year'] > int(after_year),
           in_memory_datastore.values()
       )
   )

   return {"patient": qualifying_data}

@app.route('/patient/<patient_name>')
def get_patient(patient_name):
   return in_memory_datastore[patient_name]

       
if __name__ == "__main__":
	app.run(debug=True)