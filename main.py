import sys
# Functions
# Verifies Nucleic Acid Sequence input
def verifyInput(nucleicAcid, isDNA):
   passed = True
   if isDNA:
      for base in nucleicAcid:
         if not (base == "A" or base == "T" or base == "G" or base == "C"):
            passed = False
   else:
      for base in nucleicAcid:
         if not (base == "A" or base == "U" or base == "G" or base == "C"):
            passed = False
   return passed

# Finds the complement of a Nucleic Acid Sequence, makes string uppercase
def findComplement(nucleicAcid, isDNA):
   DNAtable = str.maketrans({"A":"T","T":"A","C":"G","G":"C"})
   RNAtable = str.maketrans({"A":"U","U":"A","C":"G","G":"C"})
   nucleicAcid = nucleicAcid.upper()
   if isDNA:
      nucleicAcid = nucleicAcid.translate(DNAtable)
   else:
      nucleicAcid = nucleicAcid.translate(RNAtable)
   return nucleicAcid

# Transcribes DNA into mRNA
def transcribe(DNA):
   transcribe = str.maketrans({"A":"U","T":"A","C":"G","G":"C"})
   mRNA = DNA.translate(transcribe)
   return mRNA

# Reverse mRNA
def reverseTranscribe(nucleicAcid):
   reverseTranscription = str.maketrans({"A":"T", "U":"A", "C":"G", "G":"C"})
   nucleicAcid = nucleicAcid.translate(reverseTranscription)
   return nucleicAcid
   
# Main Section
strikes = 0
print("Welcome to the Basic Genetics Program, sourced in Python!")
while True:
   print("What would you like to do?")
   print("0. About")
   print("1. Find the complement of a Nucleic Acid Sequence")
   print("2. Transcribe a DNA Sequence")
   print("3. Translate a mRNA Sequence")
   print("4. REVERSE TRANSCRIBE a mRNA Sequence")
   print("Press 'q' to exit program")
   while True:
      choice = input()
      if choice.upper() == "Q":
         print("Exiting Program.")
         sys.exit()
      try:
         choice = int(choice)
         strikes = 0
         break
      except:
         if strikes == 0:
            print("Invalid Input, try Again. Press Q to quit.")
            strikes += 1
         elif strikes < 4:
            print(f"Try Again. Exiting in {4-strikes}.")
            strikes += 1
         else:
            sys.exit()
   if choice == 0:
      # Info
      pass
   elif choice == 1:
      # Complement of Sequence
      print("Finding Complement of a Nucleic Acid")
      print("Enter Nucleic Acid Type:")
      print("1. DNA")
      print("2. RNA")
      while True:
         choice = input()
         if choice.upper() == "Q":
            print("Exiting Program")
         try:
            choice = int(choice)
            break
         except:
            print("Invalid Input, try Again. Press Q to exit program.")
         if choice == 1:
            choice = True
            break
         elif choice == 2:
            choice = False
            break
         else:
            print("Invalid Choice. Try Again")
      while True:
         sequence = input("Enter sequence\n").upper()
         if input == "Q":
            break
         if verifyInput(sequence, choice):
            print("Your result is:")
            print(findComplement(sequence, choice))
            break
         else: 
            print("Invalid Input, try Again. Press Q to go back.")
   elif choice == 2:
      # Transcribe a DNA Sequence
      print("Transcribing a DNA Sequence:")
      while True:
         NAsequence = input("Enter DNA Strand:\n").upper()
         if NAsequence == "Q":
            break
         if verifyInput(NAsequence, True):
            print("Your result is:")
            print(transcribe(NAsequence))
            break
         else:
            print("Invalid Input, try Again. Press Q to go back.")
   elif choice == 3:
      # Translate a mRNA Sequence
      pass
   elif choice == 4:
      # Reverse Transcribe a mRNA Sequence
      print("Reverse Transcibe a mRNA Sequence")
      while True:
         sequence = input("Enter Sequence:\n").upper()
         if sequence == "Q":
            break
         if verifyInput(sequence, False):
            print("Your result is:")
            print(reverseTranscribe(sequence))
            break
         else:
            print("Invalid Input. Try Again. Press Q to go back.")
   else:
      print("That's not a valid option. Try Again.")
   