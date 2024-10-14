def add_time(start, duration, day = ""):

  list_of_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  if day != "":
    dia_inicial = day.capitalize()
  
  # separo la hora, minutos y turno mañana o tarde de la fecha inicial
  inicio = start.split(":")
  min_y_turno = inicio[1].split(" ")

  hora_inicial = int(inicio[0])
  min_inicial = int(min_y_turno[0])
  turno_inicial = min_y_turno[1]

  # separo ahora las horas y minutos a adicionar de la variable duration
  horas_y_minutos_adicionales = duration.split(":")

  horas_adicionales = int(horas_y_minutos_adicionales[0])
  minutos_adicionales = int(horas_y_minutos_adicionales[1])

  # comienzo añadiendo los minutos y chequeando el overflow
  minutos_nuevo = min_inicial + minutos_adicionales

  if minutos_nuevo >= 60:
    minutos_nuevo = minutos_nuevo - 60
    horas_adicionales = horas_adicionales + 1
  
  if minutos_nuevo < 10:
    minutos_nuevo = "0" + str(minutos_nuevo)

  # ahora añado las horas segun lo recibido en la funcion
  horas_nuevo = hora_inicial + horas_adicionales

  # declaro un contador para cada vez que pase PM->AM en la suma
  dias_sumados = 0

  # si la hora supera las 12, resto 12 y comparo. Cambio ademas AM/PM por cada chequeo
  while horas_nuevo > 12:
    horas_nuevo = horas_nuevo - 12

    if turno_inicial == "AM":
      turno_inicial = "PM"
    else:
      turno_inicial = "AM"
      dias_sumados = dias_sumados + 1

  # corrijo el error de offset cuando la hora final es 12
  if horas_nuevo == 12:
    if turno_inicial == "AM":
      turno_inicial = "PM"
    else:
      turno_inicial = "AM"
      dias_sumados = dias_sumados + 1
    
  # Chequeo la cantidad de dias avanzados para ajustar el nuevo día si se proveyó el parámetro day
  if day != "":
    indice_inicial = list_of_days.index(dia_inicial)
    indice_final = indice_inicial + dias_sumados
    while indice_final > 6:
      indice_final = indice_final - 7
    dia_final = list_of_days[indice_final]

  # Ahora comienzo a crear el string final y luego selecciono el día de la semana de la lista, si aplica
  new_time = str(horas_nuevo) + ":" + str(minutos_nuevo) + " " + turno_inicial


  if dias_sumados == 0:
    if day != "":
      new_time = new_time  + ", " + day
    return new_time

  if dias_sumados == 1:
    if day == "":
      new_time = new_time + " (next day)"
    else:
      new_time = new_time + ", " + dia_final + " (next day)"
    return new_time

  if dias_sumados > 1:
    if day == "":
      new_time = new_time + " (" + str(dias_sumados) + " days later)"
    else:
      new_time = new_time + ", " + dia_final + " (" + str(dias_sumados) + " days later)"
    return new_time

  return "Error: -1"