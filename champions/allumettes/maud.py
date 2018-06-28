def ia(nb_alumettes):
  reste = (nb_alumettes-1) % 4
  if reste == 0:
    reste = 1
  return reste
