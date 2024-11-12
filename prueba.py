from pypdf import PdfReader

reader = PdfReader("001.pdf")
text = ""
page = reader.pages[0]
text += page.extract_text()
lines = text.split('\n')

if lines:
    print(lines[0])

#print(text)




# import re
# from pypdf import PdfReader
# 
# # Leer el PDF
# reader = PdfReader("001.pdf")
# text = ""
# page = reader.pages[0]
# text += page.extract_text()
# 
# # Definir patrones regex para cada dato
# patterns = {
#     "numero_comprobante": r"N° COMPROBANTE:\s*(\w+)",
#     "cedula": r"RIF\s*(\w+)",
#     "nombre_apellido": r"RIF\s*\w+\s*([\w\s]+)",
#     "direccion_fiscal": r"DOMICILIO FISCAL\s*([\w\s]+)\s*CARACAS DISTRITO CAPITAL ZONA POSTAL 1020",
#     "fecha_inscripcion": r"FECHA DE INSCRIPCIÓN:\s*([\d/]+)",
#     "fecha_actualizacion": r"FECHA DE ÚLTIMA ACTUALIZACIÓN:\s*([\d/]+)",
#     "fecha_vencimiento": r"FECHA DE VENCIMIENTO:\s*([\d/]+)"
# }
# 
# # Extraer datos usando los patrones regex
# data = {}
# for key, pattern in patterns.items():
#     match = re.search(pattern, text)
#     if match:
#         data[key] = match.group(1)
# 
# # Imprimir los datos extraídos
# for key, value in data.items():
#     print(f"{key}: {value}")
