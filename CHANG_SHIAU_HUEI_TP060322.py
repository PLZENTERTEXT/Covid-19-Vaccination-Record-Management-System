# CHANG SHIAU HUEI
# TP060322

import os.path, sys

# Generate the necessary files
def fileCheck():
    # Return True if "patients.txt" is an existing regular file
    if os.path.isfile("patients.txt") == False:
        fh = open("patients.txt", "w")
        fh.close()
    
    # Return True if "vaccination.txt" is an existing regular file
    if os.path.isfile("vaccination.txt") == False:
        fh = open("vaccination.txt", "w")
        fh.close()

# To convert string in file to list
def listCheck(string):
    separate = list(string.split("|"))
    return separate

# To convert string in list to character
def characterCheck(string):
    separate = list(string.split("-"))
    return separate

# To count how many lines are in the file
def lineCount(fileName):
    fh = open(fileName, "r")
    lineCount = 0
    for line in fh:
        if line != "\n":
            lineCount += 1
    fh.close()
    return lineCount

# Integer validations
def integerValidation(lineShown):
    while True:
        try:
            item = int(input(lineShown))
        except:
            print("Your input is invalid. Please try again by entering integers.\n")
            continue
        if item == -1:
            sys.exit()
        else:
            return item

# Float validation
def floatValidation(lineShown):
    while True:
        try:
            item = float(input(lineShown))
            decimal = round(item, 2)
        except:
            print("Your input is invalid. Please try again by entering integers or floats.\n")
            continue
        if item == -1:
            sys.exit()
        else:
            return decimal

# Checks if the user inputted vaccination ID exists
def vacIDValid(fileUsed):
    vacID = str(input("Please insert your vaccination ID (Enter 'X' to quit): ")).upper()
    if vacID == "X":
        sys.exit()
    else:
        with open(fileUsed,"r") as fh:
            for row in fh:
                # Split the string into a list
                vacIDLine = listCheck(str(row))
                if vacIDLine[0] == vacID:
                    break
    return vacIDLine, vacID


# -------------------------------------------------------- Section 1 Functions ------------------------------------------------------------------
# Selecting a vaccination center
def vaccinationCenterSelection():
    while True:
        print("Which vaccination centre are you going to? [ VC1 / VC2 ]")
        vc = str(input("Enter 'X' to quit: "))
        # Validating input to be only "VC1" or "VC2"
        if vc.upper() == "X":
            sys.exit()
        elif (vc.upper() != "VC1") and (vc.upper() != "VC2") and (vc.upper() != "X"):
            print("Please choose either VC1 or VC2 only.\n")
            continue
        elif vc.upper() == "VC1":
            vc = "VC1"
        else:
            vc = "VC2"
        return vc

# To check if the name exists in the file chosen
def nameCheck(fileUsed):
    while True:
        valid = True
        name = str(input("Please insert your name (Enter 'X' to quit): ")).upper()
        if name == "X":
            sys.exit()
        elif len(name) > 23:
            print("Please input a name within 23 characters.\n")
        else:
            with open(fileUsed,"r") as fh:
                # Reads all lines as string elements in a list to be compared later
                info = fh.readlines()
                if lineCount(fileUsed) > 0:
                    for row in info:
                        nameLine = listCheck(str(row))
                        # Check if the second section of the line in the "patients.txt" file matches the user input
                        if nameLine[1].upper() == name.upper():
                            print("A record with this name already exists.\n")
                            valid = False
                    if valid == True:
                        return name
                else:
                    return name

# Letting the user pick a vaccine from a list
def vaccineSelection(listUsed): 
    print("You are elligble for these vaccines:", listUsed)
    while True:
        vaccine = str(input("Please choose only one vaccine from the list above (Enter 'X' to exit): ")).upper()
        if vaccine == "X":
            sys.exit()
        for vac in listUsed:
            # Matches input with the items in the list
            if vac.upper() == vaccine.upper():
                print("You have chosen " + vaccine + ".")
                return vaccine 
            else:
                continue

