from random import randint, uniform,random
from flask import Flask , render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from datetime import date
from datetime import datetime

# initializations
app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ferreycorp'
mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"

@app.route('/')
def Index():

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cliente')
    cur3 = mysql.connection.cursor()
    cur3.execute('SELECT CL.RUC,CL.RAZON_SOCIAL,CL.TELEFONO,CL.CREDITO,CL.CORREO,CL.DIRECCION,P.NUMERO_PEDIDO,P.FECHA_PEDIDO FROM CLIENTE CL, auxpedido P WHERE CL.RUC = P.RUC;') 
    data = cur.fetchall()
    datax = cur3.fetchall()
    cur.close()
    cur3.close()
    return render_template('index.html',cliente = data, clientex = datax )



@app.route('/indexc')
def indexc():
    return render_template( "indexc.html")



@app.route('/css/fonts/css/styless.css')
def css():

   
    return render_template( "css/fonts/css/styless.css")
    


@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        Random = randint(100,300)
        
        today = date.today()
        RUC = request.form['RUC']   
        RAZON_SOCIAL = request.form['RAZON_SOCIAL']
        TELEFONO = request.form['TELEFONO']
        CREDITO = request.form['CREDITO']
        CORREO = request.form['CORREO']
        DIRECCION = request.form['DIRECCION']
        NUMERO_PEDIDO = Random
        FECHA_PEDIDO =  today
        cur = mysql.connection.cursor()
        cur1 = mysql.connection.cursor()
        
        cur.execute("INSERT INTO cliente (RUC, RAZON_SOCIAL, TELEFONO, CREDITO, CORREO, DIRECCION) VALUES (%s,%s,%s,%s,%s,%s)", (RUC, RAZON_SOCIAL,TELEFONO,CREDITO,CORREO,DIRECCION))
        cur1.execute("INSERT INTO auxpedido (NUMERO_PEDIDO, RUC, FECHA_PEDIDO) VALUES (%s,%s,%s)", (NUMERO_PEDIDO, RUC, FECHA_PEDIDO)) 
        
        mysql.connection.commit()
        flash('Contact Added successfully')
        return redirect(url_for('Index'))
        





@app.route('/edit/<string:RUC>', methods = ['POST', 'GET'])
def get_contact(RUC):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cliente WHERE RUC = {0}'.format(RUC))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-contact.html', cliente = data[0])





