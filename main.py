
from flask import Flask, jsonify, render_template, request
from Sales_data.utils import SalesData

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome to Sales data outlet")
    return "Data Science"
    # return render_template("index.html")

@app.route("/predict_sales")
def get_predicted_sales():
    data = request.form
    print("Data-->",data)

    Item_Weight = eval(data['Item_Weight'])
    Item_Fat_Content = data['Item_Fat_Content']
    Item_Visibility = eval(data['Item_Visibility'])
    Item_MRP = eval(data['Item_MRP'])
    Outlet_Establishment_Year = data['Outlet_Establishment_Year']
    Outlet_Size = data['Outlet_Size']
    Outlet_Location_Type = data['Outlet_Location_Type']
    Item_Type = data['Item_Type']
    Outlet_Type = data['Outlet_Type']

    sal_out = SalesData(Item_Weight,Item_Fat_Content,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Item_Type,Outlet_Type)
    sales = sal_out.get_predicted_sale()

    return jsonify({"Result":f"Predicted sales of particular outlet is {sales} only"})


if __name__ == "__main__":
    app.run(host ='0.0.0.0',port = 5000, debug = True)