from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone XR", "+79882515787"))
catalog.append(Smartphone("Samsung", "Galaxy S20FE", "+79992586976"))
catalog.append(Smartphone("Motorola", "Razr V3", "+79281484812"))
catalog.append(Smartphone("Samsung", "Galaxy ZFold", "+79185154716"))
catalog.append(Smartphone("Nokia", "3310", "+79881948848"))

for obj in catalog:
    print(obj.make, obj.model, obj.number)

print("")