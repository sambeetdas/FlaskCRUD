from flask import Flask, request, jsonify
from query_handler import query_handler
from util_handler import util_handler



app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/authtoken', methods=[ 'POST' ])
def AuthToken():
    obj = {}
    try:
        body = request.get_json(force=True)
        username = str(body.get('username', ''))
        password = str(body.get('password', ''))
        valid_for = int(body.get('validfor', 60))

        if (username == '' or password == ''):
            return("Credentials are empty or missing")
        else:
            obj_query = query_handler()
            query = obj_query.auth(username,password)
            obj_util = util_handler()
            rows = obj_util.execute(query,False)
            result = obj_util.convert_data_to_json(rows)
            if (int(result[0]['Count']) == 0):
                return("Invalid Credentials")
            else:
                token = obj_util.GetAuthToken(username, password, valid_for)
            
            obj["result"] = {"AccessToken" : token}
    except Exception as e:
        return(str(e))
    return jsonify(obj)

@app.route('/insert', methods=[ 'POST' ])
def InsertData():
    obj = {}
    try:
        token = request.headers.get('Token','')
        if (token != ''):
            obj_util = util_handler()
            obj_query = query_handler()

            cred = obj_util.ExtractAuthToken(token)
            if (obj_util.DateValidation(cred[3]) == False):
                return("Token Expired ")
            query = obj_query.auth(cred[0],cred[1])
            rows = obj_util.execute(query,False)
            result = obj_util.convert_data_to_json(rows)
            if (int(result[0]['Count']) == 0):
                return("Access Token is Invalid. Please pass {Token: '<Valid Token>'} ")
            else:
                body = request.get_json(force=True)
                name = str(body.get('name', ''))
                phonenumber = str(body.get('phonenumber', ''))

                if (name != '' and phonenumber != ''):
                
                    query = obj_query.insert(name, phonenumber)
                
                    rows = obj_util.execute(query,True)
                    result = obj_util.convert_data_to_json(rows)
                    obj["result"] = result
        else:
            return("Access Token is missing is the header. Please pass Token: '<Valid Token>' ")

    except Exception as e:
        return(str(e))
    
    return jsonify(obj)

@app.route('/get', methods=[ 'GET' ])
@app.route('/get/<int:id>', methods=[ 'GET' ])
def GetData(id = 0):
    obj = {}
    try:
        token = request.headers.get('Token','')
        if (token != ''):
            obj_util = util_handler()
            obj_query = query_handler()

            cred = obj_util.ExtractAuthToken(token)
            if (obj_util.DateValidation(cred[3]) == False):
                return("Token Expired ")
            query = obj_query.auth(cred[0],cred[1])
            rows = obj_util.execute(query,False)
            result = obj_util.convert_data_to_json(rows)
            if (int(result[0]['Count']) == 0):
                return("Access Token is Invalid. Please pass {Token: '<Valid Token>'} ")
            else:
                if(id == 0):
                    query = obj_query.get_all()
                else:
                    query = obj_query.get_by_id(id)

                rows = obj_util.execute(query,False)
                result = obj_util.convert_data_to_json(rows)
                obj["result"] = result
        else:
            return("Access Token is missing is the header. Please pass Token: '<Valid Token>' ")
      
    except Exception as e:
        return(str(e))   
    return jsonify(obj)

@app.route('/delete/<int:id>', methods=[ 'DELETE' ])
def DeleteData(id = 0):
    obj = {}
    try:
        token = request.headers.get('Token','')
        if (token != ''):
            obj_util = util_handler()
            obj_query = query_handler()

            cred = obj_util.ExtractAuthToken(token)
            if (obj_util.DateValidation(cred[3]) == False):
                return("Token Expired ")
            query = obj_query.auth(cred[0],cred[1])
            rows = obj_util.execute(query,False)
            result = obj_util.convert_data_to_json(rows)
            if (int(result[0]['Count']) == 0):
                return("Access Token is Invalid. Please pass {Token: '<Valid Token>'} ")
            else:
                query = obj_query.delete(id)
                rows = obj_util.execute(query,True)
                result = obj_util.convert_data_to_json(rows)
                obj["result"] = result
        else:
            return("Access Token is missing is the header. Please pass Token: '<Valid Token>' ")
    except Exception as e:
        return(str(e))   
    return obj

@app.route('/update/<int:id>', methods=[ 'PUT' ])
def UpdateDate(id = 0):
    obj = {}
    try:
        token = request.headers.get('Token','')
        if (token != ''):
            obj_util = util_handler()
            obj_query = query_handler()

            cred = obj_util.ExtractAuthToken(token)
            if (obj_util.DateValidation(cred[3]) == False):
                return("Token Expired ")
            query = obj_query.auth(cred[0],cred[1])
            rows = obj_util.execute(query,False)
            result = obj_util.convert_data_to_json(rows)
            if (int(result[0]['Count']) == 0):
                return("Access Token is Invalid. Please pass {Token: '<Valid Token>'} ")
            else:
                body = request.get_json(force=True)
                name = str(body.get('name', ''))
                phonenumber = str(body.get('phonenumber', ''))

                if (name != '' and phonenumber != ''):
                    query = obj_query.update(name,phonenumber,id)
                    rows = obj_util.execute(query,True)
                    result = obj_util.convert_data_to_json(rows)
                    obj["result"] = result
        else:
            return("Access Token is missing is the header. Please pass Token: '<Valid Token>' ")

    except Exception as e:
        return(str(e))
    
    return jsonify(obj)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
