import peewee as p

db=p.MySQLDatabase('salon',user='root',password='Vivivi12345',host='127.0.0.1',port=3306)

class BaseModel(p.Model):
    id=p.AutoField()
    class Meta:
        database=db

class Client(BaseModel):
    id = p.IntegerField()
    nomer = p.CharField()
    name = p.CharField()
    class Meta:
        table_name='Clients'

class Master(BaseModel):
    number = p.CharField()
    name = p.CharField()
    class Meta:
        table_name='Masters'

class Procedures_types(BaseModel):
    type_name = p.CharField()
    class Meta:
        table_name='Proc_types'

class Brovi(BaseModel):
    none = p.BooleanField()
    type_id = p.ForeignKeyField(Procedures_types,backref='procedures_type')
    class Meta:
        table_name='Brovi'

class Res(BaseModel):
    none = p.BooleanField()
    type_id = p.ForeignKeyField(Procedures_types,backref='procedures_type')
    class Meta:
        table_name='Res'

class Manik(BaseModel):
    none = p.BooleanField()
    type_id = p.ForeignKeyField(Procedures_types,backref='procedures_type')
    class Meta:
        table_name='Manik'

class Pedik(BaseModel):
    none = p.BooleanField()
    type_id = p.ForeignKeyField(Procedures_types,backref='procedures_type')
    class Meta:
        table_name='Pedik'

class Procedures(BaseModel):
    brov_id = p.ForeignKeyField(Brovi,backref='brovi')
    res_id = p.ForeignKeyField(Res,backref='res')
    manik_id = p.ForeignKeyField(Manik,backref='manik')
    pedik_id = p.ForeignKeyField(Pedik,backref='pedik')
    class Meta:
        table_name='Procedures'

class Zapis(BaseModel):
    procedures_id = p.ForeignKeyField(Procedures,backref='proced')
    client_id = p.ForeignKeyField(Client,backref='client')
    master_id = p.ForeignKeyField(Master,backref='master')
    Date_time = p.DateTimeField()
    class Meta:
        table_name='Zapis'

class Session_date(BaseModel):
    date = p.DateTimeField()
    class Meta:
       table_name='Session_date'

class Admins(BaseModel):
    number = p.CharField()
    class Meta:
       table_name='Admins'

#with db as conn:
 #  conn.create_tables([Client,Master,Procedures_types,Brovi,Res,Manik,Pedik,Zapis,Procedures,Admins,Session_date])



    

