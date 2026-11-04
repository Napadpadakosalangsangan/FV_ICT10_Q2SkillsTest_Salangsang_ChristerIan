from pyscript import document, display

# Dictionary of non-metals
non_metals = {
  "H":  ("Hydrogen", 1, 1.008),
  "He": ("Helium", 2, 4.003),
  "C":  ("Carbon", 6, 12.011),
  "N":  ("Nitrogen", 7, 14.007),
  "O":  ("Oxygen", 8, 15.999),
  "F":  ("Fluorine", 9, 18.998),
  "Ne": ("Neon", 10, 20.180),
  "P":  ("Phosporus", 15, 30.974),
  "S":  ("Sulfur", 16, 32.060),
  "Cl": ("Chlorine", 17, 35.450),
  "Ar": ("Argon", 18, 39.950),
  "Se": ("Selenium", 34, 78.960),
  "Br": ("Bromine", 35, 79.904),
  "Kr": ("Krypton", 36, 83.798),
  "I":  ("Iodine", 53, 126.904),
  "Xe": ("Xenon", 54, 131.293),
  "Rn": ("Radon", 86, 222)
}


def check(e):

 # Getting the entered element symbol
  symbol = document.getElementById("element").value.capitalize()

# Retrieving the element's information from the dictionary above
  result = non_metals.get(symbol, ("Element not found", "-", "-"))
  name, number, mass = result

# Getting the HTML elements where the results will be displayed
  symbol_input = document.getElementById("symbol")
  name_input = document.getElementById("name")
  number_input = document.getElementById("number")
  mass_input = document.getElementById("mass")

# Displaying the information
  symbol_input.innerText = symbol
  name_input.innerText = name
  number_input.innerText = number
  mass_input.innerText = mass



  

