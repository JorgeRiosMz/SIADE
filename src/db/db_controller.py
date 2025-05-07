import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime, date

# --- Database connection manager ---
class Database:
    _connection = None

    @classmethod
    def initialize(cls, dsn: str):
        """Initialize a global connection using a DSN string."""
        cls._connection = psycopg2.connect(dsn)

    @classmethod
    def get_cursor(cls):
        """Get a cursor that returns rows as dicts."""
        if cls._connection is None:
            raise RuntimeError("Database not initialized")
        return cls._connection.cursor(cursor_factory=RealDictCursor)

    @classmethod
    def commit(cls):
        """Commit the current transaction."""
        if cls._connection:
            cls._connection.commit()


# Call once at startup:
# Database.initialize("dbname=mydb user=myuser password=mypass host=localhost")

# --- Base model with common CRUD operations ---
class BaseModel:
    table_name: str
    pkey: str

    @classmethod
    def _execute(cls, sql: str, params: tuple = ()):
        cur = Database.get_cursor()
        cur.execute(sql, params)
        Database.commit()
        return cur

    @classmethod
    def get_by_id(cls, record_id: int):
        sql = f"SELECT * FROM {cls.table_name} WHERE {cls.pkey} = %s"
        cur = cls._execute(sql, (record_id,))
        row = cur.fetchone()
        return row

    @classmethod
    def delete(cls, record_id: int):
        sql = f"DELETE FROM {cls.table_name} WHERE {cls.pkey} = %s"
        cls._execute(sql, (record_id,))


# --- User CRUD ---
class User(BaseModel):
    table_name = "usuario"
    pkey = "id_usuario"

    @classmethod
    def create(cls, name: str, email: str, password: str,
               login_time: datetime, role: str):
        sql = """
        INSERT INTO usuario (nombre, correo_electronico, contrasena, inicio_sesion, rol)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id_usuario
        """
        cur = cls._execute(sql, (name, email, password, login_time, role))
        return cur.fetchone()["id_usuario"]

    @classmethod
    def update(cls, user_id: int, **fields):
        cols = ", ".join(f"{k} = %s" for k in fields)
        params = tuple(fields.values()) + (user_id,)
        sql = f"UPDATE usuario SET {cols} WHERE id_usuario = %s"
        cls._execute(sql, params)

    @classmethod
    def list_all(cls):
        sql = "SELECT * FROM usuario"
        cur = cls._execute(sql)
        return cur.fetchall()


# --- Patient CRUD ---
class Patient(BaseModel):
    table_name = "paciente"
    pkey = "id_paciente"

    @classmethod
    def create(cls, first_name: str, last_name: str,
               birth_date: date, sex: str, phone: str):
        sql = """
        INSERT INTO paciente (nombre, apellido, fecha_nacimiento, sexo, telefono)
        VALUES (%s, %s, %s, %s, %s) RETURNING id_paciente
        """
        cur = cls._execute(sql, (first_name, last_name, birth_date, sex, phone))
        return cur.fetchone()["id_paciente"]

    @classmethod
    def update(cls, patient_id: int, **fields):
        cols = ", ".join(f"{k} = %s" for k in fields)
        params = tuple(fields.values()) + (patient_id,)
        sql = f"UPDATE paciente SET {cols} WHERE id_paciente = %s"
        cls._execute(sql, params)

    @classmethod
    def list_all(cls):
        sql = "SELECT * FROM paciente"
        cur = cls._execute(sql)
        return cur.fetchall()


# --- History CRUD ---
class History(BaseModel):
    table_name = "historial"
    pkey = "id_historial"

    @classmethod
    def create(cls, patient_id: int, user_id: int):
        sql = """
        INSERT INTO historial (id_paciente, id_usuario)
        VALUES (%s, %s) RETURNING id_historial
        """
        cur = cls._execute(sql, (patient_id, user_id))
        return cur.fetchone()["id_historial"]

    @classmethod
    def update(cls, history_id: int, **fields):
        cols = ", ".join(f"{k} = %s" for k in fields)
        params = tuple(fields.values()) + (history_id,)
        sql = f"UPDATE historial SET {cols} WHERE id_historial = %s"
        cls._execute(sql, params)

    @classmethod
    def list_all(cls):
        sql = "SELECT * FROM historial"
        cur = cls._execute(sql)
        return cur.fetchall()


# --- Disease CRUD ---
class Disease(BaseModel):
    table_name = "enfermedad"
    pkey = "id_enfermedad"

    @classmethod
    def create(cls, name: str, description: str = None):
        sql = "INSERT INTO enfermedad (nombre, descripcion) VALUES (%s, %s) RETURNING id_enfermedad"
        cur = cls._execute(sql, (name, description))
        return cur.fetchone()["id_enfermedad"]

    @classmethod
    def update(cls, disease_id: int, **fields):
        cols = ", ".join(f"{k} = %s" for k in fields)
        params = tuple(fields.values()) + (disease_id,)
        sql = f"UPDATE enfermedad SET {cols} WHERE id_enfermedad = %s"
        cls._execute(sql, params)

    @classmethod
    def list_all(cls):
        sql = "SELECT * FROM enfermedad"
        cur = cls._execute(sql)
        return cur.fetchall()


# --- Symptom CRUD ---
class Symptom(BaseModel):
    table_name = "sintoma"
    pkey = "id_sintoma"

    @classmethod
    def create(cls, name: str, description: str = None):
        sql = "INSERT INTO sintoma (nombre, descripcion) VALUES (%s, %s) RETURNING id_sintoma"
        cur = cls._execute(sql, (name, description))
        return cur.fetchone()["id_sintoma"]

    @classmethod
    def update(cls, symptom_id: int, **fields):
        cols = ", ".join(f"{k} = %s" for k in fields)
        params = tuple(fields.values()) + (symptom_id,)
        sql = f"UPDATE sintoma SET {cols} WHERE id_sintoma = %s"
        cls._execute(sql, params)

    @classmethod
    def list_all(cls):
        sql = "SELECT * FROM sintoma"
        cur = cls._execute(sql)
        return cur.fetchall()


