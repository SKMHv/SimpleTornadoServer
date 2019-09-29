# ===============================================
# SQL_DB :
# - SQL_connect(host, user, heslo, databaza)
# - SQL_disconnect()
# - SQL_hladaj(table, co, hodnota, stlpce)
# - SQL_zapis(sql)
# - SQL_historia(pouzivatelia_id, operacia)
# ===============================================

import pymysql
#import datetime

def SQL_connect(host, user, heslo, databaza):
    """
    Pripoji sa k danej databaze self.db
    :return:
    """
    print('/===============================================\\')
    print('START -> SQL_connect')
    print('--------------------')
    global SQL_conn
    SQL_conn = pymysql.connect(host=host,
                                user=user,
                                password=heslo,
                                db=databaza,
                                charset='utf8mb4',
                                autocommit=True,
                                cursorclass=pymysql.cursors.DictCursor)

def SQL_disconnect():
    print('/===============================================\\')
    print('START -> SQL_disconect')
    print('--------------------')
    SQL_conn.close()


def SQL_hladaj(sql):
    """
    Vyhlada pouzivatela podla email.
    :param email: email pouzivatela
    :return: pouzivatel s atributmi
    """
    print('/===============================================\\')
    print('START -> SQL_hladaj')
    print('-------------------')

    print(sql)
    try:
        with SQL_conn:
            cursor = SQL_conn.cursor()
            cursor.execute(sql)
            vysledok = cursor.fetchone()
            # id, meno = cursor.fetchone()
            # print(vysledok)
            # for columm in  vysledok:
            #     print(columm)
            # print(id, meno)
            print('Vraciam vysledok z hladania')
            return vysledok

    finally:
        print()
        #teraz = datetime.datetime.now()
        #print(teraz)


def SQL_zapis(sql):
    """
    Funkcia zapise hodnoty do tabulky podla sql parametra
    :param sql:
    :return:
    """
    print('/===============================================\\')
    print('START -> SQL_zapis')
    print('------------------')

    #print(sql)
    try:
        with SQL_conn:
            cursor = SQL_conn.cursor()
            cursor.execute(sql)
            #print('Pred commit historia')
            SQL_conn.commit()
    # except pymysql.err.InternalError as err:
    #     code, message = err.args[0], err.args[1]
    #     print('Error: ', code, message)

    finally:
        print()
        #print('Po commit historia')


def SQL_vymaz(sql):
    """
    Funkcia vymaze hodnoty do tabulky podla sql parametra
    :param sql:
    :return:
    """
    print('/===============================================\\')
    print('START -> SQL_vymaz')
    print('------------------')

    #print(sql)
    try:
        with SQL_conn:
            cursor = SQL_conn.cursor()
            cursor.execute(sql)
            #print('Pred commit historia')
    # except pymysql.err.InternalError as err:
    #     code, message = err.args[0], err.args[1]
    #     print('Error: ', code, message)

    finally:
        print()


def SQL_historia(pouzivatelia_id, operacia):
    """
    Zapise operaciu oo historie
    :return:
    """
    print('/===============================================\\')
    print('START -> SQL_historia')
    print('---------------------')

    sql = "INSERT INTO historia (pouzivatelia_id, operacia, cas) values ('{}', '{}', NOW())".format(pouzivatelia_id,operacia)
    SQL_zapis(sql)

def SQL_update(sql):
    """
        Funkcia zapise hodnoty do tabulky podla sql parametra
        :param sql:
        :return:
        """
    print('/===============================================\\')
    print('START -> SQL_update')
    print('------------------')

    # print(sql)
    try:
        with SQL_conn:
            cursor = SQL_conn.cursor()
            cursor.execute(sql)
            # print('Pred commit historia')
            SQL_conn.commit()
    # except pymysql.err.InternalError as err:
    #     code, message = err.args[0], err.args[1]
    #     print('Error: ', code, message)

    finally:
        print()
        # print('Po commit historia')

def SQL_auto_increment(sql):
    """
            Funkcia upravi AUTO_INCREMENT v tabulke
            :param sql:
            :return:
            """
    print('/===============================================\\')
    print('START -> SQL_update')
    print('------------------')

    # print(sql)
    try:
        with SQL_conn:
            cursor = SQL_conn.cursor()
            cursor.execute(sql)

    finally:
        print()
        # print('Po commit historia')


# -------------------------------------------------------------
# ================== TESTUJEM =================================

# Pripajam spojenie s db echolonDB
SQL_connect('127.0.0.1', 'root', 'Pipo246.', 'echolonDB')


# vymaz v tabulke pouzivatela s email = 'eva.hladka@gmail.com'
sql =  "DELETE FROM pouzivatelia WHERE email = '{}'" .format('eva.hladka@gmail.com')
SQL_vymaz(sql)

# nastav v tabulke nove
sql = "ALTER TABLE `echolonDB`.`pouzivatelia` AUTO_INCREMENT = 2 ;"
SQL_auto_increment(sql)


# zapis do tabulky pouzivatelia
sql =  "INSERT INTO pouzivatelia (meno, priezvisko, datumzalozenia, email, heslo, aktivny)" \
       " values ('{}', '{}', NOW(), '{}','{}', true)" \
    .format('Eva', 'Hladka', 'eva.hladka@gmail.com', '111111')
SQL_zapis(sql)


# zmen udaje pouzivatela email='eva.hladka@gmail.com'
sql = "UPDATE pouzivatelia SET priezvisko='{}' WHERE email='{}'" .format('Kukucka','eva.hladka@gmail.com')
SQL_update(sql)

# vyhladanie z tabulky pouzivatela email='eva.hladka@gmail.com'
sql = "SELECT {} FROM {}  WHERE {}='{}'" .format('id, meno, priezvisko, datumzalozenia, email, heslo, aktivny',
                                                 'pouzivatelia', 'email', 'eva.hladka@gmail.com')
print(SQL_hladaj(sql))


# Odpajam spojenie s  databazou
SQL_disconnect()
