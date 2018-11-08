class DataPer:
    def __init__(self, atomic_mass, element_name, element_symbol, atomic_number):
        self.atomic_mass = atomic_mass
        self.element_name = element_name
        self.element_symbol = element_symbol
        self.atomic_number = atomic_number


speed_of_light = 3*10**8
planck_constant = 6.626*10**(-34)
Rydberg_constant = 2.179e-18


def line_make():
    for x in range(0, 120):
        print("*", end="")
    print("")


def simpleCalculation(elementList):  # bring up list after each calc needs percent comp
    line_make()
    print("1.)Average Atomic Mass\t2.)Density\t3.)Electromagnetic Spectrum\t\nReturn to Return")
    Choice = input("What would you like to do? ")
    while(Choice != "Return"):
        if(Choice == "1"):
            line_make()
            print(average_atomic_mass())
            line_make()
            print("1.)Average Atomic Mass\n2.)Density\t3.)Electromagnetic Spectrum\t4.)Empirical Formula\t5.)Molecular Weight\nReturn to Return")
            Choice = input("Anything else? ")
        elif(Choice == "2"):
            line_make()
            print(density())
            line_make()
            print("1.)Average Atomic Mass\n2.)Density\t3.)Electromagnetic Spectrum\t4.)Empirical Formula\t5.)Molecular Weight\nReturn to Return")
            Choice = input("Anything else? ")
        elif(Choice == "3"):
            spectrum()
            line_make()
            print("1.)Average Atomic Mass\n2.)Density\t3.)Electromagnetic Spectrum\t4.)Empirical Formula\t5.)Molecular Weight\nReturn to Return")
            Choice = input("Anything else? ")
        else:
            print("Error has occured, please retry")
            Choice = input("What would you like to do? ")


def Compound_Problems(elementList):  # bring up list after each calc
    line_make()
    print("1.)Compound Molar Mass\t2.)Compound Mass to Moles\t3.)Compound Moles to Mass\t4.)Compound Mass to Mass\t5.)Percent Composition by mass\t6.)Percent Composition by moles\t6.)Empirical Formula\n7.)Molecular Weight and Empirical Formula")
    Choice = input("What would you like to do? ")
    while (Choice != "Return"):
        if (Choice == "1"):
            molar_mass(elementList)
            line_make()
            print("1.)Compound Molar Mass\t2.)Compound Mass to Moles\t3.)Compound Moles to Mass\t4.)Compound Mass to Mass\t")
            Choice = input("What would you like to do? ")
        elif(Choice == "2"):
            mass = input("What is the mass of the substance? ")
            print(Compound_mass_to_moles(mass, elementList))
            line_make()
            print("1.)Compound Molar Mass\t2.)Compound Mass to Moles\t3.)Compound Moles to Mass\t4.)Compound Mass to Mass\t")
            Choice = input("What would you like to do? ")
        elif (Choice == "3"):
            moles = input("How many moles of the substance do you have? ")
            print(Compound_moles_to_mass(moles, elementList))
            line_make()
            print("1.)Compound Molar Mass\t2.)Compound Mass to Moles\t3.)Compound Moles to Mass\t4.)Compound Mass to Mass\t")
            Choice = input("What would you like to do? ")
        elif (Choice == "4"):
            mass = input("Mass of Substance: ")
            print(str(Coumpound_mass_to_mass(mass, elementList)) + " grams")
            line_make()
            print("1.)Compound Molar Mass\t2.)Compound Mass to Moles\t3.)Compound Moles to Mass\t4.)Compound Mass to Mass\t")
            Choice = input("What would you like to do? ")
        elif (Choice == "5"):
            line_make()
            mass_of_substance = input("What is the mass of the entire substance? ")
            number_of_elements = input("How many elements are in this compound? ")
            element_count = 1
            final_print = ""
            while (int(number_of_elements) > 0):
                print("Element No." + element_count)
                element_name = input("What is the element name/symbol? ")
                mass_of_element = input("What is the mass of the element ")

                number_of_elements -= 1

        elif (Choice == "6"):
            line_make()
            print("Substance")
            mass_of_substance = input("What is the mass of the substance")
            element_converting_to = input("What is the element you are converting it to")
            moles_of_substance = Compound_mass_to_moles(mass_of_solution, elementList)
            moles_of_component = Compound_moles_to_moles(moles_of_substance, elementList)
            print(moles_of_component/moles_of_substance)
            line_make()
            print("1.)Compound Molar Mass\t2.)Compound Mass to Moles\t3.)Compound Moles to Mass\t4.)Compound Mass to Mass\t")
        elif (Choice == "7"):
            number_of_elements = input("How many components/elements are there? ")
            count_of_element = 1
            while (number_of_elements > 0):
                percent_of_element = input("% of element", count_of_element)


