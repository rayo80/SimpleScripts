import simplekml
import json

kml2 = simplekml.Kml()

with open("historial.json") as file:
    empresajson = json.load(file)


for item in empresajson:
    coord = item['position']['coordinates']
    pnt = kml2.newpoint(name="Pad 40",
                        coords=[(coord[1], coord[0])])
    pnt.description = f"velocidad: {item['velocidad']}\n\
                        hora: {item['hora']}\n\
                        latitud: {coord[0]}\n\
                        longitud: {coord[1]}\n"

kml2.save("historial.kml")