# Create a unique ID: Check the current IDs in the file and add 1 to the last existant ID
def uniqueIDGenerator(vc):
    vacID = 0
    with open("patients.txt","r") as fh:
        if lineCount("patients.txt") > 0:
            lines = fh.readlines()
            lastLine = lines[-1:]
            # Split the string into a list
            vacIDLine = listCheck(str(lastLine))
            # Take the first section (vacID)
            vacIDSection = characterCheck(str(vacIDLine[0]))
            # Increase second section  of vacID by 1 to generate new sequenced vacID
            increment = int(vacIDSection[1]) + 1
            vacID = vc + "-" + str(increment)
        else:
            vacID = vc + "-1"
    
    return vacID

# Extra information
def extraInformation():
    # Height 
    height = floatValidation("Please input your height in cm (Enter '-1' to quit): ")
    h = "Height:" + str(height) + "cm"

    # Weight
    weight = floatValidation("Please input your weight in kg (Enter '-1' to quit): ")
    w = "Weight:" + str(weight) + "kg"
    
    return h, w

# Print Section 1 results
def printResultsSectionOne(name, vacID):
    print("\n", " Registration Details ".center(100, "="))
    print("\n", "You have successfully registered.".center(100, " "))
    print("\n\tUser:", name)
    print("\tYour vaccination ID is " + vacID + ".")
    print("\nDo remember to head to 'Section 2 - Vaccine Administration' after taking your first vaccination dose!")

# Section 1 - New Patient Registration
def newPatientRegistration():
    while True:
        # Selecting a vaccination center
        vc = vaccinationCenterSelection()
        
        # To check if the name exists in the "patients.txt" file
        name = (nameCheck("patients.txt")).upper()

        # Age validation
        age = integerValidation("Please insert your age (Enter '-1' to quit): ")
       
        # Check which vaccine is elligible according to age and put them in a list called elligibleVac
        # Letting the user pick a vaccine from a list
        elligibleVac = []
        # Inserting elligible vaccines into a list (elligibleVac)
        if age >= 12:
            elligibleVac.append("AF")
            elligibleVac.append("DM")
            if age >= 18:
                elligibleVac.append("BV")
                elligibleVac.append("EC")
            if age <= 45:
                elligibleVac.append("CZ")
        else:
            print("You are not elligible for any vaccine.")
            break

        # Letting the user pick a vaccine from a list called elligibleVac
        vaccine = vaccineSelection(elligibleVac)

        # Validation for phoneNum
        phoneNum = integerValidation("Please insert your phone number (Without '-', Enter '-1' to exit): ")
        phoneNum = "0" + str(phoneNum)

        # Inserting email
        email = str(input("Please insert your email (Enter 'X' to quit): "))
        if email.upper() == "X":
            sys.exit()

        # To create a unique vaccination ID
        vacID = uniqueIDGenerator(vc)
        
        # Extra information
        height, weight = extraInformation()

        # Print results
        printResultsSectionOne(name, vacID)

        # To put the information in "patients.txt"
        with open ("patients.txt","a") as fh:
            fh.write(f"{vacID}|{name}|{vc}|{age}|{vaccine}|{phoneNum}|{email}|{height}|{weight}\n")
        with open ("vaccination.txt","a") as fh:
            fh.write(f"{vacID}|{name}|{vc}|{vaccine}|NEW\n")
        break


