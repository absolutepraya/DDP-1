# Kita perlu import matplotlib untuk sebuah visualisasi
# Scatter Plot. 
#
# Apa itu Scatter plot?
# https://chartio.com/learn/charts/what-is-a-scatter-plot/
#
# Jika Anda tidak bisa import matplotlib, ada kemungkinan 
# Anda belum install library matplotlib di local komputer 
# Anda. Silakan ikuti petunjuk pada
# https://matplotlib.org/stable/users/installing/index.html

import matplotlib.pyplot as plt


# ———————————————————————— FUNCTIONS FOR EFFICIENCY ————————————————————————


def value_getter(dataframe, col_name, type="numeric"):
  """
    Returns a list of values from a column in a dataframe.
    The third parameter, type, is used to check:
    1. If the column is numeric
    2. If the column is string
  """
  # Get the index of the column
  try:
    col_index = get_column_names(dataframe).index(col_name)
  except:
    # EXCEPTION: If the column is not found
    raise Exception(f"Kolom {col_name} tidak ditemukan.")
  
  col_values = []

  # Loop through each row
  for row in to_list(dataframe):
    # Check if the value is not numeric
    if type == "numeric":
      # EXCEPTION: If the value is not numeric
      if get_type(row[col_index]) == "str":
        raise Exception(f"Kolom {col_name} bukan bertipe numerik.")
      # Append the value into a list
      col_values.append(float(row[col_index]))
    # Check if the value is not string
    elif type == "string":
      # EXCEPTION: If the value is not string
      # if get_type(row[col_index]) != "str":
      #   raise Exception(f"Kolom {col_name} harus bertipe string.")
      # Append the value into a list
      col_values.append(str(row[col_index]))
    
  return col_values

def my_arange(start, stop, step):
  """
    Returns a list of values from start to stop with a certain step, just like numpy's np.arange().
    Used mainly for setting the tick locations of the X-axis and Y-axis.
  """
  values = []
  current_value = start
  # Loop until the current value is greater than or equal to stop
  while current_value < stop:
      values.append(current_value)
      current_value += step

  return values


# ———————————————————————— MANDATORY FUNCTIONS ————————————————————————


def get_type(a_str):
  """
    -- DIBUKA KE PESERTA --
    
    Fungsi ini akan mengembalikan tipe dari literal
    string a_str.
    
    get_type("0.5") -> "float"
    get_type("5.") -> "float"
    get_type("5") -> "int"
    get_type("5.a") -> "str"
    
    parameter:
    a_str (string): string literal dari sebuah nilai
    
    return (string): "int", "float", atau "str"
  """
  try:
    int(a_str)
    return "int"
  except:
    try:
      float(a_str)
      return "float"
    except:
      return "str"
    
