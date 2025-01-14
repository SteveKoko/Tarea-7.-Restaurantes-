try:
  puntuacion = float(input("Valore su experiencia en el restauante del 0 al 5: "))
  if puntuacion == 0:
    print("Vaya, reprenderé a mis trabajadores, gracias")
  elif puntuacion > 0 and puntuacion <= 1:
    print("Vaya, lamentamos oír eso, esperamos que vuelva a darnos una oportunidad")
  elif puntuacion > 1 and puntuacion <= 2:
    print("Vaya... Intentaremos mejorar, no olvides en volver")
  elif puntuacion > 2 and puntuacion <= 3:
    print("Está bien pero intentaremos mejorar, gracias.")
  elif puntuacion > 3 and puntuacion <= 4:
    print("!Gracias, nos alegramos de que le haya gustado, vuelva pronto¡")
  elif puntuacion > 4 and puntuacion < 5:
    print("!Muchas grancias, vuelva pronto¡")
  elif puntuacion == 5:
    print("!Excelente, le agradecemos de verdad la reseña, muchísimas gracias¡")
  else:
    print("Por favor introduzca un valor entre 0 y 5")
except ValueError:
  print("Intrduca un valor adecuado porfavor")