# -------------------------------------------------------- Section 2 Functions ------------------------------------------------------------------
# Updating vaccination status and displaying the interval between doses
def vaccinationStatusAndIntervalBetweenDoses(vaccine):
    # For EC Vaccine
    while True:
        valid = True
        if vaccine == "EC":
            print("Have you received your first vaccination dose? [ Y / N ]")
            choice = str(input("Enter 'X' to quit: ")).upper()
            if choice == "X":
                sys.exit()
            elif choice == "Y":
                status = "COMPLETED"
                print("You have finished your vaccination.")
            elif choice == "N":
                status = "NEW"
                print("Come back when you have received your first vaccination dose.")
            else:
                print("Invalid input, please try again.\n")
                valid = False

        # For vaccines other than EC
        else:
            print("Have you received your first vaccination dose? [ Y / N ]")
            choice = str(input("Enter 'X' to quit: ")).upper()
            if choice == "X":
                sys.exit()
            elif choice == "Y":
                print("Have you received your second vaccination dose? [ Y / N ]")
                choice2 = str(input("Enter 'X' to quit: ")).upper()
                if choice2 == "X":
                    sys.exit()
                elif choice2 == "N":
                    if vaccine == "AF":
                        intervalBetweenDoses = 2
                    elif (vaccine == "BV") or (vaccine == "CZ"):
                        intervalBetweenDoses = 3
                    else:
                        intervalBetweenDoses = 4
                    status = "COMPLETED-D1"
                    # Informing for the next vaccination dose session
                    print("Please come after", str(intervalBetweenDoses), "weeks for your second vaccination dose.")
                elif choice2 == "Y":
                    status = "COMPLETED"
                    print("You have finished your vaccination.")
                else:
                    # Goes back to asking if the user received the first vaccination dose or not
                    print("Invalid input, please try again.\n")
                    valid = False
            elif choice == "N":
                status = "NEW"
                print("Come back when you have received your first vaccination dose.")
            else:
                print("Invalid input, please try again.\n")
                valid = False
         
        if valid == True:
            return status

# Delete duplicate items in the file
def deleteDuplicate(vacID):
    with open("vaccination.txt","r") as fh:
        lines = fh.readlines()
        # Delete matching content
        with open("vaccination.txt", 'w') as fh:
            for line in lines:
                # find() returns -1 if no match is found
                if line.find(vacID) != -1:
                    pass
                else:
                    fh.write(line)

# Print Section 2 results
def printResultsSectionTwo(name, vacID, vc, vaccine, status):
    print("\n", " Vaccine Administration ".center(100, "="))
    print("\n\t1. Name\t\t\t\t:\t\t", name)
    print("\t2. Vaccination ID\t\t:\t\t", vacID)
    print("\t3. Vaccination Center\t\t:\t\t", vc)
    print("\t4. Vaccine\t\t\t:\t\t", vaccine)
    print("\t5. Vaccination Status\t\t:\t\t", status)

# Section 2 - Vaccine Administration
def vaccineAdministration():
    # Comparing the user inputted vaccination ID to the ones in the "patients.txt" file to check if it exists
    vacIDLine, vacID = vacIDValid("patients.txt")
            
    # Check if the first section of the line in the "patients.txt" file matches the user input
    if vacIDLine[0] == vacID:

        # Getting information
        name = (vacIDLine[1]).upper()
        vc = vacIDLine[2]
        vaccine = vacIDLine[4]
        print("The selected vaccine for user " + name + " is " + vaccine + ".")
        
        # Updating vaccination status and displaying the interval between doses
        status = vaccinationStatusAndIntervalBetweenDoses(vaccine)
        
        # Print results
        printResultsSectionTwo(name, vacID, vc, vaccine, status)

        # To rewrite records with the same "vacID" in "vaccination.txt" file and delete the line
        deleteDuplicate(vacID)
                         
        # Update the information in "vaccination.txt"
        with open ("vaccination.txt","a") as fh:
            fh.write(f"{vacID}|{name}|{vc}|{vaccine}|{status}\n")

    else:
        print("This vaccination ID doesn't exist. Please register in 'Section 1 - New Patient Registration' before proceeding to this section.")
    

# -------------------------------------------------------- Section 3 Functions ------------------------------------------------------------------
# Total dosage required
def totalDosageRequired(vaccine):
    if vaccine == "EC":
        totalDosage = 1
    else:
        totalDosage = 2
    return totalDosage

# Dosage required
def dosageRequired(status, vaccine):
    if status == "COMPLETED\n":
        dosage = 0
    else:
        if vaccine == "EC":
            dosage = 1
        else:
            if status == "NEW\n":
                dosage = 2
            else:
                dosage = 1
    return dosage