def read_csv(file_name, delimiter = ','):
  """
    Dataframe adalah sebuah abstraksi tabel data siap 
    proses yang dalam tugas kali ini direpresentasikan 
    sebagai 3-tuple:
    
      (data, list nama kolom, list tipe data)
    
    'data' merupakan list of lists yang menyimpan 
    nilai-nilai pada tabel dan mempunyai format:
    
    [[row_11, row_12, ..., row_1n],
     [row_21, row_22, ..., row_2n],
     ...
     [row_m1, row_m2, ..., row_mn]]
     
    Satu cell row_mn dapat bertipe string, integer,
    atau float. Jika semua cell pada kolom n berisi
    literal integer, maka ubah semuanya dalam tipe
    data integer; jika bukan integer, maka ada dua kemungkinan,
    yaitu float atau string; jika semua nilai pada
    kolom n berupa number dan ada satu yang float, maka
    jadikan semua tipe data pada kolom n tersebut sebagai
    float; jika cell-cell pada kolom n ada yang tidak 
    bisa dikonversikan ke integer maupun float, maka 
    tipe kolom n tersebut adalah string.
     
    Selain list of lists yang berisi tabel, informasi
    nama kolom juga disimpan dalam bentuk 
    'list nama kolom':
    
    [nama_kolom_1, nama_kolom_2, ..., nama_kolom_n]
    
    Elemen ketiga pada 3-tuple adalah 'list tipe data'
    pada setiap kolom. Ada tiga jenis tipe data dalam
    tugas kali ini = "str", "int", dan "float". Sebuah
    kolom bertipe "int" jika semua elemen pada kolom
    tersebut adalah literal integer; "float" jika semua
    elemen pada kolom adalah literal float (dan bukan
    literal integer); "str" jika selain kedua di atas.
    
    Fungsi ini bertugas untuk membaca sebuah file comma
    separated value, melakukan parsing, dan mengembalikan
    dataframe yang berupa 3-tuple.
    
    ASUMSI file csv:
      1. selalu ada header (nama kolom) pada baris pertama
      2. nama kolom yang diberikan sudah dijamin unik
      
    Daftar Exceptions:
      1. jika ada baris dengan jumlah kolom berbeda dari
         sebelumnya,
         
           raise Exception(f"Banyaknya kolom pada baris {x} tidak konsisten.")
           
           dengan x adalah nomor baris (1-based) yang kolomnya 
           berlebih pertama kali.
           
      2. jika tabel kosong,
            
            raise Exception("Tabel tidak boleh kosong.")
    
    parameter:
    file_name (string): nama file comma separated value
    delimiter (string): karakter pemisah antar kolom pada 
                        suatu baris.
                        
    return (list, list, list): (data, list nama kolom, list tipe data)
  """
  # TODO: Implement
  with open(file_name, "r") as f:
    # Putting all lines into a list
    contents = f.readlines()
  
  # EXCEPTION: Checking if the table is empty
  if len(contents[1:]) == 0:
    raise Exception("Tabel tidak boleh kosong.")

  # ———————— DATAFRAME 0 ————————
  dataframe_0 = []
  for line in range(1, len(contents)):
    # Split each line by delimiter into a nested list
    line_lst = contents[line].strip().split(delimiter)
    # EXCEPTION: Check if the number of columns is consistent
    if len(line_lst) != len(contents[line - 1].strip().split(delimiter)):
      raise Exception(f"Banyaknya kolom pada baris {line + 1} tidak konsisten.")
    # Append the nested list into dataframe_0
    dataframe_0.append(line_lst)
  
  # ———————— DATAFRAME 1 ————————
  # Split the first line by delimiter into a list
  dataframe_1 = contents[0].strip().split(delimiter)

  # ———————— DATAFRAME 2 ————————
  dataframe_2 = []
  # Main loop to check the type of each column
  for col in range(len(dataframe_1)):
    get_type_lst = []
    # Loop to check the type of each cell in a column
    for line in range(1, len(dataframe_0)): 
      # Append the type of each cell into a list
      get_type_lst.append(get_type(dataframe_0[line][col]))

    # Checking if string is in the list
    if "str" in get_type_lst:
      dataframe_2.append("str")
    else:
      # Checking if float is in the list
      if "float" in get_type_lst:
        dataframe_2.append("float")
      # If not, then the type of the column is int
      else:
        dataframe_2.append("int")
  
  # Return the dataframe as a list with 3 elements
  return (dataframe_0, dataframe_1, dataframe_2)

def to_list(dataframe):
  """
  
    -- DIBUKA KE PESERTA --
    
    mengembalikan bagian list of lists of items atau tabel data
    pada dataframe. Gunakan fungsi ini kedepannya jika ada keperluan
    untuk akses bagian data/tabel pada dataframe.
    
    parameter:
    dataframe (list, list, list): sebuah dataframe yang merupakan 3-tuple
    
    return (list): list of lists of items
  """
  return dataframe[0]

def get_column_names(dataframe):
  """
  
    -- DIBUKA KE PESERTA --
  
    dataframe[1] adalah berisi list of column names. Gunakan fungsi ini
    kedepannya jika ada keperluan untuk akses daftar nama kolom pada
    sebuah dataframe.
    
    parameter:
    dataframe (list, list, list): sebuah dataframe yang merupakan 3-tuple
    
    return (list): list of column names
  """
  return dataframe[1]
  
