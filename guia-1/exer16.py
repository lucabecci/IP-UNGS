"""
# Determinar cuántos segundos tiene una hora, y cuántos tiene un día.
# Escribir una expresión matemática que transforme un lapso de tiempo expresado en   segundos a uno expresado en minutos.
# Escribir otra para transformar a horas y una última que transforme a días.
# Escribir un programa en Python que pida al usuario una cantidad de segundos y muestre cuantos minutos son, así como también cuantas horas y cuantos días.
"""

# 1 hour === 3600 seconds
# 1 day === 86400 seconds

# expr: x_seconds / 60

# expr2: x_hours / 36000

# expr3: x_days / 86400
to_minutes = 60
to_hours = 3600
to_days = 86400

print("===> Ingrese la cantidad de segundos a calcular:")
n = int(input())

print("===> Su valor en minutos:", n / to_minutes)

print("===> Su valor en horas:", n / to_hours)

print("===> Su valor en days:", n / to_days)
