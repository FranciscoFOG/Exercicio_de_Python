# PROGRAMA ANALISANDO MEDIDAS #

m = float(input('Digite uma medida em metros: '))
km = m / 1000
hm = m / 100
dan = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('A medida de {}m corresponde a \n{}km e \n{}hm e \n{}dan e \n{} dm e \n{}cm e \n{}mm'.format(m, km, hm, dan, dm, cm, mm))