def get_column_types(dataframe):
  """
  
    -- DIBUKA KE PESERTA --
  
    dataframe[2] adalah berisi daftar tipe data dari
    setiap kolom tabel. Hanya ada tiga jenis tipe data,
    yaitu "str", "int", dan "float"
    
    parameter:
    dataframe (list, list, list): sebuah dataframe yang merupakan 3-tuple
    
    return (list): list of type names
  """
  return dataframe[2]

def head(dataframe, top_n=10):
  """
  
    -- DIBUKA KE PESERTA --
  
    top_n baris pertama pada tabel!
  
    Mengembalikan string yang merupakan representasi tabel
    (top_n baris pertama) dengan format:
    
     kolom_1|     kolom_2|     kolom_3|     ...
    ------------------------------------------- 
    value_11|    value_12|    value_13|     ...
    value_21|    value_22|    value_23|     ...
    ...         ...         ...
    
    Space setiap kolom dibatasi hanya 15 karakter dan right-justified.
    
    parameter:
    dataframe (list, list, list): sebuah dataframe
    top_n (int): n, untuk penampilan top-n baris saja
    
    return (string): representasi string dari penampilan tabel.
    
    Jangan pakai print()! tetapi return string!
  """
  cols = get_column_names(dataframe)
  out_str = ""
  out_str += "|".join([f"{col[:15]:>15}" for col in cols]) + "\n"
  out_str += ("-" * (15 * len(cols) + (len(cols) - 1))) + "\n"
  for row in to_list(dataframe)[:top_n]:
    out_str += "|".join([f"{col[:15]:>15}" for col in row]) + "\n"

  return out_str
  
def info(dataframe):
  """
    Mengembalikan string yang merupakan representasi informasi
    dataframe dalam format:
    
    Total Baris = xxxxx baris
    
    Kolom          Tipe
    ------------------------------
    kolom_1        tipe_1
    kolom_2        tipe_2
    ...
    
    Space untuk kolom dan tipe adalah 15 karakter, left-justified
    
    parameter:
    dataframe (list, list, list): sebuah dataframe
    
    return (string): representasi string dari info dataframe    
  """
  # TODO: Implement
  # Getting the nessesary informations
  total_baris = len(to_list(dataframe)) # Total rows
  header = get_column_names(dataframe) # Column names
  header_type = get_column_types(dataframe) # Column types

  # Formatting the str_out header
  str_out = f"Total Baris = {total_baris} baris" + "\n\n" +\
  "{:<16}".format("Kolom") + "{:<14}".format("Tipe") + "\n" +\
  "------------------------------"

  # Filling the str_out body
  for i in range(len(header)):
    str_out += "\n" + "{:<16}".format(header[i]) + "{:<14}".format(header_type[i])
  
  return str_out

def satisfy_cond(value1, condition, value2):
  """
    -- DIBUKA KE PESERTA --
    
    parameter:
    value1 (tipe apapun yang comparable): nilai pertama
    condition (string): salah satu dari ["<", "<=", "==", ">", ">=", "!="]
    value2 (tipe apapun yang comparable): nilai kedua
    
    return (boolean): hasil perbandingan value1 dan value2
    
  """
  if condition == "<":
    return value1 < value2
  elif condition == "<=":
    return value1 <= value2
  elif condition == ">":
    return value1 > value2
  elif condition == ">=":
    return value1 >= value2
  elif condition == "!=":
    return value1 != value2
  elif condition == "==":
    return value1 == value2
  else:
    raise Exception(f"Operator {condition} tidak dikenal.")

