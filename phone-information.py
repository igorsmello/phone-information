import phonenumbers

#Ajuste do telefone para usar o phonenumbers
telefone = "+5522991049407"
telefone_ajustado = phonenumbers.parse(telefone)
print(telefone_ajustado)


#Descobrir a localização do telefone
from phonenumbers import geocoder
local = geocoder.description_for_number(telefone_ajustado, 'pt-br')
print(local)


#Formatando um telefone que foi inserido em um formulário
telefone_formulario = "22991049407"

telefone_formulario_ajustado = phonenumbers.parse(telefone_formulario, "BR")

telefone_formatado = phonenumbers.format_number(telefone_formulario_ajustado,phonenumbers.PhoneNumberFormat.NATIONAL)
print(telefone_formatado)


#Descobrir a operadora do telefone
from phonenumbers import carrier

operadora = carrier.name_for_number(telefone_ajustado,'pt-br')

print(operadora)