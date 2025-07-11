#Paso 1 creamos la base, Creamos clase Empleado
class Empleado:
 #La función DEF define una función o método. le indicamos a Python que esto es un bloque de código reutilizable.
#Constructor __INIT__ inicilizará un proceso cuando se crea una instancia
   def __init__(self, nombre, puesto, salario): #self: referencia al mismo objeto
            
      #Creamos los atributos o variables de instancia.
      #self.atributo guarda los valores del input dentro del atributo del objeto.
      self.nombre = nombre   #atributo
      self.puesto = puesto   #atributo
      self.salario = salario #atributo

#Crear un método "mostrar_info" para mostrar los datos del empleado. Usamos self para acceder a los atributos del objeto.
   def mostrar_info (self):
      print("Nombre", self.nombre) # accedemos al nombre de emp1
      print("Puesto", self.puesto)
      print("Salario: $", self.salario) 

#Creamos clase derivada Gerente. creamos una clase hija que hereda de Empleado y añade un nuevo atributo: departamento.
# Paso 2: Clase derivada
class Gerente(Empleado):  # Hereda de Empleado
    def __init__(self, nombre, puesto, salario, departamento):
        super().__init__(nombre, puesto, salario)  # Llama al constructor de Empleado
        self.departamento = departamento  # Nuevo atributo

    def mostrar_info(self):  # Sobrescribe el método de Empleado
        super().mostrar_info()  # Muestra lo de Empleado
        print("Departamento:", self.departamento)

# Paso 3: Crear objeto de clase derivada
#Capturamos los datos desde consola, Crea un objeto gerente1, Llama al método mostrar_info() que usa herencia y muestra todos los datos.
nombre = input("Nombre del Gerente: ")
puesto = input("Puesto: ")
salario = float(input("Salario: "))
departamento = input("Departamento: ")

gerente1 = Gerente(nombre, puesto, salario, departamento) #Objeto (instancia de la clase)
gerente1.mostrar_info() #Ejecutamos el método mostrar_info() para gerente1, para mostrar los datos en pantalla