@app.route('/update/<string:RUC>', methods=['POST'])
def update_contact(RUC):
    if request.method == 'POST':
        RUC = request.form['RUC']   
        RAZON_SOCIAL = request.form['RAZON_SOCIAL']
        TELEFONO = request.form['TELEFONO']
        CREDITO = request.form['CREDITO']
        CORREO = request.form['CORREO']
        DIRECCION = request.form['DIRECCION']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE cliente
            SET RUC = %s,   
                RAZON_SOCIAL = %s,
                TELEFONO = %s,
                CREDITO = %s,
                CORREO = %s,
                DIRECCION = %s

            WHERE RUC = %s
        """, (RUC, RAZON_SOCIAL, TELEFONO, CREDITO, CORREO, DIRECCION, RUC))
        flash('Contact Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('Index'))





@app.route('/delete/<string:RUC>', methods = ['POST','GET'])
def delete_contact(RUC):
    cur = mysql.connection.cursor()
    cur1 = mysql.connection.cursor()
    cur.execute('DELETE FROM auxpedido WHERE RUC = {0}'.format(RUC))
    cur1.execute('DELETE FROM cliente WHERE RUC = {0}'.format(RUC))
    mysql.connection.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('Index'))



@app.route('/join', methods=['POST', 'GET'])
def join():    
        cur3 = mysql.connection.cursor()
        cur3.execute('SELECT CL.RUC,CL.RAZON_SOCIAL,CL.TELEFONO,CL.CREDITO,CL.CORREO,CL.DIRECCION,P.NUMERO_PEDIDO,P.FECHA_PEDIDO FROM CLIENTE CL, auxpedido P WHERE CL.RUC = P.RUC;') 
        datax = cur3.fetchall()
        cur3.close()
        print(datax)
        flash('Contact Added successfully')
        return render_template('index.html',clientex = datax )  
       
        
@app.route('/datos_extrax')
def edit_contactx():
    
    #cur1 = mysql.connection.cursor()
    #cur2 = mysql.connection.cursor()
    cur3 = mysql.connection.cursor()
    #NULL = None

   # cur1.execute('SELECT NUMERO_PEDIDO FROM AUXPEDIDO')
    

    cur3.execute('SELECT CL.RUC,CL.RAZON_SOCIAL,CL.TELEFONO,CL.CREDITO,P.NUMERO_PEDIDO,P.FECHA_PEDIDO,CL.DIRECCION, CL.CORREO , A.FAMILA ,A.MODELO,A.TIPO_PRODUCTO, A.NUMERO_SERIE FROM CLIENTE CL, auxpedido P , tablajproducto A WHERE CL.RUC = P.RUC;') 
    #cur2.execute("INSERT INTO tablajproducto (NUMERO_PEDIDO,NULL) VALUES (%s,%s)", (NULL, NULL))
    
    datat = cur3.fetchall()
    return render_template('index2.html', clientexxx = datat )



@app.route('/datos_extra', methods=['POST'])
def edit_contact():
    
    #cur1 = mysql.connection.cursor()
    #cur2 = mysql.connection.cursor()
    cur3 = mysql.connection.cursor()
    #NULL = None

   # cur1.execute('SELECT NUMERO_PEDIDO FROM AUXPEDIDO')
    

    cur3.execute('SELECT CL.RUC,CL.RAZON_SOCIAL,CL.TELEFONO,CL.CREDITO,P.NUMERO_PEDIDO,P.FECHA_PEDIDO,CL.DIRECCION, CL.CORREO , A.FAMILA ,A.MODELO,A.TIPO_PRODUCTO, A.NUMERO_SERIE FROM CLIENTE CL, auxpedido P , tablajproducto A WHERE CL.RUC = P.RUC;') 
    #cur2.execute("INSERT INTO tablajproducto (NUMERO_PEDIDO,NULL) VALUES (%s,%s)", (NULL, NULL))
    
    datat = cur3.fetchall()
    return render_template('index2.html', clientexxx = datat )
       

@app.route('/agregar_datos', methods=['POST'])
def rellenar_datos():
    if request.method == 'POST':

        FAMILA = request.form['FAMILA']
        MODELO = request.form['MODELO']
        NUMERO_SERIE = request.form['NUMERO_SERIE']
        TIPO_PRODUCTO = request.form['TIPO_PRODUCTO']
        curs = mysql.connection.cursor()
        curs.execute("INSERT INTO tablajproducto (FAMILA, NUMERO_SERIE, MODELO, TIPO_PRODUCTO) VALUES (%s,%s,%s,%s)", (FAMILA, NUMERO_SERIE, MODELO, TIPO_PRODUCTO))
        mysql.connection.commit()
        flash('Contact Added successfully')
        return redirect(url_for('edit_contactx'))









@app.route('/datos_extra3', methods=['POST'])
def edit_contact3():
    
    #cur1 = mysql.connection.cursor()
    #cur2 = mysql.connection.cursor()
    cur3 = mysql.connection.cursor()
    #NULL = None

   # cur1.execute('SELECT NUMERO_PEDIDO FROM AUXPEDIDO')
    

    cur3.execute('SELECT CL.RUC,CL.RAZON_SOCIAL,CL.TELEFONO,CL.CREDITO,P.NUMERO_PEDIDO,P.FECHA_PEDIDO,CL.DIRECCION, CL.CORREO , A.FAMILA ,A.MODELO,A.TIPO_PRODUCTO, A.NUMERO_SERIE FROM CLIENTE CL, auxpedido P , tablajproducto A WHERE CL.RUC = P.RUC;') 
    #cur2.execute("INSERT INTO tablajproducto (NUMERO_PEDIDO,NULL) VALUES (%s,%s)", (NULL, NULL))
    
    datat = cur3.fetchall()
    return render_template('index3.html', clientexxxx = datat )
       


@app.route('/datos_extrax3')
def edit_contactx3():
    
    #cur1 = mysql.connection.cursor()
    #cur2 = mysql.connection.cursor()
    cur3 = mysql.connection.cursor()
    #NULL = None

   # cur1.execute('SELECT NUMERO_PEDIDO FROM AUXPEDIDO')
    

    cur3.execute('SELECT CL.RUC,CL.RAZON_SOCIAL,CL.TELEFONO,CL.CREDITO,P.NUMERO_PEDIDO,P.FECHA_PEDIDO,CL.DIRECCION, CL.CORREO , A.FAMILA ,A.MODELO,A.TIPO_PRODUCTO, A.NUMERO_SERIE FROM CLIENTE CL, auxpedido P , tablajproducto A WHERE CL.RUC = P.RUC;') 
    #cur2.execute("INSERT INTO tablajproducto (NUMERO_PEDIDO,NULL) VALUES (%s,%s)", (NULL, NULL))
    
    datat = cur3.fetchall()
    return render_template('index3.html', clientexxxx = datat )






@app.route('/filtro1', methods=['POST'])
def filtro1():
    
    #cur1 = mysql.connection.cursor()
    #cur2 = mysql.connection.cursor()
    cur3 = mysql.connection.cursor()
    #NULL = None

   # cur1.execute('SELECT NUMERO_PEDIDO FROM AUXPEDIDO')
    

    cur3.execute('SELECT CL.RUC,CL.RAZON_SOCIAL,CL.TELEFONO,CL.CREDITO,P.NUMERO_PEDIDO,P.FECHA_PEDIDO,CL.DIRECCION, CL.CORREO , A.FAMILA ,A.MODELO,A.TIPO_PRODUCTO, A.NUMERO_SERIE FROM CLIENTE CL, auxpedido P , tablajproducto A WHERE CL.RUC = P.RUC AND CL.CREDITO > 8500 AND CL.CREDITO < 15000;') 
    #cur2.execute("INSERT INTO tablajproducto (NUMERO_PEDIDO,NULL) VALUES (%s,%s)", (NULL, NULL))
   
    datatt = cur3.fetchall()
    return render_template('index3.html', filtro = datatt )
       



@app.route('/filtro2', methods=['POST'])
def filtro2():
    
    #cur1 = mysql.connection.cursor()
    #cur2 = mysql.connection.cursor()
    cur4 = mysql.connection.cursor()
    #NULL = None

   # cur1.execute('SELECT NUMERO_PEDIDO FROM AUXPEDIDO')
    

    cur4.execute('SELECT CL.RUC,CL.RAZON_SOCIAL,CL.TELEFONO,CL.CREDITO,P.NUMERO_PEDIDO,P.FECHA_PEDIDO,CL.DIRECCION, CL.CORREO , A.FAMILA ,A.MODELO,A.TIPO_PRODUCTO, A.NUMERO_SERIE FROM CLIENTE CL, auxpedido P , tablajproducto A WHERE CL.RUC = P.RUC AND A.FAMILA = "FAMILIA1";') 
    #cur2.execute("INSERT INTO tablajproducto (NUMERO_PEDIDO,NULL) VALUES (%s,%s)", (NULL, NULL))
   
    datatt = cur4.fetchall()
    return render_template('index3.html', filtro = datatt )



@app.route('/filtro4', methods=['POST'])
def filtro4():
    
    #cur1 = mysql.connection.cursor()
    #cur2 = mysql.connection.cursor()
    cur4 = mysql.connection.cursor()
    #NULL = None

   # cur1.execute('SELECT NUMERO_PEDIDO FROM AUXPEDIDO')
    

    cur4.execute('SELECT NUMERO_PEDIDO, RUC, FECHA_PEDIDO FROM AUXPEDIDO WHERE CURRENT_TIMESTAMP - FECHA_PEDIDO >50;') 
    #cur2.execute("INSERT INTO tablajproducto (NUMERO_PEDIDO,NULL) VALUES (%s,%s)", (NULL, NULL))
   
    datatt = cur4.fetchall()
    return render_template('index3.html', filtroxxx = datatt )


#CONSUTA PL 
@app.route('/filtro5', methods=['POST'])
def filtro5():
    
    #cur1 = mysql.connection.cursor()
    #cur2 = mysql.connection.cursor()
    cur5 = mysql.connection.cursor()
    cur6 = mysql.connection.cursor()
    #NULL = None

   # cur1.execute('SELECT NUMERO_PEDIDO FROM AUXPEDIDO')
    #CONSULTA PLSQL
    cur6.execute('''
    CREATE FUNCTION SUMAR_IGV(MONTO INT) RETURN INT IS
     igv INT;
    PORC_IGV INT := 0.18;
BEGIN
    igv := MONTO * PORC_IGV;
    RETURN igv;
END;''')

    cur5.execute('SELECT NUMERO_PEDIDO, MONTO + SUMAR_IGV(MONTO) AS MONTO_TOTAL FROM PEDIDO;') 
    #cur2.execute("INSERT INTO tablajproducto (NUMERO_PEDIDO,NULL) VALUES (%s,%s)", (NULL, NULL))
   
    datatt = cur5.fetchall()
    return render_template('index3.html', filtroxxx = datatt )







# starting the app
if __name__ == "__main__":
    app.run(port=5000, debug=True)


