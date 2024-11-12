import fitz  # PyMuPDF

# Abrir el PDF
pdf_document = "002.pdf"
document = fitz.open(pdf_document)

# Seleccionar la página (en este caso, la primera página)
page = document.load_page(0)

# Definir las coordenadas del área (x0, y0, x1, y1)
# Puedes ajustar estas coordenadas según la ubicación deseada
rif_org = fitz.Rect(10, 10, 84, 145)  # rif y/o rif
comprobante_org = fitz.Rect(479.8050842285156, 70.83236694335938, 571.9974365234375, 79.68061065673828) # COMPROBANTE
nombre_org = fitz.Rect(90, 138.87258911132812, 210.02392578125, 147.7208251953125)  # NOMBRE
direccion_org = fitz.Rect(42.00209426879883, 158.79273986816406, 366.2537841796875, 183.72096252441406)  # DIRECCION
fecha_inscripcion_org = fitz.Rect(372.3644714355469, 136.83067321777344, 557.2546997070312, 145.6789093017578)  # FECHA INSCRIPCION
fecha_actualizacion_org = fitz.Rect(372.3644714355469, 152.79078674316406, 558.5719604492188, 161.63902282714844)  # FECHa ACTUALIZACION
fecha_vencimiento_org = fitz.Rect(372.3644714355469, 168.8707733154297, 558.0534057617188, 177.71900939941406)  # FECHa VENCIMIENTO
rect = fitz.Rect(42.00209426879883, 249.87350463867188, 228.57601928710938, 266.642333984375)  # FECHa ACTUALIZACION

# Extraer el texto del área definida
text = page.get_text("text", clip=rect)

# se coloca el exto en una sola linea
comprobante =  ' '.join(page.get_text("text", clip=comprobante_org).split())

# se coloca el exto en una sola linea
rif =  ' '.join(page.get_text("text", clip=rif_org).split())

# se coloca el exto en una sola linea
nombre =  ' '.join(page.get_text("text", clip=nombre_org).split())

# se coloca el exto en una sola linea
direccion =  ' '.join(page.get_text("text", clip=direccion_org).split())
# Eliminar la frase "DOMICILIO FISCAL " del texto 
direccion = direccion.replace("DOMICILIO FISCAL ", "")
# Eliminar la frase "(Este contribuyente no posee firmas personales)"
direccion = direccion.replace("(Este contribuyente no posee firmas personales)", "")


# se coloca el exto en una sola linea
fecha_inscripcion =  ' '.join(page.get_text("text", clip=fecha_inscripcion_org).split())
# Eliminar la frase "DOMICILIO FISCAL " del texto 
fecha_inscripcion = fecha_inscripcion.replace("FECHA DE INSCRIPCIÓN: ", "")


# se coloca el exto en una sola linea
fecha_actualizacion =  ' '.join(page.get_text("text", clip=fecha_actualizacion_org).split())
# Eliminar la frase "FECHA DE ÚLTIMA ACTUALIZACIÓN:" del texto 
fecha_actualizacion = fecha_actualizacion.replace("FECHA DE ÚLTIMA ACTUALIZACIÓN: ", "")


# se coloca el exto en una sola linea
fecha_vencimiento =  ' '.join(page.get_text("text", clip=fecha_vencimiento_org).split())
# Eliminar la frase "FECHA DE VENCIMIENTO:" del texto 
fecha_vencimiento = fecha_vencimiento.replace("FECHA DE VENCIMIENTO: ", "")


# Imprimir el texto extraído
print(f"Comprobante: {comprobante}")
print(f"RIF: {rif}")
print(f"Nombre: {nombre}")
print(f"Direccion: {direccion}")
print(f"Fecha de Inscripcion: {fecha_inscripcion}")
print(f"Fecha de Actualizacion: {fecha_actualizacion}")
print(f"Fecha de Vencimiento: {fecha_vencimiento}")