def select_rows(dataframe, col_name, condition, value):
  """
  Mengembalikan dataframe baru dimana baris-baris sudah
  dipilih hanya yang nilai col_name memenuhi 'condition'
  terkait 'value' tertentu.
  
  Gunakan/Call fungsi satisfy_cond(value1, condition, value2) yang
  sudah didefinisikan sebelumnya!
  
  contoh:
    select_rows(dataframe, "umur", "<=", 50) akan mengembalikan
    dataframe baru dengan setiap baris memenuhi syarat merupakan
    item dengan kolom umur <= 50 tahun.
    
  Exceptions:
    1. jika col_name tidak ditemukan,
    
        raise Exception(f"Kolom {col_name} tidak ditemukan.")
        
    2. jika condition bukan salah satu dari ["<", "<=", "==", ">", ">=", "!="]
    
        raise Exception(f"Operator {condition} tidak dikenal.")
  
  parameter:
  dataframe (list, list, list): sebuah dataframe
  col_name (string): nama kolom sebagai basis untuk selection
  condition (string): salah satu dari ["<", "<=", "==", ">", ">=", "!="]
  value (tipe apapun): nilai untuk basis perbandingan pada col_name
  
  return (list, list, list): dataframe baru hasil selection atau filtering
  
  """
  # TODO: Implement
  # Checking if the column is found
  try:
    # Getting the index of the column
    index = get_column_names(dataframe).index(col_name)
  except:
    # EXCEPTION: If the column is not found
    raise Exception(f"Kolom {col_name} tidak ditemukan.")
  
  # EXCEPTION: Checking if the condition is valid
  # (Already defined in the satisfy_cond() function)
  
  # Filtering the dataframe
  new_dataframe = []
  # Looping through each row
  for row in to_list(dataframe):
    # Checking if the condition is satisfied
    if get_type(row[index]) == "str":
      # If the value is string
      if satisfy_cond(row[index], condition, value):
        new_dataframe.append(row)
    else:
      # If the value is numeric (int or float)
      if satisfy_cond(float(row[index]), condition, float(value)):
        new_dataframe.append(row)

  # Returns a list the way read_csv() does
  return (new_dataframe, get_column_names(dataframe), get_column_types(dataframe))
  
def select_cols(dataframe, selected_cols):
  """
    Mengembalikan dataframe baru dimana kolom-kolom sudah
    dipilih hanya yang terdapat pada 'selected_cols' saja.
    
    contoh:
    select_cols(dataframe, ["umur", "nama"]) akan mengembalikan
    dataframe baru yang hanya terdiri dari kolom "umur" dan "nama".
    
    Exceptions:
      1. jika ada nama kolom pada selected_cols yang tidak
         ditemukan, 
         
           raise Exception(f"Kolom {selected_col} tidak ditemukan.")
           
      2. jika select_cols adalah list kosong [],
      
           raise Exception("Parameter selected_cols tidak boleh kosong.")
    
    parameter:
    dataframe (list, list, list): sebuah dataframe
    selected_cols (list): list of strings, atau list yang berisi
                          daftar nama kolom
                          
    return (list, list, list): dataframe baru hasil selection pada
                               kolom, yaitu hanya mengandung kolom-
                               kolom pada selected_cols saja.
    
  """
  # TODO: Implement
  # EXCEPTION: Checking if the selected_cols is emtpy
  if len(selected_cols) == 0:
    raise Exception("Parameter selected_cols tidak boleh kosong.")
  
  # Finding the index of each selected columns
  selected_index = []
  for col in selected_cols:
    try:
      # Getting the index of the column
      selected_index.append(get_column_names(dataframe).index(col))
    except:
      # EXCEPTION: If the column is not found
      raise Exception(f"Kolom {col} tidak ditemukan.")
  
  new_dataframe = []
  # Looping through each row
  for row in to_list(dataframe):
    new_row = []
    # Looping through each selected column
    for index in selected_index:
      # Appending the value of each selected column into a list
      new_row.append(row[index])
    # Appending the list into the new dataframe
    new_dataframe.append(new_row)
  
  # Returns a list the way read_csv() does
  return (new_dataframe, selected_cols, get_column_types(dataframe))