# Print Section 3 results
def printResultsSectionThree(name, vacID, vc, vaccine, totalDosage, dosage, status):
    print("\n", " Search Patient Record & Vaccination Status ".center(100, "="))
    print("\n\t1. Name\t\t\t\t:\t\t", name)
    print("\t2. Vaccination ID\t\t:\t\t", vacID)
    print("\t3. Vaccination Center\t\t:\t\t", vc)
    print("\t4. Vaccine\t\t\t:\t\t", vaccine)
    print("\t5. Total dosage Required\t:\t\t", str(totalDosage))
    print("\t6. Dosage Required\t\t:\t\t", str(dosage))
    print("\t7. Vaccination Status\t\t:\t\t", status)

# Section 3 - Search Patient Record & Vaccination Status
def patientRecordAndVaccineStatus():
    # Comparing the user inputted vaccination ID to the ones in the "vaccination.txt" file to check if it exists
    vacIDLine, vacID = vacIDValid("vaccination.txt")

    # Check if the first section of the line in the "vaccination.txt" file matches the user input
    if vacIDLine[0] == vacID.upper():
        # Getting VC information
        name = vacIDLine[1]
        vc = vacIDLine[2]
        vaccine = vacIDLine[3]
        status = vacIDLine[4]

        # Total dosage required information
        totalDosage = totalDosageRequired(vaccine)
        
        # Dosage required information
        dosage = dosageRequired(status, vaccine)
        
        # Print results
        printResultsSectionThree(name, vacID, vc, vaccine, totalDosage, dosage, status)

    else:
        print("This vaccination ID does not exist. Please register in 'Section 1 - New Patient Registration' to get a vaccination ID.")


# -------------------------------------------------------- Section 4 Functions ------------------------------------------------------------------
# Print Section 4 results
def printResultsSectionFour(totalVC1, totalWaitingD2VC1, totalVaccinatedVC1, totalVC2, totalWaitingD2VC2, totalVaccinatedVC2, totalWaitingD2, totalVaccinated):
    print("\n", " Statistical Information on Patients Vaccinated ".center(100, "="))
    print("\n\tFor VC1:\n\t\tNumber of people receiving vaccine in VC1\t:\t", str(totalVC1))
    print("\t\tPeople who are waiting for dose 2\t\t:\t", str(totalWaitingD2VC1))
    print("\t\tPeople who have completed vaccination\t\t:\t", str(totalVaccinatedVC1))
    print("\n\tFor VC2:\n\t\tNumber of people receiving vaccine in VC2\t:\t", str(totalVC2))
    print("\t\tPeople who are waiting for dose 2\t\t:\t", str(totalWaitingD2VC2))
    print("\t\tPeople who have completed vaccination\t\t:\t", str(totalVaccinatedVC2), "\n", "-" * 100)
    print("\n\t\tTotal people who are waiting for dose 2\t\t:\t", str(totalWaitingD2))
    print("\t\tTotal people that have completed vaccination\t:\t", str(totalVaccinated))

# Section 4 - Statistical Information on Patients Vaccinated
def statisticalInfoOnPatientsVaccinated():
    # Reset values
    totalVC1 = 0
    totalVC2 = 0
    totalWaitingD2VC1 = 0
    totalVaccinatedVC1 = 0
    totalWaitingD2VC2 = 0
    totalVaccinatedVC2 = 0

    # Opening the file for calculation
    with open("vaccination.txt","r") as fh:
        for row in fh:
            # Split the string into a list
            lineInfo = listCheck(str(row))
            # To count the people waiting for D2 and people who already vaccinated in VC1 and VC2 separately
            if lineInfo[2] == "VC1":
                totalVC1 += 1
                if lineInfo[4] == "COMPLETED-D1\n":
                    totalWaitingD2VC1 += 1
                if lineInfo[4] == "COMPLETED\n":
                    totalVaccinatedVC1 += 1
            else:
                totalVC2 += 1
                if lineInfo[4] == "COMPLETED-D1\n":
                    totalWaitingD2VC2 += 1
                if lineInfo[4] == "COMPLETED\n":
                    totalVaccinatedVC2 += 1
        
    # Get the total from both VCs
    totalWaitingD2 = totalWaitingD2VC1 + totalWaitingD2VC2
    totalVaccinated = totalVaccinatedVC1 + totalVaccinatedVC2
        
    # Print results
    printResultsSectionFour(totalVC1, totalWaitingD2VC1, totalVaccinatedVC1, totalVC2, totalWaitingD2VC2, totalVaccinatedVC2, totalWaitingD2, totalVaccinated)
    

