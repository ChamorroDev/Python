

agua=600
azucar=1200
aceite=1500
arroz=1250
fideos=790
bebida=1780
chocolate=2500
panmolde=1340

total=0



resp=int(input ("Desea llevar agua ? 1.- SI 2. -NO " ))
if resp==1:
    total=total+agua
resp=int(input ("Desea llevar azucar ? 1.- SI 2. -NO " ))
if resp==1:
    total=total+azucar
resp=int(input ("Desea llevar aceite ? 1.- SI 2. -NO " ))
if resp==1:
    total=total+aceite
resp=int(input ("Desea llevar arroz ? 1.- SI 2. -NO " ))
if resp==1:
    total=total+arroz
resp=int(input ("Desea llevar fideos ? 1.- SI 2. -NO " ))
if resp==1:
    total=total+fideos
resp=int(input ("Desea llevar bebida ? 1.- SI 2. -NO " ))
if resp==1:
    total=total+bebida
resp=int(input ("Desea llevar chocolate ? 1.- SI 2. -NO " ))
if resp==1:
    total=total+chocolate
resp=int(input ("Desea llevar pan molde ? 1.- SI 2. -NO " ))
if resp==1:
    total=total+panmolde


pref=int(input("1.- Cliente preferencial \n2.- Cliente no preferencia \nDigite su opcion"))

if pref==1:
    total=total*0.75


efectivo=int(input("Ingrese su efectivo "))




if efectivo >= total:
    vuelto= efectivo-total
    print ("Su total es $",total, ", Y su vuelto es de $", vuelto)
else: 
    print ("Dinero insuficiente, Guardias!")