def count(dataframe, col_name):
  """
    mengembalikan dictionary yang berisi frequency count dari
    setiap nilai unik pada kolom col_name.
    
    Tipe nilai pada col_name harus string !
    
    Exceptions:
      1. jika col_name tidak ditemukan,
      
           raise Exception(f"Kolom {col_name} tidak ditemukan.")
      
      2. jika tipe data col_name adalah numerik (int atau float),
      
           raise Exception(f"Kolom {col_name} harus bertipe string.")      
      
      3. jika tabel kosong, alias banyaknya baris = 0,
           
           raise Exception("Tabel kosong.")

    Peserta bisa menggunakan Set untuk mengerjakan fungsi ini.
           
    parameter:
    dataframe (list, list, list): sebuah dataframe
    col_name (string): nama kolom yang ingin dihitung rataannya
    
    return (dict): dictionary yang berisi informasi frequency count
                   dari setiap nilai unik.
  """
  # TODO: Implement
  # EXCEPTION: Checking if the table is empty
  if len(dataframe[0][1:]) == 0:
    raise Exception("Tabel kosong.")

  # Putting all values from the column into a list
  col_values = value_getter(dataframe, col_name, "string")

  counts = {}

  # Counting the frequency of each unique value
  for value in col_values:
    if value in counts:
      counts[value] += 1
    else:
      counts[value] = 1

  return counts

def mean_col(dataframe, col_name):
  """
    Mengembalikan nilai rata-rata nilai pada kolom 'col_name'
    di dataframe.
    
    Exceptions:
      1. jika col_name tidak ditemukan,
      
           raise Exception(f"Kolom {col_name} tidak ditemukan.")
      
      2. jika tipe data col_name adalah string,
      
           raise Exception(f"Kolom {col_name} bukan bertipe numerik.")      
      
      3. jika tabel kosong, alias banyaknya baris = 0,
           
           raise Exception("Tabel kosong.")
           
    parameter:
    dataframe (list, list, list): sebuah dataframe
    col_name (string): nama kolom yang ingin dihitung rataannya
    
    return (float): nilai rataan
  """
  # TODO: Implement
  # EXCEPTION: Checking if the table is empty
  if len(dataframe[1:]) == 0:
    raise Exception("Tabel kosong.")
  
  # Getting all the values from the column
  col_values = value_getter(dataframe, col_name)
  
  # Calculating the mean
  sum = 0
  for value in col_values:
    sum += value
  
  # Return the mean
  return sum / len(col_values)
  
def show_scatter_plot(x, y, x_label, y_label):
  """
    -- DIBUKA KE PESERTA --
    
    parameter:
    x (list): list of numerical values, tidak boleh string
    y (list): list of numerical values, tidak boleh string
    x_label (string): label pada sumbu x
    y_label (string): label pada sumbu y
    
    return None, namun fungsi ini akan menampilkan scatter
    plot dari nilai pada x dan y.
    
    Apa itu scatter plot?
    https://chartio.com/learn/charts/what-is-a-scatter-plot/
  """
  plt.scatter(x, y)
  plt.xlabel(x_label)
  plt.ylabel(y_label)

  # Set the X-axis and Y-axis tick locations
  plt.xticks(my_arange(0, max(x), 0.1))
  plt.yticks(my_arange(0, max(y), 0.1))

  plt.show()
  
def scatter(dataframe, col_name_x, col_name_y):
  """
    fungsi ini akan menampilkan scatter plot antara kolom col_name_x
    dan col_name_y pada dataframe.
    
    pastikan nilai-nilai pada col_name_x dan col_name_y adalah angka!
    
    Exceptions:
      1. jika col_name_x tidak ditemukan,
      
           raise Exception(f"Kolom {col_name_x} tidak ditemukan.")
           
      2. jika col_name_y tidak ditemukan,
      
           raise Exception(f"Kolom {col_name_y} tidak ditemukan.")
           
      3. jika col_name_x BUKAN numerical,
      
           raise Exception(f"Kolom {col_name_x} bukan bertipe numerik.")
           
      4. jika col_name_y BUKAN numerical,
      
           raise Exception(f"Kolom {col_name_y} bukan bertipe numerik.")
    
    parameter:
    dataframe (list, list, list): sebuah dataframe
    col_name_x (string): nama kolom yang nilai-nilainya diplot pada axis x
    col_name_y (string): nama kolom yang nilai-nilainya diplot pada axis y
    
    Call fungsi show_scatter_plot(x, y) ketika mendefinisikan fungsi
    ini!
    
    return None
  """
  # TODO: Implement
  # Get all the values of column x and y, then put it in a list
  col_values_x = value_getter(dataframe, col_name_x)
  col_values_y = value_getter(dataframe, col_name_y)

  # Call the show_scatter_plot() function
  show_scatter_plot(col_values_x, col_values_y, col_name_x, col_name_y)


