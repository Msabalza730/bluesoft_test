# Bluesoft Technical Test Django

Bluesoft Bank es un banco tradicional que se encarga de guardar el dinero de sus ahorradores,
ofrece dos tipos de cuenta; ahorros para personas naturales y corrientes para empresas.
Adicionalmente para cada cuenta se pueden hacer consignaciones y retiros.

Adicionalmente tiene que soportar algunos requerimientos para sus ahorradores:

- Consultar el saldo de la cuenta
- Consultar los movimientos más recientes
- Generar extractos mensuales

Reglas de negocio:

- Una cuenta no puede tener un saldo negativo.
- El saldo de la cuenta siempre debe ser consistente frente a dos operaciones concurrentes
(consignación, retiro)
También se deben generar reportes en tiempo real como:
- Listado de clientes con el número de transacciones para un mes es particular, organizado
descendentemente (primero el cliente con mayor # de transacciones en el mes)
- Clientes que retiran dinero fuera de la ciudad de origen de la cuenta con el valor total de
los retiros realizados superior a $1.000.000.


## Run this App

- git clone https://github.com/Msabalza730/bluesoft_test.git

- Create a virtual env 
```python
    - python -m venv env
    - source bin/activate
```
- Create a superuser: python manage.py createsuperuser

- python manage.py runserver

- go to: http://127.0.0.1:8000/admin or http://127.0.0.1:8000/api