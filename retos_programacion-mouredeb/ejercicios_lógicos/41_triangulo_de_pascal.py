def pascal_triangle(n):
    triangle = []

    for row_num in range(n): # Crea un bucle según la cantidad de filas
        row = [1] * (row_num + 1)  # Crea una nueva fila con unos
        # Se crea una lista de listas [1]

        for j in range(1, row_num): # Modifica los unos de la posición "1" a la
        #posición que representa el número de "row_num"
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

        triangle.append(row) #Añade la fila(lista) a la lista triangle
        print(row)# Va imprimiendo las filas

pascal_triangle(5)