# ———————————————————————— EXTRA FUNCTIONS ————————————————————————


def scatter_extra(dataframe, col_name_x, col_name_y, colorbar="Rings"):
  """
    This function will show a scatter plot just like before, but with a colorbar and grid lines.
  """
  # Get all the values of column colorbar, x, and y, then put it in a list
  col_values_extra = value_getter(dataframe, colorbar)
  col_values_x = value_getter(dataframe, col_name_x)
  col_values_y = value_getter(dataframe, col_name_y)

  # Make the scatter plot
  plt.scatter(col_values_x, col_values_y, c=col_values_extra, cmap='plasma', zorder=2)

  # Set the X-axis and Y-axis tick locations
  plt.xticks(my_arange(0, max(col_values_x), 0.1))
  plt.yticks(my_arange(0, max(col_values_y), 0.1))

  # Turn on the grid lines
  plt.grid(True, zorder=1)

  # Set the X-axis and Y-axis labels
  plt.xlabel(col_name_x)
  plt.ylabel(col_name_y)

  # Add a colorbar
  cbar = plt.colorbar()
  cbar.set_label(colorbar)

  # Show the plot
  plt.show()

def scatter_3d(dataframe, col_name_x, col_name_y, col_name_z):
  """
    This function will show a 3D scatter plot.
  """
  # Get all the values of column x, y, and z, then put it in a list
  col_values_x = value_getter(dataframe, col_name_x)
  col_values_y = value_getter(dataframe, col_name_y)
  col_values_z = value_getter(dataframe, col_name_z)

  # Make the 3D scatter plot
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.scatter(col_values_x, col_values_y, col_values_z, marker='o')

  # Set the X-axis, Y-axis, and Z-axis labels
  ax.set_xlabel(col_name_x)
  ax.set_ylabel(col_name_y)
  ax.set_zlabel(col_name_z)

  # Show the plot
  plt.show()

def scatter_3d_extra(dataframe, col_name_x, col_name_y, col_name_z, colorbar="Rings"):
  """
  This function will show a 3D scatter plot just like before, but with a colorbar and grid lines.
  """
  # Get all the values of column colorbar, x, y, and z, then put it in a list
  col_values_extra = value_getter(dataframe, colorbar)
  col_values_x = value_getter(dataframe, col_name_x)
  col_values_y = value_getter(dataframe, col_name_y)
  col_values_z = value_getter(dataframe, col_name_z)

  # Make the 3D scatter plot
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  scatter = ax.scatter(col_values_x, col_values_y, col_values_z, c=col_values_extra, cmap='plasma', marker='o', zorder=2)

  # Set the X-axis, Y-axis, and Z-axis labels
  ax.set_xlabel(col_name_x)
  ax.set_ylabel(col_name_y)
  ax.set_zlabel(col_name_z)

  # Turn on the grid lines
  ax.grid(True, zorder=1)

  # Add a colorbar
  cbar = plt.colorbar(scatter, ax=ax)
  cbar.set_label(colorbar)

  # Show the plot
  plt.show()

