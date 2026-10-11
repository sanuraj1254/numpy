import numpy as np

print("========== Vector & Matrix Calculator ==========")
print("1. Vector Calculator")
print("2. Matrix Calculator")

choice = int(input("Choose calculator: "))#VECTOR AREA
if choice == 1:
    def get_vector_1():
       
       x = float(input("Enter the x:"))
       y = float(input("Enter the y:"))

       array1 = np.array([x,y])

       return array1

    vector_1 = get_vector_1()
    print(vector_1)

    def get_vector_2():
        a = float(input("Enter the x:"))
        b = float(input("Enter the y:"))

        array2 = np.array([a,b])

        return array2

    vector_2 = get_vector_2()
    print(vector_2)

    print("=======Calculator=======")
    print("1. Vector Length")
    print("2. Dot Product")
    print("3. Angle Between Vectors")

    vector_choice = int(input("Choose the opreation : "))

    if vector_choice == 1:
        vect_length_1 = np.linalg.norm(vector_1)
        vect_length_2 = np.linalg.norm(vector_2)
        print("Your length of the vector_1 is : ",vect_length_1)
        print("Your length of the vector_2 is : ",vect_length_2)

    elif vector_choice == 2:
        dot_product = np.dot(vector_1 , vector_2)
        print("The dot product is : ",dot_product)

    elif vector_choice == 3:
        vect_length_1 = np.linalg.norm(vector_1)
        vect_length_2 = np.linalg.norm(vector_2)

        if vect_length_1 == 0 or vect_length_2 == 0:
            print("Angle is undefined for zero vectors ")

        else:
            dot_product = np.dot(vector_1 , vector_2)
            formula = dot_product / (vect_length_1*vect_length_2)
            angle = np.arccos(formula)
            angle = np.degrees(angle)
            print("The angle between vectors is : ",angle)  

    else:   
        print("Invalid operation! Choosen choose (1 to3).")
elif choice ==2: # MATRIX AREA          
    def get_matrix():
       
       matrix = []

       rows = int(input("Enter number of rows: "))
       columns = int(input("Enter number of columns: "))

       for i in range (rows):
          row = []

          for j in range(columns):
              number = float(input("Enter the numbers:"))
              row.append(number)
    
          matrix.append(row)

       return np.array(matrix)
       
    print("Matrix Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")

    matrix_choice = int(input("Choose operation (1-4): "))
    if matrix_choice == 1:
        print("you choose addition")

        matrix_1 = get_matrix()
        print("Your 1st matrix is:",matrix_1)
        matrix_2 = get_matrix()
        print("Your 2nd matrix is:",matrix_2)

        if matrix_1.shape == matrix_2.shape:
            addition = matrix_1 + matrix_2
            print("The addition of 1st and 2nd matrix is: ",addition)

        else:
            print("Error: Both matrices must have the same dimensions.")

    elif matrix_choice ==2:
        print("You choose subtraction")

        matrix_1 = get_matrix()
        print(matrix_1)
        matrix_2 = get_matrix()
        print(matrix_2)

        if matrix_1.shape == matrix_2.shape:
            subtraction = matrix_1 - matrix_2
            print("The subtraction of 1st and 2nd matrix is: ",subtraction)
        
        else:
            print("Error: Both matrices must have the same dimensions.")

    elif matrix_choice == 3:
        print("You choose multiplication")

        matrix_1 = get_matrix()
        print(matrix_1)
        matrix_2 = get_matrix()
        print(matrix_2)

        if matrix_1.shape == matrix_2.shape:
            multiplication = matrix_1 @ matrix_2
            print("The multiplication of 1st and 2nd matrix is: ",multiplication)
        
        else:
            print("Error: Both matrices must have the same dimensions.")
       

    elif matrix_choice == 4:
        print("You choose transpose")   

        matrix_1 = get_matrix()
        transpose = matrix_1.T

        print("Your original matrix is:")
        print(matrix_1)
        print("The transposed matrix is:")
        print(transpose)

    else:
        print("Invalid operation! Chooseen choose (1 to 4).")

else:
    print("Invalid operation! Choose 1 or 2.")
