adc.set_conv(echantillons, canal)  # initialise les parametres de conversion
 
while True:
    mesure = adc.read_rev()  # recupere la derniere conversion et relance une nouvelle conversion
    tension = adc.raw_to_v(mesure)  # conversion de la mesure en tension
    print(tension)
    time.sleep(5)