def stats(dataframe, col_name):
  """
    This function will show the extra statistics of the dataframe, including:
    - Minimum value
    - Maximum value
    - Median value
    - Quartile deviation
    - Average deviation
    - Standard deviation
    - Variance deviation
  """
  # Gettings the column values
  col_values = value_getter(dataframe, col_name)

  # Find the minimum value
  min_value = min(col_values)

  # Find the maximum value
  max_value = max(col_values)

  # Find the median value
  col_values.sort()
  if len(col_values) % 2 == 0:
    median_value = (col_values[len(col_values) // 2] + col_values[len(col_values) // 2 - 1]) / 2
  else:
    median_value = col_values[len(col_values) // 2]
  
  # Find the quartile deviation
  q1 = col_values[len(col_values) // 4]
  q3 = col_values[len(col_values) * 3 // 4]
  quartile_deviation = (q3 - q1) / 2

  # Find the average deviation
  average_deviation = 0
  for value in col_values:
    average_deviation += abs(value - mean_col(dataframe, col_name))
  average_deviation /= len(col_values)

  # Find the standard deviation
  standard_deviation = 0
  for value in col_values:
    standard_deviation += (value - mean_col(dataframe, col_name)) ** 2
  standard_deviation /= len(col_values)
  standard_deviation = standard_deviation ** 0.5

  # Find the variance deviation
  variance_deviation = 0
  for value in col_values:
    variance_deviation += (value - mean_col(dataframe, col_name)) ** 2
  variance_deviation /= len(col_values)

  # Print the statistics
  print("\nStatistics:" + "\n" +
  f"Minimum value: {min_value}" + "\n" +
  f"Maximum value: {max_value}" + "\n" +
  f"Median value: {median_value}" + "\n" +
  f"Quartile deviation: {quartile_deviation}" + "\n" +
  f"Average deviation: {average_deviation}" + "\n" +
  f"Standard deviation: {standard_deviation}" + "\n" +
  f"Variance deviation: {variance_deviation}")


# ———————————————————————— MAIN PROGRAM ————————————————————————


if __name__ == "__main__":
  # TODO: Buat program yang memanfaatkan fungsi-fungsi di atas
  
  # Memuat dataframe dari tabel pada file abalone.csv
  dataframe = read_csv("abalone.csv")
  new_dataframe = select_rows(dataframe, "Length", ">", 1000)

  print(mean_col(new_dataframe, "Rings"))

  # # Cetak 10 baris pertama
  # print(head(dataframe, top_n=10))

  # # Cetak informasi dataframe
  # print(info(dataframe))

  # # Kembalikan dataframe baru, dengan kolom Length > 0.49
  # new_dataframe = select_rows(dataframe, "Length", ">", 0.49)
  # print(head(new_dataframe, top_n=5))

  # # Kembalikan dataframe baru, dimana Sex == "M" DAN Length > 0.49
  # new_dataframe = select_rows(select_rows(dataframe, "Length", ">", 0.49), "Sex", "==", "M")
  # print(head(new_dataframe, top_n=5))

  # # Kembalikan dataframe baru yang hanya terdiri dari kolom Sex, Length, Diameter, dan Rings
  # new_dataframe = select_cols(dataframe, ["Sex", "Length","Diameter", "Rings"])
  # print(head(new_dataframe, top_n=5))

  # # Hitung mean pada kolom Length (pada dataframe original)
  # print(mean_col(dataframe, "Length"))

  # # melihat unique values pada kolom Sex, dan frekuensi kemunculannya (pada dataframe original)
  # print(count(dataframe, "Sex"))

  # # Tampilkan scatter plot antara kolom "Height" dan "Diameter"
  # scatter(dataframe, "Height", "Diameter")

  # # Tampilkan scatter plot antara kolom "Height" dan "Diameter" dengan colorbar "Rings"
  # scatter_extra(dataframe, "Height", "Diameter")

  # # Tampilkan scatter plot 3D antara kolom "Height", "Diameter", dan "Length"
  # scatter_3d(dataframe, "Height", "Diameter", "Length")

  # # Tampilkan scatter plot 3D antara kolom "Height", "Diameter", dan "Length" dengan colorbar "Rings"
  # scatter_3d_extra(dataframe, "Height", "Diameter", "Length")

  # # Tampilkan statistik tambahan dari kolom "Height"
  # stats(dataframe, "Height")