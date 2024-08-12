import pickle

def model_prediction(features):
    
    pickled_model = pickle.load(open('C:/Users/Sakshi Rohida/Desktop/deepak sir ML projects/Employee_turnover/model/Employee_Turnover_prognosis_RandomForest.pkl', 'rb'))
    event = str(list(pickled_model.predict(features)))
    
    return str(f'The event is {event}')

promoted = int(input("Enter promotion"))
review = float(input("Enter review"))
projects = int(input("Enter projects"))
salary = int(input("Enter salary"))
tenure = float(input("Enter tenure"))
satisfaction = float(input("Enter satisfaction"))
bonus = int(input("Enter bonus"))
department_IT = (input("Enter Department"))
department_admin = (input("Enter Department"))
department_engineering = (input("Enter Department Engineering"))
department_finance = (input("Enter Department finanace"))
department_logistics = (input("Enter Department Logistics"))
department_marketing = (input("Enter Department Marketing"))
department_operations = (input("Enter Department Operations"))
department_retail = (input("Enter department retail"))
department_sales = (input("Enter department sales"))
department_support = (input("Enter department support"))
left_yes=input("Enter left yes")
print(model_prediction([[promoted,	review,	projects,salary,tenure,satisfaction	,bonus,	department_IT,	department_admin,	department_engineering,	department_finance,	department_logistics	,department_marketing	,department_operations	,department_retail	,department_sales	,department_support	,left_yes]]))