# -------------------------------------------------------- Section 5 Functions ------------------------------------------------------------------
# Reading the patients' record
def readAllPatientRecords():
    allRecords = []
    with open("vaccination.txt","r") as fh:
        for row in fh:
            # Split the string into a list
            patientInformation = listCheck(str(row))
            # Putting the list into the master list
            allRecords.append(patientInformation)
    return allRecords

# Printing the patients' record
def printAllPatientRecords(records):
    # Print header
    print("\n" + "=" * 126)
    print("|" + "Vaccination ID".center(25) + "|" + "Name".center(25) + "|" + "Vaccination Center".center(25) + "|" + "Vaccine".center(20) + "|" + "Status".center(25) + "|")
    print("=" * 126)
    # Printing the list
    for counter in range(len(records)):
        items = records[counter]
        print("|" + items[0].center(25) + "| " + items[1].ljust(24) + "|" + items[2].center(25) + "|" + items[3].center(20) + "|" + (items[4].rstrip()).center(25) + "|")
    print("=" * 126)

# Section 5 - Print All Patient Records & Vaccination Status
def printAllPatientRecordsAndVaccineStatus():
    allRecords = readAllPatientRecords()
    printAllPatientRecords(allRecords)


# --------------------------------------------------------------- Menu --------------------------------------------------------------------------
def menu():
    while True:
        # Check if the file needed exists, if not then create new ones
        fileCheck()
        
        # Printing menu
        print("\n", " Welcome to the Vaccination Record Management System ".center(100, "="))
        print("\n\t1. New Patient Registration\n\t2. Vaccine Administration\n\t3. Search Patient Record & Vaccination Status")
        print("\t4. Statistical Information on Patients Vaccinated\n\t5. Print All Patient Record & Vaccination Status\n\t6. Exit")

        # Input validation
        try:
            choice = int(input("\nPlease choose any operation from the given options: "))
        except:
            print("Your input is invalid. Please try again.")
            continue
        if choice <= 0 or choice > 6:
            print("Please choose a number from 1 to 6 only.")
            continue

        # New Patient Registration
        elif choice == 1:
            newPatientRegistration()
            continue

        # Vaccine Administration
        elif choice == 2:
            if lineCount("patients.txt") > 0:
                vaccineAdministration()
            else:
                print("No record exists. Please register in 'Section 1 - New Patient Registration' before proceeding to this section.")
            continue

        # Search Patient Record & Vaccination Status
        elif choice == 3:
            if lineCount("patients.txt") > 0:
                patientRecordAndVaccineStatus()
            else:
                print("No record exists. Please register in 'Section 1 - New Patient Registration' before proceeding to this section.")
            continue

        # Statistical Information on Patients Vaccinated
        elif choice == 4:
            if lineCount("patients.txt") > 0:
                statisticalInfoOnPatientsVaccinated()
            else:
                print("No record exists. Please register in 'Section 1 - New Patient Registration' before proceeding to this section.")
            continue
        
        # Print Patient Record & Vaccination Status
        elif choice == 5:
            if lineCount("patients.txt") > 0:
                printAllPatientRecordsAndVaccineStatus()
            else:
                print("No record exists. Please register in 'Section 1 - New Patient Registration' before proceeding to this section.")
            continue

        # End the program
        else:
            break

# Start the program
menu()