from flask import Flask, render_template, request, redirect
import json
import psycopg2
# import random

app = Flask(__name__)


def get_connection():
    localhost = 'localhost'
    port = '5432'
    users = 'postgres'
    dbnames = 'fr_test'
    passwords = 'mwmw1225zwzw'
    return psycopg2.connect(
        "host=" + localhost + " port=" + port + " user=" + users + " dbname=" + dbnames + " password=" + passwords)


@app.route('/',methods=['GET','POST'])
def create():
    with get_connection() as conn:
        with conn.cursor() as cur:
            if request.method == 'POST':
                title = request.form.get('title')
                if title != '':
                    sql = "INSERT INTO todolists (title) VALUES (%s)"
                    # val = (title,)
                    cur.execute(sql, (title,))
                    conn.commit()
                    return redirect('/')
            # else:
            #     title = request.args.get('title')
        # with conn.cursor() as cur:
            cur.execute('SELECT * FROM todolists')
            result = cur.fetchall()
            todo_result = dict(result)
    return render_template('todolist.html', result=result, todo_result=todo_result)

# def home():
#     with get_connection() as conn:
#         with conn.cursor() as cur:
#             cur.execute('SELECT * FROM member')
#             results = cur.fetchall()
#             print(results)
#     return render_template('home.html')
@app.route('/detail/<int:id>',)
def delete(id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('DELETE FROM todolists WHERE id = %s',(id,))
            return redirect('/')

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            if request.method == 'POST':
                update_title = request.form.get('update_title')
                if update_title !='':
                    sql = "UPDATE todolists SET title = %s WHERE id = %s"
                    cur.execute(sql, (update_title,id,))
                    conn.commit()
                    return redirect('/')
            sql = 'SELECT * FROM todolists WHERE id = %s'
            cur.execute(sql,(id,))
            result = dict(cur.fetchall())
    return render_template('update.html',result=result,)

@app.route('/abc')
def hello():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM member')
            results = cur.fetchall()
            dic_results = dict(results)
            print(results)
            print(type(dic_results))
            print(dic_results)
            json_results = json.dumps(results, ensure_ascii=False, indent=4)
            # print(json_results)
        with open("en_results.json", "w") as f:
            json.dump(dic_results, f, ensure_ascii=False, indent=4)
    return render_template('abc.html', results=results, json_results=json_results, dic_results=dic_results)


@app.route('/def')
def hello_world():
    dic_result = {}
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM emp')
            results = cur.fetchall()
            print(results)
            id_lists = []  # 取得したresultsのidだけを入れた配列
            name_lists = []
            age_lists = []
            gender_lists = []
            dep_id_lists = []
            for tp_result in results:
                list_result = list(tp_result)  #
                print(list_result)
                list_id = list_result[0]  # list_resultのid
                id_lists.append(list_id)

                list_name = list_result[1]
                name_lists.append(list_name)

                list_age = list_result[2]
                age_lists.append(list_age)

                list_gender = list_result[3]
                gender_lists.append(list_gender)

                list_dep_id = list_result[4]
                dep_id_lists.append(list_dep_id)

                # print(id_lists)
                # dic_result = {}
                id_id = 0
                for id in id_lists:
                    dic_result[id] = {}
                    # for l in list_result:
                    #     print(l)
                    dic_result[id]['name'] = name_lists[id_id]
                    dic_result[id]['age'] = age_lists[id_id]
                    dic_result[id]['gender'] = gender_lists[id_id]
                    dic_result[id]['dep_id'] = dep_id_lists[id_id]
                    id_id += 1
            print(dic_result)
            print(type(dic_result))
            json_results = json.dumps(dic_result, ensure_ascii=False, indent=4)
            print(json_results)
            with open("en_dic_results.json", "w") as f:
                # json.dump(json_results, f, ensure_ascii=False, indent=4)
                json.dump(dic_result, f, ensure_ascii=False, indent=4)

            # dic_result['id'] = {}
            # dic_result['id']['name']='user1'
            # dic_result['id']['age'] = 20
            # print(dic_result)

            # print(results[0][1])
            # print(type(dic_results))
            # print(dic_results)
        #     json_results = json.dumps(results, ensure_ascii=False, indent=4)
        #     # print(json_results)
        # with open("en_results2.json", "w") as f:
        #         # json.dump(json_results, f, ensure_ascii=False, indent=4)
        #         json.dump(dic_results, f, ensure_ascii=False, indent=4)
    return render_template('home.html', dic_result=dic_result, json_results=json_results)

@app.route('/ghi')
def joinenp():
    dic_result = {}
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT id,name,age,gender,dep_name FROM emp INNER JOIN dep ON emp.dep_id = dep.dep_id')
            results = cur.fetchall()
            id_lists = []  # 取得したresultsのidだけを入れたリスト
            name_lists = []
            age_lists = []
            gender_lists = []
            dep_name_lists = []  # 結合するdep_nameのリスト
            for tp_result in results:
                list_result = list(tp_result)  #
                print(list_result)
                list_id = list_result[0]  # list_resultのid
                id_lists.append(list_id)

                list_name = list_result[1]
                name_lists.append(list_name)

                list_age = list_result[2]
                age_lists.append(list_age)

                list_gender = list_result[3]
                gender_lists.append(list_gender)

                list_dep_name = list_result[4]
                dep_name_lists.append(list_dep_name)

                # print(id_lists)
                # dic_result = {}
                id_id = 0
                for id in id_lists:
                    dic_result[id] = {}
                    # for l in list_result:
                    #     print(l)
                    dic_result[id]['name'] = name_lists[id_id]
                    dic_result[id]['age'] = age_lists[id_id]
                    dic_result[id]['gender'] = gender_lists[id_id]
                    dic_result[id]['dep_name'] = dep_name_lists[id_id]
                    id_id += 1
            print(dic_result)
            print(dic_result[10]['name'])
            print(type(dic_result))
            json_results = json.dumps(dic_result, ensure_ascii=False, indent=4)
            print(json_results)
            print(id_lists)
            with open("en_dic_join_results.json", "w") as f:
                # json.dump(json_results, f, ensure_ascii=False, indent=4)
                json.dump(dic_result, f, ensure_ascii=False, indent=4)

    return render_template('hoge.html',results=results,dic_result=dic_result,id_lists=id_lists)