def print_atomic_mass(element, elementList):
    return(elementList[findElement(element)].atomic_mass)


def Compound_mass_to_moles(mass, elementList):
    return(float(mass)/float(molar_mass(elementList)))


def Compound_moles_to_mass(moles, elementList):
    return(float(moles)*float(molar_mass(elementList)))


def Compound_moles_to_moles(moles, elementList):
    mole_ratio = input(
        "What is the mole ratio of the given moles to a different substance? (Enter 1 if it is just a simple Conversion) ")
    return (float(mole_ratio)*float(moles))


def Coumpound_mass_to_mass(mass, elementList):
    print("First Substance")
    moles = Compound_mass_to_moles(mass, elementList)
    moles = Compound_moles_to_moles(moles, elementList)
    print("Second Substance")
    return(Compound_moles_to_mass(moles, elementList))


def molar_mass(elementList):
    x = 0
    atomic_mass_total = 0
    while(int(x) == 0):
        number_ele = input("How many elements are there in this substance? ")
        y = int(number_ele)
        count = 1
        atomic_mass_total = 0
        final_print = ""
        while (y > 0):
            element = input("What is element number " + str(count) + "? (Insert Symbol or Name) ")
            amount_element = input("How many of these elements are there? ")
            atomic_mass_total = float(
                atomic_mass_total) + elementList[findElement(element, elementList)].atomic_mass*float(amount_element)
            y = y-1
            count = int(count)+1
            final_print = final_print+("You have " + str(amount_element) + " "+str(element)+"\n")
        print(final_print + "With a mass of " + str(atomic_mass_total))
        Check = input("Is this correct? ")
        if (Check == "Yes"):
            x = 1
    return(atomic_mass_total)


def findElement(first, elementList):  # adjust to allow user to retry #redirect to function
    x = 0
    if (len(first) <= 2):
        while (elementList[x].element_symbol != first):
            x = x+1
            if (x == 112):
                print("Error at naming the element")
                return ("-2")
        return(x)

    else:
        while (elementList[x].element_name != first):
            x = x+1
            if (x == 112):
                print("Error at naming the element")
                return ("-2")
        return(x)


def average_atomic_mass():
    num_elements = input("How many isotopes are there? ")
    total_weight = 0
    num_isotope = 1
    while (int(num_elements) > 0):
        atomic_mass = input("What is the atomic mass of isotope number " + str(num_isotope) + "? ")
        percent_abudance = input(
            "What is the percent abudance of isotope number " + str(num_isotope) + "? (in decimal form) ")
        total_weight = float(total_weight) + float(atomic_mass)*float(percent_abudance)
        num_elements = int(num_elements)-1
        num_isotope = int(num_isotope)+1
    return (total_weight)


def density():
    mass = input("What is the mass of the sample? ")
    mass_unit = input("What is the mass unit? ")
    volume = input("What is the volume of the sample? ")
    volume_unit = input("What is the volume unit? ")
    return (str(float(mass)/float(volume)) + " " + mass_unit+"/"+volume_unit)


