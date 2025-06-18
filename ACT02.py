#Creamos clase Empleado
class Empleado:

 #La función DEF define una función o método. le indicamos a Python que esto es un bloque de código reutilizable.
#Constructor __INIT__ inicilizará un proceso cuando se crea una instancia
   def __init__(self, nombre, puesto, salario):
            
      #Creamos los atributos o variables de instancia.
      #self.atributo guarda los valores del input dentro del atributo del objeto.
      self.nombre = nombre   #atributo
      self.puesto = puesto   #atributo
      self.salario = salario #atributo

#Crear un    "mostrar_info" para mostrar los datos del empleado. Usamos self para acceder a los atributos del objeto.
   def mostrar_info (self):
      print("Nombre", self.nombre) # accedemos al nombre de emp1
      print("Puesto", self.puesto)
      print("Salario: $", self.salario) 

#Capturar datos del usuario: Con inputs, Guardamos los valores que escribe el usuario en las variables: nombre, puesto y empleado.
nombre = input("Nombre del Empleado: ")
puesto = input("Puesto: ")
salario = float(input("Salario: "))#Convertimos el salario de texto a número con float()

#Creamos el objeto emp1, usará los datos capturados en el input y los enviará al constructor __init__ de la clase Empleado.
emp1 = Empleado(nombre, puesto, salario) #Objeto (instancia de la clase)

#Ejecutamos el método mostrar_info() para emp1, para mostrar en pantalla nombre, puesto y salario.
emp1.mostrar_info()
