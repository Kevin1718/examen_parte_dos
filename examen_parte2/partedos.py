import json
from urllib import response
import requests

from flask import request
from employee import Employee
from airport import Airport
from country import Country
from languaje import Languaje

def leerDoc():
    try:
        doc = open("Clientes.txt", "r")
        info=doc.readlines()
        valor=[]
        for linea in info:
            nombre,apellido, pais, idioma, aeropuerto = linea.strip().split(",")
            valor.append({"name":nombre,"surname":apellido, "pais":pais, "idioma":idioma, "aeropuerto":aeropuerto})
        doc.close()
        print("Se ha leido correctamente el archivo")
        return valor
    except FileNotFoundError as e:
        print(e)
        print("No se ha encotrado el documento")

def peticiones():
    try:
        api_url = "http://localhost:8080/apiv1/empleados/add"
        empleados=leerDoc()
        for empleado in empleados:
            employee=Employee(empleado["nombre"].strip(),empleado["apellido"].strip()) 

            employeeDatos={
                "name":employee.getName(),
                "surname":employee.getSurname(),
                "employee languajes":[
                    {
                        "code":Languaje.getCode(),
                        "name":Languaje.getName()
                    }
                ],
                "employee country":
                {
                    "code": Country.getCode(),
                    "name":Country.getName(),
                    "airports":
                    {
                        "id":Airport.getID(),
                        "name":Airport.getName()
                    }
                }  
            }
            response= requests.post(api_url,json=employeeDatos)
            

        
    except Exception as e:
        print(e)
peticiones()