# --- Sign CRUD ---
class Sign(BaseModel):
    table_name = "signo"
    pkey = "id_signo"

    @classmethod
    def create(cls, name: str, description: str = None):
        sql = "INSERT INTO signo (nombre, descripcion) VALUES (%s, %s) RETURNING id_signo"
        cur = cls._execute(sql, (name, description))
        return cur.fetchone()["id_signo"]

    @classmethod
    def update(cls, sign_id: int, **fields):
        cols = ", ".join(f"{k} = %s" for k in fields)
        params = tuple(fields.values()) + (sign_id,)
        sql = f"UPDATE signo SET {cols} WHERE id_signo = %s"
        cls._execute(sql, params)

    @classmethod
    def list_all(cls):
        sql = "SELECT * FROM signo"
        cur = cls._execute(sql)
        return cur.fetchall()


# --- Relationship Disease–Symptom CRUD ---
class DiseaseSymptom(BaseModel):
    table_name = "enfermedad_sintoma"
    pkey = "id_enfermedad"  # composite key: (id_enfermedad, id_sintoma)

    @classmethod
    def add(cls, disease_id: int, symptom_id: int):
        sql = "INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (%s, %s)"
        cls._execute(sql, (disease_id, symptom_id))

    @classmethod
    def remove(cls, disease_id: int, symptom_id: int):
        sql = "DELETE FROM enfermedad_sintoma WHERE id_enfermedad = %s AND id_sintoma = %s"
        cls._execute(sql, (disease_id, symptom_id))


# --- Relationship Disease–Sign CRUD ---
class DiseaseSign(BaseModel):
    table_name = "enfermedad_signo"
    pkey = "id_enfermedad"  # composite key: (id_enfermedad, id_signo)

    @classmethod
    def add(cls, disease_id: int, sign_id: int):
        sql = "INSERT INTO enfermedad_signo (id_enfermedad, id_signo) VALUES (%s, %s)"
        cls._execute(sql, (disease_id, sign_id))

    @classmethod
    def remove(cls, disease_id: int, sign_id: int):
        sql = "DELETE FROM enfermedad_signo WHERE id_enfermedad = %s AND id_signo = %s"
        cls._execute(sql, (disease_id, sign_id))


# --- Diagnosis CRUD ---
class Diagnosis(BaseModel):
    table_name = "diagnostico"
    pkey = "id_diagnostico"

    @classmethod
    def create(cls, history_id: int, disease_id: int, diagnosis_date: date):
        sql = """
        INSERT INTO diagnostico (id_historial, id_enfermedad, fecha_diagnostico)
        VALUES (%s, %s, %s) RETURNING id_diagnostico
        """
        cur = cls._execute(sql, (history_id, disease_id, diagnosis_date))
        return cur.fetchone()["id_diagnostico"]

    @classmethod
    def update(cls, diag_id: int, **fields):
        cols = ", ".join(f"{k} = %s" for k in fields)
        params = tuple(fields.values()) + (diag_id,)
        sql = f"UPDATE diagnostico SET {cols} WHERE id_diagnostico = %s"
        cls._execute(sql, params)

    @classmethod
    def list_all(cls):
        sql = "SELECT * FROM diagnostico"
        cur = cls._execute(sql)
        return cur.fetchall()


# --- Laboratory Test CRUD ---
class LabTest(BaseModel):
    table_name = "prueba_laboratorio"
    pkey = "id_prueba_laboratorio"

    @classmethod
    def create(cls, diagnosis_id: int, test_date: date, result: str):
        sql = """
        INSERT INTO prueba_laboratorio (id_diagnostico, fecha, resultado)
        VALUES (%s, %s, %s) RETURNING id_prueba_laboratorio
        """
        cur = cls._execute(sql, (diagnosis_id, test_date, result))
        return cur.fetchone()["id_prueba_laboratorio"]

    @classmethod
    def update(cls, lab_id: int, **fields):
        cols = ", ".join(f"{k} = %s" for k in fields)
        params = tuple(fields.values()) + (lab_id,)
        sql = f"UPDATE prueba_laboratorio SET {cols} WHERE id_prueba_laboratorio = %s"
        cls._execute(sql, params)

    @classmethod
    def list_all(cls):
        sql = "SELECT * FROM prueba_laboratorio"
        cur = cls._execute(sql)
        return cur.fetchall()


# --- Postmortem Test CRUD ---
class PostmortemTest(BaseModel):
    table_name = "prueba_postmortem"
    pkey = "id_prueba_postmortem"

    @classmethod
    def create(cls, diagnosis_id: int, test_date: date, result: str):
        sql = """
        INSERT INTO prueba_postmortem (id_diagnostico, fecha, resultado)
        VALUES (%s, %s, %s) RETURNING id_prueba_postmortem
        """
        cur = cls._execute(sql, (diagnosis_id, test_date, result))
        return cur.fetchone()["id_prueba_postmortem"]

    @classmethod
    def update(cls, post_id: int, **fields):
        cols = ", ".join(f"{k} = %s" for k in fields)
        params = tuple(fields.values()) + (post_id,)
        sql = f"UPDATE prueba_postmortem SET {cols} WHERE id_prueba_postmortem = %s"
        cls._execute(sql, params)

    @classmethod
    def list_all(cls):
        sql = "SELECT * FROM prueba_postmortem"
        cur = cls._execute(sql)
        return cur.fetchall()