def spectrum():
    line_make()
    print("1.)Convert Frequency to Wavelength\t2.)Convert Wavelength to Frequency\t3.)Find Energy\n4.)Find Frequency/Wavelength from Energy\t5.)Find Energy of an energy level(Hydrogen Atom)\t6.)Find Energy between two energy levels(Hydrogen Atom)\nReturn to return")
    Choice = input("What would you like? ")
    while(Choice != "Return"):
        if (Choice == "1"):
            line_make()
            frequency = input("What is the frequency? (In hertz) ")
            print(str(frequency_to_wavelength(frequency))+"m")
            line_make()
            print("1.)Convert Frequency to Wavelength\t2.)Convert Wavelength to Frequency\t3.)Find Energy\n4.)Find Frequency/Wavelength from Energy\t5.)Find Energy of an energy level(Hydrogen Atom)\t6.)Find Energy between two energy levels(Hydrogen Atom)\nReturn to return")
            Choice = input("What would you like? ")
        elif(Choice == "2"):
            line_make()
            wavelength = input("What is the wavelength? (In meters) ")
            print(str(wavelength_to_frequency(wavelength))+"Hz")
            line_make()
            print("1.)Convert Frequency to Wavelength\t2.)Convert Wavelength to Frequency\t3.)Find Energy\n4.)Find Frequency/Wavelength from Energy\t5.)Find Energy of an energy level(Hydrogen Atom)\t6.)Find Energy between two energy levels(Hydrogen Atom)\nReturn to return")
            Choice = input("What would you like? ")
        elif (Choice == "3"):
            line_make()
            print(str(energy_with_light()) + "Joules")
            line_make()
            print("1.)Convert Frequency to Wavelength\t2.)Convert Wavelength to Frequency\t3.)Find Energy\n4.)Find Frequency/Wavelength from Energy\t5.)Find Energy of an energy level(Hydrogen Atom)\t6.)Find Energy between two energy levels(Hydrogen Atom)\nReturn to return")
            Choice = input("What would you like? ")
        elif (Choice == "4"):
            line_make()
            light_from_energy()
            line_make()
            print("1.)Convert Frequency to Wavelength\t2.)Convert Wavelength to Frequency\t3.)Find Energy\n4.)Find Frequency/Wavelength from Energy\t5.)Find Energy of an energy level(Hydrogen Atom)\t6.)Find Energy between two energy levels(Hydrogen Atom)\nReturn to return")
            Choice = input("What would you like? ")
        elif (Choice == "5"):
            line_make()
            print(str(energy_level())+" Joules")
            line_make()
            print("1.)Convert Frequency to Wavelength\t2.)Convert Wavelength to Frequency\t3.)Find Energy\n4.)Find Frequency/Wavelength from Energy\t5.)Find Energy of an energy level(Hydrogen Atom)\t6.)Find Energy between two energy levels(Hydrogen Atom)\nReturn to return")
            Choice = input("What would you like? ")
        elif (Choice == "6"):
            line_make()
            print("Initial Level: ")
            initial = energy_level()
            print("Final Level: ")
            final = energy_level()
            if ((final-initial) > 0):
                print("Energy is absorbed")
            else:
                print("Energy is released/emissioned")
            print(str(final-initial) + " Joules")
            line_make()
            print("1.)Convert Frequency to Wavelength\t2.)Convert Wavelength to Frequency\t3.)Find Energy\n4.)Find Frequency/Wavelength from Energy\t5.)Find Energy of an energy level(Hydrogen Atom)\t6.)Find Energy between two energy levels(Hydrogen Atom)\nReturn to return")
            Choice = input("What would you like? ")

        else:
            line_make()
            print("Error has occured please try again")
            print("1.)Convert Frequency to Wavelength\t2.)Convert Wavelength to Frequency\t3.)Find Energy\n4.)Find Frequency/Wavelength from Energy\t5.)Find Energy of an energy level(Hydrogen Atom)\t6.)Find Energy between two energy levels(Hydrogen Atom)\nReturn to return")
            Choice = input("What would you like? ")


def frequency_to_wavelength(frequency):
    return (float(speed_of_light)/float(frequency))


def wavelength_to_frequency(wavelength):
    return (float(speed_of_light)/float(wavelength))


def energy_with_light():
    decision = input("Are you calculating with 1.)Frequency or 2.)Wavelength\n")
    if (int(decision) == 1):
        frequency = input("What is the frequency? (In hertz) ")
        return (float(planck_constant)*float(frequency))
    elif (int(decision) == 2):
        wavelength = input("What is the wavelength? (In meters) ")
        return(float(planck_constant)*float(wavelength_to_frequency(wavelength)))


def light_from_energy():
    amount_of_energy = input("How much energy do you have? (In joules) ")
    frequency = float(amount_of_energy)/float(planck_constant)
    wavelength = frequency_to_wavelength(frequency)
    print(str(frequency) + " Hz and " + str(wavelength) + " m")


def energy_level():
    level = input("What energy level are you given? ")
    return(float(Rydberg_constant)*-1/(float(level)**2))

def line_break():
    print("")
